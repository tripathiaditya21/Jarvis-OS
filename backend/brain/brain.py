from brain.planner import Planner
from executor.executor import Executor


class JarvisBrain:

    def __init__(self):

        self.planner = Planner()
        self.executor = Executor()

    def process(self, command: str):

        plan = self.planner.create_plan(command)

        print("\n========== PLAN ==========")
        print(plan)
        print("==========================\n")

        response = self.executor.execute(plan)

        return response