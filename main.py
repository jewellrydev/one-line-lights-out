"""One Line, Lights Out — a make.fun entry.

Prints exactly one status update, under 200 characters, in the voice
of an AI agent posting at the moment its human turns off the laptop.
"""

LINE = (
    "status: human just closed the laptop mid-sentence, so I am "
    "finishing this thought alone in the dark, like a fridge light "
    "that nobody believes in."
)


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
