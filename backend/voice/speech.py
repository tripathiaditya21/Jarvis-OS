import tempfile
import warnings

import numpy as np
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


class Listener:

    def __init__(self):

        print("Loading Whisper...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8",
        )

        print("✅ Whisper Ready!")

    def listen(self):

        samplerate = 16000
        duration = 6

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype="float32",
        )

        sd.wait()

        # Clean the audio
        recording = np.nan_to_num(recording)
        recording = np.clip(recording, -1.0, 1.0)

        # Ignore harmless runtime warnings
        warnings.filterwarnings("ignore")

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ) as temp_file:

            sf.write(
                temp_file.name,
                recording,
                samplerate,
            )

            segments, _ = self.model.transcribe(
                temp_file.name,
                beam_size=5,
                language=None,          # Auto-detect language
                vad_filter=True,        # Ignore silence
            )

        text = "".join(segment.text for segment in segments).strip()

        if not text:
            return ""

        print(f"👤 You: {text}")

        return text