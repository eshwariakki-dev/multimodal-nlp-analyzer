import librosa
import numpy as np

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=3, offset=0.5)

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_scaled = np.mean(mfcc.T, axis=0)

    return mfcc_scaled

def predict_emotion(file_path):
    features = extract_features(file_path)

    # dummy logic (replace later with model)
    energy = np.mean(features)

    if energy > 0:
        return "Happy"
    else:
        return "Neutral"


if __name__ == "__main__":
    print(predict_emotion("sample.wav"))