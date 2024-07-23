import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import datetime
import subprocess

class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")

        self.label = tk.Label(root, text="Jarvis AI Assistant", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.text_box = tk.Text(root, height=10, width=50)
        self.text_box.pack(pady=10)

        self.button_listen = tk.Button(root, text="Listen", command=self.listen_command)
        self.button_listen.pack(pady=5)

        self.button_exit = tk.Button(root, text="Exit", command=self.exit_app)
        self.button_exit.pack(pady=5)

        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_command(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, "Listening...")
            self.root.update()
            audio = self.recognizer.listen(source)

            try:
                query = self.recognizer.recognize_google(audio)
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, "You said: " + query)
                self.process_query(query.lower())
            except sr.UnknownValueError:
                messagebox.showinfo("Error", "Sorry, I didn't get that.")
            except sr.RequestError as e:
                messagebox.showinfo("Error", f"Could not request results; {e}")

    def process_query(self, query):
        if "wikipedia" in query:
            search_query = query.replace("wikipedia", "").strip()
            self.search_wikipedia(search_query)
        elif "open website" in query:
            website = query.replace("open website", "").strip()
            self.open_website(website)
        elif "execute command" in query:
            command = query.replace("execute command", "").strip()
            self.execute_command(command)

    def search_wikipedia(self, query):
        try:
            result = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia")
            self.speak(result)
        except wikipedia.exceptions.DisambiguationError:
            messagebox.showinfo("Error", "There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            messagebox.showinfo("Error", "Sorry, I couldn't find any information on that topic.")

    def open_website(self, website):
        webbrowser.open(website)

    def execute_command(self, command):
        try:
            subprocess.Popen(command.split(), shell=True)
            self.speak("Executing command.")
        except Exception:
            messagebox.showinfo("Error", "Sorry, I couldn't execute the command.")

    def exit_app(self):
        self.speak("Goodbye!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()
