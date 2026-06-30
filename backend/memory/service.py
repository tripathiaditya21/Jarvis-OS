from sqlalchemy.orm import Session

from memory.database import SessionLocal
from memory.memory import Memory


class MemoryService:

    def save(self, key: str, value: str):
        db: Session = SessionLocal()

        try:
            memory = db.query(Memory).filter(Memory.key == key).first()

            if memory:
                memory.value = value
            else:
                memory = Memory(key=key, value=value)
                db.add(memory)

            db.commit()

        finally:
            db.close()

    def get(self, key: str):
        db: Session = SessionLocal()

        try:
            memory = db.query(Memory).filter(Memory.key == key).first()

            if memory:
                return memory.value

            return None

        finally:
            db.close()