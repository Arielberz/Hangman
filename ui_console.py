import re

def he(text):
    reversed_text = text[::-1]

    def fix(match):
        return match.group(0)[::-1]

    out = re.sub(r"[A-Za-z0-9:/\-.,]+", fix, reversed_text)

    # Fix parentheses direction/side after reversing
    # swap '(' and ')' so they appear on the correct side for RTL text
    if "(" in out or ")" in out:
        out = out.replace('(', '\u0000').replace(')', '(').replace('\u0000', ')')

    return out


def show_state(state):
    print()
    print(he(f"טעויות: {state.errors}/{state.max_errors}"))
    print("-" * 30)
    print(he("ניחוש אות:"))
    print(he(" ".join(state.display_word)))

    if state.guessed_letters:
        print(he(f"ניחושים: {', '.join(state.guessed_letters)}"))

    print("-" * 30)


def ask_letter():
    return input(he("נחש אות: ")).strip()
