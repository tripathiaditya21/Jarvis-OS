from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from services.backend import BackendService


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.backend = BackendService()

        self.setWindowTitle("JARVIS OS")
        self.resize(700, 650)

        self.setStyleSheet("""
            QMainWindow{
                background:#111827;
            }

            QLabel{
                color:white;
            }

            QTextEdit{
                background:#1f2937;
                color:white;
                border-radius:12px;
                padding:10px;
                font-size:14px;
            }

            QPushButton{
                background:#2563eb;
                color:white;
                border:none;
                border-radius:18px;
                padding:15px;
                font-size:16px;
            }

            QPushButton:hover{
                background:#3b82f6;
            }
        """)

        widget = QWidget()
        layout = QVBoxLayout(widget)

        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("🤖 JARVIS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Helvetica", 26))

        layout.addWidget(title)

        self.status = QLabel("Ready to Assist")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setFont(QFont("Helvetica", 13))

        layout.addWidget(self.status)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.chat.append(
            "🤖 Hello Aditya!\n\nWelcome to JARVIS OS.\n\nHow can I help you today?"
        )

        layout.addWidget(self.chat)

        self.button = QPushButton("🎤 Talk to JARVIS")

        self.button.clicked.connect(self.listen)

        layout.addWidget(self.button)

        self.setCentralWidget(widget)

    def listen(self):

        self.status.setText("🎤 Listening...")
        self.button.setEnabled(False)

        self.repaint()

        try:

            command, response = self.backend.listen_and_process()

            # Nothing heard
            if not command:
                self.chat.append("\n🤖 I didn't hear anything.")
                return

            # Show user message
            self.chat.append(f"\n👤 You: {command}")

            # Exit commands
            exit_commands = [
                "bye",
                "goodbye",
                "exit",
                "quit",
                "close jarvis",
                "shutdown jarvis",
                "stop jarvis",
                "good night",
                "band ho jao",
                "बंद हो जाओ",
            ]

            if command.lower().strip() in exit_commands:

                self.chat.append("\n🤖 Goodbye Aditya! 👋")

                self.status.setText("Shutting down...")

                self.repaint()

                self.close()

                return

            # Show assistant response
            self.chat.append(f"\n🤖 JARVIS: {response}")

        except Exception as e:

            self.chat.append(f"\n❌ Error: {e}")

        finally:

            self.status.setText("Ready")

            self.button.setEnabled(True)