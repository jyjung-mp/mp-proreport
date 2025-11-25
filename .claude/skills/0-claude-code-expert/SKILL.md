---
name: claude-code-expert
description: |
  Claude Code 전문가 스킬. MCP 서버 개발, Skills 생성, 워크플로우 설계, CLAUDE.md 작성을 지원.

  사용 시기:
  - MCP 서버 개발 및 통합이 필요할 때
  - 새로운 Skills를 개발하거나 관리할 때
  - Claude Code 워크플로우(Brainstorm → Plan → Execute)를 설계할 때
  - 프로젝트별 CLAUDE.md 작성이 필요할 때
  - Claude Code 설정 및 최적화가 필요할 때
---

# Claude Code Expert

Claude Code를 효과적으로 활용하기 위한 종합 전문가 스킬입니다.

## 개요

이 스킬은 다음 영역에 대한 전문 지식과 템플릿을 제공합니다:

1. **MCP 서버 개발**: 외부 서비스 연동을 위한 MCP 서버 구축
2. **Skills 개발**: 재사용 가능한 전문 스킬 생성 및 관리
3. **워크플로우 설계**: Brainstorm → Plan → Execute 패턴 적용
4. **CLAUDE.md 작성**: 프로젝트별 작업 지침서 작성

## 사용 시기

다음과 같은 요청이 있을 때 이 스킬을 사용:

### MCP 서버 개발
- "Jira와 연동하는 MCP 서버를 만들고 싶어"
- "Wiki API를 Claude Code에서 사용할 수 있게 해줘"
- "MCP 서버 템플릿이 필요해"

### Skills 개발
- "PDF 편집 스킬을 만들고 싶어"
- "기존 스킬을 개선하고 싶어"
- "스킬 패키징 방법을 알려줘"

### 워크플로우 설계
- "효율적인 기획 워크플로우를 구축하고 싶어"
- "Brainstorm → Plan → Execute 패턴을 적용하고 싶어"
- "데이터 분석 워크플로우가 필요해"

### CLAUDE.md 작성
- "새 프로젝트에 맞는 CLAUDE.md를 작성해줘"
- "현재 프로젝트의 CLAUDE.md를 개선해줘"
- "CLAUDE.md 템플릿이 필요해"

## 워크플로우

### 1. MCP 서버 개발 워크플로우

#### 1.1. 요구사항 정의

**질문:**
- 어떤 외부 서비스와 연동할 것인가?
- 어떤 데이터를 제공해야 하는가?
- 어떤 작업을 수행해야 하는가?
- 인증이 필요한가?

#### 1.2. 템플릿 사용

MCP 서버 템플릿을 복사하여 시작:

```bash
cp -r .claude/skills/0-claude-code-expert/assets/mcp-server-template/ ~/my-mcp-server/
```

#### 1.3. 도구(Tool) 설계

**상세 가이드**: `references/mcp_development.md` 참조

**핵심 원칙**:
- 하나의 도구는 하나의 작업만
- 파라미터는 명확하고 검증 가능
- 설명(description)은 구체적으로
- 에러 처리는 명확하게

#### 1.4. 구현 및 테스트

1. 도구 로직 구현
2. MCP 설정 추가 (`.claude/mcp_settings.json`)
3. 환경 변수 설정
4. Claude Code 재시작
5. 테스트

### 2. Skills 개발 워크플로우

#### 2.1. 구체적인 사용 예시 수집

최소 3개 이상의 구체적인 시나리오 수집:

```
사용자: "PDF를 90도 회전시켜줘"
사용자: "이 PDF를 병합해줘"
사용자: "PDF에서 특정 페이지만 추출해줘"

→ pdf-editor 스킬 필요
```

#### 2.2. 재사용 가능한 리소스 계획

**상세 가이드**: `references/skills_development.md` 참조

각 사용 예시를 분석하여 필요한 리소스 결정:

- **scripts/**: 반복 작성되는 코드, 결정론적 작업
- **references/**: 참고 문서, 스키마, API 문서
- **assets/**: 템플릿, 이미지, 보일러플레이트

#### 2.3. SKILL.md 작성

**필수 구성**:
```markdown
---
name: skill-name
description: |
  스킬의 목적과 사용 시기를 명확히 설명.

  사용 시기:
  - 구체적인 상황 1
  - 구체적인 상황 2
---

# 스킬 제목

## 개요
...

## 사용 시기
...

## 워크플로우
...
```

**작성 스타일**:
- 명령형/부정사 형태
- 객관적이고 명령적인 톤
- Progressive Disclosure 원칙 준수

#### 2.4. 검증 및 패키징

검증 및 패키징은 skill-creator의 스크립트 사용:

```bash
# 검증
scripts/validate_skill.py .claude/skills/my-skill/

# 패키징
scripts/package_skill.py .claude/skills/my-skill/
```

### 3. 워크플로우 설계

#### 3.1. Brainstorm → Plan → Execute 패턴

**상세 가이드**: `references/workflow_patterns.md` 참조

**Phase 1: Brainstorming**
- 목적: 요구사항 명확화, 설계 방향 수립
- 산출물: 명확화된 요구사항, 설계 제안

**Phase 2: Planning**
- 목적: 상세 설계, 작업 분해
- 산출물: 화면 정의서, API 명세서, 테스트 케이스

**Phase 3: Execution**
- 목적: 검증 및 문서화
- 산출물: Wiki 문서

#### 3.2. 전문 스킬 통합

워크플로우에 전문 스킬 통합:

- **data-analyzing**: 데이터 지표 정의 및 검증
- **benchmarking**: 경쟁사 비교 분석
- **systematic-debugging**: Jira 이슈 분석

**통합 예시**:
```
Brainstorming 단계에서 데이터 요구사항 도출 시
→ data-analyzing 스킬 호출하여 계산식 검증

Brainstorming 단계에서 설계 방향 참고 시
→ benchmarking 스킬 호출하여 경쟁사 분석
```

### 4. CLAUDE.md 작성 워크플로우

#### 4.1. 템플릿 복사

```bash
cp .claude/skills/0-claude-code-expert/assets/CLAUDE_md_template.md ./CLAUDE.md
```

#### 4.2. 프로젝트 정보 입력

템플릿의 플레이스홀더를 실제 정보로 대체:

- `{프로젝트명}`
- `{YYYY-MM-DD}`
- `{프로젝트의 핵심 목적}`
- `{타겟 사용자 설명}`
- `{Wiki 최상위 페이지 URL}` 등

#### 4.3. 프로젝트 특성에 맞게 커스터마이징

**추가할 섹션 예시**:
- 비즈니스 규칙
- 데이터 소스 상세
- 특수 워크플로우
- 협업 도구 정보

#### 4.4. 워크플로우 정의

프로젝트에 맞는 워크플로우 정의:

- Brainstorm → Plan → Execute (기본)
- 특수 상황별 워크플로우 (Jira 분석, 데이터 검증 등)

#### 4.5. 전문 스킬 매핑

프로젝트에서 사용할 전문 스킬 명시:

```markdown
## 전문 스킬 활용

### 사용 가능한 스킬

1. **orchestrating**: 복잡한 문제 분석
2. **data-analyzing**: 데이터 지표 검증
3. **benchmarking**: 경쟁사 비교
```

## 리소스

이 스킬은 다음 리소스를 포함합니다:

### references/

- **mcp_development.md**: MCP 서버 개발 가이드
  - MCP 구조 및 개발 단계
  - 도구/리소스 설계 원칙
  - 실전 예시 (Cafe24 Meeting MCP)
  - 테스트 및 디버깅 방법

- **skills_development.md**: Skills 개발 가이드
  - Skills 구조 및 개발 프로세스
  - Progressive Disclosure 원칙
  - 실전 예시 (data-analyzing, benchmarking)
  - 네이밍 컨벤션 및 베스트 프랙티스

- **workflow_patterns.md**: 워크플로우 패턴
  - Brainstorm → Plan → Execute 패턴 상세
  - 특수 워크플로우 (Jira 분석, 데이터 검증, 경쟁사 비교)
  - 워크플로우 선택 가이드
  - 전문 스킬 통합 방법

### assets/

- **CLAUDE_md_template.md**: CLAUDE.md 템플릿
  - 프로젝트 개요 섹션
  - 워크플로우 정의
  - 전문 스킬 활용
  - 문서 작성 가이드

- **mcp-server-template/**: MCP 서버 템플릿
  - `server.py`: 기본 MCP 서버 구조
  - `README.md`: 사용 방법 및 커스터마이징 가이드
  - 도구 정의 및 실행 로직 예시

## 베스트 프랙티스

### MCP 서버 개발

1. **도구는 단순하게**: 복잡한 로직은 분리
2. **설명은 구체적으로**: Claude가 언제 사용할지 명확히
3. **에러는 명확하게**: 사용자가 이해할 수 있는 메시지
4. **캐싱 활용**: 반복 호출되는 데이터는 캐싱

### Skills 개발

1. **구체적인 예시부터**: 최소 3개 이상의 시나리오
2. **description은 트리거 조건**: "~할 때 사용" 형식
3. **SKILL.md는 간결하게**: 상세 내용은 references/
4. **반복 개선**: 실사용 → 발견 → 개선

### 워크플로우 설계

1. **단계 건너뛰지 않기**: 각 단계는 다음 단계의 품질 보장
2. **산출물 명확히**: 각 단계의 산출물 문서화
3. **전문 스킬 적시 활용**: 필요한 시점에 적절한 스킬 호출
4. **문서화는 필수**: 모든 워크플로우는 Wiki에 업로드

### CLAUDE.md 작성

1. **프로젝트 특성 반영**: 일반적인 내용 + 프로젝트 특수사항
2. **워크플로우 명확히**: 팀원 모두가 이해할 수 있게
3. **스킬 사용 규칙**: 언제, 어떻게 사용할지 명시
4. **지속적 업데이트**: 프로젝트 진행에 따라 갱신

## 사용 예시

### 예시 1: MCP 서버 개발

```
사용자: "Slack과 연동하는 MCP 서버를 만들고 싶어"

Claude: "claude-code-expert 스킬을 사용하여 Slack MCP 서버를 개발하겠습니다."

1. 요구사항 정의
   Q: 어떤 기능이 필요한가요?
   A: 메시지 전송, 채널 목록 조회, 스레드 답장

2. 템플릿 복사 및 커스터마이징
   - mcp-server-template을 slack-mcp-server로 복사
   - post_message, list_channels, reply_thread 도구 추가
   - Slack API 클라이언트 통합

3. 구현 가이드
   [references/mcp_development.md 참조하여 상세 구현]

4. MCP 설정 추가
   [.claude/mcp_settings.json 설정 예시 제공]
```

### 예시 2: Skills 개발

```
사용자: "데이터 검증 스킬을 만들고 싶어"

Claude: "claude-code-expert 스킬을 사용하여 데이터 검증 스킬을 개발하겠습니다."

1. 사용 예시 수집
   - "이 계산식이 맞는지 검증해줘"
   - "API 응답 데이터가 완전한지 확인해줘"
   - "지표 정의가 GA4 원칙에 맞는지 체크해줘"

2. 리소스 계획
   - references/validation_framework.md (검증 프레임워크)
   - references/data_quality_checklist.md (품질 체크리스트)

3. SKILL.md 작성
   [references/skills_development.md 참조하여 작성]

4. 패키징
   [scripts/package_skill.py 사용]
```

### 예시 3: CLAUDE.md 작성

```
사용자: "새 프로젝트를 위한 CLAUDE.md를 작성해줘. E-commerce 대시보드 프로젝트야."

Claude: "claude-code-expert 스킬을 사용하여 E-commerce 대시보드 프로젝트의 CLAUDE.md를 작성하겠습니다."

1. 템플릿 복사
   [CLAUDE_md_template.md 복사]

2. 프로젝트 정보 입력
   - 프로젝트명: E-commerce Dashboard
   - 목적: 실시간 매출 분석 및 인사이트 제공
   - 타겟: 쇼핑몰 운영자

3. 워크플로우 정의
   - Brainstorm → Plan → Execute 적용
   - 데이터 분석 워크플로우 추가 (data-analyzing 스킬)

4. 협업 도구 정보
   - Jira 프로젝트 키
   - Slack 채널
   - Wiki 구조

[완성된 CLAUDE.md 제공]
```

## 주의사항

1. **MCP 서버 보안**
   - API 키는 환경 변수로 관리
   - 민감한 정보는 로그에 남기지 않기
   - 사용자 입력은 항상 검증

2. **Skills 품질**
   - description은 명확하게 (Claude가 언제 사용할지)
   - 테스트 후 배포
   - 버전 관리

3. **워크플로우 적용**
   - 단계 건너뛰지 않기
   - 산출물 문서화
   - 전문 스킬 적시 활용

4. **CLAUDE.md 관리**
   - 프로젝트 진행에 따라 업데이트
   - 팀원과 공유 및 피드백
   - 버전 관리 (Git)

## 참고 자료

### 공식 문서
- MCP 공식 문서: https://modelcontextprotocol.io
- Claude Code 문서: https://claude.com/claude-code

### 프로젝트 예시
- Cafe24 PRO 리포트: `./CLAUDE.md`
- MCP 서버: `.claude/mcp_settings.json`
- Skills: `.claude/skills/`

### 관련 스킬
- `skill-creator`: Skills 생성 가이드 (Anthropic 공식)
- `1-orchestrating`: 복잡한 문제 분석 및 스킬 조율
- `3-data-analyzing`: 데이터 지표 검증
- `2-benchmarking`: 경쟁사 비교 분석
