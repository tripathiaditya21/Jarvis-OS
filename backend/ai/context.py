class ConversationContext:

    def __init__(self):
        self.last_app = None
        self.last_query = None
        self.history = []

    def add(self, speaker, message):
        self.history.append({
            "speaker": speaker,
            "message": message
        })

        # Keep only last 10 messages
        self.history = self.history[-10:]