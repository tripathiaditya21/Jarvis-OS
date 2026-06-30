import subprocess


class AppTool:

    @staticmethod
    def open(app_name: str) -> str:
        try:
            subprocess.run(
                ["open", "-a", app_name],
                check=True
            )

            return f"Opening {app_name}."

        except Exception:
            return f"I couldn't open {app_name}."