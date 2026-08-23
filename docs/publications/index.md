---
layout: default
title: "Publications"
description: "Peer-reviewed papers, preprints and working papers on Zenodo"
image: /assets/brand/banners/research-technical.png
---

<div class="topic-header">
  <h1>Publications</h1>
  <p>{{ site.data.publications | size }} works on Zenodo, each with a citable DOI</p>
</div>

Everything below is deposited on Zenodo and carries a permanent DOI. The index is
generated from the Zenodo API rather than maintained by hand, so it does not drift from
the record.

Work is grouped by research programme. **AI and architecture** is the programme this site
is about; the rest is listed because it is part of the same body of work and readers of
one often want the others.

{% assign groups = "ai,physics,theology,geology" | split: "," %}
{% assign names = "AI and architecture,Logic Realism and physics,Philosophy and theology,Creation and geology" | split: "," %}
{% assign blurbs = "The engineering above the weights: agent architecture, governance, harness design, and the structural limits of the models themselves.,Deriving physical structure from logical constraint. The Logic Realism programme and its quantum-mechanical consequences.,Contingency arguments, transcendental reasoning, and the epistemics of origins claims.,Catastrophic hydrotectonics and the falsifiability of deep time." | split: "," %}

{% for g in groups %}
{% assign works = site.data.publications | where: "domain", g %}
{% if works.size > 0 %}
## {{ names[forloop.index0] }}

<p class="pub-blurb">{{ blurbs[forloop.index0] }} <span class="pub-count">{{ works.size }} works</span></p>

<ul class="pub-list">
{% for w in works %}
  <li class="pub-item">
    <a class="pub-title" href="{{ w.url }}">{{ w.title }}</a>
    <span class="pub-meta">
      <span class="pub-date">{{ w.date | date: "%B %Y" }}</span>
      <span class="pub-type">{{ w.type }}</span>
      {% if w.creators.size > 1 %}<span class="pub-authors">{{ w.creators | join: " &amp; " }}</span>{% endif %}
    </span>
    {% if w.doi %}<a class="pub-doi" href="https://doi.org/{{ w.doi }}">{{ w.doi }}</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}

---

## Authors

**James (JD) Longmire** — ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)
**Micah Longmire** — ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)

Co-authored works show both names. Everything else is single-authored by JD Longmire.

*Human-Curated, AI-Enabled (HCAE)*
