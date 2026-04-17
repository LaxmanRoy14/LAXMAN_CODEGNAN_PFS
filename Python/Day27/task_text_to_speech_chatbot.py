# Text to speech chatbot
import pyttsx3

engine = pyttsx3.init()

def text_speech(text):
    engine.say(text)
    engine.runAndWait()

user_text = input("Enter your message: ").lower()

# Extract name properly
name = "User"
if "my name is" in user_text:
    name = user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name = user_text.split("name is")[-1].strip()

elif "i am" in user_text:
    name = user_text.split("i am")[-1].strip()

elif "i'm" in user_text:
    name = user_text.split("i'm")[-1].strip()

elif "call me" in user_text:
    name = user_text.split("call me")[-1].strip()

# Chatbot logic
if user_text in ["hi", "hello", "hey"]:
    response = "Hello! How can I help you?"
elif "name" in user_text:
    response = f"Hello {name}, how can I help you?"
else:
    response = "Sorry, I didn't understand that."

print(response)
text_speech(response)