from time import strftime

import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='hi-in')
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Sorry, I didn't get that. Please try again."


if __name__ == '__main__':
    say("Hello , I am Ultron")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com/"], ["wikipedia", "https://en.wikipedia.org/"],
                 ["google", "https://www.google.com/"], ["instagram", "https://www.instagram.com/"],
                 ["chat gpt", "https://www.chatgpt.com/"], ["facebook", "https://www.facebook.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open_new_tab(site[1])

        if "play music" in query.lower():
            say(f"Playing music")
            music_dir = "C:/Users/rages/Downloads/Darkside.mp3"
            os.system(f'start "" "{music_dir}"')

        if "time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M %S")
            say(f"The time is {strfTime}")

        if "open chrome".lower() in query.lower():
            chrome_dir = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.system(f'start "" "{chrome_dir}"')

        # say(query)
