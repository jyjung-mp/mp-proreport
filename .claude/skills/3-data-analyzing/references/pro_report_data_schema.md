# PRO 리포트 데이터 스키마

## 핵심 데이터 소스

### 1. CA 2.0 API (Commerce Analytics)
**Base URL:** `https://ca-api-dev.hanpda.com`

| 엔드포인트 | 용도 | 주요 필드 |
|-----------|------|-----------|
| `/ca2/sales/overview` | 매출 종합 | `order_amount`, `order_count` |
| `/ca2/adsources/channels` | 채널별 분석 | `channel`, `order_amount` |
| `/ca2/conversion/rate` | 구매 전환율 | `conversion_rate` |
| `/ca2/attribution/traffic-analysis` | 트래픽 분석 | `sessions`, `source` |

**파라미터:**
```json
{
  "shop_id": "string",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "aggregation": "monthly"
}
```

---

### 2. FAS API (Fulfillment Automation Service)
**Base URL:** `https://extsvc-qa.hanpda.com`

| 엔드포인트 | 용도 | 주요 필드 |
|-----------|------|-----------|
| `/app-requests-list` | PRO 승인 목록 | `confirm_timestamp`, `status` |
| `/tasks/pro/report` | PRO 작업 현황 | `execute_count`, `saved_time` |
| `/tasks/report-metrics` | 월별 지표 | `avg_sales`, `total_benefits` |

---

### 3. 마켓 플러스 API
**Base URL:** `https://marketplus-api.hanpda.com`

| 엔드포인트 | 용도 | 주요 필드 |
|-----------|------|-----------|
| `/api/internal/v1/order/daily-sales` | 마켓 매출 | `paid_order_amount`, `market_name` |

---

## 핵심 지표 정의

### 1. PRO 매출 기여도

```yaml
지표명: PRO 매출 기여도
영문명: PRO Revenue Contribution
정의: PRO 기능(SEO, CRM, 프로모션, 채널)을 통해 발생한 매출 합계

계산식: |
  PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출
  
  - SEO: source = "organic"
  - CRM: source = "crm"
  - 프로모션: discount_applied = true
  - 채널: 마켓플러스 API

데이터 소스:
  - API: CA 2.0 /ca2/attribution/traffic-analysis
  - 필드: order_amount, source
  - 기간: 월간

단위: 원
반올림: 정수

예외 처리:
  - NULL: 0원
  - 0: 넛지 표시
  - 음수: 오류 로깅

비즈니스 규칙:
  - 중복 방지: 하나의 주문 = 하나의 기여도
  - 우선순위: 채널 > 프로모션 > CRM > SEO

인사이트:
  - 기본: "PRO가 만들어준 매출은 {금액}원"
  - 비교: "지난달 대비 {증감률}% {증가/감소}"
  - 넛지: "SEO 기능 활성화 권장"
```

---

### 2. 절약 시간/비용

```yaml
지표명: PRO 절약 시간
영문명: Time Saved by PRO
정의: PRO 자동 처리 업무의 예상 소요 시간 합계

계산식: |
  절약_시간(분) = Σ (작업_건수 × 작업별_평균_시간)
  
  작업별 평균:
  - 상품 등록: 10분/건
  - 주문 처리: 5분/건
  - 재고 동기화: 3분/건
  - CS 응대: 15분/건

데이터 소스:
  - API: FAS /tasks/pro/report
  - 필드: execute_count, task_type
  - 기간: 월간

단위: 시간
반올림: 분 단위

환산 비용:
  - 시급: 10,000원
  - 계산식: 절약_시간 × 10,000원

예외 처리:
  - NULL: 0시간
  - 0: 넛지 표시

인사이트:
  - 기본: "{시간}시간 절약 (약 {금액}원 상당)"
  - 비교: "하루 평균 {시간}시간"
```

---

### 3. 구매 전환율 (KPI)

```yaml
지표명: 구매 전환율
영문명: Purchase Conversion Rate
정의: 방문자 대비 구매 완료 고객 비율

계산식: |
  전환율(%) = safe_divide(구매_완료_수, 방문자_수) × 100

데이터 소스:
  - API: CA 2.0 /ca2/conversion/rate
  - 필드: conversion_rate, sessions, transactions
  - 기간: 월간

단위: %
반올림: 소수점 1자리

예외 처리:
  - NULL: 0%
  - 방문자 0: "방문자 없음" 표시
  - 음수: 오류

비즈니스 규칙:
  - 업종 평균: 1.5%
  - 우수: 2.0% 이상
  - 개선 필요: 1.0% 미만

인사이트:
  - 기본: "구매 전환율은 {비율}%"
  - 비교: "업종 평균(1.5%) 대비 {차이}%p {높음/낮음}"
  - 넛지: "결제 프로세스 간소화 권장"
```

---

## 타입별 처리

### 타입 1 (Full)
**조건:** 자사몰 매출 ≥ 100만원

**노출:**
- 상단 카드 3개
- 아바타 인사이트
- 매출 추이
- PRO 매출 기여도
- KPI 6개
- PRO 처리 업무

---

### 타입 2 (Lite)
**조건:** 자사몰 < 100만원 AND 마켓 ≥ 100만원

**노출:**
- 상단 카드 3개
- 매출 추이 (마켓 중심)
- PRO 성과 (간소화)

**생략:**
- KPI 6개
- 자사몰 상세

---

### 타입 3 (Mini)
**조건:** 자사몰·마켓 모두 < 100만원

**노출:**
- 상단 카드 2개 (PRO 매출 제외)
- PRO 성과만

**생략:**
- 매출 관련 모든 지표

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

## 업데이트 규칙

- **리포트 생성**: 매월 3일 오전 8시
- **데이터 기준**: 전월 1일 ~ 말일
- **지연**: D+2 (2일 후 확정)

---

## 참고 문서

- [CA 2.0 API](https://ca-api-dev.hanpda.com/gw/webjars/swagger-ui/index.html)
- [FAS API](https://extsvc-qa.hanpda.com/docs)
- [PRO Report API](https://cafe24pro-report-api-dev.hanpda.com/docs)
