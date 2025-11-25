# Codex 트러블슈팅

> 💡 **codex-exec.sh가 대부분의 에러를 자동으로 처리합니다.**
>
> 에러 발생 시 스크립트의 메시지를 먼저 읽어보세요.
> 설치 가이드, 실행 실패 원인, 진단 정보를 자동으로 제공합니다.

---

## 스크립트가 자동 처리하는 에러

codex-exec.sh는 다음을 자동으로 감지하고 해결책을 제시합니다:

- ✅ **Missing dependencies** - codex CLI, jq 설치 가이드 제공
- ✅ **Git repository 체크** - 자동으로 `--skip-git-repo-check` 추가
- ✅ **Session ID 추출 실패** - 원인 분석과 원시 출력(처음 500자) 제공
- ✅ **Codex 실행 실패** - 가능한 원인과 해결 방법 안내

**스크립트의 에러 메시지를 신뢰하고 따르세요.**

---

## Resume 실패

**에러:**
```
Error: Codex execution failed
Invalid session ID (if resuming)
```

**해결 방법:**

1. Session ID 형식 확인:
   - 올바른 형식: `019a4d25-f1da-74a0-bba4-b7d333d3a096`
   - UUID v7 형식 (8-4-4-4-12 hex digits)

2. 이전 세션이 종료되었을 수 있음:
   ```bash
   # 새 세션으로 시작
   scripts/codex-exec.sh "프롬프트"
   ```

3. Session ID가 현재 대화에만 유효한지 확인
   - 새 Claude Code 대화 = 새 세션 필요

---

## 명령 실행 타임아웃

**증상:**
Codex 명령이 너무 오래 실행됨

**해결 방법:**

1. **작업을 더 작은 단위로 분할:**
   ```bash
   # ❌ Bad: 한 번에 모든 파일 분석
   scripts/codex-exec.sh "전체 프로젝트 분석"

   # ✅ Good: 단계별 분할
   scripts/codex-exec.sh "README.md 분석"
   # → SESSION_ID 저장
   scripts/codex-exec.sh "다음으로 src/ 구조 분석" "{저장된_SESSION_ID}"
   ```

2. **Reasoning effort 조정:**
   - 복잡한 작업: high (기본값)
   - 간단한 작업: medium 또는 low 고려

3. **사용자에게 진행 상황 보고:**
   - 장시간 작업 예상 시 사용자에게 알림
   - 중간 결과 공유

---

## 추가 문제

위에 없는 에러가 발생하면:

1. **codex-exec.sh의 에러 메시지 읽기** (가장 중요)
2. 스크립트 로직 확인: [scripts/codex-exec.sh](../scripts/codex-exec.sh)
3. Codex CLI 문서 참조: https://github.com/anthropics/codex
