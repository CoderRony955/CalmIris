import os
import logging
import datetime
import pyttsx3
import pywhatkit
import webbrowser
import google.generativeai as genai
import win32com.client
import tkinter as tk
from tkinter import simpledialog


class VoiceAssistant:
    def __init__(self):
        # Setup logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Text-to-Speech Engine
        self.engine = pyttsx3.init()

        # Gemini Configuration
        try:
            with open('config.json', 'r') as file:
                import json
                config = json.load(file)
                gemini_api_key = config.get('gemini_api_key', 'API_KEY')

            if not gemini_api_key:
                raise ValueError("No Gemini API key found")

            genai.configure(api_key=gemini_api_key)
            self.model = genai.GenerativeModel('gemini-pro')

        except Exception as e:
            logging.error(f"Initialization error: {e}")
            self.speak("Failed to initialize. Check API configuration.")
            raise

    def speak(self, text):
        """Convert text to speech"""
        try:
            # Windows SAPI speech
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(text)

            # Backup pyttsx3 method
            # self.engine.say(text)
            # self.engine.runAndWait()
        except Exception as e:
            logging.error(f"Speech error: {e}")
            print(text)

    def get_text_input(self):
        """Get text input via dialog"""
        root = tk.Tk()
        root.geometry("300x250")
        root.withdraw()
        query = simpledialog.askstring("Voice Assistant", "Ask me anything:")
        return query

    def process_command(self, query):
        """Process user command"""
        query = query.lower()

        # YouTube song/video handling
        if 'play' in query and ('song' in query or 'video' in query):
            try:
                # Extract song/video name
                search_term = query.replace('play', '').replace('song', '').replace('video', '').strip()

                if search_term:
                    # Play on YouTube
                    pywhatkit.playonyt(search_term)
                    self.speak(f"Playing {search_term} on YouTube")
                else:
                    self.speak("Please specify a song or video name")

            except Exception as e:
                logging.error(f"YouTube playback error: {e}")
                self.speak("Sorry, couldn't play the requested media")

        else:
            # Default to Gemini for other queries
            try:
                response = self.model.generate_content(query)
                self.speak(response.text)
            except Exception as e:
                logging.error(f"Gemini error: {e}")
                self.speak("I'm having trouble processing your request")

    def run(self):
        """Main assistant loop"""
        self.speak("Hello! I'm Sage your personalized AI assistant. How can I help you?")

        while True:
            query = self.get_text_input()

            # Exit conditions
            if not query or query.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                self.speak("Goodbye!")
                break

            # Process the command
            self.process_command(query)


def main():
    assistant = VoiceAssistant()
    assistant.run()


if __name__ == "__main__":
    main()