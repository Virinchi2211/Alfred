# 🎩 Alfred — Your Personal AI Butler

> *"At your service, Sir."*

Alfred is a locally-run voice assistant powered by a large language model (LLM), built with a distinct personality — witty, intelligent, loyal, and just a little sarcastic. Inspired by the AI assistants in science fiction, Alfred listens to your voice, thinks with a local LLM, and responds in a British accent.

No cloud AI costs. No data sent to OpenAI. Runs entirely on your machine.

---

## 🧠 How It Works

```
You speak → Speech-to-Text → Local LLM (Mistral via Ollama) → Text-to-Speech → Alfred responds
```

1. Alfred listens via your microphone
2. Your speech is transcribed using Google Speech Recognition
3. The transcribed text is sent to a locally running **Mistral** model via **Ollama**
4. Alfred's personality is injected as a system prompt — he's always "Sir"-ing you
5. The response is spoken back in a British English voice using `pyttsx3`

---

## ✅ What's Working

- 🎤 **Voice input** — real-time microphone listening with timeout handling
- 🧠 **Local LLM brain** — powered by Mistral running via Ollama (fully offline)
- 🔊 **Voice output** — British English text-to-speech
- 🎭 **Alfred's personality** — consistent butler persona across all interactions
- 🔁 **Continuous conversation loop** — keeps listening until you say "exit" or "shutdown"
- 🏗️ **Modular architecture** — clean separation of speech, brain, and task logic

---

## 🚧 In Progress

- `task_mapper.py` — Planned module for task-specific actions (open apps, set reminders, web search, system controls)
- Wake word detection — Trigger Alfred without pressing anything
- Conversation memory — Multi-turn context across the session

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Speech-to-Text | `SpeechRecognition` + Google API |
| LLM Backend | Ollama + Mistral (local) |
| Text-to-Speech | `pyttsx3` (British voice) |
| Audio I/O | `pyaudio` |
| Language | Python 3 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai) installed and running
- Mistral model pulled via Ollama

```bash
ollama pull mistral
```

### Installation

```bash
git clone https://github.com/Virinchi2211/Alfred.git
cd Alfred
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
# Add any API keys or config here if needed
```

### Run Alfred

```bash
python main.py
```

Alfred will greet you and start listening. Say **"exit"** or **"shutdown"** to end the session.

---

## 📁 Project Structure

```
Alfred/
├── main.py              # Entry point — conversation loop
├── requirements.txt     
├── .env                 
├── data/                # Data assets
├── scripts/             # Utility scripts
└── modules/
    ├── speech_to_text.py   # Microphone input + transcription
    ├── text_to_speech.py   # British voice output
    ├── gpt_brain.py        # LLM integration (Ollama/Mistral)
    └── task_mapper.py      # Task routing (in progress)
```

---

## 💡 Why Local LLM?

Most voice assistants send your data to cloud APIs. Alfred uses **Ollama** to run Mistral entirely on your machine — meaning:
- No API costs
- No data leaves your device
- Works offline

---

## 🔮 Roadmap

- [ ] Wake word detection ("Hey Alfred")
- [ ] Task mapper — open apps, search web, set timers
- [ ] Conversation memory across turns
- [ ] GUI interface
- [ ] Swap models easily (Llama 3, Gemma, etc.)

---

*Built with Python · Ollama · Mistral · pyttsx3 · SpeechRecognition*
