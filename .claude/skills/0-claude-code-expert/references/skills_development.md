# Skills 개발 가이드

## Skills 개요

Skills는 Claude의 능력을 확장하는 모듈형 패키지입니다. 특정 도메인이나 작업에 대한 전문 지식, 워크플로우, 도구를 제공합니다.

## Skills 구조

### 기본 구성

```
skill-name/
├── SKILL.md (필수)
│   ├── YAML frontmatter (필수)
│   │   ├── name: (필수)
│   │   └── description: (필수)
│   └── Markdown 본문 (필수)
└── 리소스 (선택)
    ├── scripts/          - 실행 가능한 스크립트
    ├── references/       - 참고 문서
    └── assets/           - 템플릿, 이미지 등
```

## Skills 개발 프로세스

### 1단계: 구체적인 사용 예시 수집

**목적**: 스킬이 실제로 어떻게 사용될지 명확히 이해

**질문:**
- 이 스킬이 해결할 문제는?
- 사용자가 어떤 요청을 할 것인가?
- 어떤 작업을 자동화할 것인가?

**예시:**
```
사용자: "PDF를 90도 회전시켜줘"
사용자: "이 PDF를 병합해줘"
사용자: "PDF에서 특정 페이지만 추출해줘"

→ pdf-editor 스킬 필요
```

### 2단계: 재사용 가능한 리소스 계획

**각 사용 예시 분석:**
1. 작업을 처음부터 어떻게 수행할까?
2. 반복적으로 수행할 때 무엇이 도움이 될까?

**리소스 유형 결정:**

#### scripts/ (스크립트)
**사용 시기:**
- 동일한 코드를 반복 작성하는 경우
- 결정론적 신뢰성이 필요한 경우

**예시:**
```bash
scripts/
├── rotate_pdf.py        # PDF 회전
├── merge_pdfs.py        # PDF 병합
└── extract_pages.py     # 페이지 추출
```

#### references/ (참고 문서)
**사용 시기:**
- Claude가 작업 중 참조할 문서
- 스키마, API 문서, 정책 등

**예시:**
```bash
references/
├── api_schema.md        # API 스키마
├── business_rules.md    # 비즈니스 규칙
└── data_dictionary.md   # 데이터 사전
```

#### assets/ (에셋)
**사용 시기:**
- 최종 산출물에 사용될 파일
- 템플릿, 이미지, 폰트 등

**예시:**
```bash
assets/
├── template.html        # HTML 템플릿
├── logo.png            # 로고 이미지
└── boilerplate/        # 프로젝트 보일러플레이트
```

### 3단계: SKILL.md 작성

#### YAML Frontmatter

```yaml
---
name: skill-name
description: |
  스킬의 목적과 사용 시기를 명확히 설명.

  사용 시기:
  - 구체적인 상황 1
  - 구체적인 상황 2
  - 구체적인 상황 3
---
```

**작성 원칙:**
- `name`: 간결하고 설명적
- `description`: Claude가 언제 사용할지 명확히 (3인칭 시점)

#### Markdown 본문

**구조:**
```markdown
# 스킬 제목

## 개요
스킬의 목적과 가치 설명

## 사용 시기
구체적인 사용 시나리오

## 워크플로우
단계별 작업 설명

## 리소스
bundled resources 사용 방법

## 예시
실제 사용 예시
```

**작성 스타일:**
- 명령형/부정사 형태 사용
- "~해야 한다" 대신 "~하라"
- 객관적이고 명령적인 톤

### 4단계: 검증 및 패키징

#### 검증
```bash
# 스킬 검증
scripts/validate_skill.py path/to/skill-folder
```

**검증 항목:**
- YAML frontmatter 형식
- 필수 필드 존재
- description 품질
- 파일 구조

#### 패키징
```bash
# 스킬 패키징 (검증 + zip 생성)
scripts/package_skill.py path/to/skill-folder
```

**결과:**
- `skill-name.zip` 생성
- 배포 가능한 패키지

### 5단계: 반복 개선

**개선 워크플로우:**
1. 실제 작업에 스킬 사용
2. 어려움이나 비효율 발견
3. SKILL.md 또는 리소스 업데이트 방법 식별
4. 변경 구현 및 재테스트

## 실전 예시

### 예시 1: data-analyzing 스킬

#### 1단계: 사용 예시 수집
```
사용자: "PRO 매출 기여도 지표 검증해줘"
사용자: "예상 성장률 계산식 정의해줘"
사용자: "이 계산식이 맞는지 확인해줘"
```

#### 2단계: 리소스 계획
- **references/ga4_analysis_framework.md**: GA4 5대 원칙, 5-tier 검증
- **references/pro_report_data_schema.md**: PRO 리포트 데이터 스키마
- **scripts/**: 필요 없음 (분석 작업이므로)
- **assets/**: 필요 없음

#### 3단계: SKILL.md 작성
```markdown
---
name: data-analyzing
description: |
  GA4 방법론 기반 PRO 리포트 데이터 분석 전문 스킬.
  지표 정의, 계산식 검증, 데이터 정합성 보장.

  사용 시기:
  - 데이터 지표 정의 및 검증
  - 계산식 검증
  - API 매핑 및 데이터 소스 확인
---

# Data Analyzing

## GA4 5대 원칙
1. Event-Based Model
2. User-Centric Analysis
...

## 5-tier 검증
1. Accuracy (정확성)
2. Completeness (완전성)
...

## 워크플로우
1. 지표 정의
2. 계산식 검증
3. 예외 처리 정의
...
```

### 예시 2: benchmarking 스킬

#### 1단계: 사용 예시 수집
```
사용자: "Shopify 리포트와 PRO 리포트를 비교해줘"
사용자: "GA4 대시보드 설계 원칙 조사해줘"
```

#### 2단계: 리소스 계획
- **references/global_ecommerce_targets.md**: 글로벌 E-commerce 타겟 목록
- **scripts/**: 필요 없음
- **assets/**: 필요 없음

#### 3단계: SKILL.md 작성
```markdown
---
name: benchmarking
description: |
  글로벌 E-commerce TOP 기업과 비교 분석하는 전문가 스킬.
  최신(2024-2025) Fact 기반 정보를 WebSearch/WebFetch로 수집.

  사용 시기:
  - 글로벌 E-commerce 기업 비교 분석
  - 업계 베스트 프랙티스 조사
---

# Benchmarking

## 비교 대상
- Shopify
- Google Analytics 4
- Amazon Seller Central

## 워크플로우
1. 비교 대상 선정
2. 최신 정보 수집 (WebSearch)
3. 비교 분석표 작성
4. 실행 가능한 권장사항 도출
5. Wiki 문서화
```

## Progressive Disclosure 원칙

### 3단계 로딩 시스템

1. **Metadata (항상 로드)**
   - name + description
   - ~100 단어

2. **SKILL.md 본문 (스킬 트리거 시)**
   - <5k 단어
   - 핵심 워크플로우

3. **Bundled Resources (필요 시)**
   - 무제한
   - Claude가 판단하여 로드

### 원칙 적용

**SKILL.md에 포함:**
- 핵심 워크플로우
- 사용 시기
- 간단한 예시

**references/에 분리:**
- 상세한 문서
- 스키마 정의
- 긴 예시

**예시:**
```markdown
# SKILL.md (간결하게)
## 데이터 검증
상세한 검증 프레임워크는 `references/ga4_analysis_framework.md` 참조

# references/ga4_analysis_framework.md (상세하게)
## GA4 5대 원칙
### 1. Event-Based Model
...
```

## 스킬 네이밍 컨벤션

### 프로젝트별 스킬 번호 체계

```
0-{skill-name}/     # 메타 스킬 (Claude Code 자체)
1-{skill-name}/     # 오케스트레이터
2-{skill-name}/     # 벤치마킹
3-{skill-name}/     # 데이터 분석
4-{skill-name}/     # 코드 관련
5-{skill-name}/     # 문서화
```

**장점:**
- 우선순위 명확
- 알파벳 정렬 시 순서 유지
- 확장 가능

### 폴더명 규칙

- 소문자 사용
- 하이픈(`-`) 구분
- 명확하고 설명적

**좋은 예:**
- `data-analyzing`
- `claude-code-expert`
- `system-document`

**나쁜 예:**
- `DataAnalyzing` (camelCase)
- `data_analyzing` (snake_case)
- `da` (약어)

## 베스트 프랙티스

1. **구체적인 예시부터 시작**
   - 추상적인 설계보다 실제 사용 예시
   - 최소 3개 이상의 구체적 시나리오

2. **description은 트리거 조건**
   - Claude가 언제 사용할지 명확히
   - "~할 때 사용" 형식

3. **SKILL.md는 간결하게**
   - 핵심만 포함
   - 상세 내용은 references/

4. **리소스는 목적별로 분리**
   - scripts: 실행 코드
   - references: 참고 문서
   - assets: 산출물용

5. **반복 개선**
   - 실사용 → 발견 → 개선
   - 한 번에 완벽하게 만들려 하지 말기

6. **문서화**
   - README 작성
   - 주석 추가
   - 사용 예시 포함

## 참고 자료

- Skill Creator 가이드: `.claude/plugins/marketplaces/anthropic-agent-skills/skill-creator/SKILL.md`
- 예시 스킬: `.claude/skills/`
- 초기화 스크립트: `scripts/init_skill.py`
- 패키징 스크립트: `scripts/package_skill.py`
