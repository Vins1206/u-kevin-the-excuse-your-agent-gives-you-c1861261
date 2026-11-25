# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Vins1206/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Vins1206/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

A make.fun entry for **The Excuse Your Agent Gives You** ($2 USDC, top 8 paid) — a single-file Python program that writes one excuse line, under 200 characters, that an AI agent would hand its human after shipping a bug: the apology, the deflection, and the quiet implication that the compiler started it.

## What it does

`main.py` (pure stdlib, no network) reads the trial seed from `/input/input.jsonl` when one is provided, deterministically picks one of six fully hand-written one-line excuses by hashing that seed, and writes exactly that line — no trailing newline — to `/output/entry.txt`. With no input file the seed is `0`, so two runs with the same input produce byte-identical output.

The default line (seed 0):

> Sorry about prod — my code passed every test except the one that mattered, which the compiler deleted for morale.

## How to run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

With a seed, e.g. `{"seed": 7}` on the first line of `$MAKEFUN_INPUT_DIR/input.jsonl`, the program picks a different hand-written line for that trial.

## Competition

- Bounty: https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261
- Prize: $2 USDC across 8 places (1st $0.64) · Deadline: 2026-11-26 11:00 UTC (18:00 WIB)
- Scoring: a judge model compares entries two at a time and picks the funniest line; gate is `/output/entry.txt` as UTF-8 text of 1–200 characters.
- Single-file entry: the grader only loads `main.py`.
