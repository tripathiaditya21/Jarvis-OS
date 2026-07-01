import sounddevice as sd
import numpy as np
from openwakeword.model import Model


class WakeWordDetector:

    def __init__(self):

        print("Loading Wake Word model...")

        self.model = Model()

        self.sample_rate = 16000

        print("✅ Wake Word Ready!")

    def wait(self):

        print("\n🎤 Waiting for wake word...")

        while True:

            audio = sd.rec(
                int(0.5 * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype="int16",
            )

            sd.wait()

            audio = np.squeeze(audio)

            prediction = self.model.predict(audio)

            for score in prediction.values():

                if score > 0.5:
                    print("✅ Wake word detected!")
                    return