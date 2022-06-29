#pip install SpeechRecognition
#pip install PyAudio

import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeInput():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" I am listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("On it.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"U said: {query}\n")

    except Exception as e:
        print("Sorry I am not sure")
        return "None"
    
    return query

if __name__ == '__main__':
    speak('Hello, welcome to your very first AI project. We are super excited for your learning')

    while True:
        query = takeInput().lower()
    
        if "open youtube" in query:
            webbrowser.open("youtube.com/manifoldailearning")
