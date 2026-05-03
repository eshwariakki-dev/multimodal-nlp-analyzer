HATE_WORDS = {"hate","kill","idiot","stupid","dumb","moron"}

def detect_hate(text):
    t = text.lower()

    for w in HATE_WORDS:
        if f" {w} " in f" {t} ":
            return "HATE"

    return "NOT HATE"