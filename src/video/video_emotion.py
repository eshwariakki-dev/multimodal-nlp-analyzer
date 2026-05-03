import cv2

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

    cap.release()

    if frame_count > 50:
        return "Active"
    else:
        return "Calm"


if __name__ == "__main__":
    print(analyze_video("sample.mp4"))