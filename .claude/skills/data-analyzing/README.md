# Data Analyzing Skill

Google Analytics 4 방법론 기반 PRO 리포트 데이터 분석 전문 스킬

## 개요

이 스킬은 Google의 데이터 전문가 관점으로 PRO 리포트의 지표를 정의하고 검증합니다. GA4(Google Analytics 4)의 핵심 원칙을 적용하여 e-commerce 데이터 분석의 업계 표준을 따릅니다.

## 핵심 기능

### 1. GA4 5대 원칙 적용
- **Event-Based**: 이벤트 기반 데이터 모델
- **User-Centric**: 사용자 여정 중심 분석
- **Predictive**: 예측 지표 설계
- **Attribution**: 다중 채널 기여도 분석
- **Privacy-First**: 프라이버시 우선 데이터 수집

### 2. 체계적 지표 정의
- 계산식 명세
- 데이터 소스 매핑
- 예외 처리 규칙
- 인사이트 생성

### 3. 5가지 검증 항목
- Accuracy (정확성)
- Completeness (완전성)
- Consistency (일관성)
- Timeliness (시의성)
- Interpretability (해석 가능성)

## 디렉토리 구조

```
data-analyzing/
├── SKILL.md                              # 메인 스킬 정의
├── references/                           # 참고 문서
│   ├── ga4_analysis_framework.md        # GA4 분석 프레임워크
│   └── pro_report_data_schema.md        # PRO 리포트 데이터 스키마
└── scripts/                              # 검증 스크립트
    └── validate_metric.py                # 지표 검증 도구
```

## 사용 방법

### 1. 새 지표 정의

```yaml
지표명: PRO 매출 기여도
영문명: PRO Revenue Contribution
정의: PRO 기능을 통해 발생한 매출 합계

계산식: |
  PRO_매출 = SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출

데이터 소스:
  - API: CA 2.0 /ca2/attribution/traffic-analysis
  - 필드: order_amount, source
  - 기간: 월간

단위: 원 (KRW)
반올림: 정수

예외 처리:
  - NULL: 0원으로 처리
  - 0: 넛지 표시
  - 음수: 오류 로깅

인사이트:
  - 기본: "PRO가 만들어준 매출은 {금액}원입니다"
  - 비교: "지난달 대비 {증감률}% {증가/감소}"
```

### 2. 지표 검증

```python
from scripts.validate_metric import MetricValidator

# 지표 정의
metric = {
    '지표명': 'PRO 매출 기여도',
    '영문명': 'PRO Revenue Contribution',
    '계산식': 'SEO_매출 + CRM_매출 + 프로모션_매출',
    '데이터_소스': {
        'API': 'CA 2.0',
        '필드': 'order_amount',
        '기간': '월간'
    },
    '단위': '원',
    '예외_처리': {
        'NULL': '0',
        '0': '넛지',
        '음수': '오류'
    }
}

# 검증 실행
validator = MetricValidator()
results = validator.validate_metric_definition(metric)
validator.print_results()
```

### 3. 계산식 테스트

```python
# 샘플 데이터
sample_data = {
    'SEO_매출': 500000,
    'CRM_매출': 300000,
    '프로모션_매출': 200000
}

# 계산 검증
result = validator.validate_calculation(
    metric['계산식'],
    sample_data
)

print(f"계산 성공: {result['value']:,}원")
```

## 주요 참고 자료

### GA4 분석 프레임워크 (`references/ga4_analysis_framework.md`)
- GA4 핵심 철학
- 데이터 검증 체크리스트
- 지표 정의 템플릿
- 대시보드 설계 원칙
- GA4 용어 사전

### PRO 리포트 데이터 스키마 (`references/pro_report_data_schema.md`)
- CA 2.0 API 매핑
- FAS API 매핑
- 마켓 플러스 API 매핑
- 핵심 지표 정의 (계산식 포함)
- 타입별 데이터 처리 규칙
- 예외 처리 표준

## 검증 스크립트

### `scripts/validate_metric.py`

**기능:**
- 지표 정의 필수 필드 검증
- 계산식 논리 검증
- 예외 처리 규칙 검증
- 샘플 데이터 테스트

**사용법:**
```bash
python3 scripts/validate_metric.py
```

**출력 예시:**
```
📊 검증 결과 요약
  오류: 0개
  경고: 1개
  정보: 0개

⚠️  경고:
  - 완전성 [예외_처리]: '음수' 값 처리 방법이 정의되지 않았습니다

🧮 계산식 테스트:
✅ 계산 성공: 1,400,000원
```

## Best Practices

### DO (권장)
- ✅ GA4 템플릿으로 모든 지표 정의
- ✅ 예외 처리 3가지(NULL, 0, 음수) 필수 정의
- ✅ 액션 가능한 인사이트 작성
- ✅ 검증 스크립트로 자동 검증
- ✅ 샘플 데이터로 테스트

### DON'T (지양)
- ❌ 계산식만 작성하고 설명 생략
- ❌ 예외 처리 누락
- ❌ 전문 용어 남발
- ❌ 맥락 없는 숫자만 표시
- ❌ 0으로 나누기 방지 누락

## 예시

### 완벽한 지표 정의

```yaml
지표명: 구매 전환율
영문명: Purchase Conversion Rate
정의: 방문자 대비 구매 완료 고객의 비율

계산식: |
  전환율(%) = safe_divide(구매_완료_수, 방문자_수) × 100

데이터 소스:
  - API: CA 2.0 /ca2/conversion/rate
  - 필드: conversion_rate, sessions, transactions
  - 기간: 월간

단위: % (퍼센트)
반올림: 소수점 1자리

예외 처리:
  - NULL: 0%로 처리
  - 방문자 0: "아직 방문자가 없습니다" 표시
  - 음수: 오류

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

### 좋은 인사이트 vs 나쁜 인사이트

**좋은 예시:**
- "지난달 대비 15% 증가한 1,234,567원"
- "업종 평균(80만원) 대비 154% 높은 수준"
- "절약한 24시간으로 신규 상품 12개를 등록할 수 있어요"
- "SEO 기능을 활성화하면 월 평균 50만원 매출을 늘릴 수 있어요"

**나쁜 예시:**
- "매출: 1,234,567원" (맥락 없음)
- "conversion_rate: 0.025" (전문 용어)
- "좋음" (구체성 없음)
- "개선 필요" (액션 불명확)

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

---

## 관련 문서

- [GA4 공식 문서](https://support.google.com/analytics/answer/9164320)
- [PRO 리포트 사양서](../../../docs/사양서/)
- [CA 2.0 API 문서](https://ca-api-dev.hanpda.com/gw/webjars/swagger-ui/index.html)
- [FAS API 문서](https://extsvc-qa.hanpda.com/docs)

## 버전 히스토리

- **v1.0.0** (2025-11-22): 초기 릴리스
  - GA4 5대 원칙 적용
  - 지표 정의 템플릿
  - 검증 스크립트 (validate_metric.py)
  - 참고 문서 2개 (GA4 프레임워크, PRO 데이터 스키마)

---

**작성자**: Claude (Sonnet 4.5)
**프로젝트**: 카페24 PRO 리포트
**마지막 업데이트**: 2025-11-22
