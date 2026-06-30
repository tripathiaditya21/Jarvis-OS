import subprocess


class Speaker:

    @staticmethod
    def speak(text: str):

        print(f"\n🤖 JARVIS: {text}")

        subprocess.run(
            [
                "say",
                "-v",
                "Samantha",
                text,
            ]
        )