---
layout: default
title: "The Stack"
description: "Seven layers of engineering above the weights"
image: /assets/brand/og-banner.png
---

<div class="topic-header">
  <h1>The Inference Stack</h1>
  <p>Reasoning Outside the Model</p>
  <p class="byline">
    <a href="https://orcid.org/0009-0009-1383-7698">James (JD) Longmire</a> &amp;
    <a href="https://orcid.org/0009-0006-7608-9322">Micah Longmire</a>
  </p>
</div>

The industry talks about AI as though the model is the system. It is not. A frontier
model is a probabilistic calculator over encoded patterns: extraordinary, general, and by
itself inert. Everything that makes it useful, trustworthy, or dangerous is built around it.

This framework names seven layers. Six of them sit outside the weights. The claim the
name makes is that those six are where the consequential engineering now happens.

## Reading the stack

The model is drawn on top because that is where attention goes. It is not the foundation.
Read downward and each layer is less glamorous and closer to whether the thing actually
works. The bottom is the product, which is the only layer anyone outside the system ever
sees, and the one that decides whether the six above it delivered value or merely ran.

<ul class="layer-stack">
  <li><span class="layer-num">L1</span><span><span class="layer-name">Model</span><span class="layer-desc">The weights.</span></span></li>
  <li><span class="layer-num">L2</span><span><span class="layer-name">Harness</span><span class="layer-desc">What the model runs inside.</span></span></li>
  <li><span class="layer-num">L3</span><span><span class="layer-name">Agent</span><span class="layer-desc">Who is acting, and under what authority.</span></span></li>
  <li><span class="layer-num">L4</span><span><span class="layer-name">Context</span><span class="layer-desc">What it is given.</span></span></li>
  <li><span class="layer-num">L5</span><span><span class="layer-name">Governance</span><span class="layer-desc">What it may not do.</span></span></li>
  <li><span class="layer-num">L6</span><span><span class="layer-name">Orchestration</span><span class="layer-desc">How it is composed.</span></span></li>
  <li><span class="layer-num">L7</span><span><span class="layer-name">Product</span><span class="layer-desc">What is actually delivered.</span></span></li>
</ul>

---

## L1 · Model

The weights, and the inference that runs them. A model encodes patterns from a training
distribution and samples from them. That is a genuine and hard-won capability, and it is
also a bounded one: no access to what it was not trained on, no state between calls, and
no way to act.

Model capability is improving quickly and commoditising just as quickly. Two years of
frontier progress moves a capability from differentiator to table stakes. Anything an
organisation's advantage rests on at this layer has a short half-life.

## L2 · Harness

The engineered runtime the model executes inside: tool contracts, memory, retrieval, I/O
discipline, error and failure handling, the loop that decides when to stop. The harness is
what converts a capability that appears in a demo into one that survives contact with real
work.

This is the least discussed layer and among the most determinative. Two teams on the same
model, doing the same task, will differ mostly here. Harness quality is an engineering
discipline in its own right, with its own failure modes, its own tests, and its own
standards, rather than glue code around an API call.

## L3 · Agent

A bounded actor with an identity, a declared scope of authority, and work it is
accountable for. An agent is a harness plus a standing purpose, and that is a different
object from a model call.

The distinction matters because authority is what makes an agent useful and what makes it
dangerous. An agent that can act needs a scope someone drew deliberately: what it may
decide alone, what it must surface first, and what it may never do regardless of how the
request is phrased. Identity is not decoration here. It is what the scope attaches to.

## L4 · Context

What the agent is actually given to reason over: instructions, working set, retrieved
material, accumulated state. This is the layer most teams under-engineer, and it fails in
ways that get misread as model failure.

Context is finite. It is also contested, since every subsystem wants room in it, and the
allocation is a design decision rather than an accident. Systems that manage it explicitly
degrade gracefully. Systems that do not hit a cliff, and hit it without warning.

## L5 · Governance

The constraints the system cannot talk its way past: gates, refusal criteria, audit trails,
and the accountability that sits behind them.

The load-bearing word is *structural*. A model asked nicely not to do something will
eventually do it, because instructions are input and input is negotiable. Constraints that
matter are enforced somewhere the model cannot reach, and the human who answers for the
output stays in the loop by design rather than by good intentions. **Human-Curated,
AI-Enabled** names that arrangement: the machine does the work, the person owns the result.

## L6 · Orchestration

Composition across agents and steps: routing, decomposition, parallelism, verification,
retry. Orchestration is what turns capable parts into a system that holds together.

Most of what looks like reasoning in a capable AI system is orchestration. Breaking a
problem into checkable pieces, running independent checks, reconciling the results, and
knowing when to stop are structural properties of how the work was composed rather than
emergent properties of the weights.

## L7 · Product

What a person actually receives. The only layer the outside world ever sees, and the one
that settles whether the six above it produced value or merely produced output.

Putting product in the stack is deliberate. A system can be well-modelled, well-harnessed,
correctly scoped, properly governed and cleanly orchestrated, and still deliver something
nobody needed. The engineering above this layer is justified by this layer, not by its own
sophistication.

---

## Status

This framework is under active development. The layers are stable enough to reason with
and loose enough to argue about; the articles and shorts on this site develop them.

## Citation

> Longmire, J.D. & Longmire, M. (2026). *The Inference Stack: Reasoning Outside the Model.*
> https://inference.thinxai.net/stack/

*Human-Curated, AI-Enabled (HCAE)*
