import random
import requests

FALLBACK_WORDS = [
    "תוכנה",
    "מחשב",
    "אלגוריתם",
    "פייתון",
    "קוד"
]

URL = "https://raw.githubusercontent.com/oprogramador/wordlists/master/hebrew.txt"


def get_word(timeout_sec=5):
    try:
        r = requests.get(URL, timeout=timeout_sec)
        r.raise_for_status()
        words = [w.strip() for w in r.text.splitlines() if w.strip() and w.isalpha()]
        return random.choice(words)
    except Exception:
        return random.choice(FALLBACK_WORDS)
