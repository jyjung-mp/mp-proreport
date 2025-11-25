# Claude Code Expert 스킬

Claude Code를 효과적으로 활용하기 위한 종합 전문가 스킬입니다.

## 개요

이 스킬은 다음 영역을 지원합니다:

- **MCP 서버 개발**: 외부 서비스 연동
- **Skills 개발**: 재사용 가능한 전문 스킬 생성
- **워크플로우 설계**: Brainstorm → Plan → Execute 패턴
- **CLAUDE.md 작성**: 프로젝트별 작업 지침서

## 사용 방법

### 1. MCP 서버 개발

```
사용자: "Slack과 연동하는 MCP 서버를 만들고 싶어"

Claude가 자동으로 이 스킬을 사용하여:
1. 요구사항 정의 질문
2. MCP 서버 템플릿 제공
3. 상세 구현 가이드
4. 테스트 방법 안내
```

### 2. Skills 개발

```
사용자: "PDF 편집 스킬을 만들고 싶어"

Claude가 자동으로:
1. 구체적인 사용 예시 수집
2. 리소스 계획 (scripts, references, assets)
3. SKILL.md 작성 가이드
4. 검증 및 패키징 지원
```

### 3. 워크플로우 설계

```
사용자: "효율적인 기획 워크플로우를 구축하고 싶어"

Claude가 자동으로:
1. Brainstorm → Plan → Execute 패턴 적용
2. 전문 스킬 통합 방법 제시
3. 체크리스트 및 산출물 정의
```

### 4. CLAUDE.md 작성

```
사용자: "새 프로젝트에 맞는 CLAUDE.md를 작성해줘"

Claude가 자동으로:
1. 템플릿 제공
2. 프로젝트 정보 입력 가이드
3. 워크플로우 및 스킬 매핑
4. 커스터마이징 지원
```

## 구조

```
0-claude-code-expert/
├── SKILL.md                              # 메인 스킬 정의
├── README.md                             # 이 파일
├── references/                           # 참고 문서
│   ├── mcp_development.md               # MCP 서버 개발 가이드
│   ├── skills_development.md            # Skills 개발 가이드
│   └── workflow_patterns.md             # 워크플로우 패턴
└── assets/                               # 템플릿 및 에셋
    ├── CLAUDE_md_template.md            # CLAUDE.md 템플릿
    └── mcp-server-template/             # MCP 서버 템플릿
        ├── server.py                    # 서버 코드
        └── README.md                    # 사용 가이드
```

## 주요 기능

### 1. MCP 서버 템플릿

[assets/mcp-server-template/](assets/mcp-server-template/)에서 제공하는 템플릿:

- 기본 MCP 서버 구조
- 도구(Tool) 정의 예시
- 에러 처리 패턴
- 로깅 및 디버깅 설정

**사용법:**
```bash
cp -r .claude/skills/0-claude-code-expert/assets/mcp-server-template/ ~/my-mcp-server/
```

### 2. CLAUDE.md 템플릿

[assets/CLAUDE_md_template.md](assets/CLAUDE_md_template.md)에서 제공하는 템플릿:

- 프로젝트 개요 섹션
- 워크플로우 정의
- 전문 스킬 활용
- 문서 작성 가이드
- 협업 가이드라인

**사용법:**
```bash
cp .claude/skills/0-claude-code-expert/assets/CLAUDE_md_template.md ./CLAUDE.md
```

### 3. 상세 가이드

#### MCP 개발 가이드
[references/mcp_development.md](references/mcp_development.md)

- MCP 구조 및 개발 단계
- 도구/리소스 설계 원칙
- 실전 예시 (Cafe24 Meeting MCP)
- 테스트 및 디버깅

#### Skills 개발 가이드
[references/skills_development.md](references/skills_development.md)

- Skills 구조 및 개발 프로세스
- Progressive Disclosure 원칙
- 실전 예시 (data-analyzing, benchmarking)
- 네이밍 컨벤션 및 베스트 프랙티스

#### 워크플로우 패턴
[references/workflow_patterns.md](references/workflow_patterns.md)

- Brainstorm → Plan → Execute 패턴 상세
- 특수 워크플로우 (Jira 분석, 데이터 검증, 경쟁사 비교)
- 워크플로우 선택 가이드
- 전문 스킬 통합 방법

## 베스트 프랙티스

### MCP 서버 개발
1. 도구는 단순하게 (하나의 도구 = 하나의 작업)
2. 설명은 구체적으로 (Claude가 언제 사용할지)
3. 에러는 명확하게 (사용자가 이해 가능)
4. 캐싱 활용 (반복 호출 최적화)

### Skills 개발
1. 구체적인 예시부터 (최소 3개 시나리오)
2. description은 트리거 조건
3. SKILL.md는 간결하게 (상세는 references/)
4. 반복 개선 (실사용 → 개선)

### 워크플로우 설계
1. 단계 건너뛰지 않기
2. 산출물 명확히 문서화
3. 전문 스킬 적시 활용
4. 문서화는 필수 (Wiki)

### CLAUDE.md 작성
1. 프로젝트 특성 반영
2. 워크플로우 명확히 정의
3. 스킬 사용 규칙 명시
4. 지속적 업데이트

## 실전 예시

### Cafe24 PRO 리포트 프로젝트

이 스킬을 활용하여 구축한 실제 프로젝트:

- **CLAUDE.md**: 프로젝트 루트의 `CLAUDE.md` 참조
- **MCP 서버**: cafe24-meeting, wiki, jira, slack
- **전문 스킬**: orchestrating, benchmarking, data-analyzing
- **워크플로우**: Brainstorm → Plan → Execute

## 관련 스킬

- **skill-creator**: Skills 생성 가이드 (Anthropic 공식)
- **1-orchestrating**: 복잡한 문제 분석 및 스킬 조율
- **2-benchmarking**: 경쟁사 비교 분석
- **3-data-analyzing**: 데이터 지표 검증
- **4-codex**: OpenAI Codex CLI 통합
- **5-system-document**: 시스템 문서화

## 참고 자료

### 공식 문서
- MCP: https://modelcontextprotocol.io
- Claude Code: https://claude.com/claude-code

### 프로젝트 예시
- Cafe24 PRO 리포트: `./CLAUDE.md`
- MCP 설정: `.claude/mcp_settings.json`
- Skills: `.claude/skills/`

---

**작성자**: Claude (Sonnet 4.5)
**작성일**: 2025-11-25
**버전**: 1.0.0
