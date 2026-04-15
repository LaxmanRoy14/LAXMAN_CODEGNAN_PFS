#Text to speech
import pyttsx3 as engine

def text_speech(text):
    engine.say(text)
    engine.runAndwait()
text_speech("Hello, I am your assistant")
