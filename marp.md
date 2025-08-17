---

marp: true title: Product Documentation — Marp Deck author: Tech Writing Team paginate: true footer: "Product Docs • [24f2008495@ds.study.iitm.ac.in](mailto:24f2008495@ds.study.iitm.ac.in)"

# Use default for portability; see custom theme section below

## theme: default

# Product Documentation

### Maintainable, version‑controlled slides

**Contact:** [24f2008495@ds.study.iitm.ac.in](mailto:24f2008495@ds.study.iitm.ac.in)

---

## Why Marp for Docs?

- Keep slides in Git with the rest of your docs
- Export **HTML / PDF / PPTX / Images**
- Built‑in math, code, and theming

> Email for queries: [**24f2008495@ds.study.iitm.ac.in**](mailto:24f2008495@ds.study.iitm.ac.in)

---



# Product Overview

*This slide uses a full‑bleed background image.*

---

## Getting Started

```bash
# Local preview server
npx @marp-team/marp-cli@latest -s .

# Export for web
marp slides.md -o dist/slides.html

# Export to PDF (allow local images)
marp slides.md --pdf --allow-local-files

# Export to PPTX
marp slides.md --pptx
```

---

## Algorithmic Complexity (Math)

Inline: \$T(n) = O(n \log n)\$

Block:

$$
T(n) = T\!\left(\frac{n}{2}\right) + n \;\;\Rightarrow\;\; T(n) = O(n \log n)
$$

> We use Big‑O to describe the upper bound of time complexity.

---

## Code Snippet (TypeScript)

```ts
interface FeatureFlag {
  key: string
  enabled: boolean
}

export function isEnabled(flags: FeatureFlag[], key: string): boolean {
  return flags.some(f => f.key === key && f.enabled)
}
```

---

## Custom Styling via Directives

You can style **per‑slide** without a separate theme file:

```html
<!-- _backgroundColor: #0b1220 -->
<!-- _color: #e2e8f0 -->
```

Or embed CSS affecting all slides:

---

## Custom Theme Specification (use in projects)

> Save the CSS below as `themes/product-docs.css` and build with:
>
> ```bash
> marp --theme-set themes/product-docs.css slides.md -o dist/slides.html
> ```

```css
/* @theme product-docs */
@import "default";

:root {
  --color-background: #0f172a; /* slate-900 */
  --color-foreground: #e2e8f0; /* slate-200 */
  --color-accent: #38bdf8;     /* sky-400 */
  --font-sans: ui-sans-serif, system-ui, Segoe UI, Roboto, Helvetica, Arial;
}

section {
  background: var(--color-background);
  color: var(--color-foreground);
}
section h1, section h2, section h3 { color: var(--color-accent); }
section code { background: rgba(56,189,248,.12); padding: .1em .25em; border-radius: .25em; }
footer { color: #94a3b8; }
```

To activate the custom theme in **front matter**, set:

```yaml
---
marp: true
theme: product-docs
paginate: true
footer: "24f2008495@ds.study.iitm.ac.in"
---
```

---

## Versioning & Publishing

- Commit `slides.md` and `/themes/product-docs.css` in the repo
- Publish `dist/slides.html` via **GitHub Pages**
- Bust caches with query string: `?v=1`, `?v=2`, ...

**Support:** [24f2008495@ds.study.iitm.ac.in](mailto:24f2008495@ds.study.iitm.ac.in)

---

## Appendix

- Keyboard: **F** full screen, **P** presenter, **B** blackout
- PDF export may require `--allow-local-files` for local images
- Check Node version if build fails

**Contact:** [24f2008495@ds.study.iitm.ac.in](mailto:24f2008495@ds.study.iitm.ac.in)

