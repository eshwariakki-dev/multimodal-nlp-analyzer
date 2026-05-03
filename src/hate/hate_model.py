from transformers import pipeline

hate_pipeline = pipeline("text-classification", model="unitary/toxic-bert")

def detect_hate(text):
    result = hate_pipeline(text)[0]

    label = result["label"]
    score = result["score"]

    if "toxic" in label.lower():
        return {"label": "HATE", "score": round(score, 4)}
    else:
        return {"label": "SAFE", "score": round(score, 4)}


if __name__ == "__main__":
    print(detect_hate("I hate you"))