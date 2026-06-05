# Cecil's Surveillance Terminal — A PyQt5 Satirical App
# Theme: Cecil Stedman from "Invincible" being perpetually paranoid
# Run: pip install PyQt5 pyttsx3

import sys
import pyttsx3                          # Offline text-to-speech
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QTextEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


# Cecil's surveillance "intel" — one per button click
INTEL = [
    "I've had a contingency for YOU since day one.",
    "Don't act surprised. I know what you Googled this morning.",
    "Omni-Man turned. Invincible could turn. YOU could turn.",
    "I bugged your fridge. The cheese confirmed my suspicions.",
    "Every hero is a threat. Some just haven't proven it yet.",
    "I'm not the bad guy. I'm the guy who stops the bad guys... badly.",
]
intel_index = [0]                       # Mutable counter for closures


class CecilApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tts = pyttsx3.init()       # Init text-to-speech engine
        self.tts.setProperty("rate", 155)   # Slow, menacing pace
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("GDA Classified Terminal — EYES ONLY")
        self.setFixedSize(480, 340)
        self.setStyleSheet(
            "background:#0d0d0d; color:#00ff88;"
            "font-family:Courier New; font-size:13px;"
        )

        layout = QVBoxLayout()
        layout.setSpacing(12)
        layout.setContentsMargins(24, 20, 24, 20)

        # Header label
        title = QLabel("☎  CECIL STEDMAN — GLOBAL DEFENSE AGENCY")
        title.setFont(QFont("Courier New", 11, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color:#ff4444; padding-bottom:4px;")
        layout.addWidget(title)

        # Intel display box
        self.intel_box = QTextEdit()
        self.intel_box.setReadOnly(True)
        self.intel_box.setText("[ AWAITING AUTHORIZATION... ]")
        self.intel_box.setStyleSheet(
            "background:#111; border:1px solid #00ff88;"
            "color:#00ff88; padding:8px;"
        )
        layout.addWidget(self.intel_box)

        # Button: receive Cecil's latest paranoid briefing
        brief_btn = QPushButton("▶  RECEIVE BRIEFING")
        brief_btn.clicked.connect(self.deliver_briefing)
        brief_btn.setStyleSheet(self._btn_style("#00ff88"))
        layout.addWidget(brief_btn)

        # Button: Cecil speaks aloud (TTS)
        speak_btn = QPushButton("🔊  PLAY AUDIO INTERCEPT")
        speak_btn.clicked.connect(self.speak_intel)
        speak_btn.setStyleSheet(self._btn_style("#ff4444"))
        layout.addWidget(speak_btn)

        self.setLayout(layout)

    def deliver_briefing(self):
        """Cycle through Cecil's paranoid intelligence reports."""
        line = INTEL[intel_index[0] % len(INTEL)]
        self.intel_box.setText(f"INTEL #{intel_index[0]+1}:\n\n  \"{line}\"")
        intel_index[0] += 1

    def speak_intel(self):
        """Make Cecil read the current intel aloud via TTS."""
        raw = self.intel_box.toPlainText()
        if "AWAITING" in raw:
            self.tts.say("Click the briefing button first. Amateur.")
        else:
            # Extract just the quote
            text = raw.split('"')[1] if '"' in raw else raw
            self.tts.say(text)
        self.tts.runAndWait()           # Blocking — keeps it simple

    def _btn_style(self, color):
        return (
            f"QPushButton {{background:#1a1a1a; color:{color};"
            f"border:1px solid {color}; padding:8px; font-size:13px;}}"
            f"QPushButton:hover {{background:{color}; color:#000;}}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CecilApp()
    window.show()
    sys.exit(app.exec_())