# Post banners

Four category banners for articles, shorts and LinkedIn posts. Native size **836x470**
(≈16:9), extracted from `_source-sheet.png`.

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

`architecture.png` and `research-technical.png` both name the seven layers and both now
match [`/stack/`](../../../stack/index.md). The other two carry no layer text.

## What the revision fixed

The first cut of `architecture.png` labelled the stack with a superseded draft taxonomy,
printed eight labels for seven layers, and repeated "RETRIEVAL" across two different
icons. `research-technical.png` had the same taxonomy problem plus rendering artifacts:
"CONTEXT" and "MEMORY" each printed twice, and a corrupted `OUTPU 1T'f` above "OUTPUT".

Both are resolved. `research-technical.png` also improved conceptually: Memory, Retrieval,
Tools and IO/Systems are now drawn as *components* in a supporting row rather than as
competing top-level layers, which is both correct and a clearer diagram than the original.

## Known, accepted

- **Blueprint micro-text.** `research-technical.png` carries illegible filler glyphs in
  the title-block strip along its bottom edge, in the manner of a real drawing's
  annotation block. At display size these are 3-4px and read as texture rather than
  words. Accepted rather than fixed; worth revisiting only if the banner is ever printed
  or shown above ~1600px.
- **Resolution.** 836px wide is below what LinkedIn (1200x627) and Open Graph (1200x630)
  prefer, so these upscale on social and will look slightly soft. A re-export at 1600x900
  is still the outstanding ask.

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
