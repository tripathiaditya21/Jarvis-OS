from wakeword.detector import WakeWordDetector

detector = WakeWordDetector()

detector.wait()

print("Wake word detected!")