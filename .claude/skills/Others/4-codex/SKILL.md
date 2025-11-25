---
name: codex
description: |
  Executes OpenAI Codex CLI wrapper with automatic session management and result extraction.
  Manages session persistence across conversation turns for context continuity.

  Use when:
  - User explicitly requests "codex로" or "codex에게 [task]"
  - Delegating complex code analysis, generation, or multi-step tasks requiring reasoning
  - Need persistent context across multiple requests within same conversation

  Auto-handles: Git detection, session tracking, JSON parsing, sandbox config (workspace-write default).
  Supports: gpt-5-codex (default, fast), gpt-5 (complex reasoning), web search (enabled by default).
---

# Codex

Codex CLI를 실행하고 대화 내에서 세션을 자동 관리하는 스킬입니다.

## 핵심 패턴

### 새 세션 시작

```bash
scripts/codex-exec.sh "{사용자_요청}"

# 출력:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096
# RESULT="[Codex 응답 내용]"
```

출력에서 **SESSION_ID를 추출하여 대화 메모리에 저장**합니다.

### 기존 세션 이어가기

저장된 SESSION_ID로 resume:

```bash
scripts/codex-exec.sh "{사용자_요청}" "{저장된_SESSION_ID}"

# 출력:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096 (동일)
# RESULT="[Codex 응답 내용]"
```

### 스크립트가 자동 처리하는 것

- ✅ Git 저장소 확인 (`--skip-git-repo-check` 자동 추가)
- ✅ Session ID 추출 및 반환
- ✅ JSON 파싱 및 결과 정리
- ✅ Resume 모드 처리

---

## 워크플로우

### 1. 첫 요청 처리

```bash
scripts/codex-exec.sh "README.md 분석해줘"

# 출력 예시:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096
# RESULT="README.md를 분석했습니다..."

# → SESSION_ID를 이 대화 내에서 기억 (예: "019a4d25-f1da-74a0-bba4-b7d333d3a096")
# → RESULT를 사용자에게 보고
```

### 2. 후속 요청 처리

```bash
scripts/codex-exec.sh "설치 가이드도 추가해줘" "019a4d25-f1da-74a0-bba4-b7d333d3a096"

# 출력:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096 (동일)
# RESULT="설치 가이드를 추가했습니다..."

# → 이전 컨텍스트 유지하며 작업 수행
# → RESULT를 사용자에게 보고
```

### 3. 새 대화에서는 새 세션

새 Claude Code 대화 = 새 세션 시작 (저장된 SESSION_ID 없음)

---

## 주의사항

### 🚨 사용자 승인 필요

다음 플래그는 사용자의 **명시적 승인** 없이 사용 금지:
- `--full-auto`: 자동 실행 모드
- `--sandbox danger-full-access`: 전체 시스템 접근

### ⚠️ 명령 실패 시

1. 에러 메시지를 사용자에게 보고
2. 다음 작업 진행 전 중단
3. 사용자 지시 대기

---

## 고급 옵션 사용

### 모델 선택 (--model)

**두 가지 모델:**

작업의 복잡도에 따라 적절한 모델을 선택합니다.

| 모델 | 사용 시기 | 예시 작업 |
|------|-----------|-----------|
| **gpt-5-codex** (기본) | 일반적인 코드 작업 | - 일반 코드 작성<br>- 버그 수정<br>- 코드 리뷰<br>- 문서 작성<br>- 파일 분석 |
| **gpt-5** | 복잡하고 깊은 사고가 필요한 작업 | - 아키텍처 설계<br>- 복잡한 리팩토링<br>- 보안 감사<br>- 알고리즘 최적화 |

**사용 예시:**
```bash
# 일반 작업 (기본값, 모델 지정 불필요)
scripts/codex-exec.sh "README.md 요약해줘"

# 복잡한 설계
scripts/codex-exec.sh "마이크로서비스 아키텍처 설계" "" --model gpt-5

# 환경 변수 사용
MODEL=gpt-5 scripts/codex-exec.sh "보안 감사"
```

**AI 판단 기준:**
- 일반 코드 작업, 분석, 리뷰 → gpt-5-codex (기본값, 생략 가능)
- 아키텍처, 복잡한 리팩토링, 보안, 알고리즘 → gpt-5

### 샌드박스 모드 (--sandbox)

**세 가지 샌드박스 레벨:**

| 모드 | 설명 | 사용 시기 |
|------|------|-----------|
| **workspace-write** (기본) | 워크스페이스 내 읽기/쓰기 가능, 외부는 승인 필요 | 일반적인 코드 작업 (기본값) |
| **read-only** | 읽기만 가능, 모든 수정/명령은 승인 필요 | 탐색 전용, 분석 전용 작업 |
| **danger-full-access** | 전체 시스템 접근 가능 | 🚨 사용자 명시적 승인 필요 |

**사용 예시:**
```bash
# 읽기 전용 모드 (안전한 탐색)
scripts/codex-exec.sh "전체 코드베이스 분석" "" --sandbox read-only

# 기본 모드 (생략 가능, workspace-write)
scripts/codex-exec.sh "버그 수정"

# 전체 접근 (사용자 승인 필요)
scripts/codex-exec.sh "시스템 설정 변경" "" --sandbox danger-full-access

# 환경 변수 사용
SANDBOX=read-only scripts/codex-exec.sh "코드 리뷰"
```

**AI 판단 기준:**
- 일반 코딩 작업 → 기본값 (workspace-write, 생략)
- 탐색/분석만 하는 경우 → read-only
- 시스템 설정, 외부 접근 필요 → 사용자에게 승인 요청 후 danger-full-access

### 웹 검색 (--search)

**⚠️ 기본 활성화됨**

웹 검색은 기본적으로 활성화되어 있습니다. 필요시 `SEARCH=0`으로 비활성화할 수 있습니다.

**기본 활성화 이유:**
- 최신 정보 자동 검색 (라이브러리 버전, API 변경사항 등)
- 외부 문서 자동 참조
- 에러 메시지 자동 검색
- 더 정확하고 최신의 답변 제공

**비활성화 예시:**
```bash
# 웹 검색 비활성화 (오프라인 작업, 빠른 응답 필요시)
SEARCH=0 scripts/codex-exec.sh "로컬 코드만 분석"

# 기본값 (웹 검색 활성화, 명시하지 않아도 됨)
scripts/codex-exec.sh "React 19의 새 기능 분석"

# 명시적으로 활성화 (불필요, 기본값과 동일)
SEARCH=1 scripts/codex-exec.sh "최신 TypeScript 베스트 프랙티스"
```

**AI 판단 기준:**
- 기본적으로 웹 검색 활성화 (별도 옵션 불필요)
- 오프라인 작업이나 빠른 응답만 필요한 경우 → `SEARCH=0` 추가
- 로컬 코드만 분석하는 경우 → `SEARCH=0` 고려

### 추가 디렉토리 접근 (--add-dir)

**사용 시나리오:**

#### 1. 다른 프로젝트 참조
```bash
# 레거시 프로젝트 코드 참조하며 마이그레이션
scripts/codex-exec.sh "인증 로직 마이그레이션" "" \
  --add-dir /Users/user/legacy-project

# 여러 프로젝트 비교
scripts/codex-exec.sh "프로젝트 A와 B 비교" "" \
  --add-dir /path/to/project-a \
  --add-dir /path/to/project-b
```

#### 2. 문서/템플릿 디렉토리 접근
```bash
# API 스펙 문서 참조
scripts/codex-exec.sh "REST API 엔드포인트 구현" "" \
  --add-dir /Users/user/api-specs

# 코드 템플릿 사용
scripts/codex-exec.sh "컴포넌트 생성" "" \
  --add-dir /Users/user/templates
```

#### 3. 환경 변수 사용
```bash
# 단일 디렉토리
ADD_DIRS="/path/to/other-project" scripts/codex-exec.sh "작업"

# 여러 디렉토리 (콜론 구분)
ADD_DIRS="/path/to/project-a:/path/to/project-b:/path/to/docs" scripts/codex-exec.sh "분석"
```

**AI 판단 기준:**
- 사용자가 "다른 프로젝트", "외부 파일", "참조" 언급 → --add-dir 고려
- 마이그레이션, 통합, 비교 작업 → 관련 디렉토리 추가
- API 스펙, 문서 참조 언급 → 해당 디렉토리 추가

### 승인 정책 (--ask-for-approval)

**네 가지 승인 모드:**

| 모드 | 설명 | 사용 시기 |
|------|------|-----------|
| **untrusted** | 신뢰하지 않는 명령만 승인 요청 | 일반적인 사용 (기본값) |
| **on-failure** | 실패한 명령에 대해서만 승인 요청 | 빠른 작업, 신뢰할 수 있는 환경 |
| **on-request** | 에이전트가 요청할 때만 승인 | 자동화 워크플로우 |
| **never** | 승인 요청 안 함 | 🚨 완전 자동화 (주의 필요) |

**사용 예시:**
```bash
# 빠른 자동 수정 (실패 시에만 승인)
scripts/codex-exec.sh "린트 에러 자동 수정" "" --ask-for-approval on-failure

# 완전 자동화 (사용자 승인 필요)
scripts/codex-exec.sh "전체 테스트 실행 및 수정" "" --ask-for-approval never

# 환경 변수 사용
APPROVAL_POLICY=on-failure scripts/codex-exec.sh "자동 리팩토링"
```

**AI 판단 기준:**
- 일반 작업 → 기본값 (untrusted, 생략)
- 빠른 자동 수정 → on-failure
- 자동화 워크플로우 → 사용자 승인 후 never

### 옵션 조합 사용

**실전 예시:**

```bash
# 복잡한 보안 감사 (웹 검색 기본 활성화)
scripts/codex-exec.sh "전체 인증 시스템 보안 감사" "" \
  --model gpt-5 \
  --sandbox read-only

# 빠른 분석 + 읽기 전용 + 웹 검색 비활성화 (오프라인)
SEARCH=0 scripts/codex-exec.sh "파일 구조 분석" "" \
  --sandbox read-only

# 레거시 프로젝트 참조하며 마이그레이션 (웹 검색 자동 포함)
scripts/codex-exec.sh "인증 시스템 마이그레이션" "" \
  --model gpt-5 \
  --add-dir /Users/user/legacy-project \
  --add-dir /Users/user/api-docs
```

**참고:**
- 웹 검색은 기본적으로 활성화되어 있어 별도로 `--search` 옵션을 추가할 필요가 없습니다
- 오프라인 작업이나 빠른 응답이 필요한 경우에만 `SEARCH=0`으로 비활성화하세요

---

## 참고 자료

상세 정보는 다음 문서 참조:

- **특수 케이스**: [references/utilities.md](references/utilities.md) - 직접 CLI 호출, 환경 변수 커스터마이징
- **문제 해결**: [references/troubleshooting.md](references/troubleshooting.md) - Resume 실패, 타임아웃
