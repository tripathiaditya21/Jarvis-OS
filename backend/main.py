from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.brain import JarvisBrain

from memory.database import Base, engine
from memory.memory import Memory  # Registers SQLAlchemy model
from memory.service import MemoryService

from automation.mac import MacAutomation

from brain.planner import Planner
from executor.executor import Executor

# ----------------------------------------------------
# Database
# ----------------------------------------------------

Base.metadata.create_all(bind=engine)

# ----------------------------------------------------
# FastAPI
# ----------------------------------------------------

app = FastAPI(
    title="JARVIS OS API",
    version="0.6.0",
    description="Personal AI Operating System",
)

# ----------------------------------------------------
# CORS
# ----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# Services
# ----------------------------------------------------

brain = JarvisBrain()
memory = MemoryService()
automation = MacAutomation()

planner = Planner()
executor = Executor()

# ----------------------------------------------------
# Models
# ----------------------------------------------------

class CommandRequest(BaseModel):
    command: str

# ----------------------------------------------------
# Routes
# ----------------------------------------------------

@app.get("/")
def home():
    return {
        "status": "online",
        "assistant": "JARVIS",
        "version": "0.6.0",
    }


@app.get("/chat")
def chat(message: str):
    return {
        "reply": brain.ask(message)
    }


@app.get("/remember")
def remember(key: str, value: str):
    memory.save(key, value)

    return {
        "status": "saved",
        "key": key,
        "value": value,
    }


@app.get("/recall")
def recall(key: str):
    return {
        "key": key,
        "value": memory.get(key),
    }


@app.get("/open")
def open_app(app: str):
    return {
        "message": automation.open_app(app)
    }


@app.post("/execute")
def execute(request: CommandRequest):
    try:
        # Step 1: Create AI plan
        plan = planner.create_plan(request.command)

        # Step 2: Execute plan
        response = executor.execute(plan)

        return {
            "success": True,
            "plan": plan,
            "response": response,
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }