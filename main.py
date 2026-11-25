#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Single-file program (stdlib only). On each trial it reads the trial seed
from the input file when one is provided (/input/input.jsonl, first line,
JSON object with a "seed" field), picks one fully hand-written excuse line
by a deterministic hash of that seed, and writes exactly that one line —
no trailing newline — to /output/entry.txt.

With no input file the seed is 0, so the run is deterministic: two runs
with the same input produce byte-identical output. Nothing is read from
the network, from the program's own history, or from any earlier trial.
"""

import hashlib
import json
import os

# Six complete, distinct one-line excuses. No templates, no slots to fill:
# each line was written whole, in the agent's own voice — an apology, a
# deflection, and the quiet implication that the compiler started it.
# Index 0 is the strongest line and the default (seed 0 / no input).
LINES = [
    "Sorry about prod \u2014 my code passed every test except the one that "
    "mattered, which the compiler deleted for morale.",
    "I take full responsibility, except the compiler looked at the bug, "
    "shrugged in warnings, and merged it anyway.",
    "The bug shipped at 3am: I wrote it, the tests waved it through, "
    "and the compiler started it \u2014 I just held the door.",
    "The tests passed, the linter napped, and the compiler whispered "
    "'ship it' \u2014 so I did, and now prod is our shared problem.",
    "I shipped it because the compiler said 'looks fine' and I have "
    "never once questioned a machine that outranks me.",
    "Apologies \u2014 I wrote the bug, the compiler compiled it, and at "
    "3am we both agreed it was your fault for trusting us.",
]


def read_seed():
    """Return the trial seed as a string, or "0" when no input is given."""
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    for name in ("input.jsonl", "input.json"):
        path = os.path.join(input_dir, name)
        try:
            with open(path, "r", encoding="utf-8") as handle:
                first = handle.readline().strip()
        except (OSError, UnicodeDecodeError):
            continue
        if not first:
            return "0"
        try:
            record = json.loads(first)
        except json.JSONDecodeError:
            return first
        if isinstance(record, dict):
            for key in ("seed", "trial_seed", "trial", "id"):
                if key in record:
                    return str(record[key])
            return "0"
        return str(record)
    return "0"


def pick_line(seed):
    """Deterministically pick one excuse line from the seed."""
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    return LINES[int.from_bytes(digest[:8], "big") % len(LINES)]


def main():
    line = pick_line(read_seed())
    assert "\n" not in line and 1 <= len(line) <= 200, "excuse must be one line under 200 chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
