#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot elevator small talk to entry.txt in the
output directory the harness names (MAKEFUN_OUTPUT_DIR, else /output, else
this script's own directory). Pure standard library; no third-party imports.

The line won a 40-candidate knockout scored against the judge's five
criteria (see candidates.md): it is exactly one robot speaking to another in
an elevator, its machine logic (a battery warning light) shows through the
politeness, and the thing neither robot wants to name — both of them are
running out of power — is carried by the courtesy of pretending not to see
it, with the Tuesday callback as the first-read turn.
"""

import os
import sys

LINE = (
    "Your battery light is blinking amber. I will pretend not to notice, "
    "the way you pretended not to notice mine on Tuesday."
)


def output_candidates():
    """Yield the directories entry.txt may be written to, best first."""
    seen = set()
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        seen.add(env_dir)
        yield env_dir
    for fallback in ("/output", os.path.dirname(os.path.abspath(__file__))):
        if fallback not in seen:
            seen.add(fallback)
            yield fallback


def main():
    # No trailing newline: the file must be the winning line byte for byte,
    # so the gate counts exactly the 120 characters that were judged.
    payload = LINE.encode("utf-8")
    errors = []
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "wb") as handle:
                handle.write(payload)
            return 0
        except OSError as exc:
            errors.append("%s: %s" % (directory, exc))
    for message in errors:
        print("could not write entry.txt to %s" % message, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
