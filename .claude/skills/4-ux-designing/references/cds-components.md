# CDS AI Design System Component Library

**버전**: 1.0.0
**마지막 업데이트**: 2025-11-25
**출처**: 카페24 CDS AI 디자인 시스템

---

## 1. Button Components

### Primary Button
```html
<button class="cds-btn cds-btn-primary">
  버튼 텍스트
</button>
```

**Specs**:
- Height: 48px (Desktop), 44px (Mobile)
- Padding: 12px 24px
- Border-radius: 8px
- Font: Pretendard SemiBold 16px
- Color: #FFFFFF on #0066FF

**States**:
- Default: Background #0066FF
- Hover: Background #0052CC
- Active: Background #003D99
- Disabled: Background #CCCCCC, Opacity 0.5

### Secondary Button
```html
<button class="cds-btn cds-btn-secondary">
  버튼 텍스트
</button>
```

**Specs**:
- Same as Primary, but:
- Color: #0066FF on #FFFFFF
- Border: 1px solid #0066FF

### Icon Button
```html
<button class="cds-btn cds-btn-icon">
  <svg>...</svg>
  버튼 텍스트
</button>
```

**Specs**:
- Icon: 16×16px, left aligned, 8px margin-right
- Use Material Icons or Custom SVG

---

## 2. Card Components

### Metric Card (PRO Report Specialized)
```html
<div class="cds-card cds-metric-card">
  <h3 class="cds-card-title">카드 제목</h3>
  <div class="cds-metric-value">1,234,567원</div>
  <div class="cds-metric-trend positive">
    <span class="cds-icon-arrow-up"></span>
    +15.3%
  </div>
</div>
```

**Specs**:
- Padding: 24px
- Background: #FFFFFF
- Border-radius: 12px
- Shadow: 0 2px 8px rgba(0, 0, 0, 0.1)
- Border: 1px solid #E0E0E0 (optional)

**Metric Value**:
- Font: Pretendard Bold 32px
- Color: #333333
- Line-height: 1.2

**Trend Indicator**:
- Positive: Color #00C73C, icon ▲
- Negative: Color #FF4444, icon ▼
- Neutral: Color #666666, icon ━

### Info Card
```html
<div class="cds-card cds-info-card">
  <div class="cds-card-header">
    <h4>카드 헤더</h4>
    <button class="cds-btn-icon">...</button>
  </div>
  <div class="cds-card-body">
    <p>카드 본문 내용</p>
  </div>
  <div class="cds-card-footer">
    <a href="#" class="cds-link">더 보기 →</a>
  </div>
</div>
```

**Specs**:
- Header: Padding 16px 24px, Border-bottom 1px solid #E0E0E0
- Body: Padding 24px
- Footer: Padding 16px 24px, Border-top 1px solid #E0E0E0

---

## 3. Typography

### Headings
```css
.cds-h1 {
  font-family: 'Pretendard', sans-serif;
  font-size: 32px;
  font-weight: 700;
  line-height: 1.25;
  color: #333333;
}

.cds-h2 {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.3;
}

.cds-h3 {
  font-size: 20px;
  font-weight: 600;
  line-height: 1.4;
}
```

### Body Text
```css
.cds-body-1 {
  font-size: 16px;
  font-weight: 400;
  line-height: 1.5;
  color: #333333;
}

.cds-body-2 {
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  color: #666666;
}

.cds-caption {
  font-size: 12px;
  font-weight: 400;
  line-height: 1.4;
  color: #999999;
}
```

---

## 4. Color System

### Primary Colors
```css
--cds-primary: #0066FF;
--cds-primary-dark: #0052CC;
--cds-primary-light: #3385FF;
```

### Semantic Colors
```css
--cds-success: #00C73C;
--cds-warning: #FFB800;
--cds-danger: #FF4444;
--cds-info: #0066FF;
```

### Neutral Colors
```css
--cds-gray-900: #333333; /* Text primary */
--cds-gray-700: #666666; /* Text secondary */
--cds-gray-500: #999999; /* Text tertiary */
--cds-gray-300: #CCCCCC; /* Border */
--cds-gray-100: #F5F5F5; /* Background */
--cds-white: #FFFFFF;
```

### Usage
- **Text**: Use gray-900 for primary, gray-700 for secondary
- **Backgrounds**: Use gray-100 for page, white for cards
- **Borders**: Use gray-300 for dividers

---

## 5. Spacing System

```css
--cds-space-1: 4px;
--cds-space-2: 8px;
--cds-space-3: 12px;
--cds-space-4: 16px;
--cds-space-6: 24px;
--cds-space-8: 32px;
--cds-space-12: 48px;
--cds-space-16: 64px;
```

### Usage Guidelines
- Element padding: Use space-4 (16px) minimum
- Section padding: Use space-6 (24px) or space-8 (32px)
- Page margin: Use space-8 (32px) or space-12 (48px)

---

## 6. Icons

### Icon Library
Use Material Icons or custom SVG icons.

**Standard Sizes**:
- Small: 16×16px (inline with text)
- Medium: 24×24px (buttons, cards)
- Large: 32×32px (feature icons)

**PRO Report Custom Icons**:
- `icon-pro-sales.svg`: PRO 매출 아이콘
- `icon-time-saved.svg`: 시간 절약 아이콘
- `icon-trend-up.svg`: 상승 추세 (▲)
- `icon-trend-down.svg`: 하락 추세 (▼)

### Usage
```html
<!-- Material Icons -->
<span class="material-icons">trending_up</span>

<!-- Custom SVG -->
<svg class="cds-icon" width="24" height="24">
  <use href="#icon-pro-sales"></use>
</svg>
```

---

## 7. Layout Grid

### Grid System
```css
.cds-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
}

.cds-row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -12px;
}

.cds-col {
  flex: 1;
  padding: 0 12px;
}
```

### Breakpoints
```css
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large Desktop */ }
```

---

## 8. Shadows

```css
--cds-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--cds-shadow-md: 0 2px 8px rgba(0, 0, 0, 0.1);
--cds-shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.15);
```

### Usage
- Cards: Use shadow-md
- Modal/Popups: Use shadow-lg
- Hover states: Increase shadow on hover

---

## 9. Border Radius

```css
--cds-radius-sm: 4px;
--cds-radius-md: 8px;
--cds-radius-lg: 12px;
--cds-radius-xl: 16px;
--cds-radius-full: 9999px; /* Circular */
```

### Usage
- Buttons: radius-md (8px)
- Cards: radius-lg (12px)
- Pills/Badges: radius-full

---

## 10. Transitions

```css
--cds-transition-fast: 150ms ease-in-out;
--cds-transition-base: 250ms ease-in-out;
--cds-transition-slow: 350ms ease-in-out;
```

### Usage
```css
.cds-btn {
  transition: all var(--cds-transition-base);
}

.cds-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--cds-shadow-md);
}
```

---

## 11. Accessibility

### Contrast Requirements
- Normal text (≥16px): Contrast ratio ≥ 4.5:1
- Large text (≥24px): Contrast ratio ≥ 3:1
- UI components: Contrast ratio ≥ 3:1

### Touch Targets
- Mobile: Minimum 44×44px (iOS)
- Android: Minimum 48×48px

### Focus States
```css
.cds-btn:focus {
  outline: 2px solid var(--cds-primary);
  outline-offset: 2px;
}
```

---

## 12. PRO Report Specific Components

### CTA Banner (매출 boost하기)
```html
<div class="cds-cta-banner">
  <div class="cds-cta-content">
    <h3>이번 달 52만원 더 벌 수 있어요</h3>
    <p>SEO 최적화로 PRO 평균 대비 +15% 가능</p>
  </div>
  <button class="cds-btn cds-btn-primary">
    지금 확인하기 →
  </button>
</div>
```

**Specs**:
- Background: Linear gradient (#F0F7FF to #FFFFFF)
- Padding: 24px
- Border-radius: 12px
- Border: 1px solid #D6E9FF

### Metric Breakdown Bar
```html
<div class="cds-metric-breakdown">
  <div class="cds-breakdown-item" style="--percentage: 40%;">
    <span class="cds-breakdown-label">SEO</span>
    <span class="cds-breakdown-value">52만</span>
    <div class="cds-breakdown-bar" style="width: var(--percentage);"></div>
  </div>
  <!-- Repeat for CRM, 프로모션, 채널 -->
</div>
```

**Specs**:
- Bar height: 8px
- Bar colors: Use primary, success, warning, info
- Spacing: 12px between items

---

**참고 자료**:
- CDS AI 공식 문서: [내부 링크]
- Pretendard 폰트: https://github.com/orioncactus/pretendard
- Material Icons: https://fonts.google.com/icons
