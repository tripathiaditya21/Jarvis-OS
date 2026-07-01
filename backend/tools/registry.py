from tools.apps import AppTool
from tools.browser import BrowserTool
from tools.files import FileTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "open_app": AppTool(),
            "browser": BrowserTool(),
            "files": FileTool(),
        }

    def get(self, action):

        return self.tools.get(action)

    def list_tools(self):

        return list(self.tools.keys())