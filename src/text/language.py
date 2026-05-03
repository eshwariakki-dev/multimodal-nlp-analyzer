from collections import Counter

def detect_script(word):
    for ch in word:
        code = ord(ch)

        # Telugu
        if 0x0C00 <= code <= 0x0C7F:
            return "te"

        # Kannada
        elif 0x0C80 <= code <= 0x0CFF:
            return "kn"

        # Hindi (Devanagari)
        elif 0x0900 <= code <= 0x097F:
            return "hi"

        # Tamil
        elif 0x0B80 <= code <= 0x0BFF:
            return "ta"

        # Malayalam
        elif 0x0D00 <= code <= 0x0D7F:
            return "ml"

    return "en"


def analyze_language(text):
    words = text.split()
    langs = []

    for w in words:
        if len(w) <= 1:
            continue
        langs.append(detect_script(w))

    count = Counter(langs)

    if not count:
        return "unknown", {}, {}

    total = sum(count.values())

    # dominant language logic
    top_lang, top_count = count.most_common(1)[0]

    if top_count / total >= 0.7:
        final_lang = top_lang
    else:
        final_lang = "+".join(sorted(count.keys()))

    word_map = {w: detect_script(w) for w in words}
    distribution = {k: round(v/total, 2) for k, v in count.items()}

    return final_lang, word_map, distribution