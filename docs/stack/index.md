---
layout: default
title: "The Stack"
description: "Seven layers of engineering above the weights"
image: /assets/brand/og-banner.png
---

<div class="topic-header">
  <h1>The Inference Stack</h1>
  <p>Reasoning Outside the Model</p>
</div>

The industry talks about AI as though the model is the system. It is not. A frontier
model is a probabilistic calculator over encoded patterns: extraordinary, general,
and by itself inert. Everything that makes it useful, trustworthy, or dangerous is
built around it.

This framework names seven layers. Six of them sit outside the weights. The claim the
name makes is that those six, plus the human who answers for the result, are where the
consequential engineering now happens.

## Reading the stack

The model is drawn on top because that is where attention goes. It is not the
foundation. Read downward and each layer is less glamorous and more determinative of
whether the system works. The person at the bottom is not a compliance afterthought;
they are what the whole thing rests on.

<ul class="layer-stack">
  <li><span class="layer-num">L1</span><span><span class="layer-name">Model</span><span class="layer-desc">The weights.</span></span></li>
  <li><span class="layer-num">L2</span><span><span class="layer-name">Context</span><span class="layer-desc">What it is given.</span></span></li>
  <li><span class="layer-num">L3</span><span><span class="layer-name">Memory</span><span class="layer-desc">What persists.</span></span></li>
  <li><span class="layer-num">L4</span><span><span class="layer-name">Retrieval</span><span class="layer-desc">What grounds it.</span></span></li>
  <li><span class="layer-num">L5</span><span><span class="layer-name">Tools</span><span class="layer-desc">What it can do.</span></span></li>
  <li><span class="layer-num">L6</span><span><span class="layer-name">Orchestration</span><span class="layer-desc">How it is composed.</span></span></li>
  <li><span class="layer-num">L7</span><span><span class="layer-name">Governance</span><span class="layer-desc">Who answers for it.</span></span></li>
</ul>

---

## L1 · Model

The weights, and the inference that runs them. A model encodes patterns from a training
distribution and samples from them. That is a genuine and hard-won capability, and it is
also a bounded one: it has no access to what it was not trained on, no state between
calls, and no way to act.

Model capability is improving quickly and commoditising just as quickly. Two years of
frontier progress moves a capability from differentiator to table stakes. Anything an
organisation's advantage rests on at this layer has a short half-life.

## L2 · Context

Everything assembled and handed to the model for a given call: instructions, working
set, retrieved material, conversation state. This is the layer most teams under-engineer
and it fails in ways that look like model failure.

Context is finite. It is also contested, since every subsystem wants room in it, and the
allocation is a design decision rather than an accident. Systems that manage it explicitly
degrade gracefully. Systems that do not hit a cliff.

## L3 · Memory

State that survives the session. A model with no memory restarts from zero every time,
which caps it at the level of a very capable stranger. Memory is what makes accumulated
context possible.

The engineering is in the discipline, not the storage: what is worth writing down, what
is retrieved and when, how staleness is detected, and what happens when a memory
contradicts current state. Written-down facts that quietly go wrong are worse than no
memory at all.

## L4 · Retrieval

Grounding in sources the model does not contain: search, document corpora, databases,
live systems. Retrieval is how a claim acquires evidence rather than plausibility.

The failure mode is subtle. Retrieval that returns something plausible but wrong is more
damaging than retrieval that returns nothing, because it launders a guess into an
apparent citation. Provenance and source discipline belong at this layer, not bolted on
afterwards.

## L5 · Tools

The point at which output stops being text and starts having consequences: writing
files, calling APIs, moving money, changing infrastructure. Tools are what turn a model
into an actor.

Blast radius becomes an engineering concern here. Which operations are reversible, which
require confirmation, which are categorically refused: these are design decisions that
have to be made deliberately and enforced structurally, because a model asked nicely not
to do something will eventually do it.

## L6 · Orchestration

Control flow across models, agents, and steps: routing, decomposition, parallelism,
verification, retry. Orchestration is what turns a call into a system.

Most of what looks like reasoning in a capable AI system is orchestration. Breaking a
problem into checkable pieces, running independent checks, reconciling the results, and
knowing when to stop are structural properties of the harness rather than emergent
properties of the weights.

## L7 · Governance

The human who curates the output and answers for it. This layer is the reason the stack
is worth building carefully, and it is the one most often described as friction.

The position taken here is that curation is load-bearing. Accountability cannot be
delegated to a substrate that holds none, and a system designed as though it can is
either supervised in practice or unaccountable in fact. **Human-Curated, AI-Enabled**
names the arrangement: the machine does the work, the person owns the result.

---

## Status

This framework is under active development. The layers are stable enough to reason with
and loose enough to argue about; the articles and shorts on this site develop them.

*Human-Curated, AI-Enabled (HCAE)*
