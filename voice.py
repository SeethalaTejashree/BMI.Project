"""
Voice Assistant using Python
----------------------------
A simple Python-based assistant that listens, responds,
and performs tasks like telling time/date and searching the web.

Features:
- Greets the user
- Tells current time and date
- Performs Google searches
- Works in both voice and text mode

Modules used:
speech_recognition, pyttsx3, datetime, webbrowser
"""

import sys
import webbrowser
from datetime import datetime

# Optional imports for voice functionality
try:
    import speech_recognition as sr
    import pyttsx3
    AUDIO_AVAILABLE = True
except Exception:
    AUDIO_AVAILABLE = False


def speak(text):
    """Speak the given text if audio is available, otherwise print."""
    if AUDIO_AVAILABLE:
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            print(f"Assistant: {text}")
    else:
        print(f"Assistant: {text}")


def listen():
    """Listen for voice command if possible, otherwise take text input."""
    if AUDIO_AVAILABLE:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        try:
            return r.recognize_google(audio)
        except Exception:
            speak("Sorry, I didn’t catch that. Please repeat.")
            return ""
    else:
        return input("You: ").strip()


def handle_command(command):
    """Handle user commands."""
    cmd = command.lower()

    if any(g in cmd for g in ["hello", "hi", "hey"]):
        speak("Hello! How can I help you?")

    elif "time" in cmd:
        speak("Current time is " + datetime.now().strftime("%H:%M:%S"))

    elif "date" in cmd:
        speak("Today's date is " + datetime.now().strftime("%Y-%m-%d"))

    elif "search" in cmd:
        query = cmd.replace("search", "").strip()
        if not query:
            speak("What should I search for?")
            query = listen()
        if query:
            speak(f"Searching the web for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")

    elif cmd in ["exit", "quit", "bye", "goodbye"]:
        speak("Goodbye! Have a great day!")
        sys.exit(0)

    else:
        speak("Sorry, I didn’t understand that. You can say 'time', 'date', 'search <query>', or 'exit'.")


def main():
    """Main program loop."""
    print("🎙️ Voice Assistant Started")
    print(f"Audio Mode: {'Enabled' if AUDIO_AVAILABLE else 'Text Mode'}")
    speak("Hi, I am your assistant. How can I help you today?")

    while True:
        try:
            command = listen()
            if not command:
                continue
            print(f"You: {command}")
            handle_command(command)
        except KeyboardInterrupt:
            speak("Exiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
