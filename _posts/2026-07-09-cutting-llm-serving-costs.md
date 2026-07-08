---
layout: post
title: "How we cut our LLM serving costs by around 80%"
date: 2026-07-09
excerpt: "The levers that actually moved the bill when we took LLM features from demo to production: right-sizing the model, cutting wasted tokens, caching, and measuring cost per feature."
---

A working LLM demo costs almost nothing. You call a big model a few times, it looks like magic, everyone is happy. The bill only becomes real when that demo turns into a feature that thousands of people use every day.

That is where I spent a lot of my time at eFishery, building and running LLM applications like Mas Ahya, a conversational assistant for fish and shrimp farmers, and a set of OCR pipelines for document processing. Over time we brought the cost of running those services down by around 80 percent, without making them worse. Here is what actually moved the number.

## Right-size the model, and cascade

The most expensive habit is using your biggest, smartest model for every single call. Most requests do not need it. A lot of the work in an LLM app is not hard reasoning, it is classification, extraction, routing, short rewrites, and formatting. Those run fine on a smaller and much cheaper model.

What worked for us was a cascade: a small model handles the request first, and only escalates to a larger one when the task genuinely needs it. You get most of the quality at a fraction of the cost, because the expensive model only runs when it earns its keep.

## Stop paying for tokens you do not need

Every token in and out is money, and it is easy to waste them without noticing. The usual culprits: stuffing the whole conversation history into every call, retrieving ten documents when three would do, repeating a long system prompt on every request, and letting the model ramble in free text when you only needed a structured answer.

Tightening prompts, trimming retrieved context to what is relevant, and asking for structured output all cut tokens directly. This is unglamorous work, but it compounds across millions of calls.

## Cache like you mean it

In real usage, people ask the same things. Farmers asked Mas Ahya variations of the same seasonal questions. If you are recomputing an answer you already produced yesterday, you are burning money.

Exact-match caching on identical inputs is the easy win. Semantic caching, where near-duplicate questions reuse a previous answer, goes further but needs care so you do not serve a stale or slightly-wrong response. Caching intermediate steps like embeddings, retrieval results, and parsed documents helped as much as caching final answers.

## Batch and go async where latency allows

Not every LLM task is a live chat. OCR over a 500 page document, scoring a backlog, generating reports: none of that needs to finish in the half second a user is waiting. Moving that work into background queues let us batch requests, smooth out spikes, and use cheaper throughput instead of paying for low latency we did not need.

Knowing which features are latency-sensitive and which are not is half the battle.

## You cannot cut what you cannot see

For a long time our LLM cost was one number on a monthly invoice, which tells you nothing about where to act. The turning point was breaking cost down per feature and per request: which endpoint, which model, how many tokens, how often.

Once you can see that a single rarely-used feature is eating a third of the bill, the decision makes itself. Tracing token usage per call is not overhead, it is the map you need to spend the rest of your effort well.

## Cheaper must never mean worse

The trap in all of this is shipping a cost cut that quietly degrades quality. Every change we made was checked against an evaluation set before it went out. If a smaller model or a trimmed prompt dropped answer quality below the bar, it did not ship, no matter how much it saved.

Building that evaluation habit early is what let us move fast on cost without gambling with the user experience. It also turned "is this good enough?" from an argument into a measurement.

## The model is only half the system

None of these are clever tricks. They are the boring, operational side of running AI in production, and that is exactly the point. The model is only half the system. The other half is the engineering around it: what you route where, what you cache, what you measure, and what you refuse to ship.

Treating cost as a design constraint from the start, instead of a surprise at the end of the month, is what makes an LLM feature something a company can actually afford to keep running.
