#!/usr/bin/env python3
"""
PRO 리포트 지표 검증 스크립트
GA4 방법론 기반 데이터 검증
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum


class ValidationLevel(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationResult:
    level: ValidationLevel
    category: str
    message: str
    field: Optional[str] = None


class MetricValidator:
    """GA4 기반 지표 검증기"""

    def __init__(self):
        self.results: List[ValidationResult] = []

    def validate_metric_definition(self, metric: Dict[str, Any]) -> List[ValidationResult]:
        """지표 정의 검증 (5단계)"""
        self.results = []

        # 필수 필드 검증
        required = ['지표명', '영문명', '정의', '계산식', '데이터_소스', '단위']
        for field in required:
            if field not in metric or not metric[field]:
                self.results.append(ValidationResult(
                    level=ValidationLevel.ERROR,
                    category="필수 필드",
                    message=f"'{field}' 누락",
                    field=field
                ))

        self._validate_accuracy(metric)
        self._validate_completeness(metric)
        self._validate_consistency(metric)
        self._validate_interpretability(metric)

        return self.results

    def _validate_accuracy(self, metric: Dict[str, Any]):
        """정확성 검증"""
        if '계산식' in metric:
            formula = metric['계산식']
            if '/' in formula and 'safe_divide' not in formula.lower():
                self.results.append(ValidationResult(
                    level=ValidationLevel.WARNING,
                    category="정확성",
                    message="나눗셈 연산: 0으로 나누기 방지 확인",
                    field="계산식"
                ))

    def _validate_completeness(self, metric: Dict[str, Any]):
        """완전성 검증"""
        if '예외_처리' in metric:
            for key in ['NULL', '0', '음수']:
                if key not in metric['예외_처리']:
                    self.results.append(ValidationResult(
                        level=ValidationLevel.WARNING,
                        category="완전성",
                        message=f"'{key}' 처리 방법 미정의",
                        field="예외_처리"
                    ))
        else:
            self.results.append(ValidationResult(
                level=ValidationLevel.ERROR,
                category="완전성",
                message="예외 처리 규칙 미정의",
                field="예외_처리"
            ))

    def _validate_consistency(self, metric: Dict[str, Any]):
        """일관성 검증"""
        if '반올림' not in metric:
            self.results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                category="일관성",
                message="반올림 규칙 미정의",
                field="반올림"
            ))

    def _validate_interpretability(self, metric: Dict[str, Any]):
        """해석 가능성 검증"""
        if '인사이트' not in metric or not metric['인사이트']:
            self.results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                category="해석 가능성",
                message="인사이트 미정의",
                field="인사이트"
            ))

    def validate_calculation(self, formula: str, sample_data: Dict[str, Any]) -> Dict[str, Any]:
        """계산식 검증 (샘플 데이터)"""
        result = {'valid': True, 'value': None, 'errors': []}

        try:
            namespace = {
                'safe_divide': lambda a, b: a / b if b != 0 else 0,
                'abs': abs,
                'round': round,
                **sample_data
            }
            value = eval(formula, {"__builtins__": {}}, namespace)
            result['value'] = value

            if value is None:
                result['errors'].append("계산 결과 None")
                result['valid'] = False

        except ZeroDivisionError:
            result['valid'] = False
            result['errors'].append("0으로 나누기 오류")
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"계산 오류: {str(e)}")

        return result

    def print_results(self):
        """검증 결과 출력"""
        if not self.results:
            print("✅ 검증 통과")
            return

        errors = [r for r in self.results if r.level == ValidationLevel.ERROR]
        warnings = [r for r in self.results if r.level == ValidationLevel.WARNING]

        print(f"\n📊 검증 결과: 오류 {len(errors)}개, 경고 {len(warnings)}개\n")

        if errors:
            print("❌ 오류:")
            for r in errors:
                print(f"  - {r.category} [{r.field}]: {r.message}")
            print()

        if warnings:
            print("⚠️  경고:")
            for r in warnings:
                print(f"  - {r.category} [{r.field}]: {r.message}")


def main():
    """메인 - 사용 예시"""
    sample_metric = {
        '지표명': 'PRO 매출 기여도',
        '영문명': 'PRO Revenue Contribution',
        '정의': 'PRO 기능을 통해 발생한 매출 합계',
        '계산식': 'SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출',
        '데이터_소스': {
            'API': 'CA 2.0',
            '필드': 'order_amount',
            '기간': '월간'
        },
        '단위': '원',
        '반올림': '정수',
        '예외_처리': {
            'NULL': '0원',
            '0': '넛지',
            '음수': '오류'
        },
        '인사이트': 'PRO가 만들어준 매출은 {금액}원'
    }

    validator = MetricValidator()
    validator.validate_metric_definition(sample_metric)
    validator.print_results()

    print("\n🧮 계산식 테스트:")
    sample_data = {
        'SEO_매출': 500000,
        'CRM_매출': 300000,
        '프로모션_매출': 200000,
        '채널_매출': 400000
    }
    calc = validator.validate_calculation(sample_metric['계산식'], sample_data)

    if calc['valid']:
        print(f"✅ 계산 성공: {calc['value']:,}원")
    else:
        print(f"❌ 계산 실패: {calc['errors']}")


if __name__ == '__main__':
    main()
