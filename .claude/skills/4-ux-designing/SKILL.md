---
name: 4-ux-designing
description: This skill should be used when the user requests UI/UX design improvements for the PRO Report project, including redesigning buttons, CTA elements, entire screens, or creating customer-centric interfaces. Specializes in optimizing conversion-focused design elements like "매출 boost하기" buttons and dashboard layouts. Use this skill when users mention improving visual appeal, clickability, user engagement, or overall screen redesign for cafe24 PRO Report shopkeepers. Works seamlessly with 1-orchestrating, 2-benchmarking, and 3-data-analyzing skills.
---

# PRO Report UX/UI Designer

## Overview

Transform PRO Report interfaces into high-converting, customer-centric designs. This skill specializes in redesigning UI elements (buttons, cards, CTAs) and full screens for cafe24 PRO Report, targeting shopkeepers who need clear, actionable insights. Outputs include Figma prototypes, HTML/CSS implementations, and design specifications using CDS AI design system.

## When to Use This Skill

Activate this skill when users request:
- "이 버튼을 더 이쁘게 만들어줘" (button redesign)
- "매출 boost하기 버튼이 눌러보고 싶게 바꿔줘" (CTA optimization)
- "전체 화면을 고객 중심으로 다시 그려줘" (full screen redesign)
- "PRO 리포트 카드 레이아웃 개선해줘" (layout improvement)
- Improving visual appeal and clickability of any PRO Report component

## Core Design Philosophy

### 1. Customer-First Design (고객이 원하는 화면)
- **Clarity over decoration**: 사장님이 5초 안에 이해할 수 있는 디자인
- **Action-oriented**: 매출 증대로 연결되는 명확한 행동 유도
- **Data visibility**: 핵심 지표를 한눈에 파악

### 2. PRO Report Context
Target User: 카페24 쇼핑몰 사장님
- 매일 확인: PRO 매출 기여도, 절약 시간/비용, 오늘의 매출
- 빠른 의사결정이 필요한 바쁜 사장님
- 모바일 우선 (Admin 앱에서 주로 확인)

Key Questions to Answer Through Design:
- "PRO가 내 매출에 얼마나 기여했나?"
- "PRO가 시간을 얼마나 절약해줬나?"
- "다음에 뭘 해야 하나?"

## Design Workflow

### Step 1: Understand Context
Ask clarifying questions:
- "어떤 요소를 개선하고 싶으신가요? (버튼, 카드, 전체 화면?)"
- "현재 문제점이 무엇인가요? (안 이쁨, 안 눌러짐, 이해 안 됨?)"
- "목표 액션은 무엇인가요? (클릭 유도, 정보 전달, 다음 단계 안내?)"

### Step 2: Design Exploration
Generate 2-3 design variants:
- **Option A**: Conservative (기존 스타일 유지, 소폭 개선)
- **Option B**: Moderate (CDS AI 기반, 균형 잡힌 개선)
- **Option C**: Bold (완전히 새로운 접근, 고객 중심 재설계)

### Step 3: Output Generation
Choose output format based on user preference:
- **Figma Make**: Interactive prototype
- **Gemini Antigravity**: AI-generated design
- **Nano Banana**: Component-based design
- **HTML/CSS**: Code implementation
- **Design Spec**: Confluence wiki documentation

### Step 4: Validation & Iteration
- CDS AI compliance check
- Accessibility validation (contrast ratio, touch target size)
- Mobile responsiveness verification
- User feedback incorporation

## Design Patterns for PRO Report

### Pattern 1: High-Converting CTA Buttons

**Before**:
```
┌─────────────────┐
│ 매출 boost하기  │ ← Plain, low engagement
└─────────────────┘
```

**After (Option A - Conservative)**:
```
┌─────────────────────────┐
│ 💰 매출 boost하기       │ ← Icon + Color
│ 평균 +25% 증가          │ ← Social proof
└─────────────────────────┘
```

**After (Option B - CDS AI)**:
```
┌──────────────────────────────┐
│  📈 매출 25% 더 올리기       │ ← Benefit-focused
│  PRO 기능 3가지 추천         │ ← Clear value prop
│  [지금 확인하기 →]           │ ← Strong CTA
└──────────────────────────────┘
```

**After (Option C - Bold)**:
```
╔═══════════════════════════════╗
║ 이번 달 52만원 더 벌 수 있어요 ║ ← Specific benefit
║                               ║
║ [SEO 최적화로 달성 →]         ║ ← Actionable path
║ PRO 평균 대비 +15% 가능       ║ ← Benchmark
╚═══════════════════════════════╝
```

Design Principles:
- Use specific numbers (52만원) over generic phrases (매출 올리기)
- Show outcome, not feature ("52만원 더" vs "매출 boost")
- Make next step obvious with arrow icon (→)

### Pattern 2: Data Visualization Cards

**Tier 1 Card Structure** (PRO 매출 기여도):
```
┌─────────────────────────────────────┐
│ PRO가 만들어준 매출                 │ ← Clear label
│                                     │
│     1,234,567원                     │ ← Big number
│     ▲ 지난달 대비 +15.3%            │ ← Trend
│                                     │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ SEO     CRM    프로모션   채널     │ ← Breakdown
│ 52만    38만    28만      5.4만    │
│ ████    ███     ██        █        │ ← Visual bar
└─────────────────────────────────────┘
```

Design Principles:
- Big number for primary metric (font-size: 32px)
- Trend indicator with color (green ▲ for positive)
- Breakdown with mini bar chart (visual comparison)
- Touch target ≥ 44×44px (mobile)

### Pattern 3: Action-Oriented Insight Messages

**Generic (Avoid)**:
```
PRO가 절약해준 시간은 42.5시간입니다.
```

**Actionable (Use)**:
```
┌─────────────────────────────────────┐
│ PRO가 42.5시간 절약해줬어요         │
│ = 신규 상품 85개 기획할 시간        │ ← Concrete value
│                                     │
│ [더 많은 시간 확보하기 →]           │ ← Next action
└─────────────────────────────────────┘
```

Design Principles:
- Translate abstract metrics to concrete value
- Suggest next actionable step
- Use conversational tone (했어요, 할 수 있어요)

## CDS AI Design System Integration

### Color Palette
```
Primary: #0066FF (PRO Blue)
Success: #00C73C (Growth Green)
Warning: #FFB800 (Attention Yellow)
Danger: #FF4444 (Alert Red)
Neutral: #333333 (Text), #F5F5F5 (Background)
```

### Typography
```
Heading 1: Pretendard Bold 32px (핵심 숫자)
Heading 2: Pretendard SemiBold 24px (섹션 제목)
Body 1: Pretendard Regular 16px (본문)
Body 2: Pretendard Regular 14px (부가 설명)
Caption: Pretendard Regular 12px (힌트)
```

### Spacing System
```
4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px
```

### Component Library Reference
Access via: `references/cds-components.md`

## Output Formats

### Format 1: Figma Prototype
Generate Figma URL with:
- Interactive prototype (clickable buttons)
- Design specs (spacing, colors, typography)
- Component variants (hover, active, disabled states)

**Example Output**:
```markdown
## Figma Prototype

**URL**: https://figma.com/design/[project-id]
**Screens**:
- 상단 핵심 카드 (Before/After)
- 매출 boost 버튼 개선안 3종
- 인사이트 메시지 레이아웃

**Design Specs**:
- Button: 160×48px, Radius 8px, Primary color
- Card: Padding 24px, Shadow 0 2px 8px rgba(0,0,0,0.1)
- Typography: Pretendard SemiBold 16px
```

### Format 2: HTML/CSS Implementation
Generate production-ready code:
```html
<!-- PRO 매출 기여도 카드 -->
<div class="pro-metric-card">
  <h3 class="card-title">PRO가 만들어준 매출</h3>
  <div class="metric-value">1,234,567원</div>
  <div class="metric-trend positive">
    <span class="icon">▲</span>
    지난달 대비 +15.3%
  </div>
  <div class="metric-breakdown">
    <!-- Breakdown items -->
  </div>
</div>

<style>
.pro-metric-card {
  padding: 24px;
  background: #FFFFFF;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.metric-value {
  font-family: 'Pretendard', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: #333333;
  margin: 16px 0;
}

.metric-trend.positive {
  color: #00C73C;
  font-weight: 600;
}
/* ... */
</style>
```

### Format 3: Confluence Wiki Documentation
Generate design specification for developers:
```markdown
# [PRO 리포트] 매출 boost 버튼 개선

## Before/After
[스크린샷]

## Design Specs
- Size: 160×48px (Mobile), 200×56px (Desktop)
- Color: Primary #0066FF
- Typography: Pretendard SemiBold 16px
- Icon: 📈 (16×16px, left aligned)
- States: Default, Hover, Active, Disabled

## Implementation Notes
- Touch target ≥ 44×44px
- Contrast ratio ≥ 4.5:1 (WCAG AA)
- Ripple effect on click (Material Design)
```

## Accessibility Checklist

Before finalizing any design, validate:
- [ ] Color contrast ratio ≥ 4.5:1 for text, ≥ 3:1 for UI components
- [ ] Touch target size ≥ 44×44px (iOS), ≥ 48×48px (Android)
- [ ] Focus indicator visible for keyboard navigation
- [ ] Alt text for decorative icons (or aria-hidden="true")
- [ ] Responsive breakpoints: Mobile 375px, Tablet 768px, Desktop 1280px

## Example Workflows

### Workflow 1: Button Redesign Request
```
User: "매출 boost하기 버튼을 더 이쁘게 만들어줘"

Designer Skill Response:
1. "현재 버튼의 문제점을 파악했습니다. (plain text, low engagement)"
2. "3가지 개선안을 제안드립니다:"
   - Option A: Conservative (아이콘 + 색상 개선)
   - Option B: CDS AI (benefit-focused messaging)
   - Option C: Bold (완전히 새로운 접근)
3. "어떤 방향이 마음에 드시나요?"
```

### Workflow 2: Full Screen Redesign
```
User: "전체 화면을 고객이 정말 원하는 화면으로 다시 그려줘"

Designer Skill Response:
1. "PRO 리포트 핵심 질문 3가지를 기반으로 재설계하겠습니다:"
   - "PRO가 내 매출에 얼마나 기여했나?"
   - "PRO가 시간을 얼마나 절약해줬나?"
   - "다음에 뭘 해야 하나?"
2. "정보 계층 구조 재정의 (F-pattern layout)"
3. "Figma 프로토타입 생성 중..."
4. "HTML/CSS 코드 구현 완료"
```

## Quality Standards

Every design output must meet:
- **Visual Hierarchy**: Clear primary/secondary/tertiary levels
- **Whitespace**: Minimum 16px between elements, 24px for sections
- **Consistency**: CDS AI components used throughout
- **Performance**: Images optimized (WebP), CSS minified
- **Localization**: Korean-first, but extensible to multi-language

## Resources

### references/
- `cds-components.md`: CDS AI design system component library
- `proreport-metrics.md`: PRO Report core metrics and messaging guide
- `accessibility-guidelines.md`: WCAG 2.1 AA compliance checklist

### assets/
- `templates/card-layout.html`: Reusable card component template
- `templates/button-variants.html`: CTA button variants (primary, secondary, outline)
- `icons/`: PRO Report icon set (SVG, optimized)
- `mockups/`: Before/After design examples

### scripts/
- `generate-figma-url.py`: Auto-generate Figma prototype URL
- `validate-contrast.py`: Check color contrast ratio (WCAG compliance)
- `export-design-tokens.py`: Export CDS AI design tokens (JSON)

---

## Orchestrating Support

This skill is designed to work seamlessly with the `orchestrating` skill for complex, multi-faceted design projects.

### When Orchestrating Should Invoke This Skill

The orchestrating skill should call `proreport-ux-designer` when:

1. **UI/UX Design Tasks**: Any request involving visual design, layout, or user interface improvements
2. **Conversion Optimization**: When improving CTAs, buttons, or engagement elements
3. **Full Screen Redesign**: Complete interface overhauls requiring design expertise
4. **Component Design**: Creating or improving specific UI components (cards, buttons, forms)

### Orchestrating Workflow Examples

#### Example 1: End-to-End Feature Design
```
User Request: "PRO 리포트에 고객 성장 단계 배지를 추가하고 화면에 이쁘게 표시해줘"

Orchestrating Workflow:
1. Call `data-analyzing` skill → Define growth stage metrics
2. Call `proreport-ux-designer` skill → Design badge UI and layout
3. Call `system-document` skill → Document in Wiki
```

#### Example 2: Data-Driven Design Improvement
```
User Request: "매출 추이 그래프를 더 직관적으로 개선하고 벤치마크도 추가해줘"

Orchestrating Workflow:
1. Call `benchmarking` skill → Research Shopify/Amazon chart patterns
2. Call `data-analyzing` skill → Validate metric calculations
3. Call `proreport-ux-designer` skill → Design improved chart UI
4. Call `system-document` skill → Create design spec in Wiki
```

#### Example 3: Complete Screen Redesign
```
User Request: "PRO 리포트 메인 화면을 전체적으로 재설계하고 문서화해줘"

Orchestrating Workflow:
1. Call `data-analyzing` skill → Prioritize metrics (Tier 1/2/3)
2. Call `benchmarking` skill → Study competitor dashboards
3. Call `proreport-ux-designer` skill → Create new layout design
4. Call `system-document` skill → Generate comprehensive Wiki page
```

### Input/Output Contract for Orchestrating

**Expected Input from Orchestrating**:
```json
{
  "task_type": "button_redesign | card_layout | full_screen | component_design",
  "current_design": "Description or screenshot URL",
  "requirements": {
    "target_metric": "PRO 매출 기여도",
    "goal": "Increase click-through rate by 25%",
    "constraints": ["Mobile-first", "CDS AI compliant"]
  },
  "context": {
    "data_insights": "From data-analyzing skill",
    "benchmarks": "From benchmarking skill"
  }
}
```

**Output to Orchestrating**:
```json
{
  "design_variants": [
    {
      "name": "Option A - Conservative",
      "description": "...",
      "figma_url": "https://figma.com/...",
      "html_code": "...",
      "accessibility_score": "AA compliant"
    }
  ],
  "recommendations": "Use Option B for highest conversion",
  "implementation_notes": "...",
  "next_steps": ["User testing", "Developer handoff"]
}
```

### Collaboration Signals

**Signal to Orchestrator**: Request additional data analysis
```
"Need metric validation for growth score calculation.
Please invoke data-analyzing skill to verify formula."
```

**Signal to Orchestrator**: Request benchmarking
```
"Need competitor research for dashboard layout patterns.
Please invoke benchmarking skill to study Shopify/Amazon."
```

**Signal to Orchestrator**: Request documentation
```
"Design complete. Ready for Wiki documentation.
Please invoke system-document skill with design specs."
```

### Handoff Points

1. **From data-analyzing → proreport-ux-designer**:
   - Metric definitions validated
   - Calculation formulas confirmed
   - Data hierarchy established

2. **From benchmarking → proreport-ux-designer**:
   - Competitor UI patterns identified
   - Best practices documented
   - Design inspiration gathered

3. **From proreport-ux-designer → system-document**:
   - Design specifications finalized
   - HTML/CSS code ready
   - Accessibility validated

---

**Key Differentiators**:
- PRO Report domain expertise (shopkeeper needs, core metrics)
- Multi-format output (Figma, HTML/CSS, Wiki)
- Conversion-focused design (CTA optimization, action-oriented)
- CDS AI design system integration (brand consistency)
- Accessibility-first approach (WCAG AA compliance)
- **Orchestrating-ready**: Seamless integration with other expert skills
