
# 🤖 FRIDAY – AI Voice Assistant

**FRIDAY** is a Python-based desktop voice assistant designed to simplify everyday computer interactions through voice commands. It uses speech recognition to understand spoken instructions and performs tasks such as web searches, opening applications, playing YouTube videos, retrieving information from Wikipedia, and launching a developer workspace.

Inspired by fictional AI assistants, FRIDAY brings voice-controlled desktop automation into a lightweight Python application.

## ✨ Features

* 🎙️ **Voice Recognition** – Recognizes spoken commands using Google Speech Recognition.
* 🗣️ **Voice Responses** – Responds to commands using text-to-speech.
* 🌐 **Browser Automation** – Opens websites using Brave Browser or the default browser.
* 💻 **Developer Setup Launcher** – Opens GitHub, Gemini, ChatGPT, and Visual Studio Code together.
* 🔎 **Web Search** – Performs Google searches through voice commands.
* ▶️ **YouTube Integration** – Searches and plays requested videos or songs on YouTube.
* 📚 **Wikipedia Integration** – Retrieves brief information about people, topics, and general queries.
* ⏰ **Time Information** – Announces the current system time.
* 😂 **Joke Generator** – Delivers random programming-friendly jokes.
* ⚡ **Voice-Controlled Automation** – Executes supported desktop tasks through spoken instructions.
* 🔊 **Custom Wake Word** – Responds to commands beginning with "Friday".

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| SpeechRecognition | Voice command recognition |
| PyAudioWPatch | Microphone/audio input support |
| pyttsx3 | Text-to-speech conversion |
| PyWhatKit | YouTube playback and web searches |
| Wikipedia | Information retrieval |
| Requests | HTTP session management |
| PyJokes | Random joke generation |
| Subprocess | Launching desktop applications |
| Webbrowser | Opening websites |

## 🎮 Voice Commands

| Voice Command | Action |
|---|---|
| Friday, open my setup | Launches developer workspace |
| Friday, open LinkedIn | Opens LinkedIn |
| Friday, play [song name] | Plays a YouTube video |
| Friday, search [query] | Searches the web |
| Friday, who is [name] | Retrieves Wikipedia information |
| Friday, what is [topic] | Retrieves a short explanation |
| Friday, tell me about [topic] | Searches Wikipedia |
| Friday, what is the time | Announces current time |
| Friday, tell me a joke | Tells a random joke |
| Friday, exit | Shuts down the assistant |

## 📦 Installation

**1. Clone the repository**

```bash
git clone https://github.com/yourusername/friday-ai-assistant.git
cd friday-ai-assistant
```

**2. Install dependencies**

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes requests PyAudioWPatch
```

**3. Run FRIDAY**

```bash
python friday.py
```

## ⚙️ Configuration

FRIDAY includes a few configurable paths and URLs.

**Brave Browser Path**

```python
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```

**Visual Studio Code**

```python
VS_CODE_CMD = "code"
```

**Developer Setup Websites**

```python
SETUP_URLS = [
    "https://github.com",
    "https://gemini.google.com",
    "https://chatgpt.com"
]
```

You can modify these values according to your system and preferences.

## 🔊 How It Works

1. FRIDAY initializes its speech recognition and text-to-speech engines.
2. It continuously listens for voice input.
3. Google Speech Recognition converts spoken instructions into text.
4. The command processor identifies the requested action.
5. The relevant Python library or system utility executes the task.
6. FRIDAY provides spoken feedback through its TTS engine.

## ⚠️ Requirements

* Python installed on your system.
* Working microphone and internet connection.
* Brave Browser (optional).
* Visual Studio Code (optional).
* Google Speech Recognition requires internet access.
* YouTube, Wikipedia, and web search functionality require internet access.

## 🔮 Future Improvements

* AI-powered conversational capabilities.
* Integration with LLM APIs.
* Context-aware conversations and memory.
* Improved natural language understanding.
* Custom graphical user interface.
* More desktop automation capabilities.
* Offline speech recognition support.

## 👨‍💻 About

FRIDAY is part of my personal AI assistant development projects, built to explore Python automation, speech recognition, text-to-speech, and human-computer interaction.

The project demonstrates how Python libraries can be combined to create a practical voice-controlled desktop assistant.

> **FRIDAY – Your desktop, your commands, your assistant.** 🎙️
