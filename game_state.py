class GameState:
    def __init__(self, word, max_errors=4):
        self.word = word
        self.max_errors = max_errors
        self.errors = 0
        self.guessed_letters = set()
        self.display_word = ["_" for _ in word]

    def guess(self, ch):
        if ch in self.guessed_letters:
            return "already"

        self.guessed_letters.add(ch)

        if ch in self.word:
            for i, letter in enumerate(self.word):
                if letter == ch:
                    self.display_word[i] = ch
            return "hit"
        else:
            self.errors += 1
            return "miss"

    def is_won(self):
        return "_" not in self.display_word

    def is_lost(self):
        return self.errors >= self.max_errors
