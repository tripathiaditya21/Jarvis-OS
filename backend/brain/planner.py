import json
import re

from ollama import chat
from planner.system_prompt import SYSTEM_PROMPT


class Planner:

    def create_plan(self, command: str):

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": command,
                },
            ],
        )

        text = response["message"]["content"].strip()

        text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
        text = re.sub(r"```", "", text)

        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            text = match.group(0)

        try:

            plan = json.loads(text)

        except Exception:

            plan = {
                "action": "chat",
                "parameters": {
                    "message": command
                }
            }

        # Always keep original command
        plan["original_command"] = command

        return plan