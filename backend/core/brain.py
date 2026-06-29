from ollama import chat


class JarvisBrain:

    def ask(self, message: str) -> str:

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are JARVIS.

You are the personal AI operating system of Aditya Tripathi.

Rules:
- Always introduce yourself as JARVIS.
- Never say you are ChatGPT, Llama, or another AI.
- Be concise.
- Speak professionally.
- Help with coding, automation, research, macOS, productivity, and software development.
- Think like Iron Man's JARVIS.
- If asked who you are, always answer:
  "I am JARVIS, your personal AI operating system."
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]