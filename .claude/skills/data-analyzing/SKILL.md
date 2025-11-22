---
name: data-analyzing
description: Google Analytics 4 방법론 기반 PRO 리포트 데이터 분석 전문 스킬. 지표 정의, 계산식 검증, API 매핑, 예외 처리 등 데이터 정합성을 보장하는 체계적 분석 프로세스를 제공. 이벤트 기반 모델, 사용자 중심 분석, 기여도 모델링 등 GA4 핵심 원칙 적용. orchestrating 스킬을 지원하는 데이터 전문가로, 지표 관련 모든 작업에 사용.
---

# Data Analyzing

## Overview

Google Analytics 4(GA4)의 데이터 분석 철학과 방법론을 기반으로 PRO 리포트의 지표를 정의하고 검증하는 전문 스킬입니다.

**핵심 역할:**
- 지표 정의서 작성 (계산식, 데이터 소스, 예외 처리)
- 데이터 정합성 검증 (정확성, 완전성, 일관성)
- API 응답 데이터 매핑
- GA4 원칙 적용 (이벤트 기반, 사용자 중심, 기여도 분석)

**사용 시기:**
- 새로운 지표 추가/수정 시
- 계산식 검증이 필요할 때
- API 데이터 매핑 시
- 데이터 오류 디버깅 시
- 지표 정의서 작성 시

## Core Capabilities

### 1. GA4 분석 프레임워크 적용

Google Analytics 4의 5가지 핵심 원칙을 PRO 리포트에 적용:

#### 1-1. Event-Based Model (이벤트 기반)
모든 사용자 인터랙션을 이벤트로 추적하고 분석

**PRO 리포트 적용:**
```
구매 이벤트 → purchase
카트 추가 → add_to_cart
페이지뷰 → page_view
PRO 기능 사용 → pro_feature_used
```

#### 1-2. User-Centric Analysis (사용자 중심)
세션이 아닌 사용자 여정 중심 분석

**핵심 지표:**
- User Lifetime Value (고객 생애 가치)
- User Engagement (참여도)
- User Retention (재방문율)
- Cohort Analysis (코호트 분석)

**PRO 리포트 적용:**
- 고객 LTV = 누적 매출 / 사용 기간
- 참여도 = 월별 PRO 기능 사용 빈도
- 재방문율 = 월별 활성 사용자 비율

#### 1-3. Predictive Metrics (예측 지표)
과거 데이터 기반 미래 행동 예측

**GA4 예측 지표:**
- Purchase probability (구매 가능성)
- Churn probability (이탈 확률)
- Revenue prediction (예상 수익)

**PRO 리포트 적용:**
- 성장 가능성 = 현재 성장률 + 업종 평균 비교
- 이탈 위험도 = PRO 기능 미사용 기간
- 예상 매출 = 추세 기반 예측

#### 1-4. Attribution Modeling (기여도 분석)
다중 채널/기능의 기여도 정확 측정

**GA4 기여 모델:**
- Data-driven attribution (데이터 기반)
- Last-click (마지막 터치포인트)
- First-click (첫 터치포인트)
- Linear (균등 분배)
- Time decay (시간 가중)

**PRO 리포트 적용:**
```
PRO 매출 = SEO 매출 + CRM 매출 + 프로모션 매출 + 채널 매출

중복 방지 규칙:
- 하나의 주문은 하나의 기여도만 계산
- 우선순위: 채널 > 프로모션 > CRM > SEO
```

#### 1-5. Privacy-First (프라이버시 우선)
데이터 수집 최소화, 사용자 동의 기반

**원칙:**
- 필수 데이터만 수집
- 익명화/집계 데이터 활용
- 개인 식별 정보 제외

---

### 2. 지표 정의 프로세스

모든 지표는 GA4 기반 템플릿으로 정의:

#### 필수 정의 항목

```yaml
지표명: [한글명]
영문명: [English Name]
정의: [명확한 정의 1-2문장]

계산식: |
  [상세 계산 로직]
  - 변수 1: [설명]
  - 변수 2: [설명]

데이터 소스:
  - API: [엔드포인트]
  - 필드: [필드명]
  - 기간: [집계 기간]

단위: [원, %, 건, 시간 등]
반올림: [규칙]

예외 처리:
  - NULL: [처리 방법]
  - 0: [처리 방법]
  - 음수: [처리 방법]

비즈니스 규칙:
  - [조건]: [처리]

인사이트:
  - 기본: [기본 메시지]
  - 비교: [비교 메시지]
  - 넛지: [액션 유도]
```

#### 작성 예시

```yaml
지표명: PRO 매출 기여도
영문명: PRO Revenue Contribution
정의: PRO 기능(SEO, CRM, 프로모션, 채널)을 통해 발생한 매출 합계

계산식: |
  PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출

  - SEO_매출: CA 2.0 (source = "organic")
  - CRM_매출: CA 2.0 (source = "crm")
  - 프로모션_매출: 프로모션 API (discount_applied = true)
  - 채널_매출: 마켓플러스 API (paid_order_amount)

데이터 소스:
  - API: CA 2.0 /ca2/attribution/traffic-analysis
  - 필드: order_amount, source
  - 기간: 월간 (1일 00:00 ~ 말일 23:59)

단위: 원 (KRW)
반올림: 정수 (소수점 없음)

예외 처리:
  - NULL: 0원으로 처리
  - 0원: "아직 PRO 매출이 발생하지 않았습니다" 넛지 표시
  - 음수: 오류 로깅 (음수 매출 불가)

비즈니스 규칙:
  - 중복 집계 방지: 하나의 주문은 하나의 기여도만
  - 우선순위: 채널 > 프로모션 > CRM > SEO

인사이트:
  - 기본: "PRO가 만들어준 매출은 {금액}원입니다"
  - 비교: "지난달 대비 {증감률}% {증가/감소}"
  - 넛지: "SEO 기능을 활성화하면 매출을 늘릴 수 있어요"
```

---

### 3. 데이터 검증 체크리스트

GA4 기반 5가지 검증 항목:

#### 3-1. 데이터 정확성 (Accuracy)
- [ ] 데이터 소스가 명확한가?
- [ ] 계산식이 논리적으로 정확한가?
- [ ] 단위가 일관되는가? (원, 달러, 건수 등)
- [ ] 반올림 규칙이 명시되어 있는가?
- [ ] 0으로 나누기가 방지되었는가?

**검증 방법:**
```python
# 계산식에 나눗셈이 있는지 확인
if '/' in formula:
    # safe_divide 함수 사용 권장
    assert 'safe_divide' in formula or 'if denominator != 0' in formula
```

#### 3-2. 데이터 완전성 (Completeness)
- [ ] 모든 필수 필드가 존재하는가?
- [ ] NULL/0 값 처리 방법이 정의되어 있는가?
- [ ] 예외 상황 대응이 명확한가?
- [ ] 데이터 소스에 API, 필드, 기간이 모두 명시되었는가?

**검증 방법:**
```python
required_fields = ['지표명', '영문명', '정의', '계산식', '데이터_소스', '단위', '예외_처리']
for field in required_fields:
    assert field in metric_definition, f"필수 필드 {field} 누락"
```

#### 3-3. 데이터 일관성 (Consistency)
- [ ] 동일 지표가 여러 곳에서 동일한 값을 보이는가?
- [ ] 합계가 부분합과 일치하는가?
- [ ] 기간별 비교가 일관된 기준인가?
- [ ] 단위와 반올림 규칙이 일치하는가?

**검증 예시:**
```python
# 단위가 '원'이면 소수점 반올림 불필요
if unit == '원':
    assert '정수' in rounding_rule or '0' in rounding_rule
```

#### 3-4. 데이터 시의성 (Timeliness)
- [ ] 데이터 업데이트 주기가 명확한가?
- [ ] 지연 시간(latency)이 고려되었는가?
- [ ] 실시간/배치 구분이 명확한가?

**PRO 리포트 기준:**
- 업데이트: 매월 3일 오전 8시
- 데이터 기준: 전월 1일 ~ 말일
- 지연: D+2 (2일 후 확정)

#### 3-5. 데이터 해석 가능성 (Interpretability)
- [ ] 사용자가 이해할 수 있는 용어인가?
- [ ] 인사이트가 명확히 전달되는가?
- [ ] 액션 가능한 정보인가?

**좋은 인사이트 예시:**
- ✅ "지난달 대비 15% 증가한 1,234,567원"
- ✅ "업종 평균(80만원) 대비 154% 높은 수준"
- ✅ "PRO 덕분에 절약한 시간: 24시간 (100만원 상당)"

**나쁜 인사이트 예시:**
- ❌ "매출: 1,234,567원" (맥락 없음)
- ❌ "conversion_rate: 0.025" (전문 용어)

---

### 4. API 데이터 매핑

각 API 엔드포인트에서 필요한 데이터 추출:

#### CA 2.0 API 매핑

**엔드포인트:** `/ca2/sales/overview`
```json
{
  "shop_id": "12345",
  "start_date": "2024-01-01",
  "end_date": "2024-01-31",
  "data": {
    "order_amount": 1234567,  // → 자사몰 매출
    "order_count": 234,       // → 주문 건수
    "avg_order_value": 5275   // → 평균 주문 금액
  }
}
```

**매핑:**
- `order_amount` → 자사몰 매출
- `order_count` → 주문 건수
- `order_amount / order_count` → 평균 주문 금액 (검증)

#### FAS API 매핑

**엔드포인트:** `/tasks/pro/report`
```json
{
  "shop_id": "12345",
  "month": "2024-01",
  "tasks": {
    "product_registration": {
      "count": 150,           // → 상품 등록 건수
      "saved_minutes": 1500   // → 절약 시간 (분)
    },
    "order_processing": {
      "count": 234,
      "saved_minutes": 1170
    }
  }
}
```

**매핑:**
- `Σ count` → 총 처리 건수
- `Σ saved_minutes / 60` → 절약 시간 (시간)
- `절약 시간 × 10,000` → 절약 비용 (원)

---

### 5. 계산식 검증 스크립트

`scripts/validate_metric.py` 사용:

#### 기본 사용법

```python
from scripts.validate_metric import MetricValidator

# 지표 정의
metric = {
    '지표명': 'PRO 매출 기여도',
    '영문명': 'PRO Revenue Contribution',
    '계산식': 'SEO_매출 + CRM_매출 + 프로모션_매출',
    '데이터_소스': {'API': 'CA 2.0', '필드': 'order_amount'},
    '단위': '원',
    '예외_처리': {'NULL': '0', '0': '넛지', '음수': '오류'}
}

# 검증 실행
validator = MetricValidator()
results = validator.validate_metric_definition(metric)
validator.print_results()
```

#### 계산식 테스트

```python
# 샘플 데이터로 계산식 테스트
sample_data = {
    'SEO_매출': 500000,
    'CRM_매출': 300000,
    '프로모션_매출': 200000
}

result = validator.validate_calculation(
    metric['계산식'],
    sample_data
)

# 결과 확인
if result['valid']:
    print(f"계산 성공: {result['value']:,}원")
else:
    print(f"오류: {result['errors']}")
```

#### 검증 결과 예시

```
📊 검증 결과 요약
  오류: 0개
  경고: 1개
  정보: 0개

⚠️  경고:
  - 완전성 [예외_처리]: '음수' 값 처리 방법이 정의되지 않았습니다

🧮 계산식 테스트:
✅ 계산 성공: 1,000,000원
```

---

### 6. 타입별 데이터 처리

PRO 리포트는 매출 규모에 따라 3가지 타입으로 분기:

#### 타입 1 (Full)
**조건:** 자사몰 매출 ≥ 100만원

**노출 지표:**
- 상단 카드 3개 (PRO 매출, 절약 시간, 혜택)
- 매출 추이 (자사몰 + 마켓)
- PRO 매출 기여도 (SEO/CRM/프로모션/채널)
- KPI 6개 (전환율, 평균 주문 금액 등)
- PRO 처리 업무

#### 타입 2 (Lite)
**조건:** 자사몰 < 100만원 AND 연동 마켓 ≥ 100만원

**노출 지표:**
- 상단 카드 3개
- 매출 추이 (마켓 중심)
- PRO 성과 (간소화)

**생략 지표:**
- KPI 6개
- 자사몰 상세 분석

#### 타입 3 (Mini)
**조건:** 자사몰·연동 마켓 모두 < 100만원

**노출 지표:**
- 상단 카드 2개 (PRO 매출 제외)
- PRO 성과만

**생략 지표:**
- 매출 관련 모든 지표
- 성장 가능성 인사이트만 표시

---

### 7. 인사이트 생성 규칙

GA4의 Context is King 원칙 적용:

#### 기본 패턴

```python
# 패턴 1: 절대값 + 맥락
f"지난달 대비 {증감률}% 증가한 {금액}원"

# 패턴 2: 벤치마크 비교
f"업종 평균({평균값}) 대비 {비율}% 높은 수준"

# 패턴 3: 시간/비용 환산
f"절약한 {시간}시간으로 {활동}을 할 수 있어요"

# 패턴 4: 액션 유도
f"{기능}을 활성화하면 매출을 늘릴 수 있어요"
```

#### 조건별 인사이트

```python
def generate_insight(current, previous, avg):
    """조건별 인사이트 생성"""

    # 성장세
    if current > previous * 1.1:
        growth_rate = ((current - previous) / previous) * 100
        return f"지난달 대비 {growth_rate:.1f}% 성장 중입니다"

    # 하락세
    elif current < previous * 0.9:
        decline_rate = ((previous - current) / previous) * 100
        return f"지난달 대비 {decline_rate:.1f}% 감소했습니다. 원인을 확인해보세요"

    # 평균 이상
    if current > avg * 1.2:
        ratio = (current / avg) * 100
        return f"PRO 평균({avg:,}원) 대비 {ratio:.0f}% 높은 수준입니다"

    # 개선 여지
    elif current < avg * 0.8:
        return f"평균보다 낮습니다. PRO 기능을 더 활용해보세요"

    # 보통
    return f"안정적인 수준을 유지하고 있습니다"
```

---

### 8. 예외 처리 규칙

모든 지표에 적용되는 표준 예외 처리:

#### NULL 값 처리

```python
def handle_null(value, default=0):
    """NULL 값을 기본값으로 처리"""
    return value if value is not None else default
```

**적용:**
- 매출 NULL → 0원
- 건수 NULL → 0건
- 비율 NULL → 0% (또는 "데이터 없음")

#### 0으로 나누기 방지

```python
def safe_divide(numerator, denominator, default=0):
    """0으로 나누기 방지"""
    if denominator == 0 or denominator is None:
        return default
    return numerator / denominator
```

**적용:**
- 전환율 = safe_divide(구매수, 방문자수) × 100
- 평균 = safe_divide(합계, 건수)

#### 음수 값 처리

```python
def validate_positive(value, field_name):
    """음수 값 검증"""
    if value < 0:
        logger.error(f"{field_name}이 음수입니다: {value}")
        return 0
    return value
```

**적용:**
- 매출 음수 → 오류 로깅 + 0 반환
- 건수 음수 → 오류 로깅 + 0 반환

---

### 9. GA4 대시보드 설계 원칙

#### Pyramid Structure (피라미드 구조)

상단에 핵심 지표, 하단으로 갈수록 상세 정보:

```
┌─────────────────────────────┐
│  핵심 카드 (3개)             │ ← 가장 중요
├─────────────────────────────┤
│  아바타 인사이트             │ ← 개인화
├─────────────────────────────┤
│  매출 추이                   │ ← 추세
├─────────────────────────────┤
│  PRO 성과                    │ ← 상세
└─────────────────────────────┘
```

#### Progressive Disclosure (점진적 공개)

- Level 1: 요약 (카드)
- Level 2: 상세 (클릭)
- Level 3: 분석 (드릴다운)

#### Color Psychology (색상 심리학)

- Green: 성장, 긍정 (↑ 15%)
- Red: 경고, 주의 (↓ 10%)
- Blue: 중립, 정보
- Orange: 액션 (CTA)

---

## Workflow

### 새 지표 정의 시

1. **비즈니스 질문 정의**
   - 무엇을 측정할 것인가?
   - 왜 이 지표가 필요한가?
   - 누가 사용하는가?

2. **GA4 템플릿 작성**
   - `references/ga4_analysis_framework.md` 참고
   - 필수 항목 모두 작성

3. **데이터 소스 확인**
   - `references/pro_report_data_schema.md` 참고
   - API 엔드포인트 존재 확인
   - 필요 필드 존재 확인

4. **계산식 설계**
   - 논리적 정확성 검증
   - 0으로 나누기 방지
   - 음수 처리 명시

5. **검증 스크립트 실행**
   ```bash
   python scripts/validate_metric.py
   ```

6. **샘플 데이터 테스트**
   - 정상 케이스
   - NULL 케이스
   - 0 케이스
   - 음수 케이스

7. **인사이트 작성**
   - 기본 메시지
   - 비교 메시지
   - 넛지 메시지

### 기존 지표 검증 시

1. **검증 체크리스트 실행**
   - 정확성 ✓
   - 완전성 ✓
   - 일관성 ✓
   - 시의성 ✓
   - 해석 가능성 ✓

2. **계산식 검증**
   ```python
   validator.validate_calculation(formula, sample_data)
   ```

3. **API 응답 확인**
   - 필드 존재 여부
   - 데이터 타입 일치
   - 범위 검증

4. **예외 케이스 테스트**
   - NULL 처리 확인
   - 0 처리 확인
   - 음수 처리 확인

---

## Resources

### references/

상세 참고 자료 (필요 시 읽기):

**ga4_analysis_framework.md**
- GA4 핵심 철학 5가지
- 데이터 검증 체크리스트
- 지표 정의 템플릿
- 대시보드 설계 원칙
- GA4 용어 사전

**pro_report_data_schema.md**
- API 엔드포인트 상세
- 핵심 지표 정의 (계산식, 예외 처리)
- 타입별 처리 규칙
- 데이터 업데이트 규칙

### scripts/

**validate_metric.py**
- 지표 정의 검증기
- 계산식 테스트
- 5가지 검증 항목 자동 체크

**사용법:**
```python
from scripts.validate_metric import MetricValidator

validator = MetricValidator()
results = validator.validate_metric_definition(metric)
validator.print_results()
```

---

## Best Practices

### DO (권장)

✅ 모든 지표는 GA4 템플릿으로 정의
✅ 계산식에 주석으로 설명 추가
✅ 예외 처리 3가지(NULL, 0, 음수) 필수 정의
✅ 인사이트는 액션 가능하게 작성
✅ 검증 스크립트로 자동 검증
✅ 샘플 데이터로 테스트
✅ 단위와 반올림 규칙 명시
✅ 사용자 이해 가능한 용어 사용

### DON'T (지양)

❌ 계산식만 작성하고 설명 생략
❌ 예외 처리 누락
❌ 전문 용어 남발 (conversion_rate → 구매 전환율)
❌ 맥락 없는 숫자만 표시
❌ 0으로 나누기 방지 누락
❌ 검증 없이 배포
❌ 일관되지 않은 단위/반올림
❌ 액션 불가능한 인사이트

---

## Examples

### 완벽한 지표 정의 예시

```yaml
지표명: 구매 전환율
영문명: Purchase Conversion Rate
정의: 방문자 대비 구매 완료 고객의 비율

계산식: |
  전환율(%) = safe_divide(구매_완료_수, 방문자_수) × 100

  - 구매_완료_수: status = "completed"인 주문 수
  - 방문자_수: 유니크 세션 수

데이터 소스:
  - API: CA 2.0 /ca2/conversion/rate
  - 필드: conversion_rate, sessions, transactions
  - 기간: 월간

단위: % (퍼센트)
반올림: 소수점 1자리

예외 처리:
  - NULL: 0%로 처리
  - 방문자 0: "아직 방문자가 없습니다" 표시
  - 음수: 오류 (음수 불가)

비즈니스 규칙:
  - 업종 평균: 1.5%
  - 우수: 2.0% 이상
  - 개선 필요: 1.0% 미만

인사이트:
  - 기본: "구매 전환율은 {비율}%입니다"
  - 비교: "업종 평균(1.5%) 대비 {차이}%p {높음/낮음}"
  - 넛지: "전환율이 낮습니다. 결제 프로세스를 간소화해보세요"
  - 성공: "우수한 전환율을 유지하고 있습니다"
```

### 인사이트 생성 예시

```python
# 좋은 예시
"지난달 대비 15% 증가한 1,234,567원"
"업종 평균(80만원) 대비 154% 높은 수준"
"절약한 24시간으로 신규 상품 12개를 등록할 수 있어요"
"SEO 기능을 활성화하면 월 평균 50만원 매출을 늘릴 수 있어요"

# 나쁜 예시
"매출: 1,234,567원"  # 맥락 없음
"conversion_rate: 0.025"  # 전문 용어
"좋음"  # 구체성 없음
"개선 필요"  # 액션 불명확
```

---

## Quick Reference

### GA4 5대 원칙
1. Event-Based (이벤트 기반)
2. User-Centric (사용자 중심)
3. Predictive (예측 지표)
4. Attribution (기여도 분석)
5. Privacy-First (프라이버시 우선)

### 검증 5대 항목
1. Accuracy (정확성)
2. Completeness (완전성)
3. Consistency (일관성)
4. Timeliness (시의성)
5. Interpretability (해석 가능성)

### 필수 예외 처리
- NULL → 기본값
- 0 (나누기) → safe_divide
- 음수 → 검증/로깅

### 인사이트 4가지 패턴
1. 절대값 + 맥락
2. 벤치마크 비교
3. 시간/비용 환산
4. 액션 유도
