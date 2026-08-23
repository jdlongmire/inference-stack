---
layout: default
title: "Shorts"
description: "Short-form video from The Inference Stack"
image: /assets/brand/banners/concept-explainer.png
---

<div class="topic-header">
  <h1>Shorts</h1>
  <p>The argument, in ninety seconds to three minutes</p>
</div>

Short-form vertical video developed from the articles on this site. Each takes a single
claim from the stack and makes it standalone. The written version always lives here too.

{% assign shorts = site.data.shorts | where: "brand", "inference-stack" | sort: "date" | reverse %}
{% for v in shorts %}
<div class="short-feature">
  <video class="short-video" controls preload="none"
         poster="{{ v.poster | relative_url }}"
         width="1080" height="1920">
    <source src="{{ v.video | relative_url }}" type="video/mp4">
    Your browser does not support embedded video.
    <a href="{{ v.video | relative_url }}">Download the file</a> instead.
  </video>
  <div class="short-feature-body">
    <h2 id="{{ v.slug }}">{{ v.title }}</h2>
    <p class="short-feature-meta">{{ v.duration }} &middot; {{ v.layer }} &middot; {{ v.date | date: "%B %-d, %Y" }}</p>
    <p>{{ v.summary }}</p>
    <p class="short-feature-tagline">{{ v.tagline }}</p>
  </div>
</div>
{% endfor %}

## How these are made

Scripts are drafted from the articles, narrated in a cloned voice, and rendered as 9:16
vertical video. The pipeline is deliberately boring: deterministic render, a mobile safe
area that survives phone cropping, and a build-wide noise floor so the audio does not
shift between sections.

*Human-Curated, AI-Enabled (HCAE)*
