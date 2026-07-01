import subprocess
from pathlib import Path
import shutil


class FileTool:

    @staticmethod
    def execute(parameters):

        action = parameters.get("action")

        # --------------------------
        # Open Folder
        # --------------------------

        if action == "open_folder":

            folder = parameters.get("path")

            folder = str(Path(folder).expanduser())

            subprocess.run(["open", folder])

            return f"Opening {folder}"

        # --------------------------
        # Create Folder
        # --------------------------

        if action == "create_folder":

            folder = Path(parameters.get("path")).expanduser()

            folder.mkdir(parents=True, exist_ok=True)

            return f"Created folder {folder.name}"

        # --------------------------
        # Delete File
        # --------------------------

        if action == "delete_file":

            file = Path(parameters.get("path")).expanduser()

            if file.exists():

                file.unlink()

                return f"Deleted {file.name}"

            return "File not found."

        # --------------------------
        # Move File
        # --------------------------

        if action == "move_file":

            src = Path(parameters.get("source")).expanduser()
            dst = Path(parameters.get("destination")).expanduser()

            shutil.move(str(src), str(dst))

            return "File moved."

        return "Unknown file action."