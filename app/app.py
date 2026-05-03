import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.text.pipeline import process_text
from src.audio.audio_pipeline import process_audio
from src.video.video_pipeline import process_video

st.set_page_config(layout="wide")

st.title("Multimodal Language & Sentiment Analyzer")

tab1, tab2, tab3 = st.tabs(["Text", "Audio", "Video"])

# -------- TEXT --------
with tab1:
    text = st.text_area("Enter text")

    if st.button("Analyze Text"):
        result = process_text(text)

        c1, c2, c3 = st.columns(3)

        c1.metric("Language", result["sentence_language"])
        c2.metric("Sentiment", result["sentiment"]["label"])
        c3.metric("Hate Speech", result["hate_speech"])

        st.subheader("Word-Level Language")
        st.json(result["word_level_language"])

        st.subheader("Language Distribution")
        st.json(result["corpus_language"]["distribution"])


# -------- AUDIO --------
with tab2:
    audio = st.file_uploader("Upload WAV", type=["wav"])

    if audio:
        with open("temp.wav", "wb") as f:
            f.write(audio.read())

        result = process_audio("temp.wav")

        if "error" in result:
            st.error(result["error"])
        else:
            st.write("Transcription:", result["transcription"])
            st.metric("Language", result["sentence_language"])
            st.metric("Sentiment", result["sentiment"]["label"])


# -------- VIDEO --------
with tab3:
    video = st.file_uploader("Upload MP4", type=["mp4"])

    if video:
        with open("temp.mp4", "wb") as f:
            f.write(video.read())

        result = process_video("temp.mp4")

        if "error" in result:
            st.error(result["error"])
        else:
            st.write("Transcription:", result["transcription"])
            st.metric("Language", result["sentence_language"])
            st.metric("Sentiment", result["sentiment"]["label"])