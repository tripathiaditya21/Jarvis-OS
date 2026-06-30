# 🤖 JARVIS OS

> Your Personal AI Operating System powered by Local LLMs, Voice AI and macOS Automation.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Ollama](https://img.shields.io/badge/Ollama-LLM-orange)
![Whisper](https://img.shields.io/badge/Whisper-Voice-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)

---

## 🚀 Overview

JARVIS OS is a personal AI operating system inspired by Iron Man's JARVIS.

Unlike a traditional chatbot, JARVIS can:

- 🎤 Listen to voice commands
- 🧠 Understand natural language
- 💬 Have conversations
- 🖥️ Control macOS applications
- 🧠 Remember user information
- 🔊 Speak responses
- 🤖 Run completely on your local machine using Ollama

---

# ✨ Features

### 🧠 AI Brain

- Local LLM using Ollama
- Natural language understanding
- Multilingual support (English, Hindi, Hinglish)

---

### 🎤 Voice Assistant

- Whisper Speech-to-Text
- Text-to-Speech
- Continuous voice interaction

---

### 🖥️ macOS Automation

- Open applications
- Launch system tools
- Control desktop workflow

Examples:

- Open Safari
- Open WhatsApp
- Open VS Code
- Open Spotify

---

### 🧠 Memory System

Persistent SQLite memory

Example:

Remember my internship company is Fidelity.

Later...

What is my internship company?

↓

Fidelity

---

### ⚡ FastAPI Backend

REST API

```
GET /
POST /execute
GET /remember
GET /recall
```

---

### 🎨 React Frontend

Modern UI for interacting with JARVIS.

---

# 🏗️ Architecture

```

                🎤 Voice

↓

Whisper STT

↓

Planner (LLM)

↓

Executor

↓

┌──────────────┬───────────────┬───────────────┐

Apps          Memory        Browser

↓

macOS

↓

🔊 Speaker

```

---

# 🛠 Tech Stack

- Python
- FastAPI
- React
- SQLite
- SQLAlchemy
- Ollama
- Whisper
- Faster Whisper
- Speech Recognition
- macOS Automation

---

# 📂 Project Structure

```

Jarvis-OS/

├── backend/
│   ├── automation/
│   ├── brain/
│   ├── executor/
│   ├── memory/
│   ├── planner/
│   ├── tools/
│   ├── voice/
│   └── main.py
│
├── frontend/
│
└── README.md

```

---

# ⚙️ Installation

Clone

```bash
git clone https://github.com/tripathiaditya21/Jarvis-OS.git
```

Backend

```bash
cd Jarvis/backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Run

```bash
python -m uvicorn main:app --reload
```

Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🎤 Example Commands

Open Safari

Open WhatsApp

Open VS Code

Tell me a joke

---

# 🛣 Roadmap

- [x] Local LLM
- [x] Voice Assistant
- [x] Memory
- [x] App Automation
- [ ] Wake Word ("Jarvis")
- [ ] Floating Desktop Assistant
- [ ] Global Shortcut
- [ ] Browser Automation
- [ ] File Assistant
- [ ] Vision AI
- [ ] Calendar Integration
- [ ] Email Assistant

---

# 📸 Demo

Coming Soon

---

# 🤝 Contributing

Contributions are welcome!

---

# 👨‍💻 Author

**Aditya Tripathi**

B.Tech Computer Science Engineering

AI • Machine Learning • Full Stack Development

---

⭐ If you like this project, give it a star!
