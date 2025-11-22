# PRO 리포트 데이터 스키마

## 핵심 데이터 소스

### 1. CA 2.0 API (Commerce Analytics)

**Base URL:** `https://ca-api-dev.hanpda.com`

#### 주요 엔드포인트

| 엔드포인트 | 용도 | 주요 필드 | 집계 기간 |
|-----------|------|-----------|----------|
| `/ca2/sales/overview` | 매출 종합 | `order_amount`, `order_count` | 일/주/월 |
| `/ca2/adsources/channels` | 채널별 분석 | `channel`, `order_amount`, `sessions` | 일/주/월 |
| `/ca2/conversion/rate` | 구매 전환율 | `conversion_rate`, `sessions`, `transactions` | 일/주/월 |
| `/ca2/attribution/traffic-analysis` | 트래픽 분석 | `sessions`, `referrer_domain`, `source` | 일/주/월 |

**인증:** Bearer Token (FAS에서 발급)

**파라미터:**
```json
{
  "shop_id": "string",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "aggregation": "daily|weekly|monthly"
}
```

---

### 2. FAS API (Fulfillment Automation Service)

**Base URL:** `https://extsvc-qa.hanpda.com`

#### 주요 엔드포인트

| 엔드포인트 | 용도 | 주요 필드 | 집계 기간 |
|-----------|------|-----------|----------|
| `/app-requests-list` | PRO 승인 목록 | `confirm_timestamp`, `status`, `shop_id` | - |
| `/tasks/pro/report` | PRO 작업 현황 | `execute_count`, `saved_time`, `report_type` | 월간 |
| `/tasks/report-metrics` | 월별 지표 | `avg_sales`, `total_benefits` | 월간 |

**인증:** API Key (환경변수)

---

### 3. 마켓 플러스 API

**Base URL:** `https://marketplus-api.hanpda.com`

#### 주요 엔드포인트

| 엔드포인트 | 용도 | 주요 필드 | 집계 기간 |
|-----------|------|-----------|----------|
| `/api/internal/v1/order/daily-sales` | 마켓 매출 | `paid_order_amount`, `market_name` | 일간 |

---

## 핵심 지표 정의

### 1. 상단 핵심 카드

#### 1-1. PRO가 만들어준 매출

```yaml
지표명: PRO 매출 기여도
영문명: PRO Revenue Contribution
정의: PRO 기능(SEO, CRM, 프로모션, 채널)을 통해 발생한 매출 합계
계산식: |
  PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출

  - SEO_매출: CA 2.0 (source = "organic")
  - CRM_매출: CA 2.0 (source = "crm" OR referrer LIKE "%cafe24.crm%")
  - 프로모션_매출: 프로모션 API (discount_applied = true)
  - 채널_매출: 마켓플러스 API (paid_order_amount)

데이터 소스:
  - API: CA 2.0 /ca2/attribution/traffic-analysis
  - 필드: order_amount, source, referrer_domain
  - 기간: 월간 (1일 00:00 ~ 말일 23:59)

단위: 원 (KRW)
반올림: 정수 (소수점 없음)

예외 처리:
  - NULL: 0원으로 처리
  - 0원: "아직 PRO 매출이 발생하지 않았습니다" 넛지 표시
  - 음수: 오류 로깅 (음수 매출 불가)

비즈니스 규칙:
  - 중복 집계 방지: 하나의 주문은 하나의 기여도만 계산
  - 우선순위: 채널 > 프로모션 > CRM > SEO (중복 시)
  - 타입 2/3: 동일하게 표시

인사이트:
  - 기본: "PRO가 만들어준 매출은 {금액}원입니다"
  - 비교: "지난달 대비 {증감률}% {증가/감소}"
  - 넛지: "SEO 기능을 활성화하면 매출을 늘릴 수 있어요"
```

#### 1-2. 절약한 시간/비용

```yaml
지표명: PRO 절약 시간
영문명: Time Saved by PRO
정의: PRO가 자동 처리한 업무의 예상 소요 시간 합계
계산식: |
  절약_시간(분) = Σ (작업_건수 × 작업별_평균_시간)

  작업별 평균 시간:
  - 상품 등록: 10분/건
  - 주문 처리: 5분/건
  - 재고 동기화: 3분/건
  - CS 응대: 15분/건

데이터 소스:
  - API: FAS /tasks/pro/report
  - 필드: execute_count, task_type
  - 기간: 월간

단위: 시간 (시간:분 형식)
반올림: 분 단위 (60분 = 1시간)

환산 비용:
  - 시급: 10,000원 (최저시급 기준)
  - 계산식: 절약_시간(시간) × 10,000원

예외 처리:
  - NULL: 0시간으로 처리
  - 0시간: "아직 PRO 기능을 사용하지 않았습니다" 넛지

인사이트:
  - 기본: "{시간}시간 절약 (약 {금액}원 상당)"
  - 비교: "하루 평균 {시간}시간 절약"
  - 넛지: "자동화 기능을 더 활용해보세요"
```

#### 1-3. PRO 혜택

```yaml
지표명: PRO 누적 혜택
영문명: PRO Total Benefits
정의: PRO 사용 기간 동안 받은 총 혜택 금액
계산식: |
  누적_혜택 = 절약_비용 + 추가_매출 + 프로모션_할인

데이터 소스:
  - API: FAS /tasks/report-metrics
  - 필드: total_benefits
  - 기간: 누적 (PRO 승인일 ~ 현재)

단위: 원 (KRW)
반올림: 정수

인사이트:
  - 기본: "PRO로 받은 혜택은 총 {금액}원입니다"
  - 비교: "월 평균 {금액}원 혜택"
```

---

### 2. 아바타 인사이트

```yaml
지표명: 개인화 인사이트
영문명: Personalized Insights
정의: 사용자별 맞춤 분석 및 권장 사항
계산식: |
  규칙 기반 인사이트 생성:

  1. 시간 환산:
     - IF 절약_시간 > 10시간 THEN "한 달간 {시간}시간 절약"

  2. PRO 평균 비교:
     - IF 현재_매출 > PRO_평균_매출 * 1.2 THEN "PRO 평균 대비 {비율}% 높음"
     - ELSE IF 현재_매출 < PRO_평균_매출 * 0.8 THEN "개선 여지 있음"

  3. 성장 추세:
     - IF (이번달 - 지난달) / 지난달 > 0.1 THEN "성장세"
     - ELSE IF (이번달 - 지난달) / 지난달 < -0.1 THEN "하락세"

  4. 액션 제안:
     - IF SEO_매출 = 0 THEN "SEO 기능을 활성화해보세요"
     - IF 프로모션_사용 = 0 THEN "프로모션으로 매출을 높여보세요"

데이터 소스:
  - API: FAS /tasks/report-metrics
  - 필드: avg_sales (PRO 평균)

인사이트 템플릿:
  - "절약한 {시간}시간으로 {활동}을 할 수 있어요"
  - "PRO 평균보다 {비율}% {높은/낮은} 수준입니다"
  - "{기능}을 활성화하면 매출을 늘릴 수 있어요"
```

---

### 3. 매출 추이

```yaml
지표명: 월별 매출 추이
영문명: Monthly Sales Trend
정의: 자사몰과 연동 마켓의 월별 매출 변화
계산식: |
  월별_매출 = {
    "자사몰": CA_2.0_order_amount,
    "연동_마켓": 마켓플러스_paid_order_amount
  }

데이터 소스:
  - API: CA 2.0 /ca2/sales/overview (자사몰)
  - API: 마켓플러스 /api/internal/v1/order/daily-sales (마켓)
  - 기간: 최근 6개월

시각화:
  - 차트 타입: Line Chart (선 그래프)
  - X축: 월 (YYYY-MM)
  - Y축: 매출 (원)
  - 계열: 자사몰 (파란색), 연동 마켓 (주황색)

인사이트:
  - 추세: "지난 6개월간 {증가/감소/유지}"
  - 비교: "자사몰이 전체 매출의 {비율}%"
```

---

### 4. PRO 매출 기여도 (상세)

```yaml
지표명: PRO 기능별 매출 기여도
영문명: PRO Feature Contribution Breakdown
정의: SEO, CRM, 프로모션, 채널 판매별 매출 상세
계산식: |
  각 기능별:
  - SEO: organic 트래픽 매출
  - CRM: CRM 캠페인 매출
  - 프로모션: 할인/쿠폰 적용 매출
  - 채널: 마켓 플러스 매출

시각화:
  - 차트 타입: Horizontal Bar Chart (가로 막대)
  - 정렬: 매출 높은 순

인사이트:
  - "가장 효과적인 기능은 {기능}입니다"
  - "{기능}이 전체 PRO 매출의 {비율}%"
```

---

### 5. 쇼핑몰 운영 현황 (KPI 6개)

```yaml
지표명: 핵심 KPI
영문명: Key Performance Indicators

KPI 1: 구매 전환율
계산식: (구매 완료 수 / 방문자 수) × 100
데이터: CA 2.0 /ca2/conversion/rate
단위: %
목표: 1.5% (업종 평균)

KPI 2: 평균 주문 금액
계산식: 총 매출 / 주문 건수
데이터: CA 2.0 /ca2/sales/overview
단위: 원
목표: 50,000원

KPI 3: 재구매율
계산식: (재구매 고객 수 / 전체 구매 고객 수) × 100
데이터: CA 2.0 /ca2/customer/retention
단위: %
목표: 30%

KPI 4: 장바구니 이탈률
계산식: (장바구니 추가 - 구매 완료) / 장바구니 추가 × 100
데이터: CA 2.0 /ca2/funnel/cart
단위: %
목표: 70% 이하

KPI 5: 트래픽 소스 분포
계산식: 각 소스별 세션 수 비율
데이터: CA 2.0 /ca2/attribution/traffic-analysis
단위: %
표시: Direct, Organic, Referral, Social, Paid

KPI 6: 모바일 비율
계산식: (모바일 세션 / 전체 세션) × 100
데이터: CA 2.0 /ca2/device/analysis
단위: %
목표: 70% 이상
```

---

## 데이터 타입별 처리 규칙

### 타입 1 (Full)
**조건:** 자사몰 매출 ≥ 100만원

**노출 섹션:**
- 상단 카드 3개
- 아바타 인사이트
- 매출 추이
- PRO 매출 기여도
- 쇼핑몰 운영 현황 (KPI 6개)
- PRO 처리 업무
- 후불 광고 배너 (조건부)

---

### 타입 2 (Lite)
**조건:** 자사몰 < 100만원 AND 연동 마켓 ≥ 100만원

**노출 섹션:**
- 상단 카드 3개
- 매출 추이 (마켓 중심)
- PRO 성과 (간소화)

**변경 사항:**
- KPI 섹션 미노출
- 인사이트 간소화

---

### 타입 3 (Mini)
**조건:** 자사몰·연동 마켓 모두 < 100만원

**노출 섹션:**
- 상단 카드 2개 (PRO 매출 제외)
- PRO 성과만

**변경 사항:**
- 매출 관련 지표 미노출
- 성장 가능성 인사이트

---

## 예외 처리 규칙

### NULL 값 처리
```python
def handle_null(value, default=0):
    """NULL 값을 기본값으로 처리"""
    return value if value is not None else default
```

### 0으로 나누기 방지
```python
def safe_divide(numerator, denominator, default=0):
    """0으로 나누기 방지"""
    if denominator == 0 or denominator is None:
        return default
    return numerator / denominator
```

### 음수 값 처리
```python
def validate_positive(value, field_name):
    """음수 값 검증"""
    if value < 0:
        logger.error(f"{field_name} cannot be negative: {value}")
        return 0
    return value
```

---

## 데이터 업데이트 규칙

### 업데이트 주기
- **리포트 생성**: 매월 3일 오전 8시
- **데이터 기준**: 전월 1일 00:00 ~ 말일 23:59
- **지연 시간**: D+2 (2일 후 확정)

### 재계산 조건
- API 오류 발생 시
- 데이터 정합성 문제 발견 시
- 사용자 요청 시 (수동)

---

## 참고 문서

- CA 2.0 API 문서: https://ca-api-dev.hanpda.com/gw/webjars/swagger-ui/index.html
- FAS API 문서: https://extsvc-qa.hanpda.com/docs
- PRO Report API: https://cafe24pro-report-api-dev.hanpda.com/docs
- 5대 핵심지표 시트: https://docs.google.com/spreadsheets/d/1G6XltIhDA2AGT6jDOKVFWzy5ZGfZCU4BfwegW-nC7rk/
