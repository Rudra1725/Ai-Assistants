import datetime
import os
import subprocess
import sys
import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
import requests
import wikipedia

try:
    import pyaudiowpatch as pyaudio
    sys.modules['pyaudio'] = pyaudio
except ImportError:
    pass

import speech_recognition as sr

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
VS_CODE_CMD = "code"

SETUP_URLS = [
    "https://github.com",
    "https://gemini.google.com",
    "https://chatgpt.com"
]

LINKEDIN_URL = "https://www.linkedin.com"

wiki_session = requests.Session()
wiki_session.headers.update({"User-Agent": "DesktopVoiceAssistant/1.0"})
wikipedia.requests = wiki_session

listener = sr.Recognizer()
listener.dynamic_energy_threshold = False
listener.energy_threshold = 300
listener.pause_threshold = 0.8

engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break


def speak(text):
    print(f"FRIDAY: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")


def open_browser_urls(urls):
    if os.path.exists(BRAVE_PATH):
        subprocess.Popen([BRAVE_PATH] + urls)
    else:
        for url in urls:
            webbrowser.open_new_tab(url)


def listen(phrase_time_limit=6):
    try:
        with sr.Microphone() as source:
            audio = listener.listen(source, timeout=None, phrase_time_limit=phrase_time_limit)
            return listener.recognize_google(audio, language="en-in").lower()
    except (sr.UnknownValueError, sr.WaitTimeoutError):
        return ""
    except sr.RequestError:
        speak("Network connection error.")
        return ""
    except Exception:
        return ""


def launch_setup():
    speak("Launching your developer setup.")
    open_browser_urls(SETUP_URLS)

    try:
        subprocess.Popen(VS_CODE_CMD, shell=True)
    except Exception:
        speak("Unable to launch Visual Studio Code.")


def execute_command(command):
    print(f"You: {command}")

    if any(phrase in command for phrase in ["open my setup", "open setup"]):
        launch_setup()

    elif any(phrase in command for phrase in ["open linkedin", "open linkedin profile", "open linkdin", "open link din"]):
        speak("Opening LinkedIn.")
        open_browser_urls([LINKEDIN_URL])

    elif command.startswith("play "):
        song = command.replace("play", "", 1).strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif command.startswith("search ") or "search for " in command:
        query = command.replace("search for", "").replace("search", "").strip()
        speak(f"Searching for {query}")
        pywhatkit.search(query)

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {current_time}.")

    elif any(phrase in command for phrase in ["who is", "what is", "tell me about"]):
        query = command
        for phrase in ["who is", "what is", "tell me about"]:
            query = query.replace(phrase, "")
        query = query.strip()

        try:
            results = wikipedia.search(query)
            if results:
                info = wikipedia.summary(results[0], sentences=2, auto_suggest=False)
                speak(info)
            else:
                speak("I could not find anything matching that on Wikipedia.")
        except Exception:
            speak("Sorry, I could not fetch that information.")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif any(word in command for word in ["exit", "shutdown", "quit"]):
        speak("Powering down. Have a productive day.")
        sys.exit(0)

    else:
        speak("Command not recognized.")


def main():
    speak("Friday is online and actively listening.")
    print("Always listening... Speak your command directly.")

    while True:
        command = listen(phrase_time_limit=6)
        if command:
            if command.startswith("friday "):
                command = command.replace("friday", "", 1).strip()
            execute_command(command)


if __name__ == "__main__":
    main()