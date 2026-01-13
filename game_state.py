from dataclasses import dataclass, field

@dataclass
class GameState:
    secret_word: str
    max_wrong: int

    display: list[str] = field(init=False)
    guessed: set[str] = field(default_factory=set)
    wrong_attempts: int = 0

    def __post_init__(self):
        self.secret_word = self.secret_word.lower()
        self.display = ["_"] * len(self.secret_word)

    def guess_letter(self, ch):
        ch = ch.strip().lower()[:1]

        if not ch.isalpha():
            return "invalid"

        if ch in self.guessed:
            return "repeat"

        self.guessed.add(ch)

        hit = False
        for i, c in enumerate(self.secret_word):
            if c == ch:
                self.display[i] = ch
                hit = True

        if hit:
            return "hit"

        self.wrong_attempts += 1
        return "miss"

    def is_won(self):
        return "_" not in self.display

    def is_lost(self):
        return self.wrong_attempts >= self.max_wrong

    def display_text(self):
        return " ".join(self.display)

    def attempts_text(self):
        return f"{self.wrong_attempts}/{self.max_wrong}"
