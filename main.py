import os

# One Line, One Laugh — short enough to read in a breath.
# One character pair (dog, cat), one reversal in the final clause.
ENTRY_TEXT = "I taught my dog 14 commands. He obeys exactly one: the one the cat gives him."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
