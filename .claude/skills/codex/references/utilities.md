# Codex 고급 설정

> **대부분의 경우 이 문서는 필요하지 않습니다.** 표준 bash 지식으로 충분합니다.

---

## 환경 변수 커스터마이징

프로젝트 디렉토리를 변경하려면:

```bash
PROJECT_DIR="/custom/path" scripts/codex-exec.sh "프롬프트"
```

---

## 직접 Codex CLI 호출

스크립트 대신 직접 호출이 필요한 **특수 케이스**:

### 실시간 스트리밍 출력

진행 과정을 실시간으로 보려면:

```bash
# 스크립트는 --json으로 출력 숨김
# 직접 호출하면 실시간 스트리밍

codex exec --skip-git-repo-check "복잡한 분석 작업"
```

### 커스텀 Codex 옵션

`--model`, `--color` 등 특수 옵션:

```bash
codex exec --skip-git-repo-check --model o3 --color never "작업"
```

### 원시 텍스트 출력

JSON 파싱 없이 원시 출력:

```bash
output=$(codex exec --skip-git-repo-check "질문" 2>&1)
echo "$output"
```

---

## 결과 처리

스크립트 출력을 직접 파싱하세요:

```bash
# 출력 전체 저장
output=$(scripts/codex-exec.sh "README.md 분석")

# SESSION_ID 추출
session_id=$(echo "$output" | grep "^SESSION_ID=" | cut -d= -f2)

# RESULT 추출 (따옴표 제거)
result=$(echo "$output" | grep "^RESULT=" | cut -d= -f2- | sed 's/^"//;s/"$//')

# 사용 예시
echo "Session: $session_id"
echo "Result: $result"

# 반복 처리
for file in *.md; do
    output=$(scripts/codex-exec.sh "Analyze $file")
    result=$(echo "$output" | grep "^RESULT=" | cut -d= -f2-)
    echo "$result" > "${file}.analysis"
done
```
