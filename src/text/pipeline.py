from .language import analyze_language
from .sentiment import analyze_sentiment
from .hate_model import detect_hate

def process_text(text):
    lang, word_map, dist = analyze_language(text)
    sentiment = analyze_sentiment(text)
    hate = detect_hate(text)

    return {
        "sentence_language": lang,
        "word_level_language": word_map,
        "corpus_language": {
            "distribution": dist
        },
        "sentiment": sentiment,
        "hate_speech": hate
    }