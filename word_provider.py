import random
import requests

FALLBACK_WORDS = [
    "python", "hangman", "computer", "programming", "school", "banana", "israel"
]

def fetch_random_word(timeout_sec=5.0):
    url = "https://random-word-api.herokuapp.com/word?number=1"
    try:
        r = requests.get(url, timeout=timeout_sec)
        r.raise_for_status()
        data = r.json()
        word = data[0].lower()
        if word.isalpha():
            return word
    except Exception:
        pass

    return random.choice(FALLBACK_WORDS)
