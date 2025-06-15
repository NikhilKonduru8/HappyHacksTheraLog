🧠 TheraLog – Your Free, Private AI Therapist

Hackathon Project By: Nikhil Konduru, Arnav Garg, and Aditya Gaur

TheraLog is an AI-powered, on-demand mental health assistant designed for individuals who may feel hesitant to speak to a real therapist due to stigma or privacy concerns. This tool offers a supportive, judgment-free space where users can talk, be heard, and receive intelligent, personalized feedback — completely free.

🧩 Key Features
Real-time Emotional Analysis: TheraLog uses voice tone and facial expression recognition to understand the user’s emotional state during a video session.

Speech-to-Text Processing: Converts spoken input into accurate text to improve the quality of conversation and analysis.

AI-Driven Feedback: Integrates with the Gemini API to generate thoughtful responses and practical advice tailored to what the user is going through.

Streamlit Frontend: Provides a clean, accessible web interface where users can interact with the AI securely and seamlessly.

⚙️ Technologies Used
Python – Backend processing and API integration

Streamlit – Interactive frontend user interface

Gemini API – Language understanding and response generation

OpenCV / MediaPipe / Emotion Detection Models – (if applicable) Facial expression tracking

SpeechRecognition / Whisper / other – Voice input and speech-to-text conversion

🚀 How It Works
The user starts a session and begins speaking to the AI.

TheraLog analyzes:

The tone of voice

Facial expressions through webcam input

The spoken content, converted to text

All data is passed to the Gemini API, which interprets the emotional and contextual state of the user.

The API returns a compassionate, relevant response shown in the Streamlit interface.

The cycle continues in real-time, simulating a dynamic conversation with a virtual therapist.

💡 Motivation
Many people avoid seeking therapy due to fear of being judged or simply because of cost and accessibility. TheraLog was built to bridge that gap using the power of AI — offering an empathetic, helpful, and always-available listener that respects user privacy.

🔒 Privacy Note
All processing can be done locally if configured correctly. No personal data is stored or shared.

📌 Future Improvements
More accurate tone/facial expression models

Mood tracking over time

Custom feedback modes (comfort, motivation, logic-based)

Integration with journaling or mental wellness tools
