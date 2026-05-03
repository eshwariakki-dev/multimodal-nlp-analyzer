from moviepy import VideoFileClip
from src.audio.audio_pipeline import process_audio

def process_video(video_path):
    clip = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    clip.audio.write_audiofile(audio_path)

    return process_audio(audio_path)