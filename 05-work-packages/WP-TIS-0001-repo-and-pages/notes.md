# WP-TIS-0001 — working notes

## Open decisions for JD

1. **The seven layer names are settled.** JD supplied them 2026-08-23: L1 Model,
   L2 Harness, L3 Agent, L4 Context, L5 Governance, L6 Orchestration, L7 Product.
   These replaced thinx-Claude's draft (Model / Context / Memory / Retrieval / Tools /
   Orchestration / Governance), which was a reading of the logo's icons and was wrong in
   substance: the real taxonomy is architectural (harness, agent, product) rather than
   infrastructural (memory, retrieval, tools). Prose on `/stack/` was rewritten, not
   renamed, because the concepts changed.

2. **Logo icons no longer map to the layer names.** The artwork carries seven icons
   (brain, document, database, search, wrench, node-tree, person). Against the real names
   only two land cleanly: brain to Model at position 1 and node-tree to Orchestration at
   position 6. Document/database/search/wrench were drawn for a memory-and-retrieval
   reading that is not the framework. The site does not currently render the icons in the
   layer list, so nothing is visibly wrong today, but the lockup and any future diagram
   will disagree with the names. Open for JD: re-cut the icon set, or accept the artwork
   as illustrative rather than a legend.

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
