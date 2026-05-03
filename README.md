# Multimodal Language & Sentiment Analyzer

## Overview
This project analyzes text, audio, and video to detect:
- Language (multilingual, Indian + English)
- Sentiment (Positive, Negative, Neutral)
- Hate speech (Safe, Offensive, Hate)

## Features
- Works with:
  - Text (word, sentence, paragraph)
  - Audio (speech to text + analysis)
  - Video (audio extraction + analysis)
- Supports multilingual inputs including Indian regional languages
- Displays output in English
- Clean UI built with Streamlit

## Tech Stack
- Python
- HuggingFace Transformers
- Streamlit
- MoviePy
- SpeechRecognition
- Librosa

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py
