from transformers import pipeline

# Load the pre-trained Speech Emotion Recognition pipeline
emotion_recognition = pipeline("audio-classification", model="r-f/wav2vec-english-speech-emotion-recognition")

audio_path = "audio.wav"

# Perform emotion recognition
emotion = emotion_recognition(audio_path)

emotion1 = emotion[0]["label"]
emotion2 = emotion[1]["label"]

print(f"The emotions you feel are: {emotion1} and {emotion2}")
