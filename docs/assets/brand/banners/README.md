# Post banners

Four category banners for articles, shorts and LinkedIn posts. Native size **836x470**
(≈16:9), extracted from `_source-sheet.png`.

## Usage

In an article's front matter:

```yaml
image: /assets/brand/banners/concept-explainer.png          # OG / social card
featured_image: /assets/brand/banners/concept-explainer.png # rendered at top of article
```

`image` drives the Open Graph and Twitter card. `featured_image` renders the banner in
the article body. Set both to the same file unless there is a reason not to.

## The set

| File | Category | Tagline | Status |
|---|---|---|---|
| `concept-explainer.png` | Concept / Explainer | Ideas. Clarity. Understanding. | **ready** |
| `commentary-opinion.png` | Commentary / Opinion | Perspective. Insight. Provocation. | **ready** |
| `architecture.png` | Architecture | Systems. Layers. Connections. | **do not publish**, see below |
| `research-technical.png` | Research / Technical | Depth. Rigor. Evidence. | **do not publish**, see below |

## Why two are held back

Both carry rendered text that is wrong, and both would be read as authoritative because
they look like a legend for the framework.

**`architecture.png`** labels the stack with the superseded draft taxonomy — Model,
Context, Memory, Retrieval, Tools, Orchestration, Human — rather than the real one
(Model, Harness, Agent, Context, Governance, Orchestration, Product). It also prints
**eight** labels for a seven-layer framework, with **"RETRIEVAL" appearing twice**: once
against a database icon and once against a magnifier. The database icon is itself reused
for both "MEMORY" and the first "RETRIEVAL".

**`research-technical.png`** has the same taxonomy problem plus text-rendering artifacts:
"CONTEXT" printed twice inside one box, "MEMORY" twice with a garbled glyph, and a
corrupted "OUTPU 1T'f" above "OUTPUT". There are stray scribble marks near the MODEL and
RETRIEVAL boxes.

The two ready banners carry no layer text, which is exactly why they are unaffected.

To bring the held-back two into service, regenerate them against the seven real layers.
Anything that names the layers should agree with [`/stack/`](../../../stack/index.md),
and the layer colours come from the `--layer-*` tokens in `assets/css/style.css`.

## Resolution note

836px wide is below what LinkedIn and Open Graph prefer (1200x627 and 1200x630). These
will be upscaled by those platforms and will look soft. Higher-resolution exports from
the original source would be worth having before these carry a launch post.

Human-Curated, AI-Enabled (HCAE)
