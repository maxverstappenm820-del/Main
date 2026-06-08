# Digital Clock Program
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize attributes before calling initUI
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

        # Connect and start timer
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Show the time immediately without waiting for first tick
        self.update_time()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 320, 150)

        # Center the window on screen
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        # Load custom font; fall back to Arial if file is missing
        font_id = QFontDatabase.addApplicationFont("DG.TTF")
        families = QFontDatabase.applicationFontFamilies(font_id)
        font_family = families[0] if families else "Arial"
        clock_font = QFont(font_family, 36)

        # Configure the time label
        self.time_label.setFont(clock_font)
        self.time_label.setAlignment(Qt.AlignCenter)
        # Fixed stylesheet: removed invalid '°' from hsl color
        self.time_label.setStyleSheet(
            "color: hsl(135, 77%, 55%);"   # bright green — visible on black
            "font-size: 36px;"
            "font-weight: bold;"
            "letter-spacing: 4px;"
        )

        # Layout: central widget holds a VBox with the label
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout(central_widget)   # set layout on the widget, not the window
        vbox.addWidget(self.time_label)
        vbox.setContentsMargins(20, 20, 20, 20)

        # Window background
        self.setStyleSheet("background-color: #0a0a0a;")

    def update_time(self):
        # "AP" gives "AM"/"PM"; "hh" gives 12-hour format with leading zero
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())