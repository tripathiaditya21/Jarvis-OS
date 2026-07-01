import subprocess

from tools.app_registry import APP_ALIASES


class AppTool:

    @staticmethod
    def execute(parameters):

        app = parameters.get("app", "").strip()

        if not app:
            return "No application specified."

        # Convert to lowercase
        lookup = app.lower()

        # Resolve alias
        app_name = APP_ALIASES.get(lookup, app)

        # 👇 ADD THESE TWO LINES HERE
        print("Planner app:", app)
        print("Resolved app:", app_name)

        try:
            subprocess.run(
                ["open", "-a", app_name],
                check=True,
            )

            return f"Opening {app_name}."

        except subprocess.CalledProcessError:
            return f"'{app_name}' is not installed."

        except Exception as e:
            return f"Error opening '{app_name}': {e}"