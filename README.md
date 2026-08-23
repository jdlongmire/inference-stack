# longmire-repo-template

**Purpose.** A new repo should not start from an empty directory. This template carries forward
a structure, a governance convention, and a set of working rules that have already been paid for
elsewhere, so a build begins with the scaffolding in place and the known failure modes already
designed out.

It implements **VWMM** (VSOK · WBS · MBSE · **MOSA**), the structural convention declared the
org-wide standard by [`mxm-assistant-001`](https://github.com/ologos-repos/mxm-assistant-001)'s
`ADR-MXM-META-0001` (2026-08-07), with zero-padded ordinals so the sequence keeps sorting once
it passes nine.

It is deliberately **thin**. Every file here is either structure or a stub explaining what
belongs in it. Nothing is prescribed that a repo would have to argue its way out of, and any
deviation is recorded in one place (`decisions/`) rather than discovered later by surprise.

---

## The tree

```text
00-meta-model/          decisions about the product's own meta-model
01-strategic-baseline/  VSOK: why this exists and what success is
02-systems-baseline/    the apparatus: requirements, architecture, behavior, interfaces, verification
03-solutions-baseline/  the built thing
04-construct/           MxM governance surface
05-work-packages/       units of delivery, each with a declared authority boundary
decisions/              decisions about the repo's own construct
profiles/               optional overlays for a repo class
mode.md                 always-loaded doorway; any model attaches here first
```

### 00-meta-model/

Decisions about **the product's own meta-model** — the modeling conventions, taxonomy, and
structural apparatus of what the repo builds. Kept apart from decisions about the repo's own
construct (those live in `decisions/`) so a product-modeling change and a repo-governance change
are never conflated in one record. Naming: `ADR-<SLUG>-NNNN-slug.md`.

### 01-strategic-baseline/

**VSOK** — Vision, Strategy, Objectives, Key Results. The *why*.

`1.1-vision/` what this exists to achieve · `1.2-strategy/` the approach taken and what was
rejected · `1.3-objectives-krs/` measurable objectives, where increment planning lands ·
`1.4-alignment-references/` what is inherited by reference rather than restated.

### 02-systems-baseline/

The **apparatus**: what the thing must do and how its parts fit, kept distinct from the thing.

`2.1-requirements/` numbered and traceable. A design decision with no requirement behind it is
needs-capture wearing design's clothes · `2.2-architecture/` structure and rationale ·
`2.3-behavior/` how it acts, including on failure · **`2.4-interfaces/` where MOSA lives** ·
`2.5-verification/` how any claim of "done" is proven.

### 03-solutions-baseline/

The built thing. Sub-number (`3.1-`, `3.2-`, …) as the repo class requires rather than inventing
a parallel top-level scheme. See `profiles/` for a class that does exactly this.

### 04-construct/

The repo's own **MxM** governance surface: mission, mind, morals, memory, methods, means.
`mode.md` at root is always loaded; these are read on demand. Keep each short. A surface nobody
reads governs nothing, and a long one does not get read.

### 05-work-packages/

Units of coherent multi-step delivery, one directory each, `package.yaml` inside.

### decisions/

**Repo construct ADRs** — decisions about the repo's own structure, conventions, and governance
adoption. Product decisions go in `00-meta-model/` instead. Naming:
`ADR-<SLUG>-META-NNNN-slug.md`.

The template ships `ADR-SLUG-META-0001` pre-drafted here. Fill it in first: it is where a repo
records that it adopted the VWMM convention and, more importantly, **where it deviates and
why**. A deviation that is never written down becomes an inconsistency somebody has to
reverse-engineer.

---

## Setting up a new repo

```bash
gh repo create <owner>/<name> --private --template jdlongmire/longmire-repo-template
git clone https://github.com/<owner>/<name>.git && cd <name>
```

Then, in order:

1. **Pick the slug.** A short uppercase id used in every ADR and work-package number, e.g.
   `HTF`, `MXM`, `NGAF`. Replace `<SLUG>` throughout, and rename
   `decisions/ADR-SLUG-META-0001-…` to match.
2. **Fill `mode.md`.** This is the highest-leverage file in the repo because it is what an
   arriving model reads before anything else. State what the repo is, who decides what, and the
   handful of rules that always apply. Route everything else rather than inlining it.
3. **Author `ADR-<SLUG>-META-0001`** in `decisions/`. Record the convention adoption and any
   deviation. If there is no deviation, say so explicitly.
4. **Adopt a profile** if one fits (`profiles/`), and name that adoption in the meta-ADR.
5. **Write `01-strategic-baseline/1.1-vision/`** before writing any content. If the vision is
   hard to state, the repo is not ready to be built yet.
6. **Delete what does not apply.** An empty governance surface is worse than an absent one. If
   `04-construct/means.md` will never have content, remove it rather than leaving a stub that
   implies a surface exists.

---

## Working instructions

### The loop

Work moves through work packages, not through ad-hoc edits.

1. **Author the package before starting.** Copy `05-work-packages/TEMPLATE/package.yaml` into
   `WP-<SLUG>-NNNN-slug/`. Fill `scope` including its out-of-scope half, and fill
   `authority_boundary` honestly.
2. **Get it approved** if it touches anything reserved to the principal. `status: proposed` →
   `approved`.
3. **Execute inside the boundary.** Anything outside it returns to the principal first, mid-flight,
   rather than being executed and reported afterwards.
4. **Verify as written.** The `verification` field is the test. If it cannot fail, it is not a
   verification, it is an assertion.
5. **Close with a disposition.** `done`, or `cancelled` with the reason recorded.

### Rules that apply regardless of package

- **Do not fabricate.** Verify before asserting. Unsure of a path, name, figure: check it.
- **Surface a flipped result before writing it down.** When a check reverses the expected
  direction of a claim, that is a decision point, not a conclusion to execute unilaterally. The
  check itself is never optional.
- **Record access failures.** A paywall or a 403 is a fact about the evidence base. Log the URL,
  status and date *in the document where the claim lives*. Then escalate before settling for a
  summary: open-access mirror, **the direct PDF path rather than the HTML landing page**,
  supplementary files, preprint, the citing literature, and only then a secondary.
- **Record refuted variants.** A superseded attempt stays in the repo, labelled with the reason
  it died. A history showing no casualties is not a history.
- **Reach before refusing.** Enumerate the tools actually available and try, before concluding
  something cannot be done.
- **Commit code with the doc it grounds**, in the same commit. Never a claim first with the code
  to follow, never code with no claim pointing at it.

### Naming

| Thing | Form |
|---|---|
| Meta ADR (repo construct) | `decisions/ADR-<SLUG>-META-NNNN-slug.md` |
| Product ADR | `00-meta-model/ADR-<SLUG>-NNNN-slug.md` |
| Work package | `05-work-packages/WP-<SLUG>-NNNN-slug/package.yaml` |
| Requirement | `REQ-<SLUG>-NNNN` |

Ordinals zero-padded everywhere.

---

## Three design decisions worth understanding

These are the parts of the template that came from real failures rather than from a sense of
tidiness, and they are the parts worth not stripping out.

**`2.4-interfaces/` and MOSA.** Modules declare what they **provide** and what they **consume**.
The payoff is that the dependency graph becomes explicit and machine-checkable for cycles, and
replacing a module shows exactly what breaks. Without it, couplings accumulate silently and are
only visible by tracing them by hand, which nobody does until something has already gone wrong.

**`authority_boundary` on every work package.** This is what converts a principal's reserved
decisions from *remembered* into *structural*. A package that could touch a commitment, an
external publication, or a verdict names that edge before work starts. It is also the mechanism
that makes agent delegation safe: an agent can be handed a package and the boundary travels with
it.

**`commitment: committed | stretch`** (optional, see the work-package README). A *committed*
package is bounded and will land. A *stretch* package is an investigation, and the commitment is
to run the attempt **to a recorded resolution, not to a positive result** — so a recorded
refutation closes it *successfully*. Without that distinction, negative results get logged as
costs against the work rather than as the completed work they are, which quietly biases a repo
toward only recording things that went well.

---

## Profiles

An overlay for a repo class, adding structure on top of the base convention without changing it.
Adopt one by saying so in the meta-ADR.

- [`profiles/research-programme.md`](profiles/research-programme.md) — Lakatosian research
  programme. Adds the falsifiability ladder as `3.x` sub-numbering, a four-condition discriminator
  standard, the Tier 2 versus Tier 3 distinction that keeps interpretive work from being judged
  by prediction rules, and twelve working rules each traceable to a specific failure.

New profiles are welcome. A profile should be additive, should say which repo class it serves,
and should explain *why* each addition exists rather than only what it is.

---

*Human-Curated, AI-Enabled (HCAE)*
