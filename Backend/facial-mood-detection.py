
from fer import Video
from fer import FER

video_filename = "aditya.mov"
video = Video(video_filename)

# Create the emotion detector
detector = FER(mtcnn=True)

# Analyze the video, display=True if you want it to show live
raw_data = video.analyze(detector, display=True)

# Convert raw data into a DataFrame
df = video.to_pandas(raw_data)

# Get the emotion columns
emotion_columns = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Sum up all emotion scores
emotion_totals = df[emotion_columns].sum()

# Find the emotion with the highest total score
main_emotion = emotion_totals.idxmax()

print(f"The main emotion throughout the video is: {main_emotion}")
