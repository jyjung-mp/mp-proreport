# 카페24 PRO 리포트 통합 사양서

작성자: Claude (Sonnet 4.5)
작성일: 2025-01-23
버전: 1.0.0
프로젝트: 카페24 PRO 리포트

---

## 목차

1. 프로젝트 개요
2. 설계 철학 및 원칙
3. 화면 구조 (7개 섹션)
4. 데이터 지표 정의
5. API 명세 및 데이터 소스
6. 비즈니스 로직
7. 예외 처리 및 검증
8. 참고 자료

---

## 1. 프로젝트 개요

### 1-1. 서비스 목적

**PRO 리포트**는 PRO의 성과를 "증명"하고, 이를 바탕으로 매출 성장을 위한 마케팅 행동을 "유도"하는 월간 성장 리포트입니다.

**핵심 가치:**
- Proof + Inducement: 투자 가치 증명을 넘어, 실제 마케팅 액션(SNS, 광고) 연결
- 선순환 구조: 증명(데이터) → 유도(액션) → 강화(성장) → 재증명
- 관리 효율화: 사장님 스스로 문제를 인지하고 해결책(PRO 기능)을 선택

### 1-2. 타겟 사용자

**주 사용자:** 카페24 PRO 서비스를 이용하는 쇼핑몰 사장님
**사용 환경:** 웹 (Admin), 모바일 (Admin 앱)
**사용 빈도:** 월 1회 (매월 3일 오전 8시 자동 업데이트)

### 1-3. 통합 설계 배경

기존 4가지 리포트(기존 PRO, 현재 PRO, 엔터프라이즈, GA4/Shopify/Amazon)를 분석하여, 글로벌 Top E-commerce 수준의 통합 리포트를 설계했습니다.

**통합 원칙:**
1. **Shopify의 직관성**: 실시간 업데이트, 드래그앤드롭 커스터마이징, 원클릭 액션
2. **엔터프라이즈의 전략성**: 4단계 퍼널, 좋은/나쁜/개선 전략 제안, 경쟁사 비교
3. **현재 PRO의 차별성**: PRO 기여도 명확 표시, 절약 시간/비용 환산
4. **GA4의 예측성**: AI 기반 성장 예측, 이상 감지

**제거 요소:**
- 기존 PRO의 복잡한 GA4식 분석 (정보 과부하)
- 의미 없는 0원 데이터 표시 → 넛지 화면으로 대체
- 우선순위 없는 인사이트 나열 → 최우선 1개만 표시

---

## 2. 설계 철학 및 원칙

### 2-1. 정보 계층 구조

사용자가 5초, 30초, 2분, 즉시 실행의 4단계로 정보를 파악할 수 있도록 설계했습니다.

**Level 1 (최우선) - 5초 내 파악**
- 이번 달 총 매출 (큰 숫자)
- 성장률 (지난달 대비)
- AI 인사이트 (가장 중요한 1개)

**Level 2 (문제 진단) - 30초 내 파악**
- 4단계 퍼널 (어디가 문제인지)
- 경쟁사 비교 (내 위치 파악)

**Level 3 (상세 분석) - 2분 내 파악**
- PRO 성과 (PRO가 뭘 했는지)
- 매출 추이 (트렌드)
- 상품 성과 (어떤 상품이 잘 팔리는지)

**Level 4 (액션) - 즉시 실행**
- 액션 플랜 (좋은/나쁜/개선 + 원클릭 버튼)

### 2-2. UX 디자인 원칙

1. **매출 중심**: 매출, 성장률을 최상단에 큰 숫자로 표시
2. **문제 진단 강화**: 4단계 퍼널로 문제 지점 명확 파악
3. **액션 제안 구체화**: 좋은/나쁜/개선 3단 구조 + 원클릭 버튼
4. **실시간성**: 60초 갱신 + 모바일 푸시 알림
5. **경쟁사 비교**: 업종 평균 + 레이더 차트

### 2-3. GA4 기반 데이터 철학

모든 지표는 GA4 5대 원칙을 따릅니다.

1. **Event-Based**: 모든 인터랙션을 이벤트로 추적
2. **User-Centric**: 사용자 여정 중심 분석
3. **Predictive**: 과거 데이터 기반 미래 예측
4. **Attribution**: 다중 채널/기능 기여도 측정
5. **Privacy-First**: 최소 데이터 수집, 익명화/집계 활용

---

## 3. 화면 구조 (7개 섹션)

### Section 1: 한눈에 보는 핵심 지표 (Hero Section)

**목적:** 5초 내 이번 달 성과 파악

**구성 요소:**
- 이번 달 총 매출
- 성장률 (지난달 대비)
- PRO가 만든 매출
- 다음 목표
- 3개월 추세 그래프

**데이터:**
- 이번 달 총 매출: CA 2.0 /ca2/sales/overview → order_amount
- 성장률: (이번달 - 지난달) / 지난달 × 100
- PRO 매출: PRO 매출 기여도 합계
- 다음 목표: 업종 평균 매출 - 내 매출

**화면 규칙:**
- 매출은 정수, 쉼표 구분 (예: 8,364,117원)
- 성장률 색상: 증가(초록), 감소(빨강), 동일(회색)
- 3개월 추세: Sparkline 그래프 (SVG)

---

### Section 2: AI 인사이트 카드 (최우선 1개)

**목적:** 가장 중요한 발견 1개만 표시하여 집중도 향상

**인사이트 우선순위 로직:**
1. Red Indicator (평균 미달 지표) 개수 집계
2. 개선 시 예상 매출 증대 효과 계산
3. 효과가 가장 큰 1개 지표 선택
4. 해당 지표의 개선 방안 제시

**인사이트 템플릿:**
- 타입: Red Indicator (평균 미달)
- 메시지:
  - 현재 상태: "지표명 현재값 → 업종 평균(평균값) 미달"
  - 해결 방안: "PRO 기능 활성화로 지표명 증가율배 증가 가능"
- 액션 버튼:
  - 텍스트: "PRO 기능 설정하기"
  - 링크: /admin/pro/기능

**예시 케이스:**

| 지표 | 현재값 | 평균 | 개선 방안 | 예상 효과 |
|------|--------|------|-----------|-----------|
| 재구매율 | 2.7% | 10% | CRM 활성화 | +200만원/월 |
| 전환율 | 2.4% | 3.5% | 프로모션 | +180만원/월 |
| AOV | 91,007원 | 120,000원 | 번들 상품 | +150만원/월 |

→ 재구매율 개선 시 효과가 가장 크므로 CRM 인사이트 표시

---

### Section 3: 4단계 성장 퍼널 (엔터프라이즈 방식)

**목적:** 어느 단계에서 문제가 발생하는지 명확히 파악

**4단계 퍼널 정의:**

| 단계 | 지표명 | 계산식 | 데이터 소스 | 기준값 |
|------|--------|--------|-------------|--------|
| TRAFFIC | 유입 방문자 | 총 sessions | CA 2.0 /ca2/attribution/traffic-analysis | - |
| ENGAGEMENT | 탐색률 | (상품 조회 / 방문자) × 100 | CA 2.0 /ca2/funnel/engagement | 70% |
| CONVERSION | 구매 전환율 | (구매 완료 / 방문자) × 100 | CA 2.0 /ca2/conversion/rate | 3.5% |
| RETENTION | 재구매율 | (재구매 고객 / 총 고객) × 100 | CA 2.0 /ca2/retention/rate | 10% |

**Red Indicator 표시 조건:**
- 현재값 < 업종 평균 → ⚠ (주황색 경고)
- 현재값 ≥ 업종 평균 → ✓ (초록색 체크)

**개선 제안 매핑:**

| 문제 단계 | 원인 | PRO 해결책 | 예상 효과 |
|----------|------|-----------|-----------|
| TRAFFIC | 검색 유입 부족 | SEO 최적화 | 유입 +250% |
| ENGAGEMENT | 상품 매력도 부족 | 상품 설명 개선, 이미지 최적화 | 탐색률 +20% |
| CONVERSION | 결제 장벽 높음 | 할인 프로모션, 간편결제 | 전환율 +30% |
| RETENTION | 재구매 유도 부족 | CRM 자동 메시지 | 재구매율 2배 |

---

### Section 4: 매출 분석 (Shopify 방식 + 경쟁사 비교)

**목적:** 매출 트렌드와 업종 평균 대비 내 위치 파악

**좌측 - 월별 매출 추이:**
- 자사몰 매출: CA 2.0 /ca2/sales/overview → order_amount (shop_only)
- 연동 마켓 매출: 마켓 플러스 API /api/internal/v1/order/daily-sales → paid_order_amount
- 기간: 최근 3개월

**우측 - 경쟁사 비교 (레이더 차트):**

| 지표 | 내 값 | 업종 평균 | 비율 (%) | 데이터 소스 |
|------|-------|----------|----------|-------------|
| 매출 | 8,364,117원 | 5,400,000원 | 154% | CA 2.0 |
| 전환율 | 2.4% | 3.5% | 69% | CA 2.0 |
| AOV | 91,007원 | 120,000원 | 76% | CA 2.0 |
| 재구매율 | 2.7% | 10% | 27% | CA 2.0 |
| CLV | 104,505원 | 180,000원 | 58% | FAS |

**레이더 차트 시각화:**
- 5각형 레이더 차트
- 업종 평균: 회색 점선
- 내 값: 파란색 실선
- 100% 기준선: 검은색 실선

---

### Section 5: PRO 성과 (현재 PRO 방식 + 넛지 강화)

**목적:** PRO가 만들어준 매출과 절약 시간/비용을 명확히 표시

**1. PRO 매출 기여도 정의:**

**지표명:** PRO 매출 기여도
**영문명:** PRO Revenue Contribution
**정의:** PRO 기능(SEO, CRM, 프로모션, 채널)을 통해 발생한 매출 합계

**계산식:**
- PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출
- SEO: source = "organic"
- CRM: source = "crm"
- 프로모션: discount_applied = true
- 채널: 마켓플러스 API

**데이터 소스:**
- API: CA 2.0 /ca2/attribution/traffic-analysis
- 필드: order_amount, source
- 기간: 월간

**단위:** 원
**반올림:** 정수

**예외 처리:**
- NULL: 0원
- 0: 넛지 표시
- 음수: 오류 로깅

**비즈니스 규칙:**
- 중복 방지: 하나의 주문 = 하나의 기여도
- 우선순위: 채널 > 프로모션 > CRM > SEO

**인사이트:**
- 기본: "PRO가 만들어준 매출은 금액원"
- 비교: "지난달 대비 증감률% 증가/감소"
- 넛지: "SEO 기능 활성화로 예상 매출 +150만원"

---

**2. 절약 시간/비용 정의:**

**지표명:** PRO 절약 시간
**영문명:** Time Saved by PRO
**정의:** PRO 자동 처리 업무의 예상 소요 시간 합계

**계산식:**
- 절약_시간(분) = Σ (작업_건수 × 작업별_평균_시간)
- 작업별 평균:
  - 상품 등록: 10분/건
  - 주문 처리: 5분/건
  - 재고 동기화: 3분/건
  - CS 응대: 15분/건

**데이터 소스:**
- API: FAS /tasks/pro/report
- 필드: execute_count, task_type
- 기간: 월간

**단위:** 시간
**반올림:** 분 단위

**환산 비용:**
- 시급: 10,000원
- 계산식: 절약_시간 × 10,000원

**예외 처리:**
- NULL: 0시간
- 0: 넛지 표시

**인사이트:**
- 기본: "시간시간 절약 (약 금액원 상당)"
- 비교: "하루 평균 시간시간"

---

**3. 넛지 화면 설계:**

각 기능의 기여 매출이 0원일 경우 넛지 표시

**넛지 메시지 템플릿:**

| 기능 | 조건 | 메시지 | 예상 효과 | 액션 |
|------|------|--------|-----------|------|
| SEO | SEO 매출 = 0 | "SEO 미사용 중" | 검색 유입 +250%, 매출 +150만원/월 | [SEO 설정하기] |
| CRM | CRM 매출 = 0 | "CRM 자동 메시지 미사용 중" | 재구매율 2배, 매출 +200만원/월 | [CRM 템플릿 선택] |
| 프로모션 | 프로모션 매출 = 0 | "프로모션 미진행 중" | 전환율 +30%, 매출 +180만원/월 | [10% 할인 시작] |
| 채널 | 채널 매출 = 0 | "연동 마켓 미사용 중" | 노출 +500%, 매출 +250만원/월 | [마켓 연동하기] |

---

### Section 6: 다음 달 액션 플랜 (엔터프라이즈 3단 구조)

**목적:** 즉시 실행 가능한 구체적 액션 제안

**3단 분류 로직:**

**좋은 전략 (계속 유지):**
- 조건: 지난달 대비 개선된 지표
- 예시:
  - 재구매율: 2.0% → 2.7% (35% 증가)
  - CRM 활용: 자동 메시지 발송 건수 +50%

**개선 전략 (즉시 실행):**
- 조건: Red Indicator (평균 미달) 지표
- 예시:
  - 전환율: 2.4% < 평균(3.5%) → 할인 프로모션 권장
  - SEO: 검색 유입 0건 → SEO 설정 권장

**나쁜 전략 (즉시 중단):**
- 조건: 광고비 대비 매출 낮음, ROI < 100%
- 예시:
  - 광고 채널 A: 광고비 50만원, 매출 30만원 → ROI 60%
  - 프로모션 B: 할인율 30%, 전환율 변화 없음

**액션 버튼 링크:**
- [계속하기]: 해당 기능 통계 페이지
- [실행하기]: PRO 기능 설정 페이지 (예: /admin/pro/crm)
- [중단하기]: 광고 관리 페이지

---

### Section 7: 상품 성과 Top 3 (엔터프라이즈 방식)

**목적:** 어떤 상품이 잘 팔리고, 어떤 상품을 개선해야 하는지 파악

**좌측 - 잘 팔리는 상품 (매출 기여도):**
- 데이터: CA 2.0 /ca2/products/top-sellers
- 정렬: 매출 내림차순
- 표시: Top 3
- 액션: [프로모션 추가] → 번들 상품 생성

**우측 - 개선 필요 상품 (조회 많지만 전환 낮음):**
- 조건: 조회수 > 평균 AND 전환율 < 평균
- 데이터: CA 2.0 /ca2/products/low-conversion
- 정렬: 조회수 내림차순
- 표시: Top 3
- 액션: [상품 설명 개선] → 상품 수정 페이지

**상품 성과 지표:**

**지표명:** 상품별 전환율
**영문명:** Product Conversion Rate
**정의:** 상품 조회 대비 구매 완료 비율

**계산식:**
- 전환율(%) = safe_divide(구매_완료_수, 조회_수) × 100

**데이터 소스:**
- API: CA 2.0 /ca2/products/performance
- 필드: product_id, view_count, purchase_count
- 기간: 월간

**단위:** %
**반올림:** 소수점 1자리

**예외 처리:**
- NULL: 0%
- 조회수 0: "조회 없음" 표시

**인사이트:**
- 기본: "전환율 비율%"
- 비교: "평균(3.0%) 대비 차이%p 높음/낮음"
- 넛지: "상품 설명 개선으로 전환율 +50% 가능"

---

## 4. 데이터 지표 정의

### 4-1. 핵심 지표 요약

| 지표명 | 계산식 | 데이터 소스 | 단위 | 기준값 |
|--------|--------|-------------|------|--------|
| 이번 달 총 매출 | SUM(order_amount) | CA 2.0 | 원 | - |
| 성장률 | (이번달 - 지난달) / 지난달 × 100 | CA 2.0 | % | 0% |
| PRO 매출 기여도 | SEO + CRM + 프로모션 + 채널 | CA 2.0 + 마켓플러스 | 원 | - |
| 유입 방문자 (TRAFFIC) | SUM(sessions) | CA 2.0 | 명 | - |
| 탐색률 (ENGAGEMENT) | (상품 조회 / 방문자) × 100 | CA 2.0 | % | 70% |
| 구매 전환율 (CONVERSION) | (구매 완료 / 방문자) × 100 | CA 2.0 | % | 3.5% |
| 재구매율 (RETENTION) | (재구매 고객 / 총 고객) × 100 | CA 2.0 | % | 10% |
| 절약 시간 | Σ(작업 건수 × 평균 시간) | FAS | 시간 | - |
| 절약 비용 | 절약 시간 × 10,000원 | FAS | 원 | - |
| 평균 주문 금액 (AOV) | 총 매출 / 주문 수 | CA 2.0 | 원 | 120,000원 |
| 고객 생애 가치 (CLV) | 누적 매출 / 고객 수 | FAS | 원 | 180,000원 |

### 4-2. 검증 체크리스트 (GA4 5-tier)

모든 지표는 다음 5단계 검증을 통과해야 합니다.

**1. Accuracy (정확성)**
- [x] 데이터 소스 명확 (API 엔드포인트, 필드)
- [x] 계산식 논리적
- [x] 단위 일관성
- [x] 0으로 나누기 방지 (safe_divide 함수)

**2. Completeness (완전성)**
- [x] 필수 필드 존재 확인
- [x] NULL/0/음수 처리 정의
- [x] 예외 상황 대응 명시

**3. Consistency (일관성)**
- [x] 동일 지표 = 동일 값
- [x] 합계 = 부분합
- [x] 단위/반올림 일치

**4. Timeliness (시의성)**
- [x] 업데이트 주기 명확 (매월 3일 오전 8시)
- [x] 데이터 지연 고려 (D+2)

**5. Interpretability (해석 가능성)**
- [x] 사용자 이해 가능 용어
- [x] 인사이트 명확
- [x] 액션 가능

---

## 5. API 명세 및 데이터 소스

### 5-1. CA 2.0 API

**Base URL:** https://ca-api-dev.hanpda.com

#### 5-1-1. 매출 종합 조회

**엔드포인트:** GET /ca2/sales/overview

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)",
  "aggregation": "monthly"
}
```

**응답:**
```
{
  "order_amount": 8364117,
  "order_count": 92,
  "previous_order_amount": 4700000,
  "growth_rate": 78.0
}
```

**사용 섹션:** Section 1 (Hero), Section 4 (매출 추이)

---

#### 5-1-2. 채널별 분석

**엔드포인트:** GET /ca2/adsources/channels

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)"
}
```

**응답:**
```
{
  "channels": [
    {
      "channel": "organic",
      "order_amount": 800000,
      "order_count": 15
    },
    {
      "channel": "crm",
      "order_amount": 0,
      "order_count": 0
    }
  ]
}
```

**사용 섹션:** Section 5 (PRO 성과 - SEO/CRM)

---

#### 5-1-3. 구매 전환율

**엔드포인트:** GET /ca2/conversion/rate

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)"
}
```

**응답:**
```
{
  "conversion_rate": 2.4,
  "sessions": 26822,
  "transactions": 92,
  "industry_average": 3.5
}
```

**사용 섹션:** Section 3 (4단계 퍼널 - CONVERSION)

---

#### 5-1-4. 트래픽 분석

**엔드포인트:** GET /ca2/attribution/traffic-analysis

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)"
}
```

**응답:**
```
{
  "sessions": 26822,
  "pageviews": 120000,
  "sources": [
    {
      "source": "organic",
      "sessions": 5000,
      "order_amount": 800000
    }
  ]
}
```

**사용 섹션:** Section 3 (4단계 퍼널 - TRAFFIC)

---

### 5-2. FAS API

**Base URL:** https://extsvc-qa.hanpda.com

#### 5-2-1. PRO 작업 현황

**엔드포인트:** GET /tasks/pro/report

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)"
}
```

**응답:**
```
{
  "execute_count": 288,
  "saved_time": 28824,
  "tasks": [
    {
      "task_type": "product_register",
      "count": 50,
      "avg_time_per_task": 10
    },
    {
      "task_type": "order_process",
      "count": 180,
      "avg_time_per_task": 5
    }
  ]
}
```

**사용 섹션:** Section 5 (PRO 성과 - 절약 시간)

---

### 5-3. 마켓 플러스 API

**Base URL:** https://marketplus-api.hanpda.com

#### 5-3-1. 마켓 매출 조회

**엔드포인트:** GET /api/internal/v1/order/daily-sales

**파라미터:**
```
{
  "shop_id": "string (필수)",
  "start_date": "YYYY-MM-DD (필수)",
  "end_date": "YYYY-MM-DD (필수)"
}
```

**응답:**
```
{
  "total_sales": 3100000,
  "markets": [
    {
      "market_name": "쿠팡",
      "paid_order_amount": 1500000
    },
    {
      "market_name": "11번가",
      "paid_order_amount": 1600000
    }
  ]
}
```

**사용 섹션:** Section 4 (매출 추이 - 연동 마켓), Section 5 (PRO 성과 - 채널 판매)

---

## 6. 비즈니스 로직

### 6-1. 리포트 타입 분기

**타입 1 (Full):**
- 조건: 자사몰 매출 ≥ 100만원
- 노출: 전체 7개 섹션

**타입 2 (Lite):**
- 조건: 자사몰 < 100만원 AND 연동 마켓 ≥ 100만원
- 노출: Section 1, 2, 4 (매출 추이), 5 (PRO 성과 간소화)
- 생략: Section 3 (4단계 퍼널), 6 (액션 플랜), 7 (상품 성과)

**타입 3 (Mini):**
- 조건: 자사몰·마켓 모두 < 100만원
- 노출: Section 1 (카드 2개만), 5 (PRO 성과만)
- 생략: Section 2~4, 6~7

### 6-2. PRO 매출 기여도 중복 방지

하나의 주문이 여러 PRO 기능에 중복 집계되지 않도록 우선순위 적용:

**우선순위:**
1. 채널 판매 (연동 마켓)
2. 프로모션 (할인)
3. CRM (자동 메시지)
4. SEO (검색 유입)

**로직:**
```python
def calculate_pro_revenue(order):
    if order.market_name:
        return "channel"
    elif order.discount_applied:
        return "promotion"
    elif order.source == "crm":
        return "crm"
    elif order.source == "organic":
        return "seo"
    else:
        return None

# 집계
channel_revenue = sum([order.amount for order in orders if calculate_pro_revenue(order) == "channel"])
promotion_revenue = sum([order.amount for order in orders if calculate_pro_revenue(order) == "promotion"])
crm_revenue = sum([order.amount for order in orders if calculate_pro_revenue(order) == "crm"])
seo_revenue = sum([order.amount for order in orders if calculate_pro_revenue(order) == "seo"])
```

### 6-3. 넛지 표시 조건

각 PRO 기능의 기여 매출이 0원일 경우 넛지 표시:

```python
def should_show_nudge(feature_revenue):
    return feature_revenue == 0

# 예시
if should_show_nudge(crm_revenue):
    display_crm_nudge()
```

---

## 7. 예외 처리 및 검증

### 7-1. 예외 처리 표준

#### NULL 값 처리
```python
def handle_null(value, default=0):
    """NULL 값을 기본값으로 대체"""
    return value if value is not None else default
```

#### 0으로 나누기 방지
```python
def safe_divide(numerator, denominator, default=0):
    """0으로 나누기 방지, 안전한 나눗셈"""
    if denominator == 0 or denominator is None:
        return default
    return numerator / denominator
```

**사용 예시:**
```python
# 전환율 계산
conversion_rate = safe_divide(transactions, sessions, default=0) * 100

# 성장률 계산
growth_rate = safe_divide(current_sales - prev_sales, prev_sales, default=0) * 100
```

#### 음수 값 검증
```python
def validate_positive(value, field_name):
    """음수 값 검증 및 로깅"""
    if value < 0:
        logger.error(f"{field_name} 음수 값 감지: {value}")
        return 0
    return value
```

### 7-2. 데이터 검증 체크리스트

**API 응답 검증:**
- [ ] 응답 코드 200 확인
- [ ] 필수 필드 존재 확인
- [ ] 데이터 타입 일치 확인 (숫자, 문자열 등)
- [ ] 범위 검증 (예: 전환율 0~100%)

**계산식 검증:**
- [ ] 합계 = 부분합 일치
- [ ] 비율 합계 = 100%
- [ ] 음수 값 없음
- [ ] 소수점 반올림 일관

**화면 표시 검증:**
- [ ] 쉼표 구분 (예: 8,364,117원)
- [ ] 소수점 자릿수 일관 (전환율: 1자리)
- [ ] 단위 표시 (원, %, 시간)
- [ ] 색상 코드 일관 (증가: 초록, 감소: 빨강)

---

## 8. 참고 자료

### 8-1. 프로젝트 문서

- **비교 분석 문서**: https://wiki.simplexi.com/pages/viewpage.action?pageId=2802894087
- **데이터 스키마**: .claude/skills/3-data-analyzing/references/pro_report_data_schema.md
- **GA4 분석 프레임워크**: .claude/skills/3-data-analyzing/references/ga4_analysis_framework.md

### 8-2. API 문서

- **CA 2.0 API**: https://ca-api-dev.hanpda.com/gw/webjars/swagger-ui/index.html
- **FAS API**: https://extsvc-qa.hanpda.com/docs
- **PRO Report API**: https://cafe24pro-report-api-dev.hanpda.com/docs

### 8-3. Figma 디자인

- **타입 1 (Full)**: https://alias-slash-26808627.figma.site/
- **타입 2 (Lite)**: https://daisy-linear-09681413.figma.site/
- **타입 3 (Mini)**: https://symbol-plain-76893611.figma.site/

### 8-4. 벤치마킹 자료

- **Shopify Analytics**: https://www.shopify.com/analytics
- **Google Analytics 4**: https://analytics.google.com/
- **Amazon Seller Central**: https://sellercentral.amazon.com/

---

## 변경 이력

| 버전 | 날짜 | 작성자 | 변경 내용 |
|------|------|--------|-----------|
| 1.0.0 | 2025-01-23 | Claude (Sonnet 4.5) | 초기 버전 작성 |

---

**문서 승인:**
- 기획: [담당자명]
- 개발: [담당자명]
- CTO: [필요시]

**다음 단계:**
1. 팀 내 리뷰 (1~2일)
2. 개발팀 리뷰 (1~2일)
3. CTO 리뷰 (필요시)
4. Jira 티켓 생성 및 개발 시작
