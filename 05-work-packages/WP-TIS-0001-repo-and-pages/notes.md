# WP-TIS-0001 — working notes

## Open decisions for JD

1. **The seven layer names are a draft.** L1 Model, L2 Context, L3 Memory, L4 Retrieval,
   L5 Tools, L6 Orchestration, L7 Governance — derived from the seven icons in the logo
   (brain, document, database, search, wrench, node-tree, person). The logo commits to
   seven distinct layers; it does not name them. These names are thinx-Claude's reading
   and need JD's sign-off before they are treated as settled, because everything
   downstream (articles, shorts, the framework page) will reference them.

2. **Layer order.** The logo draws the model on top and the person at the bottom. The
   site reads that as deliberate: the model is where attention goes, the human is what
   the stack rests on. If the intent was the reverse, the diagram and the prose both
   invert.

3. **aithinkr.net disposition.** Left live and untouched. It now duplicates every article
   this site carries. Options when JD wants to close that: 301 the whole domain here,
   leave it as a dated archive with a banner, or retire it. Not actioned.

## Judgment calls made

- **Refactor, not rebuild.** The Jekyll site was copied wholesale from AI-Research and
  rebranded in place rather than reimplemented. It is a mature site (36 articles, search,
  Giscus comments, MathJax, SEO/JSON-LD, light/dark themes) and reproducing that from
  scratch would have lost working behaviour for no gain.
- **Palette sampled from the lockup, not invented.** The seven `--layer-*` tokens in
  `docs/assets/css/style.css` are median-sampled from the brand artwork. Site neutrals
  moved from the inherited monochrome to the brand navy family; amber (`#e0a53c`, layer 5)
  is the accent, which also matches the `ACCENT` already shipped in the video factory.
- **Giscus repointed with real IDs.** Discussions were enabled on the new repo and the
  actual `data-repo-id` / `data-category-id` fetched from the GraphQL API rather than
  left pointing at AI-Research or stubbed.
- **In-site cross-links made relative.** Article bodies linking to
  `https://aithinkr.net/articles/...` now use `/articles/...` so they resolve here
  instead of bouncing readers to the archive.

## Not done, and why

- **CI workflow** (`.github/workflows/pages.yml`) — drafted and blocked by the harness
  hard-stop on CI surfaces. Needs a Chief-Architect override. It would give a build gate
  on PRs plus a broken-internal-link check, which matters more than usual here because
  36 migrated articles just had their links rewritten.
- **Branch protection** — deliberately sequenced after CI, since a required-check rule
  needs a check to require.
- **DNS record** — `inference` CNAME to `jdlongmire.github.io`, **DNS-only / grey cloud**.
  Proxying it blocks the ACME challenge and Pages never issues a certificate.

Human-Curated, AI-Enabled (HCAE)
