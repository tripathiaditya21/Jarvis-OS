import tempfile
import sounddevice as sd
import soundfile as sf

from faster_whisper import WhisperModel


class Listener:

    def __init__(self):

        print("Loading Whisper...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper Ready!")

    def listen(self):

        duration = 5
        samplerate = 16000

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32",
        )

        sd.wait()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as f:

            sf.write(
                f.name,
                recording,
                samplerate,
            )

            segments, info = self.model.transcribe(
                f.name,
                beam_size=5,
            )

            text = ""

            for segment in segments:
                text += segment.text

        text = text.strip()

        print(f"👤 You: {text}")

        return text