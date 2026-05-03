from textblob import TextBlob

def analyze_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0.2:
        return {"label": "POSITIVE"}
    elif score < -0.2:
        return {"label": "NEGATIVE"}
    return {"label": "NEUTRAL"}