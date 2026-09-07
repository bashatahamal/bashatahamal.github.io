---
layout: post
index: W.14
title: "What counts as a clean lead before you even score it"
ogImage: images/og/writing/what-counts-as-a-clean-lead.png
date: 2026-02-01
tags: [LLM, Data Quality, Judgment]
excerpt: "Before Leadflow's multi-client scoring problem, there was an earlier one at Berning: raw prospect data is messy in ways that break a scoring system before it ever gets a chance to score anything."
---

Multi-client scoring only became a problem worth thinking hard about once the pipeline had leads that were clean enough to score in the first place. Before that, at the start of building Leadflow at Berning, the actual bottleneck sat earlier in the pipeline: getting raw prospect data into something structured enough for any scoring logic, whoever's criteria it was applying, to trust.

## Confident and wrong looks identical to confident and right

Raw data does not announce that it is unreliable. A record can look complete and still be quietly wrong in ways that are easy to miss: a mismatched detail, a technically accurate field that means something different than it appears to. None of that is exotic. It is the ordinary state of anything pulled from a raw source, and a system fed that directly will produce confident output either way, because nothing about scoring alone tells it the input was bad.

```mermaid
flowchart LR
  A[Raw prospect data] --> B{Actually reliable?}
  B -- no --> C[Confident, wrong score]
  B -- yes --> D[Trustworthy score]
```

*Both branches produce a score that looks the same on the screen. Only one of them means anything.*

## Trust is earned before judgment is applied

Whatever a client's specific criteria were, they all shared one hidden assumption: that the facts about a prospect being judged were actually correct. Get that assumption wrong and no amount of thoughtful scoring logic downstream fixes it, it just applies more careful weights to the same bad input, which is worse than doing nothing, because it looks considered.

## Why the boring part came first

If I had started with scoring and treated everything before it as an afterthought, every demo would have looked fine on the examples I happened to pick, and quietly failed on the messy reality every real dataset actually is. Building the unglamorous part first is what let me trust the interesting part once it existed.
