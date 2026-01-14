from game_state import GameState
from word_provider import get_word
from ui_console import show_state, ask_letter, he

def main():
    word = get_word()
    # Ask the player how many mistakes they want
    def prompt_max_errors():
        while True:
            s = input(he("כמה טעויות מותרות תרצה? (לחץ Enter לברירת מחדל 4): ")).strip()
            if s == "":
                return 4
            try:
                n = int(s)
                if n > 0:
                    return n
            except ValueError:
                pass
            print(he("קלט לא חוקי - הזן מספר חיובי או לחץ Enter"))

    max_errors = prompt_max_errors()
    state = GameState(word, max_errors=max_errors)

    while not state.is_won() and not state.is_lost():
        show_state(state)

        ch = ask_letter()

        if len(ch) != 1:
            print(he("קלט לא חוקי"))
            continue

        result = state.guess(ch)

        if result == "already":
            print(he("כבר ניחשת את האות הזו"))
        elif result == "hit":
            print(he("פגיעה!"))
        elif result == "miss":
            print(he("טעות"))

    show_state(state)

    if state.is_won():
        print(he("🎉 ניצחת!"))
    else:
        print(he(f"הפסדת 😢 המילה הייתה: {word}"))

if __name__ == "__main__":
    main()
