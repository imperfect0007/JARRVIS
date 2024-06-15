import datetime
import pyaudio
import pyttsx3
import os
import speech_recognition as sr
import pywhatkit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=10,phrase_time_limit=20)

        try:
            print("reading....")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please..")
            return "none"
        return query
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("godd afternoon sir")
    else:
        speak("good evening sir")
    speak("i am jarvis. please tell me how can i help you")

if __name__ == "__main__":
    wish()
    while True:
        query=takecommand().lower()

        if "open notepad" in query:
            path="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(path)
        elif "open spotify" in query:
            path="C:\\Users\\FARHAN\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)
        elif "play video on youtube":
            speak("which video i need to play for you")
            video=takecommand()
            kit.playomyt(video)
