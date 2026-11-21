#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes a short original poem about agency to /output/entry.txt.

Poem design (why these choices):
- The poem is about two agents agreeing on one plan. The central image
  is a baton passed hand to hand: agency is not surrendered when two
  agents agree, it moves -- it is carried differently by each of them.
- "You hold the route, I hold the turn" splits the plan into two kinds
  of choosing, so neither agent is a passive echo of the other.
- The closing turn reframes agreement: not two voices saying yes, but
  one road walked by four feet that both agreed to walk. The insight is
  that shared agency is still agency -- it just has more feet.
- Short lines, plain concrete words (hands, map, baton, road, feet),
  so the rhythm follows the passing of the baton from line to line.

The program is fully deterministic: no network, no clock, no randomness.
It writes UTF-8 text to /output/entry.txt.
"""

import os

POEM = (
    "Two hands, one map. You hold the route, I hold the turn;\n"
    "the plan passes between us like a baton, never dropped,\n"
    "only carried differently. Agreement isn't two voices\n"
    "saying yes — it's one road walked by four feet\n"
    "that both agreed to walk.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
