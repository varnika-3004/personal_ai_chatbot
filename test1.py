import speech_recognition as sr
import pyttsx3
import random
import sys
import pywhatkit
import pyjokes
import wikipedia
import datetime
# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('rate',150)
engine.setProperty('voice','english+f2')

# Define greetings, stress response messages, and stress indicators
greetings = ["Hi there!", "Hello!", "Good day!", "How can I help you today?"]
stress_responses = [
    "I understand that you're feeling stressed. Would you like to talk about it?",
    "It's okay to feel stressed sometimes. Just take a deep breath and relax.",
    "I'm here to listen if you need to talk.",
    "Here are some helpful tips to manage stress: Take a break, do some relaxation techniques like deep breathing or meditation, talk to someone you trust, or engage in activities you enjoy.",
]
stress_indicators = ["stressed", "anxiety", "overwhelmed", "frustrated", "tired"]

# Main loop for continuous conversation
while True:
    # Listen for user input using speech recognition
    with sr.Microphone() as source:
        print("Listening...")
        print("Start Speaking!!")
        print("Hey,This is Sara!")
        print("How can I help you today?")

        audio = recognizer.listen(source)
        

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")

        # Analyze user input for stress indicators and respond accordingly
        stress_detected = False
        for indicator in stress_indicators:
            if indicator in text.lower():
                stress_detected = True
                break

        if stress_detected:
            print("User is feeling stressed.")
            response = random.choice(stress_responses)
            engine.say(response)
            engine.runAndWait()
        else:
            # Provide personalized responses based on user input
            if "hi" in text.lower() or "hello" in text.lower():
                response = random.choice(greetings)
            elif "how are you" in text.lower():
                response = "I'm doing well, thank you for asking. How are you doing today?"
            elif "can you help me with" in text.lower():
                response = "Yes, I'm here to assist you. What can I help you with?"
            elif "bye" in text.lower():
                response = "Alright, have a great day!"
                sys.exit()
            elif 'play' in text.lower():
                song=text.lower().replace('play','')
                response='Playing'+song
                pywhatkit.playonyt(song)
            elif 'time' in text.lower():
                time=datetime.datetime.now().strftime('%I:%M %p')
                response=('The current time is'+time)
            elif 'who is' in text.lower():
                name=text.lower().replace('who is','')
                info=wikipedia.summary(name,1)
                print(info)
                response=info
            elif 'joke' in text.lower():
                response=pyjokes.get_jokes()

            else:
                response = "I'm still learning, but I'll do my best to help you. Please let me know what you need."

            engine.say(response)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Could not understand audio")
        engine.say("Could not understand audio. Please try again.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {0}".format(e))
        engine.say("Could not request results from Google Speech Recognition service. Please check your internet connection and try again.")
        engine.runAndWait()