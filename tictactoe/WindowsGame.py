import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QStatusBar, QVBoxLayout


class WindowsGame:
    def __init__(self):
        self.player = 'X'
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(300, 300, 300, 300)
        self.window.setWindowTitle("Tic Tac Toe")
        self.buttons = []
        layout = QVBoxLayout()
        self.play_again_btn = QPushButton("Play Again")
        self.play_again_btn.clicked.connect(self.reset)
        self.play_again_btn.setEnabled(False)
        self.button_widget = QWidget()
        layout.addWidget(self.button_widget)
        layout.addWidget(self.play_again_btn)
        self.status_bar = QStatusBar()
        self.create_grid()
        self.create_status()
        central =QWidget()
        central.setLayout(layout)
        self.window.setCentralWidget(central)

    def reset(self):
        self.player = 'X'
        self.status_bar.showMessage(self.player + " plays")
        self.play_again_btn.setEnabled(False)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText('-')
                self.buttons[row][col].setEnabled(True)
                self.buttons[row][col].setStyleSheet("background-color: lightgray; font-size: 25px")

    def start(self):
        self.window.show()
        sys.exit(self.app.exec())

    def create_grid(self):
        layout = QGridLayout()
        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton("-")
                btn.setFixedWidth(150)
                btn.setFixedHeight(150)
                btn.setStyleSheet("font-size: 25px")
                btn.clicked.connect(lambda state, b=btn:  self.button_pressed(b))
                row_buttons.append(btn)
                layout.addWidget(btn, row, col, 1, 1)
            self.buttons.append(row_buttons)
        self.button_widget.setLayout(layout)


    def create_status(self):
        self.window.setStatusBar(self.status_bar)
        self.status_bar.showMessage("X plays")

    def button_pressed(self, btn):
        btn.setText(self.player)
        btn.setEnabled(False)
        btn.setStyleSheet("background-color: red; font-size: 25px")
        self.player = 'X' if self.player == 'O' else 'O'
        self.status_bar.showMessage(self.player + " plays")
        win = self.winner()
        if win is not None:
            self.play_again_btn.setEnabled(True)
            self.status_bar.showMessage(win + " WINS!!!!!")
            for row in range(3):
                for col in range(3):
                    self.buttons[row][col].setEnabled(False)
        else:
            if self.tie():
                self.play_again_btn.setEnabled(True)
                self.status_bar.showMessage("IT'S A TIE!!!!!")

    def tie(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col].text() == '-':
                    return False
        return True

    def winner(self):
        for i in range(3):
            if self.buttons[i][0].text() != '-':
                if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text():
                    return self.buttons[i][0].text()
            if self.buttons[0][i].text() != '-':
                if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text():
                    return self.buttons[0][i].text()
        if self.buttons[1][1].text() != '-':
            if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text():
                return self.buttons[1][1].text()
            if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text():
                return self.buttons[1][1].text()



if __name__ == '__main__':
    game = WindowsGame()
    game.start()