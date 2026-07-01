import re

from executor.executor import Executor
from core.brain import JarvisBrain as ChatBrain
from ai.context import ConversationContext


class JarvisBrain:

    def __init__(self):
        self.executor = Executor()
        self.chat = ChatBrain()
        self.context = ConversationContext()

    def process(self, command: str):

        # ----------------------------
        # Store user message
        # ----------------------------
        self.context.add("user", command)

        text = command.lower().strip()

        # ----------------------------
        # Exit Commands
        # ----------------------------
        if text in [
            "bye",
            "goodbye",
            "exit",
            "quit",
            "shutdown jarvis",
        ]:
            response = "Goodbye Aditya. Have a great day!"
            self.context.add("jarvis", response)
            return response

        # ----------------------------
        # Open Applications
        # ----------------------------
        if any(word in text for word in [
            "open",
            "launch",
            "start",
            "khol",
            "kholo",
        ]):

            app = re.sub(
                r"(?i)(open|launch|start|kholo|khol|please)",
                "",
                command,
            ).strip()

            plan = {
                "action": "open_app",
                "parameters": {
                    "app": app
                }
            }

            response = self.executor.execute(plan)

            self.context.last_app = app
            self.context.add("jarvis", response)

            return response

        # ----------------------------
        # Google Search
        # ----------------------------
        if "search" in text or "google" in text:

            query = re.sub(
                r"(?i)(search|google|for)",
                "",
                command,
            ).strip()

            plan = {
                "action": "browser",
                "parameters": {
                    "action": "google_search",
                    "query": query
                }
            }

            response = self.executor.execute(plan)

            self.context.last_query = query
            self.context.add("jarvis", response)

            return response

        # ----------------------------
        # YouTube Search
        # ----------------------------
        if "youtube" in text:

            query = re.sub(
                r"(?i)(youtube|search)",
                "",
                command,
            ).strip()

            plan = {
                "action": "browser",
                "parameters": {
                    "action": "youtube_search",
                    "query": query
                }
            }

            response = self.executor.execute(plan)

            self.context.last_query = query
            self.context.add("jarvis", response)

            return response

        # ----------------------------
        # Remember
        # ----------------------------
        if text.startswith("remember"):

            sentence = re.sub(
                r"(?i)remember",
                "",
                command,
            ).strip()

            if " is " in sentence:

                key, value = sentence.split(" is ", 1)

                plan = {
                    "action": "remember",
                    "parameters": {
                        "key": key.strip(),
                        "value": value.strip()
                    }
                }

                response = self.executor.execute(plan)

                self.context.add("jarvis", response)

                return response

        # ----------------------------
        # Recall
        # ----------------------------
        if text.startswith("what is"):

            key = re.sub(
                r"(?i)what is",
                "",
                command,
            ).replace("?", "").strip()

            plan = {
                "action": "recall",
                "parameters": {
                    "key": key
                }
            }

            response = self.executor.execute(plan)

            self.context.add("jarvis", response)

            return response

        # ----------------------------
        # Follow-up Commands
        # ----------------------------
        if text.startswith("search") and self.context.last_app:

            plan = {
                "action": "browser",
                "parameters": {
                    "action": "google_search",
                    "query": command.replace("search", "").strip()
                }
            }

            response = self.executor.execute(plan)

            self.context.add("jarvis", response)

            return response

        # ----------------------------
        # Normal Conversation
        # ----------------------------
        response = self.chat.ask(command)

        self.context.add("jarvis", response)

        return response