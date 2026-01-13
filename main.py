from word_provider import fetch_random_word
from game_state import GameState
from ui_console import ask_max_wrong, ask_letter, show_state, show_result

def main():
    max_wrong = ask_max_wrong()
    word = fetch_random_word()
    game = GameState(word, max_wrong)

    while not game.is_won() and not game.is_lost():
        show_state(game.display_text(), game.attempts_text(), sorted(game.guessed))
        result = game.guess_letter(ask_letter())

        if result == "invalid":
            print("קלט לא חוקי")
        elif result == "repeat":
            print("כבר ניחשת")
        elif result == "hit":
            print("פגיעה")
        elif result == "miss":
            print("טעות")

    show_state(game.display_text(), game.attempts_text(), sorted(game.guessed))
    show_result(game.is_won(), game.secret_word)

if __name__ == "__main__":
    main()
