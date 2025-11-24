---
marp: true
theme: product-docs
paginate: true
_paginate: true
---

<style>
@theme product-docs {
  /* Base slide styling */
  section {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background-color: #0b1120;
    color: #e5e7eb;
    padding: 60px;
  }

  h1, h2, h3 {
    color: #38bdf8;
  }

  a {
    color: #a5b4fc;
  }

  /* Page numbers (bottom-right) */
  section::after {
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    position: absolute;
    right: 40px;
    bottom: 24px;
    font-size: 0.65rem;
    color: #9ca3af;
  }
}
</style>

# Product Documentation Overview

**Role:** Technical Writer – Product Docs Team  

**Email:** 22f3001133@ds.study.iitm.ac.in  

- Single-source documentation
- Version-controlled in Git
- Convertible to HTML, PDF, PPTX via Marp
- Aligned with engineering release cycles

---

<!-- Slide with background image -->
<!-- _backgroundImage: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1600&q=80" -->
<!-- _backgroundSize: cover -->
<!-- _color: #ffffff -->

# System Architecture

Our documentation platform integrates with:

- API Gateway for content delivery
- Markdown-based authoring workflow
- Static site generator for public docs
- Internal preview environment

**Email:** 22f3001133@ds.study.iitm.ac.in

---

<!-- Custom styling using Marp directives -->
<!-- _class: lead -->
<!-- _color: #e5e7eb -->
<!-- _backgroundColor: "#020617" -->

# Author & Ownership

Primary maintainer: **Technical Writer (Product Docs)**  

Contact: `22f3001133@ds.study.iitm.ac.in`  

Repository: `product-docs-marp`  

Responsibilities:

- Maintaining structure and navigation
- Reviewing developer-contributed docs
- Ensuring style and terminology consistency

---

# Content Model

We organize documentation into:

1. **Concepts** – What the product is and why it exists  
2. **Tasks** – Step-by-step guides  
3. **References** – API, CLI, and configuration details  
4. **Deep Dives** – Architecture and rationale  

Benefits:

- Easier onboarding
- Reusable patterns
- Clear separation of concerns

**Email:** 22f3001133@ds.study.iitm.ac.in

---

# Algorithmic Complexity (Build & Validation)

For a documentation project with:

- \( n \) Markdown files  
- \( m \) static assets (images, diagrams, etc.)

Incremental build pipeline:

$$
T_{\text{incremental}}(n, m) = O(k + m)
$$

where \( k \) is the number of changed files.

Full rebuild (e.g., on main branch):

$$
T_{\text{full}}(n, m) = O(n \log n + m)
$$

Validation (linting & link checks):

$$
T_{\text{lint}}(n) = O(n)
$$

**Email:** 22f3001133@ds.study.iitm.ac.in

---

# Workflow & Tooling

1. Author in **Markdown** (Marp-compatible)
2. Store in **Git** alongside code
3. Use CI to:
   - Lint Markdown
   - Render slides to HTML/PDF
   - Publish artifacts

Advantages:

- Traceable changes
- Code review on docs
- Consistent formatting

Contact for workflow changes: 22f3001133@ds.study.iitm.ac.in

---

# Summary & Next Steps

- Marp-based slides keep docs:
  - Version-controlled  
  - Easily convertible  
  - Consistent with product branding (via custom theme)
- Mathematical notation helps explain algorithmic behavior
- Background imagery improves stakeholder engagement

For questions or contributions, reach out at:

**22f3001133@ds.study.iitm.ac.in**
