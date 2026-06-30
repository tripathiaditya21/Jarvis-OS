import subprocess


class MacAutomation:

    def open_app(self, app_name: str):
        subprocess.run(
            ["open", "-a", app_name],
            check=False
        )

        return f"Opening {app_name}."