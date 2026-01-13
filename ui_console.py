import re

try:
    from colorama import Back, init
    init(autoreset=True)
    USE_COLOR = True
except Exception:
    USE_COLOR = False
    Back = None

def he(s: str) -> str:
    rev = s[::-1]
    return re.sub(r"[A-Za-z0-9@#%&*/._+\-]+", lambda m: m.group(0)[::-1], rev)

def ask_max_wrong():
    while True:
        print(he("כמה טעויות מותר?"))
        n = input()
        if n.isdigit() and int(n) > 0:
            return int(n)
        print(he("נא להכניס מספר חיובי."))

def ask_letter():
    print(he("נחש אות:"))
    return input()

def show_state(display, attempts, guessed):
    if USE_COLOR:
        print(Back.BLUE + display)
    else:
        print(display)

    print(he("טעויות:") + " " + attempts)
    if guessed:
        print(he("ניחושים:") + " " + ", ".join(guessed))
    print("-" * 25)

def show_result(won, word):
    if won:
        print(he("ניצחת! המילה:") + " " + word)
    else:
        print(he("הפסדת. המילה:") + " " + word)
