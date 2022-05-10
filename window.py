from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys


def button_clicked():
    print("Button is clicked")

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()
button = QPushButton("Click me")
button.setToolTip("Click this button")
button.clicked.connect(button_clicked)
layout.addWidget(button)
window.setLayout(layout)
window.show()

app.exec()