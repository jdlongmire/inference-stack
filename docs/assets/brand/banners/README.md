# Post banners

Four category banners for articles, shorts and LinkedIn posts.

**Delivery size 1200x675** (16:9). The generator caps at 836x470, so the shipped files are
Lanczos upscales with mild unsharp, measured crisper on dense text than a plain resize.
The untouched 836x470 originals are kept alongside as `*-836.png` for any future
re-render, and the 4-up sheet as `_source-sheet.png`.

A 4px inset is taken off every edge before scaling: splitting the 4-up sheet leaves a
bright 2-4px seam on whichever edges faced the interior divider, which would otherwise
render as a stray light line along the banner.

**All four are cleared for use** as of the 2026-08-23 revision. Every one passed the
checklist at the bottom of this file.

## Usage

In an article's front matter:

```yaml
image: /assets/brand/banners/concept-explainer.png          # OG / social card
featured_image: /assets/brand/banners/concept-explainer.png # rendered at top of article
```

`image` drives the Open Graph and Twitter card. `featured_image` renders the banner in
the article body. Set both to the same file unless there is a reason not to.

## The set

| File | Category | Tagline | Use for |
|---|---|---|---|
| `architecture.png` | Architecture | Systems. Layers. Connections. | Posts about the stack itself, or any named layer |
| `concept-explainer.png` | Concept / Explainer | Ideas. Clarity. Understanding. | Introducing an idea, defining a term |
| `research-technical.png` | Research / Technical | Depth. Rigor. Evidence. | Papers, evidence-led argument, measurement |
| `commentary-opinion.png` | Commentary / Opinion | Perspective. Insight. Provocation. | Position pieces, industry commentary |

`architecture.png` and `research-technical.png` both name the seven layers and both
match [`/stack/`](../../../stack/index.md). The other two carry no layer text.

`architecture.png` now carries a one-line gloss per layer, so it works as a standalone
explainer rather than only as decoration. `research-technical.png` nests Tools, Memory,
Retrieval and Systems *inside* the L2 Harness box and adds Identity & Scope under L3
Agent, which is the correct containment: those are harness components, not layers.

## What the revision fixed

The first cut of `architecture.png` labelled the stack with a superseded draft taxonomy,
printed eight labels for seven layers, and repeated "RETRIEVAL" across two different
icons. `research-technical.png` had the same taxonomy problem plus rendering artifacts:
"CONTEXT" and "MEMORY" each printed twice, and a corrupted `OUTPU 1T'f` above "OUTPUT".

Both are resolved. `research-technical.png` also improved conceptually: Memory, Retrieval,
Tools and IO/Systems are now drawn as *components* in a supporting row rather than as
competing top-level layers, which is both correct and a clearer diagram than the original.

## Known, accepted

- **`architecture.png` draws eight plates for seven layers.** Measured, not eyeballed:
  seven leader lines against eight plate rims, and the lines do not land consistently on
  a plate. The seven layers themselves are enumerated correctly and completely in the
  label column, which is what a reader actually reads, so the error is confined to the
  decorative stack. It is still wrong in a diagram whose entire point is seven, and the
  prior revision had this right with seven plates each carrying its own icon. Fix on the
  next pass by specifying "exactly seven plates, one leader line per plate, each line
  terminating on its own plate."
- **Heading tint** on `architecture.png` now runs as a deliberate cool-to-warm progression
  (saturation 0.18 at L1 rising to 0.90 at L7) rather than the three arbitrary tinted rows
  of the previous revision. Resolved.
- **Resolution** is handled by upscaling rather than at source, since the generator caps
  at 836x470. Files are 1200x675 and will still be slightly soft against native 1200px
  artwork. Good enough for LinkedIn and Open Graph, both of which accept 16:9.

## Checklist for any future banner that names the layers

The rule in `mode.md`: anything that names or depicts the layers must agree with
`/stack/`. Before replacing a file here:

- Count the layers. Seven, not six, not eight.
- Read every label. Seven distinct names, in the documented order, each appearing once:
  Model, Harness, Agent, Context, Governance, Orchestration, Product.
- Check each icon is used once and is paired consistently wherever it repeats.
- Zoom to at least 300% and read every other string, including small text inside boxes,
  for garbling and duplication.

Human-Curated, AI-Enabled (HCAE)
