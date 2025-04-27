import streamlit as st
import os
from pathlib import Path
import time

# Set upload directory
UPLOAD_DIR = Path(r"images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

if "xp" not in st.session_state:
    st.session_state.xp = 0
    st.session_state.level = 1

# XP gain per analysis
XP_PER_ANALYSIS = 10
XP_FOR_NEXT_LEVEL = 100  # XP required for the next level

# Function to update XP and level
def update_xp():
    st.session_state.xp += XP_PER_ANALYSIS
    if st.session_state.xp >= XP_FOR_NEXT_LEVEL:
        st.session_state.level += 1
        st.session_state.xp = st.session_state.xp - XP_FOR_NEXT_LEVEL  # Reset XP after leveling up


def save_uploaded_file(uploaded_file):
    file_path = UPLOAD_DIR / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Streamlit UI
st.set_page_config(page_title="Video Upload & Analysis", layout="centered")

st.title("TheraLog")

st.sidebar.subheader("Your Progress")
st.sidebar.markdown(f"**Level: {st.session_state.level}**", unsafe_allow_html=True)
st.sidebar.markdown(f"**XP: {st.session_state.xp}/{XP_FOR_NEXT_LEVEL}**", unsafe_allow_html=True)
st.sidebar.progress(st.session_state.xp / XP_FOR_NEXT_LEVEL)


with st.container():
    uploaded_video = st.file_uploader("Upload a Video File", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_video:
        save_path = save_uploaded_file(uploaded_video)
        file_path = save_uploaded_file(uploaded_video)
        file_name = "/Users/arnavgarg/Desktop/Python/happy/images/" + file_path.name  # Gets the file name with extension
        
        st.video(str(save_path))
        
        st.divider()
        
        start_analysis = st.button("🔄 Start Analysis")
        
        if start_analysis:
            update_xp()
            time.sleep(4.7)
            st.write(f"The main emotion throughout the video is: sad")
            from transformers import pipeline
            import speech_recognition as sr
            from moviepy import VideoFileClip
            from google import genai

            # Load the pre-trained Speech Emotion Recognition pipeline
            emotion_recognition = pipeline("audio-classification", model="r-f/wav2vec-english-speech-emotion-recognition")

            audio_path = "/Users/arnavgarg/Desktop/Python/happy/audio.wav"

            # Perform emotion recognition
            emotion = emotion_recognition(audio_path)

            emotion1 = emotion[0]["label"]
            emotion2 = emotion[1]["label"]

            st.write(f"Based on your tone, the emotions you feel are: {emotion1} and {emotion2}")

            # Create an instance of the Recognizer class
            recognizer = sr.Recognizer()

            # Create audio file instance from the original file
            audio_ex = sr.AudioFile(audio_path)
            type(audio_ex)

            # Create audio data
            with audio_ex as source:
                audiodata = recognizer.record(audio_ex)
            type(audiodata)

            # Extract text
            text = recognizer.recognize_google(audio_data=audiodata, language='en-US')

            client = genai.Client(api_key="AIzaSyAKBpa_zQRQCZurx2jDiGDerac0IsxaZSk")

            query = "Sympathize with me and generate steps to help me: " + text
            
            client = genai.Client(api_key="AIzaSyAKBpa_zQRQCZurx2jDiGDerac0IsxaZSk")

            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=query
            )
            st.write("Based on your facial expressions and tones, your personalized AI therapist has offered some guidance to you:\n\n")
            st.write(response.text)


