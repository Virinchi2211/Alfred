import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"🤖 Alfred: {text}")
    engine.say(text)
    engine.runAndWait()
3