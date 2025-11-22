---
name: data-analyzing
description: Google Analytics 4 방법론 기반 PRO 리포트 데이터 분석 전문 스킬. 지표 정의, 계산식 검증, 데이터 정합성 보장. orchestrating 스킬의 데이터 전문가로 동작.
---

# Data Analyzing

## 핵심 역할

GA4 방법론으로 PRO 리포트 지표를 정의하고 검증하는 데이터 전문가

**사용 시기:**
- 새로운 지표 추가/수정
- 계산식 검증
- API 데이터 매핑
- 데이터 오류 디버깅

## GA4 5대 원칙

### 1. Event-Based (이벤트 기반)
모든 인터랙션을 이벤트로 추적
- 구매: `purchase`
- 카트 추가: `add_to_cart`
- PRO 기능 사용: `pro_feature_used`

### 2. User-Centric (사용자 중심)
사용자 여정 중심 분석
- 고객 LTV = 누적 매출 / 사용 기간
- 참여도 = 월별 PRO 기능 사용 빈도

### 3. Predictive (예측 지표)
과거 데이터 기반 미래 예측
- 성장 가능성 = 현재 성장률 + 업종 평균
- 이탈 위험도 = PRO 기능 미사용 기간

### 4. Attribution (기여도 분석)
다중 채널/기능 기여도 측정
```
PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출
중복 방지: 하나의 주문은 하나의 기여도만
우선순위: 채널 > 프로모션 > CRM > SEO
```

### 5. Privacy-First (프라이버시 우선)
최소 데이터 수집, 익명화/집계 활용

---

## 지표 정의 템플릿

```yaml
지표명: [한글명]
영문명: [English Name]
정의: [1-2문장]

계산식: |
  [수식]

데이터 소스:
  - API: [엔드포인트]
  - 필드: [필드명]
  - 기간: [집계 기간]

단위: [원, %, 건, 시간]
반올림: [규칙]

예외 처리:
  - NULL: [처리]
  - 0: [처리]
  - 음수: [처리]

인사이트:
  - 기본: [기본 메시지]
  - 비교: [비교 메시지]
  - 넛지: [액션 유도]
```

**예시:**
```yaml
지표명: PRO 매출 기여도
영문명: PRO Revenue Contribution
정의: PRO 기능을 통해 발생한 매출 합계

계산식: |
  SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출

데이터 소스:
  - API: CA 2.0 /ca2/attribution/traffic-analysis
  - 필드: order_amount, source
  - 기간: 월간

단위: 원
반올림: 정수

예외 처리:
  - NULL: 0원
  - 0: 넛지 표시
  - 음수: 오류

인사이트:
  - 기본: "PRO가 만들어준 매출은 {금액}원"
  - 비교: "지난달 대비 {증감률}% {증가/감소}"
  - 넛지: "SEO 기능 활성화 권장"
```

---

## 검증 5단계

### 1. Accuracy (정확성)
- [ ] 데이터 소스 명확
- [ ] 계산식 논리적
- [ ] 단위 일관
- [ ] 0으로 나누기 방지

### 2. Completeness (완전성)
- [ ] 필수 필드 존재
- [ ] NULL/0/음수 처리 정의
- [ ] 예외 상황 대응

### 3. Consistency (일관성)
- [ ] 동일 지표 동일 값
- [ ] 합계 = 부분합
- [ ] 단위/반올림 일치

### 4. Timeliness (시의성)
- [ ] 업데이트 주기 명확 (PRO: 매월 3일)
- [ ] 지연 고려 (D+2)

### 5. Interpretability (해석 가능성)
- [ ] 사용자 이해 가능 용어
- [ ] 인사이트 명확
- [ ] 액션 가능

---

## 인사이트 패턴

```python
# 패턴 1: 절대값 + 맥락
f"지난달 대비 {증감률}% 증가한 {금액}원"

# 패턴 2: 벤치마크 비교
f"업종 평균({평균}) 대비 {비율}% 높은 수준"

# 패턴 3: 시간/비용 환산
f"절약한 {시간}시간으로 {활동} 가능"

# 패턴 4: 액션 유도
f"{기능} 활성화로 매출 증대 가능"
```

**Good:**
- "지난달 대비 15% 증가한 1,234,567원"
- "업종 평균(80만원) 대비 154% 높음"

**Bad:**
- "매출: 1,234,567원" (맥락 없음)
- "conversion_rate: 0.025" (전문 용어)

---

## 예외 처리 표준

### NULL 값
```python
def handle_null(value, default=0):
    return value if value is not None else default
```

### 0으로 나누기
```python
def safe_divide(numerator, denominator, default=0):
    if denominator == 0 or denominator is None:
        return default
    return numerator / denominator
```

### 음수 값
```python
def validate_positive(value, field_name):
    if value < 0:
        logger.error(f"{field_name} 음수: {value}")
        return 0
    return value
```

---

## Workflow

### 새 지표 정의
1. 비즈니스 질문 정의
2. GA4 템플릿 작성 (`references/ga4_analysis_framework.md` 참고)
3. 데이터 소스 확인 (`references/pro_report_data_schema.md` 참고)
4. 계산식 설계 (safe_divide, 음수 처리)
5. 검증 스크립트 실행 (`python scripts/validate_metric.py`)
6. 샘플 데이터 테스트 (정상/NULL/0/음수)
7. 인사이트 작성 (기본/비교/넛지)

### 기존 지표 검증
1. 검증 체크리스트 (5단계)
2. 계산식 검증 (`validator.validate_calculation()`)
3. API 응답 확인 (필드/타입/범위)
4. 예외 케이스 테스트

---

## Resources

### references/
- **ga4_analysis_framework.md**: GA4 철학, 검증 체크리스트, 지표 템플릿
- **pro_report_data_schema.md**: API 매핑, 핵심 지표 정의, 타입별 처리

### scripts/
- **validate_metric.py**: 지표 정의 검증, 계산식 테스트

**사용:**
```python
from scripts.validate_metric import MetricValidator

validator = MetricValidator()
results = validator.validate_metric_definition(metric)
validator.print_results()
```

---

## Best Practices

### DO
- GA4 템플릿으로 모든 지표 정의
- 예외 처리 3가지(NULL, 0, 음수) 필수
- 액션 가능한 인사이트
- 검증 스크립트 자동 검증
- 사용자 이해 가능 용어

### DON'T
- 계산식만 작성 (설명 생략)
- 예외 처리 누락
- 전문 용어 남발
- 맥락 없는 숫자
- 0으로 나누기 방지 누락

---

**이 스킬은 orchestrating 스킬의 전문가로 동작합니다.**
