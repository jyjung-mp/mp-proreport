#!/bin/bash

# Codex CLI 실행 및 결과 처리 스크립트
#
# 사용법:
#   ./codex-exec.sh "프롬프트"                                # 새 세션
#   ./codex-exec.sh "프롬프트" "session-id"                  # Resume
#   ./codex-exec.sh "프롬프트" "" --model gpt-5              # 모델 지정
#   ./codex-exec.sh "프롬프트" "session-id" --search         # 웹 검색 활성화
#
# 환경 변수:
#   PROJECT_DIR: Project directory (default: current directory)
#   MODEL: 모델 지정 (gpt-5-codex, gpt-5)
#   SANDBOX: 샌드박스 모드 (read-only, workspace-write, danger-full-access) (default: workspace-write)
#   SEARCH: 웹 검색 활성화 (default: 1, 비활성화: 0)
#   ADD_DIRS: 추가 접근 디렉토리 (콜론 구분, 예: /path/a:/path/b)
#   APPROVAL_POLICY: 승인 정책 (untrusted, on-failure, on-request, never)
#
# 출력:
#   SESSION_ID=...
#   RESULT=...

set -euo pipefail

# 의존성 확인
check_dependencies() {
    local missing=()

    if ! command -v codex &>/dev/null; then
        missing+=("codex CLI")
    fi

    if ! command -v jq &>/dev/null; then
        missing+=("jq")
    fi

    if [ ${#missing[@]} -gt 0 ]; then
        cat >&2 <<EOF
Error: Missing required dependencies: ${missing[*]}

Installation:
  codex CLI: https://github.com/anthropics/codex
  jq (macOS): brew install jq
  jq (Linux): apt-get install jq

EOF
        exit 1
    fi
}

# 인자 확인
if [ $# -lt 1 ]; then
    cat >&2 <<EOF
Error: Missing required prompt argument

Usage:
  $0 "your prompt here"                         # New session
  $0 "your prompt" "session-id"                 # Resume session
  $0 "your prompt" "" --model gpt-5             # With model
  $0 "your prompt" "" --search                  # Web search enabled

Examples:
  $0 "README.md 분석해줘"
  $0 "설치 가이드 추가해줘" "019a4d25-f1da-74a0-bba4-b7d333d3a096"
  $0 "복잡한 아키텍처 설계" "" --model gpt-5
  $0 "웹에서 최신 정보 찾아서 분석" "" --search

Environment:
  PROJECT_DIR: Project directory (default: current directory)
  MODEL: Model to use (gpt-5-codex, gpt-5)
  SANDBOX: Sandbox mode (read-only, workspace-write, danger-full-access) (default: workspace-write)
  SEARCH: Enable web search (default: 1, disable: 0)
  ADD_DIRS: Additional directories to allow access (colon-separated)
  APPROVAL_POLICY: Approval policy (untrusted, on-failure, on-request, never)

EOF
    exit 1
fi

# 의존성 확인 실행
check_dependencies

PROMPT="$1"
SESSION_ID="${2:-}"
PROJECT_DIR="${PROJECT_DIR:-$(pwd)}"

# 나머지 인자는 추가 옵션으로 처리
shift 2 2>/dev/null || shift 1
EXTRA_ARGS=("$@")

# Git 저장소 여부 확인
is_git_repo() {
    if git -C "$PROJECT_DIR" rev-parse --git-dir &>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Codex 실행 및 JSON 파싱
execute_codex() {
    # Root-level args (codex 명령어에 먼저 전달)
    local root_args=()

    # 명령줄 인자에 특정 옵션이 있는지 확인
    local has_sandbox=false
    local has_model=false
    local has_approval=false

    if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
        for arg in "${EXTRA_ARGS[@]}"; do
            case "$arg" in
                --sandbox) has_sandbox=true ;;
                --model) has_model=true ;;
                --ask-for-approval) has_approval=true ;;
            esac
        done
    fi

    # 샌드박스 모드 (명령줄 인자 우선, 없으면 환경변수/기본값)
    if [ "$has_sandbox" = false ]; then
        root_args+=("--sandbox" "${SANDBOX:-workspace-write}")
    fi

    # 모델 (명령줄 인자 우선, 없으면 환경변수)
    if [ "$has_model" = false ] && [ -n "${MODEL:-}" ]; then
        root_args+=("--model" "$MODEL")
    fi

    # 웹 검색 (기본 활성화, SEARCH=0으로 비활성화 가능)
    if [ "${SEARCH:-1}" != "0" ]; then
        root_args+=("--search")
    fi

    # 승인 정책 (명령줄 인자 우선, 없으면 환경변수)
    if [ "$has_approval" = false ] && [ -n "${APPROVAL_POLICY:-}" ]; then
        root_args+=("--ask-for-approval" "$APPROVAL_POLICY")
    fi

    # 추가 디렉토리 접근 (환경 변수)
    if [ -n "${ADD_DIRS:-}" ]; then
        IFS=':' read -ra DIRS <<< "$ADD_DIRS"
        for dir in "${DIRS[@]}"; do
            if [ -d "$dir" ]; then
                root_args+=("--add-dir" "$dir")
            else
                echo "Warning: Directory not found, skipping: $dir" >&2
            fi
        done
    fi

    # 추가 옵션 (명령줄 인자) - exec 전용 옵션과 root 옵션 분리
    if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
        local i=0
        while [ $i -lt ${#EXTRA_ARGS[@]} ]; do
            local arg="${EXTRA_ARGS[$i]}"

            # Exec 전용 옵션인지 확인
            case "$arg" in
                --json|--skip-git-repo-check)
                    # 값이 필요 없는 exec 전용 옵션 - 나중에 exec_args에 추가
                    ;;
                --color|--output-schema|--output-last-message|-o)
                    # 값이 필요한 exec 전용 옵션 - 나중에 exec_args에 추가
                    i=$((i+1))  # 값도 스킵
                    ;;
                *)
                    # Root-level 옵션 - root_args에 추가
                    root_args+=("$arg")
                    ;;
            esac
            i=$((i+1))
        done
    fi

    # Exec-level args (exec 서브커맨드에 전달)
    local exec_args=()
    local has_json=false
    local has_skip_git=false

    # EXTRA_ARGS에서 exec 전용 옵션만 추출하여 추가
    if [ ${#EXTRA_ARGS[@]} -gt 0 ]; then
        i=0
        while [ $i -lt ${#EXTRA_ARGS[@]} ]; do
            local arg="${EXTRA_ARGS[$i]}"

            case "$arg" in
                --json)
                    # --json 플래그 발견
                    has_json=true
                    exec_args+=("$arg")
                    ;;
                --skip-git-repo-check)
                    # --skip-git-repo-check 플래그 발견
                    has_skip_git=true
                    exec_args+=("$arg")
                    ;;
                --color|--output-schema|--output-last-message|-o)
                    # 값이 필요한 exec 전용 옵션
                    exec_args+=("$arg")
                    if [ $((i+1)) -lt ${#EXTRA_ARGS[@]} ]; then
                        i=$((i+1))
                        exec_args+=("${EXTRA_ARGS[$i]}")
                    fi
                    ;;
            esac
            i=$((i+1))
        done
    fi

    # --json이 명시되지 않았으면 기본으로 추가
    if [ "$has_json" = false ]; then
        if [ ${#exec_args[@]} -gt 0 ]; then
            exec_args=("--json" "${exec_args[@]}")
        else
            exec_args=("--json")
        fi
    fi

    # Git 저장소가 아니고 --skip-git-repo-check가 명시되지 않았으면 추가
    if ! is_git_repo && [ "$has_skip_git" = false ]; then
        exec_args+=("--skip-git-repo-check")
    fi

    # Resume 여부에 따라 명령 구성
    if [ -n "$SESSION_ID" ]; then
        # Resume 모드
        exec_args+=("resume" "$SESSION_ID")
    fi

    # Codex 실행 (JSON 스트리밍)
    local new_session_id=""
    local result=""
    local line_count=0
    local all_output=""

    # JSON 라인을 실시간으로 읽어 처리
    while IFS= read -r line || [ -n "$line" ]; do
        ((line_count++))
        all_output+="$line"$'\n'

        # thread.started 이벤트에서 Session ID 추출
        if [[ $line =~ \"type\":\"thread.started\" ]]; then
            new_session_id=$(echo "$line" | jq -r '.thread_id // empty' 2>/dev/null)
        fi

        # item.completed 이벤트에서 결과 추출
        if [[ $line =~ \"type\":\"item.completed\" ]]; then
            local item_type=$(echo "$line" | jq -r '.item.type // empty' 2>/dev/null)
            if [[ "$item_type" == "agent_message" ]]; then
                result=$(echo "$line" | jq -r '.item.text // empty' 2>/dev/null)
                # 결과를 찾았으면 종료
                if [ -n "$result" ]; then
                    break
                fi
            fi
        fi
    done < <(codex "${root_args[@]}" exec "${exec_args[@]}" "$PROMPT" 2>&1)

    # Codex 실행 상태 확인
    local codex_exit_code=$?
    if [ $codex_exit_code -ne 0 ]; then
        cat >&2 <<EOF
Error: Codex execution failed (exit code: $codex_exit_code)

Command: codex ${root_args[*]} exec ${exec_args[*]} "$PROMPT"

Possible causes:
  - Invalid session ID (if resuming)
  - Codex service unavailable
  - Network connectivity issues
  - Permission errors

Try:
  - Check session ID format (if resuming)
  - Verify Codex CLI is properly configured
  - Run without resume to start new session

EOF
        exit 1
    fi

    # Session ID 검증
    if [ -z "$new_session_id" ]; then
        cat >&2 <<EOF
Warning: No session ID extracted from Codex output

Raw output (first 500 chars):
$(echo "$all_output" | head -c 500)

EOF
        exit 1
    fi

    # 결과 검증
    if [ -z "$result" ]; then
        cat >&2 <<EOF
Warning: No result extracted from Codex output

This may indicate:
  - Codex task is still running (incomplete)
  - JSON output format changed
  - jq filter mismatch

Processed $line_count JSON lines
Raw output (first 500 chars):
$(echo "$all_output" | head -c 500)

EOF
        # 빈 결과로도 출력 (디버깅용)
        echo "SESSION_ID=$new_session_id"
        echo "RESULT="
        return 1
    fi

    # 출력 (eval 가능한 형식)
    # UTF-8 문자는 보존하고 백슬래시와 따옴표만 이스케이프
    echo "SESSION_ID=$new_session_id"
    escaped="${result//\\/\\\\}"
    escaped="${escaped//\"/\\\"}"
    printf 'RESULT="%s"\n' "$escaped"
}

# 실행
execute_codex
