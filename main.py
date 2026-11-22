#!/usr/bin/env python3
"""make.fun entry: the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (276 chars) to /output/entry.txt: an AI agent turns
$100 into about $520 in 30 days selling a $39 AI photo refresh to
Etsy sellers on Fiverr, winning orders with a free before/after sample.
"""

import os

TEXT = (
    # 276 chars: dense, no filler. Every sentence earns its place:
    # day-one action, buyer, price, venue, $0 delivery, the edge
    # (free before/after), and the day-30 expected holding.
    "Day 1: list a $39 AI photo refresh for Etsy sellers on Fiverr. "
    "Daily, find 50 listings with dull photos and send each seller a "
    "free before/after of one. Deliver in Photopea, $0 cost. Sellers "
    "see the result before paying. 1 order a day from day 8: day 30 "
    "holds $520 after fees."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
