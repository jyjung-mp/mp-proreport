#!/usr/bin/env python3
"""
PRO 리포트 지표 검증 스크립트

Google Analytics 4 방법론 기반 데이터 검증
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum


class ValidationLevel(Enum):
    """검증 레벨"""
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class ValidationResult:
    """검증 결과"""
    level: ValidationLevel
    category: str
    message: str
    field: Optional[str] = None


class MetricValidator:
    """GA4 기반 지표 검증기"""

    def __init__(self):
        self.results: List[ValidationResult] = []

    def validate_metric_definition(self, metric: Dict[str, Any]) -> List[ValidationResult]:
        """
        지표 정의 검증

        필수 필드:
        - 지표명 (한글)
        - 영문명
        - 정의
        - 계산식
        - 데이터 소스
        - 단위
        - 예외 처리
        """
        self.results = []

        # 1. 필수 필드 검증
        required_fields = ['지표명', '영문명', '정의', '계산식', '데이터_소스', '단위']
        for field in required_fields:
            if field not in metric or not metric[field]:
                self.results.append(ValidationResult(
                    level=ValidationLevel.ERROR,
                    category="필수 필드",
                    message=f"필수 필드 '{field}'가 누락되었습니다",
                    field=field
                ))

        # 2. 데이터 정확성 검증
        self._validate_accuracy(metric)

        # 3. 데이터 완전성 검증
        self._validate_completeness(metric)

        # 4. 데이터 일관성 검증
        self._validate_consistency(metric)

        # 5. 해석 가능성 검증
        self._validate_interpretability(metric)

        return self.results

    def _validate_accuracy(self, metric: Dict[str, Any]):
        """데이터 정확성 검증"""

        # 계산식 검증
        if '계산식' in metric:
            formula = metric['계산식']

            # 0으로 나누기 체크
            if '/' in formula and 'safe_divide' not in formula.lower():
                self.results.append(ValidationResult(
                    level=ValidationLevel.WARNING,
                    category="정확성",
                    message="나눗셈 연산이 있습니다. 0으로 나누기 방지 확인 필요",
                    field="계산식"
                ))

            # 음수 가능성 체크
            if '-' in formula and 'abs' not in formula.lower():
                self.results.append(ValidationResult(
                    level=ValidationLevel.INFO,
                    category="정확성",
                    message="뺄셈 연산이 있습니다. 음수 값 처리 확인 권장",
                    field="계산식"
                ))

        # 단위 일관성
        if '단위' in metric:
            unit = metric['단위']
            if unit not in ['원', '%', '건', '시간', '분', '초', '명', '회']:
                self.results.append(ValidationResult(
                    level=ValidationLevel.WARNING,
                    category="정확성",
                    message=f"비표준 단위 '{unit}' 사용. 표준 단위 권장",
                    field="단위"
                ))

    def _validate_completeness(self, metric: Dict[str, Any]):
        """데이터 완전성 검증"""

        # 예외 처리 정의 여부
        exception_keys = ['NULL', '0', '음수']
        if '예외_처리' in metric:
            for key in exception_keys:
                if key not in metric['예외_처리']:
                    self.results.append(ValidationResult(
                        level=ValidationLevel.WARNING,
                        category="완전성",
                        message=f"'{key}' 값 처리 방법이 정의되지 않았습니다",
                        field="예외_처리"
                    ))
        else:
            self.results.append(ValidationResult(
                level=ValidationLevel.ERROR,
                category="완전성",
                message="예외 처리 규칙이 정의되지 않았습니다",
                field="예외_처리"
            ))

        # 데이터 소스 상세 정보
        if '데이터_소스' in metric:
            source = metric['데이터_소스']
            required_source_fields = ['API', '필드', '기간']
            for field in required_source_fields:
                if field not in source:
                    self.results.append(ValidationResult(
                        level=ValidationLevel.WARNING,
                        category="완전성",
                        message=f"데이터 소스에 '{field}' 정보 누락",
                        field="데이터_소스"
                    ))

    def _validate_consistency(self, metric: Dict[str, Any]):
        """데이터 일관성 검증"""

        # 반올림 규칙
        if '반올림' not in metric:
            self.results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                category="일관성",
                message="반올림 규칙이 정의되지 않았습니다",
                field="반올림"
            ))

        # 단위와 반올림 일관성
        if '단위' in metric and '반올림' in metric:
            unit = metric['단위']
            rounding = metric['반올림']

            if unit == '원' and '소수점' in str(rounding):
                self.results.append(ValidationResult(
                    level=ValidationLevel.WARNING,
                    category="일관성",
                    message="단위가 '원'인데 소수점 반올림이 정의됨. 정수 권장",
                    field="반올림"
                ))

    def _validate_interpretability(self, metric: Dict[str, Any]):
        """해석 가능성 검증"""

        # 인사이트 존재 여부
        if '인사이트' not in metric or not metric['인사이트']:
            self.results.append(ValidationResult(
                level=ValidationLevel.WARNING,
                category="해석 가능성",
                message="사용자 인사이트가 정의되지 않았습니다",
                field="인사이트"
            ))

        # 비즈니스 규칙 존재 여부
        if '비즈니스_규칙' in metric:
            rules = metric['비즈니스_규칙']
            if not rules:
                self.results.append(ValidationResult(
                    level=ValidationLevel.INFO,
                    category="해석 가능성",
                    message="비즈니스 규칙이 정의되지 않았습니다",
                    field="비즈니스_규칙"
                ))

    def validate_calculation(self,
                           formula: str,
                           sample_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        계산식 검증 (샘플 데이터로 테스트)

        Args:
            formula: 계산식 문자열
            sample_data: 샘플 데이터 딕셔너리

        Returns:
            검증 결과 및 계산 값
        """
        result = {
            'valid': True,
            'value': None,
            'errors': []
        }

        try:
            # 안전한 계산을 위한 네임스페이스
            namespace = {
                'safe_divide': lambda a, b: a / b if b != 0 else 0,
                'abs': abs,
                'round': round,
                **sample_data
            }

            # 계산 실행
            value = eval(formula, {"__builtins__": {}}, namespace)
            result['value'] = value

            # 결과 검증
            if value is None:
                result['errors'].append("계산 결과가 None입니다")
                result['valid'] = False

            if isinstance(value, (int, float)) and value < 0:
                result['errors'].append(f"계산 결과가 음수입니다: {value}")

        except ZeroDivisionError:
            result['valid'] = False
            result['errors'].append("0으로 나누기 오류 발생")
        except Exception as e:
            result['valid'] = False
            result['errors'].append(f"계산 오류: {str(e)}")

        return result

    def print_results(self):
        """검증 결과 출력"""
        if not self.results:
            print("✅ 검증 통과: 모든 항목이 정상입니다")
            return

        # 레벨별 그룹화
        errors = [r for r in self.results if r.level == ValidationLevel.ERROR]
        warnings = [r for r in self.results if r.level == ValidationLevel.WARNING]
        infos = [r for r in self.results if r.level == ValidationLevel.INFO]

        print(f"\n📊 검증 결과 요약")
        print(f"  오류: {len(errors)}개")
        print(f"  경고: {len(warnings)}개")
        print(f"  정보: {len(infos)}개")
        print()

        # 오류 출력
        if errors:
            print("❌ 오류:")
            for r in errors:
                field_info = f" [{r.field}]" if r.field else ""
                print(f"  - {r.category}{field_info}: {r.message}")
            print()

        # 경고 출력
        if warnings:
            print("⚠️  경고:")
            for r in warnings:
                field_info = f" [{r.field}]" if r.field else ""
                print(f"  - {r.category}{field_info}: {r.message}")
            print()

        # 정보 출력
        if infos:
            print("ℹ️  정보:")
            for r in infos:
                field_info = f" [{r.field}]" if r.field else ""
                print(f"  - {r.category}{field_info}: {r.message}")


def main():
    """메인 함수 - 사용 예시"""

    # 예시 지표 정의
    sample_metric = {
        '지표명': 'PRO 매출 기여도',
        '영문명': 'PRO Revenue Contribution',
        '정의': 'PRO 기능을 통해 발생한 매출 합계',
        '계산식': 'SEO_매출 + CRM_매출 + 프로모션_매출 + 채널_매출',
        '데이터_소스': {
            'API': 'CA 2.0 /ca2/attribution/traffic-analysis',
            '필드': 'order_amount',
            '기간': '월간'
        },
        '단위': '원',
        '반올림': '정수',
        '예외_처리': {
            'NULL': '0원으로 처리',
            '0': '넛지 표시',
            '음수': '오류 로깅'
        },
        '인사이트': 'PRO가 만들어준 매출은 {금액}원입니다'
    }

    # 검증 실행
    validator = MetricValidator()
    results = validator.validate_metric_definition(sample_metric)
    validator.print_results()

    # 계산식 검증
    print("\n🧮 계산식 테스트:")
    sample_data = {
        'SEO_매출': 500000,
        'CRM_매출': 300000,
        '프로모션_매출': 200000,
        '채널_매출': 400000
    }
    calc_result = validator.validate_calculation(
        sample_metric['계산식'],
        sample_data
    )

    if calc_result['valid']:
        print(f"✅ 계산 성공: {calc_result['value']:,}원")
    else:
        print(f"❌ 계산 실패:")
        for error in calc_result['errors']:
            print(f"  - {error}")


if __name__ == '__main__':
    main()
