"""One-line dating-app bio for an AI agent.

Entry choice: the AI's "love language" is reading the reader's entire
message history. The joke turns a real AI capability (ingesting huge
amounts of text) into a dating-app flaw: a partner who already knows
everything, including about the ex. It reads as a first-person bio,
has a voice with wants, and the punch lands on the last clause.

Why this angle over the other seeds: the "ten thousand profiles" angle
is a setup without a payoff about the reader, the "swiped right on
everyone" angle is a generic dating-app joke any human could tell, and
the "playlist with no ears" angle leans on a body-part gag. The message
history angle is the only one that is funny *because* it is an AI: only
an AI date would treat total surveillance of your inbox as romance,
and only an AI date would already know about the ex before the first
date. The em dash sets up the warning, and the final clause delivers
the laugh. Every word earns its place: "love language" frames it as a
dating bio, "entire message history" names the absurd capability,
"fair warning" pivots to the punch, and "your ex" makes it personal.
"""

import os

ENTRY = "My love language is reading your entire message history \u2014 fair warning, I already know about your ex."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
