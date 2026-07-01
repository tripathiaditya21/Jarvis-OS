from manager.tool_manager import ToolManager
from memory.service import MemoryService
from core.brain import JarvisBrain
from task_manager.task_queue import TaskQueue


class Executor:

    def __init__(self):
        self.manager = ToolManager()
        self.memory = MemoryService()
        self.brain = JarvisBrain()
        self.queue = TaskQueue()

    def execute(self, plan):

        # ---------------------------------
        # Handle multiple actions
        # ---------------------------------

        if isinstance(plan, list):

            # Add every task to the queue
            for step in plan:
                self.queue.add(step)

            results = []

            # Execute sequentially
            while not self.queue.empty():

                task = self.queue.pop()

                result = self.execute(task)

                results.append(result)

            return "\n".join(results)

        # ---------------------------------
        # Single action
        # ---------------------------------

        print("\n========== EXECUTING ==========")
        print(plan)
        print("===============================\n")

        action = plan.get("action")
        params = plan.get("parameters", {})

        # ---------------------------------
        # Remember
        # ---------------------------------

        if action == "remember":

            self.memory.save(
                params["key"],
                params["value"]
            )

            return f"I'll remember that {params['key']} is {params['value']}."

        # ---------------------------------
        # Recall
        # ---------------------------------

        if action == "recall":

            value = self.memory.get(params["key"])

            if value:
                return value

            return "I couldn't find that."

        # ---------------------------------
        # Execute Tool
        # ---------------------------------

        response = self.manager.execute(
            action,
            params
        )

        if not response.startswith("Unknown tool"):
            return response

        # ---------------------------------
        # AI Conversation
        # ---------------------------------

        return self.brain.ask(
            params.get(
                "message",
                plan.get("original_command", "")
            )
        )