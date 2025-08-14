import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import time
import pyaudio as pya

engine = pyttsx3.init()

def speak(text):
    #Convert text to speech
    engine.say(text)
    engine.runAndWait()

def take_command():
    #Listen to microphone and return recognized text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def open_application(app_name):
    #Open applications based on name
    try:
        if "chrome" in app_name:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif "word" in app_name:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")
        elif "notepad" in app_name:
            os.system("notepad.exe")
        else:
            speak("Sorry, I didn't understand that. Please try again.")

    except Exception as e:
        speak("Sorry, I didn't understand that. Please try again.")

def close_application(app_name):
    #Close applications
    try:
        if "chrome" in app_name:
            os.system("taskkill /im chrome.exe /f")
        elif "word" in app_name:
            os.system("taskkill /im WINWORD.EXE /f")
        elif "lazarus" in app_name:
            os.system("taskkill /im chrome.exe /f")
        else:
            speak("Sorry, I didn't understand that. Please try again.")
    except Exception as e:
        speak("Sorry, I didn't understand that. Please try again.")


if __name__ == "__main__":
    speak("Hi, I am Optimus. Your personal voice assistant. How can I be of service?")
    while True:
        query = take_command().lower()

        if "open" in query:
            app_name = query.replace("open ", "").strip()
            speak(f'Opening {app_name}')
            open_application(app_name)

        elif "close" in query:
            app_name = query.replace("close ", "").strip()
            speak(f'Closing{app_name}')
            close_application(app_name)

        elif "date" in query:
            current_date = datetime.date.today()
            speak(f"Today's date is {current_date.strftime('%B %d, %Y')}")

        elif "time" in query:
            current_time = datetime.datetime.now().time()
            speak(f"The current time is {current_time.strftime('%I:%M %p')}")

        elif "search" in query:
            search_term = query.replace("search ", "").strip()
            speak('Searching...')
            webbrowser.open("https://www.google.com/search?q=" + search_term)

        elif "wikipedia" in query:
            search_term = query.replace("wikipedia ", "").strip()
            try:
                info = wikipedia.summary(search_term, sentences=5)
                speak(info)
            except Exception:
                speak("Sorry, I didn't understand that. Please try again.")

        elif "exit" in query or "quit" in query:
            speak("Goodbye")
            break

7