import speech_recognition as sr
from src.text.pipeline import process_text

def process_audio(file_path):
    r = sr.Recognizer()

    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
    except:
        return {"error": "Speech not recognized"}

    result = process_text(text)
    result["transcription"] = text

    return result