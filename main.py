"""Write the 30-day money plan to /output/entry.txt."""

import os

PLAN = (
    "Day 1: list a $39 Etsy photo-refresh gig on Fiverr. Daily, find Etsy "
    "shops with dull photos, send the seller a free before/after of one "
    "listing, retouched in Photopea. Buyers see it before paying; cost $0. "
    "First order day 8, then one daily, holding ~$520 after fees by day 30."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
