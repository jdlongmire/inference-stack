---
layout: default
title: "Publications"
description: "Peer-reviewed papers, preprints and working papers on AI and architecture, each with a citable DOI"
image: /assets/brand/banners/research-technical.png
---

{% assign pubs = site.data.publications | where: "domain", "technology" | sort: "date" | reverse %}

<div class="topic-header">
  <h1>Publications</h1>
  <p>{{ pubs | size }} works on AI and architecture, each with a citable DOI</p>
</div>

Peer-reviewed papers, preprints and working papers on the engineering above the weights:
agent architecture, governance, harness design, and the structural limits of the models
themselves. Everything here is deposited on Zenodo with a permanent DOI.

This index is generated from the Zenodo API rather than maintained by hand, so it does
not drift from the record.

<ul class="pub-list">
{% for w in pubs %}
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

---

## Authors

**James (JD) Longmire** — ORCID [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)
**Micah Longmire** — ORCID [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)

Co-authored works show both names; everything else is single-authored by JD Longmire.

This page indexes the AI and architecture work only. JD also publishes on foundational
physics, philosophy of religion, and origins science; the full record is on the ORCID
profile above.

*Human-Curated, AI-Enabled (HCAE)*
