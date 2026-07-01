from ai.brain import JarvisBrain
from voice.speech import Listener
from voice.tts import Speaker


def main():

    print("=" * 50)
    print("🤖 JARVIS OS")
    print("=" * 50)

    brain = JarvisBrain()
    listener = Listener()

    Speaker.speak("Jarvis is online. How can I help you?")

    while True:

        try:

            command = listener.listen()

            if not command:
                continue

            command = command.strip()

            # Exit commands
            if command.lower() in [
                "exit",
                "quit",
                "goodbye",
                "bye",
                "shutdown jarvis",
            ]:
                Speaker.speak("Goodbye Aditya. Have a great day!")
                break

            print(f"\n👤 You: {command}")

            print("\n🧠 Thinking...")

            response = brain.process(command)

            print(f"\n🤖 JARVIS: {response}")

            Speaker.speak(response)

        except KeyboardInterrupt:

            Speaker.speak("Goodbye Aditya.")
            break

        except Exception as e:

            print(f"\n❌ Error: {e}")

            Speaker.speak(
                "Sorry, something went wrong."
            )


if __name__ == "__main__":
    main()