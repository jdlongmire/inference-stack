---
layout: default
title: "The Inference Stack"
image: /assets/brand/og-banner.png
---

<div class="stack-hero">
  <img src="{{ '/assets/brand/lockup-dark-640.png' | relative_url }}" alt="The Inference Stack – Reasoning Outside the Model" />
  <p class="hero-thesis">
    A frontier model is a probabilistic calculator over encoded patterns. It is not
    the system. <strong>The consequential engineering is no longer inside the weights</strong>.
    It is in the six layers that carry the model, and the one that answers for it.
  </p>
</div>

## The seven layers

<ul class="layer-stack">
  <li><span class="layer-num">L1</span><span><span class="layer-name">Model</span><span class="layer-desc">The weights. A probabilistic calculator over encoded patterns, bounded by its training distribution. Increasingly commoditised, and increasingly not where the differentiation lives.</span></span></li>
  <li><span class="layer-num">L2</span><span><span class="layer-name">Context</span><span class="layer-desc">What the model is given to reason over: instructions, working set, assembled state. Finite, contested, and governed. This is the layer where the token cliff bites.</span></span></li>
  <li><span class="layer-num">L3</span><span><span class="layer-name">Memory</span><span class="layer-desc">State that survives the session. What gets written down, what gets recalled, what decays. The difference between a tool and a colleague.</span></span></li>
  <li><span class="layer-num">L4</span><span><span class="layer-name">Retrieval</span><span class="layer-desc">Grounding in sources the model does not contain. Search, corpora, provenance: where claims acquire evidence rather than plausibility.</span></span></li>
  <li><span class="layer-num">L5</span><span><span class="layer-name">Tools</span><span class="layer-desc">Action on the world. The point at which output stops being text and starts having consequences, and the point at which blast radius becomes an engineering concern.</span></span></li>
  <li><span class="layer-num">L6</span><span><span class="layer-name">Orchestration</span><span class="layer-desc">Control flow across models, agents, and steps. Routing, decomposition, verification, retry. The layer that turns a call into a system.</span></span></li>
  <li><span class="layer-num">L7</span><span><span class="layer-name">Governance</span><span class="layer-desc">The human who curates and answers for the result. Not a compliance wrapper but the load-bearing foundation: Human-Curated, AI-Enabled.</span></span></li>
</ul>

[Read the framework in full]({{ '/stack/' | relative_url }})

---

## Latest articles

<div class="paper-grid">
{% assign articles = site.pages | where_exp: "page", "page.path contains 'articles/'" | where_exp: "page", "page.layout == 'article'" | sort: "date" | reverse %}
{% for article in articles limit: 6 %}
  <div class="paper-card">
    <h3><a href="{{ article.url | relative_url }}">{{ article.title }}</a></h3>
    <p>{{ article.description | default: "An article from The Inference Stack." }}</p>
    <div class="meta">{{ article.date | date: "%B %d, %Y" }}</div>
    <a href="{{ article.url | relative_url }}" class="card-link">Read Article</a>
  </div>
{% endfor %}
</div>

[All articles]({{ '/articles/' | relative_url }}) &middot; [Shorts]({{ '/shorts/' | relative_url }})

---

## Authors

**James (JD) Longmire**, Northrop Grumman Fellow, Chief Architect for Digital Ecosystems.

- ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)
- Email: jdlongmire@outlook.com
- GitHub: [jdlongmire](https://github.com/jdlongmire)
- Substack: [AI Research & Philosophy](https://airesearchandphilosophy.substack.com/)

**Micah Longmire**, CEO and CTO of Ologos Corp; senior systems and AI architect.

- ORCID: [0009-0006-7608-9322](https://orcid.org/0009-0006-7608-9322)
- GitHub: [bobbyhiddn](https://github.com/bobbyhiddn)

**AI assistance disclosure.** This work was developed with assistance from AI language models. All substantive claims, arguments, and errors remain the authors' responsibility. **Human-Curated, AI-Enabled (HCAE)**.
