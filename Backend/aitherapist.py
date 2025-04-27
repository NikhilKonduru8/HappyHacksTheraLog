import speech_recognition as sr
from moviepy import VideoFileClip
from google import genai

def extract_audio(video_path, output_audio_path):
    # Load the video file
    video = VideoFileClip(video_path)

    # Extract audio
    audio = video.audio

    # Save the audio file
    audio.write_audiofile(output_audio_path)

extract_audio("happy/check-in.mov", "happy/audio.wav")

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Create audio file instance from the original file
audio_ex = sr.AudioFile('happy/audio.wav')
type(audio_ex)

# Create audio data
with audio_ex as source:
    audiodata = recognizer.record(audio_ex)
type(audiodata)

# Extract text
text = recognizer.recognize_google(audio_data=audiodata, language='en-US')

query = "Sympathize with me and generate steps to help me: " + text

client = genai.Client(api_key="your_api_key")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=query
)
print(response.text)




