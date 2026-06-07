import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import ( QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
                             , QVBoxLayout, QHBoxLayout, QPushButton,
                              QLineEdit, QComboBox, QCheckBox,QGridLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Max Verstappen Fan App")
        self.setGeometry(100, 100, 400, 350)

        # Image label (shows verstappen.jpeg if it exists, otherwise shows text)
        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 16))
        self.label.setGeometry(0, 0, 300, 200)

        pixmap = QPixmap("verstappen.jpeg")
        if not pixmap.isNull():
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
        else:
            self.label.setText("I love Max Verstappen")
            self.label.setAlignment(Qt.AlignCenter)

        # Center the label in the window
        self.label.setGeometry(
            self.width() // 2 - 150,
            self.height() // 2 - 150,
            300,
            150
        )

        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me", self)
        self.button.setGeometry(150, 290, 100, 40)
        self.button.setStyleSheet("background-color: lightblue; border: 3px solid black;")
        self.button.clicked.connect(self.on_button_click)
        # Button is now enabled so it can be clicked
        self.button.setDisabled(False)

        self.label.setStyleSheet("color: red; font-size: 18px; font-weight: bold;")

    def on_button_click(self):
        QMessageBox.information(self, "Button Clicked", "You clicked the button!")

        # Update button appearance
        self.button.setStyleSheet("background-color: lightgreen; border: 3px solid green;")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)

        # Replace central area with a grid of 6 colored labels
        center_widget = QWidget()
        self.setCentralWidget(center_widget)

        label1 = QLabel("1")
        label2 = QLabel("2")
        label3 = QLabel("3")
        label4 = QLabel("4")
        label5 = QLabel("5")
        label6 = QLabel("6")

        for lbl in [label1, label2, label3, label4, label5, label6]:
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setFont(QFont("Arial", 18, QFont.Bold))
            lbl.setMinimumHeight(80)

        label1.setStyleSheet("background-color: lightblue;   border: 1px solid black;")
        label2.setStyleSheet("background-color: lightgreen;  border: 1px solid green;")
        label3.setStyleSheet("background-color: lightyellow; border: 1px solid goldenrod;")
        label4.setStyleSheet("background-color: lightcoral;  border: 1px solid coral;")
        label5.setStyleSheet("background-color: lightgray;   border: 1px solid gray;")
        label6.setStyleSheet("background-color: lightpink;   border: 1px solid pink;")

        grid = QGridLayout()
        grid.setSpacing(6)
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 0)
        grid.addWidget(label6, 2, 1)

        center_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()