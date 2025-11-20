import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import pywhatkit as kit

#by using this function ultron speaks
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

#by using this ultron takes our command as voice and convert it into string
def takecommand():
    r = sr.Recognizer()

    r.energy_threshold = 4000
    r.pause_threshold = 1
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening quietly...")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-IN')
            print(f"User Said: {query}")
            return query.lower()
        except:
            return "none"

#by using this ultron ask us what we want him to do next
def ask_after_task():
    say("What should I do next sir?")

# contacts are going to be used in whatsapp msg
contacts = {
    "vartul": "+919509574204",
    "aryan": "+917253031304",
    "bro": "+919693763713",
    "jayant": "+91",
    "mayank": "+919211168123"
}

# Real codes starts
if __name__ == '__main__':
    say("Ultron activated. Say 'Ultron'.")

    ACTIVE = False

    while True:

        query = takecommand()

        if query == "none" or len(query) < 3:
            continue

       # word for waking up ultron
        if "ultron" in query:
            ACTIVE = True
            say("Yes sir, what should I do?")
            continue

        # If Ultron isn't activated yet , it remains  silent
        if not ACTIVE:
            continue

        # word for quiting the code
        if "quit" in query or "exit" in query or "ultron stop" in query:
            say("Shutting down Ultron sir.")
            break

        # code for opening websites
        sites = [
            ["youtube", "https://www.youtube.com/"],
            ["wikipedia", "https://www.wikipedia.com/"],
            ["google", "https://www.google.com/"],
            ["instagram", "https://www.instagram.com/"],
            ["facebook", "https://www.facebook.com/"],
            ["chat gpt", "https://www.chatgpt.com/"],
            ["whatsapp", "https://www.whatsapp.com/"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open_new_tab(site[1])
                ask_after_task()

        # codes for opening apps or software
        apps = [
            ["chrome", "C:/Program Files/Google/Chrome/Application/chrome.exe"],
            ["vs code", r"C:\Users\rages\AppData\Local\Programs\Microsoft VS Code\Code.exe"],
            ["code", r"C:\Users\rages\AppData\Local\Programs\Microsoft VS Code\Code.exe"],
            ["camera", "microsoft.windows.camera:"],
            ["notepad", "notepad"],
            ["calculator", "calc"],
        ]

        for app in apps:
            if f"open {app[0]}" in query:
                say(f"Opening {app[0]} sir...")
                os.system(f'start "" "{app[1]}"')
                ask_after_task()

       # codes for playing music or songs
        if "play songs on youtube" in query:
            say("Playing songs sir...")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=CsrsR_sC2jE")
            ask_after_task()

        if "play music" in query:
            say("Playing music sir...")
            music_dir = r"C:\Users\rages\Downloads\Darkside.mp3"
            os.system(f'start "" "{music_dir}"')
            ask_after_task()

        # code of time
        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")
            ask_after_task()

        # codes for shutdown or restart or sleep the computer/laptop
        if "shutdown" in query:
            say("Shutting down your system sir.")
            os.system("shutdown /s /t 3")

        if "restart" in query:
            say("Restarting your system sir.")
            os.system("shutdown /r /t 3")

        if "sleep" in query or "computer off" in query or "pc sleep" in query:
            say("Putting your computer to sleep sir.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        # codes for whatsapp msg
        if "send message" in query:
            say("To whom should I send the message?")
            name = takecommand()

            if name not in contacts:
                say("This contact is not saved sir.")
                ask_after_task()
                continue

            number = contacts[name]
            say("What is the message sir?")
            message = takecommand()

            try:
                say(f"Sending message to {name}")
                kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
                say("Message sent sir.")
            except:
                say("Sorry sir, unable to send.")

            ask_after_task()





