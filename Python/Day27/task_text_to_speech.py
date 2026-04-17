# Text to speech
import pyttsx3

engine = pyttsx3.init()

def text_speech(text):
    engine.say(text)
    engine.runAndWait()

text_speech("Hello, I am your assistant")
