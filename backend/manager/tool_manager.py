from tools.registry import ToolRegistry


class ToolManager:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, action, parameters):

        tool = self.registry.get(action)

        if tool:
            return tool.execute(parameters)

        return f"Unknown tool: {action}"

    def available_tools(self):

        return self.registry.list_tools()