Sara - Voice-Activated AI Chatbot
Sara is an intelligent voice-activated chatbot capable of recognizing speech, converting it to text, playing music, searching Wikipedia, telling jokes, and much more. It also includes features to detect stress-related keywords and respond with helpful suggestions.

Features
Speech to Text: Converts spoken words into text using Google's Speech Recognition API.
Play Music: Sara can play songs from YouTube based on user commands.
Stress Detection: The chatbot can detect stress-related keywords and respond with stress-relief suggestions.
Wikipedia Search: Easily search for any topic on Wikipedia using your voice.
Jokes: Need a laugh? Ask Sara to tell you a joke.
Time: Sara can inform you of the current time.
Personalized Conversations: Sara responds to greetings and can assist with simple queries.
Technologies Used
Python: The main programming language used.
SpeechRecognition: For converting speech to text.
Pyttsx3: For text-to-speech functionality, enabling the chatbot to "speak" responses.
Pywhatkit: To search and play YouTube videos (used for playing music).
Wikipedia API: For fetching quick summaries from Wikipedia.
Pyjokes: For generating random jokes.
Datetime: For fetching the current time.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/sara-chatbot.git
Navigate to the project directory:

bash
Copy code
cd sara-chatbot
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the chatbot:

bash
Copy code
python chatbot.py
Use voice commands such as:

"Play [song name]"
"Who is [name]?" (for Wikipedia search)
"Tell me a joke"
"What is the time?"
"I'm feeling stressed"
You can exit the chatbot at any time by saying "exit" or "quit."

Key Code Snippets
Greeting the User:

python
Copy code
greetings = ["Hi", "Hello!", "Good day!", "How can I help you today?"]
Detecting Stress Indicators:

python
Copy code
stress_indicators = ["stressed", "anxiety", "overwhelmed", "frustrated", "tired"]
Playing Music:

python
Copy code
if 'play' in text.lower():
    song = text.lower().replace('play', '')
    pywhatkit.playonyt(song)
Searching Wikipedia:

python
Copy code
if 'who is' in text.lower():
    info = wikipedia.summary(name, 1)
Contributing
Feel free to submit any issues or pull requests to improve the bot.

License
This project is licensed under the MIT License - see the LICENSE file for details.
