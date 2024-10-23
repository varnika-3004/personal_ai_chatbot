Sara - Voice-Activated AI Chatbot


Sara is an AI-powered voice-activated chatbot designed to make your life easier through natural language interaction. It can recognize speech, perform tasks like playing music, searching Wikipedia, telling jokes, and detecting stress from your speech to offer helpful responses. This project showcases how a simple chatbot can be enhanced with multiple features using Python libraries.

Project Overview

Sara acts as your personal assistant, able to:

Convert Speech to Text: Sara uses speech recognition to understand what you say and respond appropriately.
Play Music: By simply saying "play [song name]," Sara fetches and plays your requested song from YouTube.
Search Wikipedia: Sara can answer factual questions by searching Wikipedia and providing short summaries.
Tell Jokes: Lighten your mood with random jokes upon request.
Time Inquiry: Ask Sara for the current time, and she will respond with the exact time.
Stress Detection: If Sara detects stress-related words like "anxious" or "frustrated," she provides comforting responses or stress-relief tips.
Features
Speech to Text: Sara uses Google’s Speech Recognition to convert your spoken words into text for processing.
Music Playback: Integrates with YouTube via the pywhatkit library to play music based on user requests.
Wikipedia Search: Queries Wikipedia and provides a concise summary of any topic.
Jokes: Sara uses pyjokes to tell you a joke whenever you ask.
Current Time: Sara can fetch the current time using Python's datetime module.
Stress Response: Detects stress-related keywords in speech and responds with helpful tips and support.


Technology Stack

Python: The main programming language used to develop this chatbot.
SpeechRecognition: Converts speech to text using Google’s Speech API.
Pyttsx3: A text-to-speech library for converting text responses into speech.
Pywhatkit: Handles YouTube searches to play music on user request.
Wikipedia API: Fetches data and summaries from Wikipedia.
Pyjokes: Provides jokes to lighten the conversation.
Datetime: Fetches the current time when asked.


Setup and Installation

Prerequisites
Python 3.x installed on your system.
An internet connection for voice recognition and Wikipedia search.

Error Handling

Sara includes basic error handling for issues like:
Speech Recognition Failures: If Sara cannot understand your speech, she will prompt you to try again.
Network Errors: If there is a problem with Google’s Speech Recognition service, Sara will inform you of the issue.


Contributing
Feel free to contribute to this project by submitting issues or making pull requests. Any improvements or feature suggestions are welcome!

Fork the repository.
Create a new branch for your feature.
Submit a pull request with your changes.
