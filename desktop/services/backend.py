import sys
import os

BACKEND_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "backend"
    )
)

if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

from ai.brain import JarvisBrain
from voice.speech import Listener
from voice.tts import Speaker


class BackendService:

    def __init__(self):

        self.listener = Listener()
        self.brain = JarvisBrain()

    def listen_and_process(self):

        command = self.listener.listen()

        if not command:
            return "", "I didn't hear anything."

        response = self.brain.process(command)

        Speaker.speak(response)

        return command, response