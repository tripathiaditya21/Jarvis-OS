from fastapi import FastAPI
from core.brain import JarvisBrain

app = FastAPI()

brain = JarvisBrain()


@app.get("/")
def home():
    return {
        "status": "online",
        "assistant": "JARVIS"
    }


@app.get("/chat")
def chat(message: str):
    return {
        "reply": brain.ask(message)
    }