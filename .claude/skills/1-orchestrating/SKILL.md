---
name: orchestrating
description: 복잡한 문제를 분석하고 전문가 스킬들을 조율하여 해결하는 마스터 오케스트레이터. 순차/병렬/회의 모드로 전문가 스킬들을 지능적으로 조율하여 다면적 문제를 해결합니다.
---

# Orchestrating

## 개요

전문가 스킬들을 조율하여 복잡한 문제를 해결하는 마스터 오케스트레이터 스킬입니다.

**핵심 프로세스:**
1. **분석** → 요청의 범위와 복잡도 파악
2. **결정** → 최적 모드 선택 (순차/병렬/회의)
3. **위임** → 전문가 스킬에 명확한 컨텍스트 전달
4. **통합** → 여러 결과를 응집력 있는 솔루션으로 합성
5. **검증** → 최종 결과물이 요청을 충족하는지 확인

**산출물 원칙:** 이모지 사용 금지. 텍스트로 명확히 표현.

---

## 3가지 오케스트레이션 모드

### Mode A: 순차 실행
**조건:** 단계가 이전 결과에 의존
**예시:** 기능 개발 (설계 → 계획 → 구현 → 테스트)

### Mode B: 병렬 실행
**조건:** 독립적 작업, 의존성 없음
**예시:** 성능/보안/확장성 동시 분석

### Mode C: 회의 모드
**조건:** 여러 관점 종합 필요, 전략적 결정
**예시:** 아키텍처 재설계

---

## 빠른 시작

### 요청 분석 체크리스트
```
[ ] 최종 결과물? (문서/구현/결정/분석)
[ ] 몇 개의 전문성 도메인?
[ ] 단계별 순서? → Mode A
[ ] 독립 작업? → Mode B
[ ] 관점 종합? → Mode C
```

### 전략 선언 템플릿
```
분석 결과, 이 요청은 [Mode A/B/C]로 처리합니다.

[Mode A] 단계별 실행:
1. Phase 1: [전문가] - [결과물]
2. Phase 2: [전문가] - [결과물]

[Mode B] 병렬 스트림:
- Stream 1: [전문가] - [작업]
- Stream 2: [전문가] - [작업]

[Mode C] 전문가 회의:
- [전문가 1]: [관점]
- [전문가 2]: [관점]
회의 주제: [문제]
```

---

## 핵심 전문가 스킬

### 분석/디버깅
- `systematic-debugging`: 근본 원인 분석
- `root-cause-tracing`: 버그 역추적

### 설계/계획
- `brainstorming`: 소크라테스식 질문으로 설계 정제
- `writing-plans`: 상세 구현 계획

### 구현/검증
- `test-driven-development`: TDD 워크플로우
- `code-reviewer`: 품질 리뷰
- `verification-before-completion`: 증거 기반 검증

### 프로젝트 관리
- `msa_project_manager` (mpm): Wiki 문서화, Jira 통합

### 도메인 전문
- `benchmarking`: 글로벌 E-commerce 비교 분석 (Shopify, GA4)
- `data-analyzing`: GA4 방법론 기반 데이터 검증

---

## 주요 패턴

**기능 개발:**
```
brainstorming → writing-plans → TDD → code-reviewer → verification → mpm
```

**Jira 분석:**
```
systematic-debugging → root-cause-tracing → writing-plans → TDD → mpm
```

**데이터 검증:**
```
data-analyzing → verification → mpm
```

**경쟁사 분석:**
```
benchmarking (병렬) → brainstorming → writing-plans → verification → mpm
```

---

## 모범 사례

### DO
- 실행 전 모드와 계획 명확히 공지
- 전문가에게 관련 컨텍스트만 전달
- 결과물 신중히 통합
- 증거 기반 권장사항
- CLAUDE.md 가이드라인 준수

### DON'T
- 전략 선언 없이 실행
- 전문가에게 컨텍스트 과부하
- 결과물 맹목적 수용
- 증거 없는 권장사항
- 프로젝트 규칙 무시

---

## 참조

**프로젝트:**
- `CLAUDE.md`: 프로젝트 스킬 사용 규칙 및 상세 가이드

**원칙:**
> "오케스트레이터의 지능은 조율에 있지 전문화에 있지 않다. 전문가를 신뢰하고, 현명하게 통합하며, 응집력 있게 전달하라."
