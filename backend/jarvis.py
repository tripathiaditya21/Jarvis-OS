from brain.planner import Planner
from executor.executor import Executor

from voice.speech import Listener
from voice.tts import Speaker


planner = Planner()
executor = Executor()

listener = Listener()

Speaker.speak("Jarvis is online.")

while True:

    command = listener.listen()

    if not command:
        continue

    if command.lower() in [
        "exit",
        "quit",
        "stop",
        "goodbye"
    ]:

        Speaker.speak("Goodbye Aditya.")

        break

    try:

        plan = planner.create_plan(command)

        response = executor.execute(plan)

        Speaker.speak(response)

    except Exception as e:

        Speaker.speak("Sorry, something went wrong.")

        print(e)