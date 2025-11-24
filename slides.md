---
marp: true
title: Product Documentation Presentation
theme: custom-theme
paginate: true
author: Sweta (22f3001133@ds.study.iitm.ac.in)
keywords: product, documentation, software, engineering
size: 16:9
style: |
  @theme custom-theme
  
  :root {
    --color-background: #f5f7fa;
    --color-foreground: #2d3748;
    --color-primary: #3182ce;
    --color-secondary: #805ad5;
    --font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
  }
  
  section {
    font-family: var(--font-family);
    color: var(--color-foreground);
    background-color: var(--color-background);
    padding: 60px;
    font-size: 28px;
    line-height: 1.5;
  }
  
  h1 {
    font-size: 60px;
    color: var(--color-primary);
    font-weight: 700;
    margin-bottom: 20px;
  }
  
  h2 {
    font-size: 48px;
    color: var(--color-secondary);
    font-weight: 600;
    margin-bottom: 30px;
    border-bottom: 3px solid var(--color-primary);
    padding-bottom: 10px;
  }
  
  h3 {
    font-size: 36px;
    color: var(--color-primary);
    font-weight: 600;
    margin: 20px 0 15px 0;
  }
  
  p {
    margin: 15px 0;
    line-height: 1.6;
  }
  
  ul, ol {
    margin-left: 40px;
  }
  
  li {
    margin: 12px 0;
  }
  
  code {
    background-color: #edf2f7;
    color: var(--color-secondary);
    padding: 4px 8px;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
  }
  
  pre {
    background-color: #2d3748;
    color: #e2e8f0;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 18px;
    margin: 15px 0;
  }
  
  strong {
    color: var(--color-secondary);
    font-weight: 600;
  }
  
  /* Page number styling */
  section::after {
    content: 'Page ' attr(data-marpit-pagination);
    position: absolute;
    bottom: 20px;
    right: 30px;
    font-size: 20px;
    color: var(--color-primary);
    font-weight: 600;
  }
  
  /* Title slide styling */
  section.title h1 {
    font-size: 72px;
    margin-bottom: 40px;
  }
  
  section.title h2 {
    font-size: 32px;
    border: none;
    color: var(--color-foreground);
  }
  
  section.title p {
    font-size: 24px;
    color: var(--color-primary);
  }
  
  /* Content slide styling */
  section.content-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  /* Emphasis box */
  .emphasis-box {
    background-color: #ebf4ff;
    border-left: 4px solid var(--color-primary);
    padding: 20px;
    margin: 20px 0;
    border-radius: 4px;
  }
  
  .emphasis-box strong {
    color: var(--color-primary);
  }
  
  /* Equation styling */
  .equation {
    background-color: #f9fafb;
    border: 1px solid #e2e8f0;
    padding: 15px;
    border-radius: 4px;
    margin: 20px 0;
    font-size: 24px;
  }
  
  /* Table styling */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
  }
  
  table th {
    background-color: var(--color-primary);
    color: white;
    padding: 12px;
    text-align: left;
  }
  
  table td {
    border: 1px solid #e2e8f0;
    padding: 12px;
  }
  
  table tr:nth-child(even) {
    background-color: #f9fafb;
  }
  
  /* Directive styling */
  .directive-highlight {
    background-color: #fef5e7;
    border-left: 5px solid #f39c12;
    padding: 15px;
    margin: 15px 0;
    border-radius: 4px;
  }
  
  .code-highlight {
    background-color: #fff3cd;
    border-left: 5px solid #ff6b6b;
    padding: 10px 15px;
    font-family: 'Courier New', monospace;
    margin: 10px 0;
  }
---

<!-- Slide 1: Title Slide -->
# Product Documentation System

## Comprehensive Guide to Technical Documentation

**Author:** Sweta  
**Email:** 22f3001133@ds.study.iitm.ac.in  
**Date:** November 2025  
**Organization:** Software Engineering Team

---

<!-- Slide 2: Overview with Custom Styling -->
## Documentation Architecture

<div class="emphasis-box">
<strong>Key Objective:</strong> Create maintainable, version-controlled documentation that converts seamlessly across multiple formats.
</div>

### Core Components

- **Version Control Integration** - Git-based workflow
- **Format Flexibility** - HTML, PDF, PPTX exports
- **Custom Theming** - Brand-aligned styling
- **Mathematical Support** - LaTeX equations
- **Responsive Design** - Works on all devices

---

<!-- Slide 3: Algorithmic Complexity - Mathematical Equations -->
## Algorithmic Complexity Analysis

Understanding performance characteristics of our system:

<div class="equation">
$$
T(n) = O(n \log n) + O(m)
$$
</div>

Where:
- **n** = number of operations
- **m** = memory overhead

### Time Complexity Breakdown

$$
\begin{aligned}
\text{Best Case} &: O(n) \\
\text{Average Case} &: O(n \log n) \\
\text{Worst Case} &: O(n^2)
\end{aligned}
$$

---

<!-- Slide 4: Features Table -->
## Feature Comparison Matrix

| Feature | Basic | Professional | Enterprise |
|---------|-------|--------------|------------|
| Page Numbers | ❌ | ✅ | ✅ |
| Custom Themes | ❌ | ✅ | ✅ |
| Math Equations | ❌ | ✅ | ✅ |
| Background Images | ❌ | ✅ | ✅ |
| Version Control | ✅ | ✅ | ✅ |
| Multi-format Export | ❌ | ✅ | ✅ |

---

<!-- Slide 5: Background Image Slide with footer directive -->
![bg contain](https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80)

## Version Control Integration

### Git Workflow for Presentations

- Commit markdown source files
- Track changes with meaningful commit messages
- Collaborative editing through pull requests
- Automatic builds on push events

<!-- footer: Marp - Markdown Presentation Ecosystem -->

---

<!-- Slide 6: Code Implementation with multiple directives -->
## Implementation Example

### Docker-based Deployment

<div class="code-highlight">
<!-- _class: directive-highlight -->
# Use Marp directives for slide control
</div>

```bash
# Install Marp CLI
npm install --save-dev @marp-team/marp-cli

# Convert to HTML
marp slides.md --output slides.html

# Convert to PDF
marp slides.md --output slides.pdf

# Watch mode for live editing
marp -w slides.md
```

---

<!-- Slide 7: Advanced Mathematics -->
## Statistical Distribution Functions

### Normal Distribution Equation

<div class="equation">
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$
</div>

### Complexity Matrix Notation

$$
\begin{pmatrix}
O(1) & O(\log n) & O(n) \\
O(n \log n) & O(n^2) & O(2^n)
\end{pmatrix}
$$

<!-- _footer: "Statistical analysis - Performance metrics" -->

---

<!-- Slide 8: Best Practices with scoped styling directive -->
## Best Practices for Documentation

<!-- _class: content-slide -->

### Maintainability Checklist

- ✅ Use semantic markdown for consistency
- ✅ Store custom themes in separate CSS files
- ✅ Implement automated testing for exports
- ✅ Use meaningful commit messages
- ✅ Document all custom directives
- ✅ Maintain version compatibility

### Quality Assurance

<div class="emphasis-box">
<strong>Pro Tip:</strong> Integrate with CI/CD pipelines to automatically build and test presentations on every commit.
</div>

---

<!-- Slide 9: Directory Structure with styling -->
## Project Organization

<!-- _class: content-slide -->

```
project-root/
├── slides.md           # Main presentation file
├── theme/
│   └── custom-theme.css # Custom theme definition
├── images/
│   ├── background.png
│   ├── logo.svg
│   └── diagrams/
├── .github/
│   └── workflows/
│       └── build.yml   # CI/CD pipeline
├── .gitignore
├── package.json
└── README.md
```

---

<!-- Slide 10: Deployment with footer -->
## CI/CD Pipeline Integration

<!-- _footer: "Automated builds with GitHub Actions" -->

### GitHub Actions Workflow

```yaml
name: Build Presentation
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
      - run: npm install
      - run: npx marp slides.md -o dist/slides.html
      - uses: actions/upload-artifact@v2
```

---

<!-- Slide 11: Marp Directives Reference -->
## Marp Directives Explained

### Global Directives (in frontmatter)

<div class="directive-highlight">
- **marp: true** - Enables Marp processing
- **paginate: true** - Show page numbers
- **theme** - Specify custom theme name
- **size: 16:9** - Set slide dimensions
</div>

### Slide-level Directives

- **<!-- _class: custom-class -->** - Apply CSS class to slide
- **<!-- _footer: "text" -->** - Add footer to slide
- **<!-- _header: "text" -->** - Add header to slide
- **![bg]()** - Background image directive

---

<!-- Slide 12: Directive Use Cases -->
## Practical Directive Applications

<!-- _class: content-slide -->
<!-- _footer: "Advanced Marp directive patterns" -->

### Image Sizing Directives

- `![bg cover](image.jpg)` - Fill entire slide
- `![bg contain](image.jpg)` - Fit within slide
- `![bg fit](image.jpg)` - Proportional scaling

### Scoped Directives

- **_paginate: skip** - Hide page number on specific slide
- **_class: title** - Apply custom class to individual slide
- **_header/footer** - Override global header/footer

---

<!-- Slide 13: Advanced Styling with Directives -->
## Combining Directives and Styling

<!-- _class: content-slide -->

### Color Directive Pattern

```markdown
<!-- _style: "background-color: #3182ce; color: white;" -->
# Custom Styled Section
```

### Layout Directives

```markdown
<!-- _class: center middle -->
# Centered Content
```

### Combining Multiple Directives

```markdown
<!-- _class: custom-layout -->
<!-- _footer: "Slide 13: Advanced Patterns" -->
<!-- _header: "Product Documentation" -->
```

---

<!-- Slide 14: Performance with Directives -->
## Performance Metrics

<!-- _footer: "Performance Analysis - Build Optimization" -->

### Build Time Analysis

$$
\begin{aligned}
\text{Parse Time} &\approx 50ms \\
\text{Render Time} &\approx 200ms \\
\text{Export Time} &\approx 800ms \\
\text{Total Build} &\approx 1050ms
\end{aligned}
$$

**Optimization Goal:** Sub-second incremental builds

---

<!-- Slide 15: Contact & Resources -->
## Contact Information & Resources

<!-- _footer: "Questions? Reach out!" -->

### Technical Lead

**Email:** 22f3001133@ds.study.iitm.ac.in

### Documentation Resources

- **Marp Official:** https://marp.app
- **GitHub Repository:** https://github.com/marp-team/marp
- **VS Code Extension:** Marp for VS Code
- **CLI Documentation:** https://github.com/marp-team/marp-cli
- **Directives Guide:** https://marpit.marp.app/directives

### Further Reading

All examples in this presentation follow Marp best practices including comprehensive directive usage.

---

## Thank You

<!-- _class: center -->
<!-- _footer: "End of Presentation" -->

Questions? Contact: **22f3001133@ds.study.iitm.ac.in**

*This presentation is version-controlled and can be exported to multiple formats.*
