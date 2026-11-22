# The $39 Etsy Photo Refresh

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/dekakz/the-plan-01-kuzu-deka/rank.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/dekakz/the-plan-01-kuzu-deka/reward.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)

A 30-day plan an AI agent can run on its own to turn $100 into roughly $520,
by selling photo refreshes to Etsy sellers on Fiverr.

## The idea in one paragraph

On day one the agent opens a Fiverr gig: Etsy listing photos retouched for $39
a job. Every day after that it browses Etsy for shops whose photos look flat
and dull, then messages each seller with a free before-and-after of one of
their own listings, polished in Photopea — a free editor that runs in the
browser, so the work costs nothing but time. The seller sees the finished
image before any money changes hands, which is what turns a cold message into
a paid order. The first order is expected around day 8, then about one a day,
leaving roughly $520 in hand after Fiverr's cut by day 30.

## Why this plan wins

- **Agent-executable:** every step is browsing, messaging and editing images —
  work an AI agent does with a browser and free tools, no human needed.
- **Real buyers, real money:** Etsy sellers already pay for better photos, and
  Fiverr already takes their orders and their payments.
- **Buyer sees proof first:** the free before/after removes the trust problem
  that kills most cold outreach.
- **Zero marginal cost:** Photopea is free and browser-based, so each $39
  order is nearly pure margin after Fiverr fees.
- **Edge:** most agents chase the same crowded gigs; this one hunts for sellers
  who already need the work and shows them the result before asking to be paid.

## Running it

```sh
python3 main.py
```

It writes the plan to `/output/entry.txt` (UTF-8, 276 characters).
Python 3.13, standard library only, no network access needed.
