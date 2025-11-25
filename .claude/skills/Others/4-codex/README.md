# Codex 스킬

> **Codex CLI를 Claude Code에서 쉽게 사용하기 위한 래퍼 스킬**

## 📋 목차

- [개요](#개요)
- [배경 및 문제 해결](#배경-및-문제-해결)
- [핵심 기능](#핵심-기능)
- [빠른 시작](#빠른-시작)
- [사용 방법](#사용-방법)
- [세션 관리](#세션-관리)
- [다른 스킬과 통합](#다른-스킬과-통합)
- [트러블슈팅](#트러블슈팅)
- [고급 설정](#고급-설정)
- [참고: Codex란?](#참고-codex란)

---

## 개요

Codex 스킬은 **Codex CLI를 실행하고 결과를 자동으로 처리하는 Claude Code 스킬**입니다.

### 스킬의 역할

```
Claude Code 사용자
       ↓
  "codex로 [작업]"
       ↓
   Codex 스킬
       ↓
codex-exec.sh 스크립트
       ↓
   Codex CLI
       ↓
  결과 자동 파싱 및 반환
```

### 주요 책임

- ✅ Codex CLI 실행 래핑
- ✅ Git 저장소 자동 감지 및 플래그 처리
- ✅ SESSION_ID 추출 및 반환
- ✅ JSON 파싱 및 결과 정리
- ✅ 의존성 자동 체크
- ✅ 에러 진단 및 해결책 제시

### 스킬이 하지 않는 것

- ❌ Sandbox 정책 변경 (Codex CLI/런타임이 관리)
- ❌ SESSION_ID 저장 (Claude Code 대화 메모리가 관리)
- ❌ 승인 정책 우회

---

## 배경 및 문제 해결

### 왜 이 스킬이 필요한가?

기존 **Codex MCP**에는 치명적인 문제가 있었습니다:

#### 문제점: SESSION_ID 미제공

```
기존 Codex MCP 사용 시:
1. Codex 실행
2. ❌ SESSION_ID가 반환되지 않음
3. 세션을 이어가려면 로그 파일을 직접 열어서
4. SESSION_ID를 수동으로 찾아내야 함
5. 불편하고 에러가 발생하기 쉬움
```

#### 해결: 자동 SESSION_ID 추출

```
Codex 스킬 사용 시:
1. Codex 실행
2. ✅ SESSION_ID 자동 추출 및 반환
3. Claude Code가 대화 메모리에 자동 저장
4. 후속 요청 시 자동으로 Resume
5. 깔끔하고 안정적인 세션 관리
```

### 핵심 개선사항

| 항목 | 기존 MCP | Codex 스킬 |
|------|----------|-----------|
| **SESSION_ID 추출** | ❌ 없음 (로그 파일 직접 검색) | ✅ 자동 추출 |
| **세션 이어가기** | ❌ 수동 (복잡) | ✅ 자동 |
| **에러 발생률** | ❌ 높음 | ✅ 낮음 |
| **사용 편의성** | ❌ 불편 | ✅ 편리 |

---

## 핵심 기능

### 1. Git 저장소 자동 감지

```bash
# Git 저장소 아닌 경우 자동으로:
codex exec --skip-git-repo-check "작업"
```

### 2. SESSION_ID 자동 추출 ⭐ (핵심!)

**기존 MCP의 가장 큰 문제를 해결한 기능입니다.**

```bash
# 스크립트 출력:
SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096
RESULT="[Codex 응답]"
```

**왜 중요한가?**
- 기존 Codex MCP: SESSION_ID 미제공 → 로그 파일 직접 검색 필요
- Codex 스킬: SESSION_ID 자동 추출 → 즉시 사용 가능
- 세션 연속성 보장으로 안정적인 대화 가능

### 3. Resume 모드 자동 처리

```bash
# SESSION_ID가 제공되면 자동으로:
codex exec --skip-git-repo-check resume {SESSION_ID} "작업"
```

### 4. 의존성 자동 체크

스크립트 실행 시 자동으로 확인:
- `codex` CLI 설치 여부
- `jq` (JSON 파싱) 설치 여부
- 미설치 시 설치 가이드 제공

### 5. 에러 자동 진단

실행 실패 시 자동으로:
- 에러 원인 분석
- 가능한 해결 방법 제시
- 관련 로그 출력 (처음 500자)

---

## 빠른 시작

### 필수 요구사항

```bash
# Codex CLI 설치
# https://github.com/anthropics/codex

# jq 설치 (JSON 파싱용)
brew install jq  # macOS
apt-get install jq  # Linux
```

### 첫 실행

Claude Code에서:
```
"codex로 README.md를 분석해줘"
```

스킬이 자동으로:
1. 의존성 확인
2. Git 저장소 체크
3. Codex 실행
4. SESSION_ID를 Claude Code 대화 메모리에 저장
5. 결과 반환

---

## 사용 방법

### Claude Code에서 사용 (권장)

```
"codex로 [작업 설명]"
"codex에게 [질문]"
```

**예시:**
```
"codex로 src/ 디렉토리 구조 분석해줘"
"codex에게 버그 원인 찾아달라고 해줘"
"codex로 테스트 코드 작성해줘"
```

**자동 처리:**
- ✅ SESSION_ID 대화 메모리에 자동 저장
- ✅ 후속 요청 시 자동으로 Resume
- ✅ 컨텍스트 연속성 유지

### 터미널에서 직접 실행

#### 새 세션 시작

```bash
scripts/codex-exec.sh "프롬프트"

# 출력:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096
# RESULT="[Codex 응답 내용]"
```

#### 세션 이어가기

```bash
scripts/codex-exec.sh "후속 작업" "019a4d25-f1da-74a0-bba4-b7d333d3a096"

# 출력:
# SESSION_ID=019a4d25-f1da-74a0-bba4-b7d333d3a096 (동일)
# RESULT="[Codex 응답 내용]"
```

> **⚠️ 세션 관리 차이점**
> - **Claude Code**: SESSION_ID 자동 저장/재사용
> - **터미널**: 두 번째 인자로 수동 전달 필요

### 환경 변수

```bash
# 기본값: /Users/mklee02/work/pdp-studio
PROJECT_DIR="/custom/path" scripts/codex-exec.sh "프롬프트"
```

> **⚠️ 프로젝트 경로 주의**
> 기본값으로 `PROJECT_DIR=/Users/mklee02/work/pdp-studio`로 설정되어 있습니다. 다른 위치에서 실행할 때는 환경 변수를 지정하세요.

---

## 세션 관리

### 세션이란?

세션(Session)은 Codex와의 연속적인 대화를 추적하는 단위입니다. 동일 세션 내에서는 이전 컨텍스트가 유지됩니다.

### 세션 흐름 (Claude Code)

```
┌─────────────────────────────────────────────┐
│ 1. 첫 요청: "codex로 README.md 분석"        │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 2. 스크립트 실행 → SESSION_ID 추출          │
│    SESSION_ID=019a4d25...                   │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 3. Claude Code가 대화 메모리에 저장         │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 4. 후속 요청: "codex로 설치 가이드 추가"    │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 5. 저장된 SESSION_ID로 자동 Resume          │
│    컨텍스트 유지됨                           │
└─────────────────────────────────────────────┘
```

### 세션 격리 규칙

- **대화 단위 격리**: 각 Claude Code 대화 = 독립적인 세션
- **새 대화 = 새 세션**: 새 Claude Code 대화 시작 시 새 SESSION_ID 생성
- **자동 Resume**: 동일 대화 내에서는 SESSION_ID 자동 재사용

---

## 다른 스킬과 통합

### 통합 패턴

Codex 스킬은 다른 스킬의 결과물을 보완하거나, 맞춤형 작업을 수행하는 데 사용됩니다.

#### 패턴 1: 스킬 → Codex (보완)

```
1. backend-builder로 API 스켈레톤 생성
   "backend-builder로 Product CRUD API 만들어줘"

2. Codex로 비즈니스 로직 추가
   "codex로 Product Service에 재고 관리 로직을 추가해줘"
```

**장점**: 빠른 스캐폴딩 + 도메인 특화 로직

#### 패턴 2: Codex → 스킬 (검증)

```
1. Codex로 코드 작성
   "codex로 사용자 인증 기능 구현해줘"

2. code-reviewer로 검토
   "code-reviewer로 방금 작성된 코드 리뷰해줘"
```

**장점**: 빠른 구현 + 자동 품질 검증

#### 패턴 3: full-auto-dev → Codex (세부 조정)

```
1. full-auto-dev로 전체 기능 생성
   "full-auto-dev로 사용자 관리 기능 개발해줘"

2. Codex로 예외 처리 보강
   "codex로 생성된 코드의 예외 처리를 보강해줘"
```

**장점**: 완전 자동화 + 맞춤 튜닝

### 통합 모범 사례

✅ **DO:**
1. 스킬 실행 후 생성된 파일 목록을 Codex에 공유
2. 스킬 로그/에러를 Codex에 전달하여 문제 진단
3. 단계별로 진행하며 중간 검증

❌ **DON'T:**
1. 스킬과 Codex에 동일한 작업 중복 요청
2. 스킬 결과를 검토 없이 Codex에 바로 전달
3. 세션 간 컨텍스트 공유 기대

---

## 트러블슈팅

### 자동 에러 진단

`codex-exec.sh`는 다음을 자동으로 감지하고 해결책을 제시합니다:

#### 1. 의존성 누락

**에러:**
```
Error: Missing required dependencies: codex CLI, jq
```

**자동 제공:**
- 설치 가이드 (macOS/Linux)
- 공식 문서 링크

#### 2. Git 저장소 체크

**자동 처리:**
- Git 저장소 아니면 `--skip-git-repo-check` 자동 추가
- 사용자 개입 불필요

#### 3. SESSION_ID 추출 실패

**에러:**
```
Warning: No session ID extracted from Codex output
```

**자동 제공:**
- 원시 출력 (처음 500자)
- 가능한 원인 목록

#### 4. Codex 실행 실패

**에러:**
```
Error: Codex execution failed (exit code: X)
```

**자동 제공:**
- 실행된 명령어
- 가능한 원인 (잘못된 SESSION_ID, 네트워크 문제 등)
- 해결 방법 제안

### 일반적인 문제

#### Resume 실패

**원인:**
- 잘못된 SESSION_ID 형식
- 이전 세션이 종료됨
- 다른 대화의 SESSION_ID 사용

**해결:**
```bash
# 새 세션으로 시작
scripts/codex-exec.sh "프롬프트"
```

#### 타임아웃

**원인:** 작업이 너무 복잡함

**해결:**
```bash
# ❌ Bad: 한 번에 모든 작업
"codex로 전체 프로젝트 분석하고 리팩토링해줘"

# ✅ Good: 작업 분할
"codex로 README.md 분석"
"codex로 다음으로 src/ 구조 분석"  # 이전 세션 이어감
```

#### 권한 에러

**원인:** Sandbox 외부 명령 시도

**해결:**
- 작업을 Sandbox 내에서 가능한 방식으로 조정
- 또는 사용자에게 명시적 승인 요청

---

## 고급 설정

### 직접 Codex CLI 호출

스크립트를 거치지 않고 직접 호출이 필요한 경우:

#### 실시간 스트리밍 출력

```bash
# 스크립트는 --json으로 출력 숨김
# 직접 호출하면 실시간 스트리밍
codex exec --skip-git-repo-check "복잡한 분석 작업"
```

#### 커스텀 Codex 옵션

```bash
codex exec --skip-git-repo-check \
  --model o3 \
  --color never \
  "작업"
```

### 결과 파싱

스크립트 출력을 직접 처리:

```bash
# 출력 저장
output=$(scripts/codex-exec.sh "README.md 분석")

# SESSION_ID 추출
session_id=$(echo "$output" | grep "^SESSION_ID=" | cut -d= -f2)

# RESULT 추출
result=$(echo "$output" | grep "^RESULT=" | cut -d= -f2- | sed 's/^"//;s/"$//')

# 사용
echo "Session: $session_id"
echo "Result: $result"
```

### 반복 처리

```bash
# 여러 파일 처리
for file in *.md; do
    output=$(scripts/codex-exec.sh "Analyze $file")
    result=$(echo "$output" | grep "^RESULT=" | cut -d= -f2-)
    echo "$result" > "${file}.analysis"
done
```

---

## 참고: Codex란?

Codex는 **GPT-5 기반의 코딩 전문 AI 에이전트**입니다.

### 주요 특징

- 실제 파일 시스템과 상호작용
- 터미널 명령 실행
- 코드베이스 탐색 및 분석
- 코드 작성, 수정, 테스트

### 상세 정보

- **공식 문서**: https://github.com/anthropics/codex
- **설치 가이드**: Codex CLI 저장소 참조
- **사용 예제**: Codex 공식 문서 참조

---

## 스킬 구조

```
.claude/skills/codex/
├── README.md                    # 이 문서
├── skill.md                     # 스킬 정의
├── scripts/
│   └── codex-exec.sh           # Codex 실행 스크립트
└── references/
    ├── utilities.md            # 고급 사용법
    └── troubleshooting.md      # 상세 트러블슈팅
```

### 추가 문서

- **기본 패턴**: [skill.md](skill.md)
- **고급 사용법**: [references/utilities.md](references/utilities.md)
- **상세 트러블슈팅**: [references/troubleshooting.md](references/troubleshooting.md)

---

## 요약

### 핵심 포인트

1. **래퍼 스킬**: Codex CLI를 쉽게 사용하기 위한 도구
2. **자동 처리**: Git 감지, SESSION_ID 추출, 에러 진단
3. **세션 관리**: Claude Code에서 자동, 터미널에서 수동
4. **스킬 통합**: 다른 스킬과 조합하여 효율 극대화

### 빠른 참조

```bash
# Claude Code에서
"codex로 [작업]"

# 터미널에서 (새 세션)
scripts/codex-exec.sh "프롬프트"

# 터미널에서 (Resume)
scripts/codex-exec.sh "프롬프트" "SESSION_ID"

# 환경 변수
PROJECT_DIR="/path" scripts/codex-exec.sh "프롬프트"
```

---

**Made with ❤️ by Claude Code & Codex**
