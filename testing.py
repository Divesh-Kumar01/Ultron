import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import pywhatkit as kit
from difflib import get_close_matches



def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)



def greet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        say("Good Morning!")
    elif 12 <= hour < 18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")



def takecommand(show_logs=True):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        if show_logs:
            print("\nListening...")

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        if show_logs:
            print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        if show_logs:
            print(f"User Said: {query}")

        return query.lower()

    except Exception as e:
        if show_logs:
            print("Could not understand. Error:", e)
        return ""



contacts = {
    "vartul": "+919509574204",
    "aryan": "+917253031304",
    "bro": "+919693763713",
    "jayant": "+917983060701",
    "mayank": "+919211168123"
}



def match_contact(name):
    name = name.lower().strip()
    all_names = list(contacts.keys())

    match = get_close_matches(name, all_names, n=1, cutoff=0.6)

    return match[0] if match else None


# ========== MAIN PROGRAM ==========
if __name__ == '__main__':
    greet()
    say("Hello, I am Ultron Version 3. I am now online and ready.")

    while True:

        query = takecommand()

        
        if "introduce yourself" in query or "who are you" in query or "what can you do" in query:
            intro = ("Hello sir. I am Ultron, your personal voice assistant. "
                "I can open websites, launch applications, search Wikipedia, tell you the time, "
                "play music, and send WhatsApp messages. "
                "I listen to your commands and execute them instantly. "
                "I am always learning and improving to assist you better.")
            say(intro)
            print(intro)
            continue


        
        if any(word in query for word in ["quit", "exit", "stop", "goodbye"]):
            say("Shutting down sir. Have a great day.")
            break

        
        sites = [
            ["youtube", "https://www.youtube.com/"],
            ["wikipedia", "https://www.wikipedia.org/"],
            ["google", "https://www.google.com/"],
            ["instagram", "https://www.instagram.com/"],
            ["facebook", "https://www.facebook.com/"],
            ["chat gpt", "https://www.chatgpt.com/"]
        ]

        for name, url in sites:
            if f"open {name}" in query:
                say(f"Opening {name} sir...")
                webbrowser.open_new_tab(url)

        
        if "play music" in query:
            say("Playing music sir")
            music_dir = "C:/Users/rages/Downloads/Darkside.mp3"
            os.system(f'start \"\" \"{music_dir}\"')

        
        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {strfTime}")

    

        
        apps = [
            ["chrome", "C:/Program Files/Google/Chrome/Application/chrome.exe"],
            ["camera", "microsoft.windows.camera:"],
            ["notepad", "notepad"],
            ["calculator", "calc"]
        ]

        for app_name, app_path in apps:
            if f"open {app_name}" in query:
                say(f"Opening {app_name} sir...")
                os.system(f'start \"\" \"{app_path}\"')

        
        if "send message" in query:
            say("To whom should I send the message?")
            print("\nListening for contact name...")
            name = takecommand()

            matched_name = match_contact(name)

            if not matched_name:
                say("This contact is not saved sir.")
                print("Contact not found:", name)
                continue

            number = contacts[matched_name]

            say(f"What is the message for {matched_name}?")
            print("\nListening for message...")
            message = takecommand()

            if message.strip() == "":
                say("I didn't catch the message sir. Please try again.")
                continue

            try:
                say(f"Sending message to {matched_name}")
                kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
                say("Message sent sir.")
                print("Message sent:", message)
            except Exception as e:
                say("Sorry sir, unable to send.")
                print("Error:", e)

