from modules.speech_to_text import listen_to_audio
from modules.text_to_speech import speak
from modules.gpt_brain import get_response

def main():
    speak("Hello, I am Alfred. Ready when you are.")

    while True:
        command = listen_to_audio()
        if command:
            if "exit" in command.lower() or "shutdown" in command.lower():
                speak("Shutting down. Goodbye, Sir.")
                break

            reply = get_response(command)
            speak(reply)

if __name__ == "__main__":
    main()
