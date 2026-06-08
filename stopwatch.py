# python PyQt5 stopwatch.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QListWidget
)
from PyQt5.QtCore import QTimer, QElapsedTimer, Qt


class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 320, 420)
        self._center_window()

     
        self.elapsed_seconds = 0  
        self.lap_count = 0

        
        self.elapsed_timer = QElapsedTimer()
        self.base_ms = 0           


        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self._update_display)

       
        self.time_label = QLabel("00:00:00", self)
        self.time_label.setAlignment(Qt.AlignCenter)
    
        self.time_label.setStyleSheet(
            "font-size: 48px; font-weight: bold; color: #2c3e50;"
            "letter-spacing: 4px;"
        )

        self.start_button = QPushButton("▶  Start")
        self.stop_button  = QPushButton("⏸  Stop")
        self.reset_button = QPushButton("↺  Reset")
        self.lap_button   = QPushButton("⚑  Lap")

        self.start_button.setStyleSheet("background-color: #27ae60; color: white; font-size: 14px; padding: 8px; border-radius: 6px;")
        self.stop_button.setStyleSheet( "background-color: #e74c3c; color: white; font-size: 14px; padding: 8px; border-radius: 6px;")
        self.reset_button.setStyleSheet("background-color: #95a5a6; color: white; font-size: 14px; padding: 8px; border-radius: 6px;")
        self.lap_button.setStyleSheet(  "background-color: #2980b9; color: white; font-size: 14px; padding: 8px; border-radius: 6px;")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.lap_button.clicked.connect(self.lap)

        
        self.lap_list = QListWidget()
        self.lap_list.setStyleSheet("font-size: 13px;")
        self.lap_list.setFixedHeight(160)

     
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(8)
        for btn in (self.start_button, self.stop_button, self.reset_button, self.lap_button):
            btn_layout.addWidget(btn)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)
        main_layout.addWidget(self.time_label)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(QLabel("Laps:"))
        main_layout.addWidget(self.lap_list)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self._set_button_states(running=False)



    def start(self):
        if not self.timer.isActive():
            self.elapsed_timer.start()      
            self.timer.start()
            self._set_button_states(running=True)

    def stop(self):
        if self.timer.isActive():
        
            self.base_ms += self.elapsed_timer.elapsed()
            self.timer.stop()
            self._set_button_states(running=False)

    def reset(self):
        self.timer.stop()
        self.base_ms = 0
        self.elapsed_seconds = 0
        self.lap_count = 0
        self.time_label.setText("00:00:00")
        self.lap_list.clear()
        self._set_button_states(running=False)

    def lap(self):
        if self.timer.isActive():
            self.lap_count += 1
            current = self.time_label.text()
            self.lap_list.addItem(f"Lap {self.lap_count:>3}:  {current}")
            self.lap_list.scrollToBottom()


    def _update_display(self):
        total_ms = self.base_ms + self.elapsed_timer.elapsed()
        total_secs = total_ms // 1000

        if total_secs != self.elapsed_seconds:
            self.elapsed_seconds = total_secs
            h =  total_secs // 3600
            m = (total_secs % 3600) // 60
            s =  total_secs % 60
            self.time_label.setText(f"{h:02}:{m:02}:{s:02}")

    def _set_button_states(self, running: bool):
        self.start_button.setEnabled(not running)
        self.stop_button.setEnabled(running)
        self.lap_button.setEnabled(running)

    def _center_window(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width()  - self.width())  // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())