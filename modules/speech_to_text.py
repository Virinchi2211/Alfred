import speech_recognition as sr

def listen_to_audio():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Listening... (say something)")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("🔊 Audio captured, recognizing...")
    except sr.WaitTimeoutError:
        print("⌛ Timeout: No speech detected.")
        return ""

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"⚠️ API error: {e}")
        return ""
