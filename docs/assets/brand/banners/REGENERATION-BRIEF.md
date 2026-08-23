# Banner regeneration brief

Paste-ready prompts for the two held-back banners, plus a re-export ask that applies to
all four. Each section states what is wrong and why it matters before the prompt, so the
prompt can be edited without losing the reasoning behind it.

---

> **Status: both banners regenerated and cleared, 2026-08-23.** `architecture.png` and
> `research-technical.png` both passed the checklist and are in service. The prompts below
> are kept as the working spec for any future banner that names the layers, not as
> outstanding work. The one remaining ask is the 1600x900 re-export in section 3.
>
> A separate 3:2 reference poster, `assets/brand/stack-reference.png`, is published on
> `/stack/` and is the authoritative labelled diagram.

## Shared brand facts

Any prompt should carry these. They are the canonical values, taken from
`assets/css/style.css` (`--layer-*`) and the published framework at `/stack/`.

**The seven layers, in order, top to bottom:**

| # | Layer | Colour | One-line meaning |
|---|---|---|---|
| L1 | Model | `#1c2b3a` (near-black navy plate) | The weights |
| L2 | Harness | `#2f5f9c` (blue) | What the model runs inside |
| L3 | Agent | `#5b9bc4` (light blue) | Who is acting, under what authority |
| L4 | Context | `#569b93` (teal) | What it is given |
| L5 | Governance | `#e0a53c` (amber) | What it may not do |
| L6 | Orchestration | `#d9682b` (orange) | How it is composed |
| L7 | Product | `#46586a` (slate) | What is actually delivered |

**Background:** `#00040b` to `#0b1420`, near-black navy.
**Accent for category labels:** teal-cyan, as in the existing set.
**Wordmark lockup:** top-left, unchanged, with the "REASONING / OUTSIDE / THE MODEL"
tagline stacked to its right in blue small caps.
**Category label:** bottom-left, teal, all caps, with a thin vertical rule to its left
and a plain-sentence tagline beneath.

---

## 1. `architecture.png` — Architecture

### What is wrong

Three separate defects, in order of severity:

1. **Wrong taxonomy.** The labels read Model, Context, Memory, Retrieval, Retrieval,
   Tools, Orchestration, Human. That was a draft reading and is not the framework. The
   real seven are in the table above. This matters more than a normal branding slip
   because the banner is laid out as a labelled diagram, so a reader takes it as the
   authoritative legend for the stack.
2. **Eight labels for a seven-layer framework.** Count them: the rendered image has eight
   rows. The framework has seven layers. Any labelled version of the stack must have
   exactly seven.
3. **"RETRIEVAL" printed twice**, on two consecutive rows, against two different icons
   (a database and a magnifier). The database icon is also reused for the row labelled
   "MEMORY" immediately above. So one label is duplicated and one icon is duplicated.

The composition itself is good and should be preserved. Only the labelled column and its
icons need to change.

### Prompt

```
Wide 16:9 banner, 1600x900, dark near-black navy background (#00040b to #0b1420) with a
subtle circuit-trace texture and soft cyan and orange light-streak curves in the lower
left.

Top left: the wordmark "THE INFERENCE STACK" in white, with a small isometric layered
stack logo mark to its left, and the tagline "REASONING / OUTSIDE / THE MODEL" stacked in
blue small caps to its right, separated by a thin vertical rule.

Centre right: an exploded isometric stack of EXACTLY SEVEN rounded rhombus plates, evenly
spaced, viewed from a low angle. The top plate is a dark navy panel (#1c2b3a) containing
a white node-and-edge network graph. The six plates below it, in order downward:
#2f5f9c, #5b9bc4, #569b93, #e0a53c, #d9682b, #46586a.

From each of the seven plates, a thin coloured leader line runs right to a small round
node, then to a line-art icon and an all-caps label. Match each line's colour to its
plate. The seven rows, top to bottom, with NO repeats:

1. brain icon - MODEL
2. bracket-frame enclosing a chip icon - HARNESS
3. person-with-badge icon - AGENT
4. document icon - CONTEXT
5. shield-with-check icon - GOVERNANCE
6. node-tree icon - ORCHESTRATION
7. package-box icon - PRODUCT

Each of the seven labels appears exactly once. Each of the seven icons is distinct from
the other six. Seven plates, seven leader lines, seven icons, seven labels.

Bottom left: a thin vertical teal rule, then "ARCHITECTURE" in teal all caps, and beneath
it "Systems. Layers. Connections." in white sentence case.

Clean, technical, restrained. No extra text anywhere in the image.
```

---

## 2. `research-technical.png` — Research / Technical

### What is wrong

1. **Wrong taxonomy**, same as above: the boxes read Model, Context, Memory, Retrieval,
   Tools (MCP), Orchestration. Harness, Agent, Governance and Product are absent.
2. **Text-rendering artifacts.** "CONTEXT" is printed twice inside a single box, once at
   the top and once at the bottom. "MEMORY" is likewise printed twice, one instance
   followed by a garbled glyph. Above the output box sits a corrupted string reading
   roughly `OUTPU 1T'f`. There are stray scribble marks near the MODEL and RETRIEVAL
   boxes that read as artifacts rather than deliberate annotation.
3. Because the banner is drawn as a blueprint schematic, the duplicated and garbled text
   reads as a badly proofed engineering drawing, which undercuts the "Depth. Rigor.
   Evidence." tagline directly beneath it.

The blueprint treatment is the strongest thing about this banner and should be kept. The
diagram content needs rebuilding on the real layers.

### Prompt

```
Wide 16:9 banner, 1600x900, dark navy blueprint background (#00040b to #0b1420) with a
faint blue grid and corner registration marks, in the style of a technical drawing.

Top left: the wordmark "THE INFERENCE STACK" in white, with a small isometric layered
stack logo mark to its left, and the tagline "REASONING / OUTSIDE / THE MODEL" stacked in
blue small caps to its right, separated by a thin vertical rule.

Centre: a clean blueprint-style flow diagram in thin cyan-blue line art, rounded
rectangular boxes, each box containing one line-art icon above one all-caps label.
Connect the boxes with thin arrows, solid for the main path and dashed for supporting
inputs. Exactly these boxes and no others:

- MODEL (node-and-edge network icon), top centre
- HARNESS (bracket-frame enclosing a chip icon), directly beneath MODEL
- AGENT (person-with-badge icon), left of HARNESS
- CONTEXT (document icon), right of HARNESS
- GOVERNANCE (shield-with-check icon), left, below AGENT
- ORCHESTRATION (node-tree icon), centre, below HARNESS
- PRODUCT (package-box icon), right, below CONTEXT, as the terminal box

Main path: MODEL down to HARNESS, HARNESS down to ORCHESTRATION, ORCHESTRATION right to
PRODUCT. Dashed supporting inputs: AGENT into HARNESS, CONTEXT into HARNESS, GOVERNANCE
into ORCHESTRATION.

Each label appears exactly ONCE in the whole image. No label is repeated inside or
outside its own box. No decorative or filler text, no stray annotation marks, no partial
or garbled words anywhere.

Bottom left: a thin vertical teal rule, then "RESEARCH / TECHNICAL" in teal all caps, and
beneath it "Depth. Rigor. Evidence." in white sentence case.

Precise, clean, legible. Every piece of text in the image must be a real word, spelled
correctly, rendered once.
```

---

## 3. Re-export ask — applies to all four banners

The two banners that are fine in content, `concept-explainer.png` and
`commentary-opinion.png`, do not need regenerating. They do need re-exporting.

Native size is **836x470**. LinkedIn wants 1200x627 and Open Graph wants 1200x630, so at
current size every one of these upscales and goes soft on social. Ask for **1600x900**
and downscale locally, which keeps one master per banner and leaves room for a 1200-wide
crop without loss.

If the originals still exist in the generating tool, a straight re-render at higher
resolution is preferable to upscaling what is here.

---

## Checking a regenerated banner before it ships

The rule in `mode.md`: anything that names or depicts the layers must agree with
`/stack/`. Concretely, before replacing a file here:

- Count the layers. Seven, not six, not eight.
- Read every label aloud. Seven distinct names, matching the table at the top of this
  file, each appearing once.
- Check each icon is used once.
- Read every other string in the image for garbling and duplication, including small
  text inside boxes.
- Confirm the plate colours run in the documented order.

## Palette note: the graphic and the CSS deliberately differ

The reference graphic runs a continuous blue-to-orange gradient. The `--layer-*` CSS
tokens do not, and should not be changed to match.

The reason is measurable. As seven stacked 4px accent bars, the graphic's gradient has a
smallest adjacent CIELAB deltaE of **5.8** (L1 Model against L2 Harness, both near-identical
blues). The current tokens have a smallest adjacent deltaE of **27.5**. Below roughly 10,
adjacent bars are not reliably distinguishable.

The gradient works in the graphic because the plates are separated in space and each one
carries its own label. It would not work as a legend of bare colour bars. The two palettes
serve different jobs and are allowed to disagree; what must never disagree is the layer
names, their order, and their meanings.

Human-Curated, AI-Enabled (HCAE)
