from tools.apps import AppTool
from memory.service import MemoryService
from core.brain import JarvisBrain


class Executor:

    def __init__(self):
        self.memory = MemoryService()
        self.brain = JarvisBrain()

    def execute(self, plan):

        action = plan.get("action")
        params = plan.get("parameters", {})

        if action == "open_app":
            return AppTool.open(params.get("app"))

        if action == "remember":

            self.memory.save(
                params.get("key"),
                params.get("value"),
            )

            return "Done."

        if action == "recall":

            value = self.memory.get(
                params.get("key")
            )

            if value:
                return value

            return "I couldn't find that."

        # Everything else becomes conversation
        return self.brain.ask(
            plan.get(
                "original_command",
                params.get("message", "")
            )
        )