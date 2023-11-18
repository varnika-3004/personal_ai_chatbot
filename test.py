import speech_recognition as sr
import pyttsx3 
import pywhatkit 
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()


engine=pyttsx3.init()

voices=engine.getProperty("voices")
engine.setProperty('rate',150)
engine.setProperty('voice','english+f2')



def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            print("Hey,This is Sara")
            print("How can I help you today")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'sara' in command:
                command=command.replace('sara','')
                print(command)
    except:
        pass
    return command

def run_bot():
    command=user_commands()
    if 'play' in command:
        song =command.replace('play','')
        engine_talk('Playing'+song )
        pywhatkit.playonyt(song)
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is'+time)
    if 'who is' in command:
        name=command.replace('who is','')
        info=wikipedia.summary(name,1)
        print(info)
        engine_talk(info)
    if 'joke' in command:
        engine_talk(pyjokes.get_joke())
    else:
        engine_talk('Could not hear properly')
run_bot()
