import sys
import os
from math import floor

from PyQt5.QtWidgets import QMainWindow ,QWidget, QApplication
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QCursor

Form = uic.loadUiType(os.path.join(os.getcwd(), "gui-main.ui"))[0]

class App(QMainWindow, QWidget, Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.progressBar.hide()
        # self.btnStart.clicked.connect(self.start)
        self.btnSetTimer.clicked.connect(self.set)

        # self.btnResume.clicked.connect(self.resume)
        self.btnResume.hide()

        # self.btnPause.clicked.connect(self.pause)
        self.btnPause.hide()

        self.timer = QBasicTimer()
        self.step = 0
        self.totalTime = 100

        self.lcd.hide()

    def set(self):
        textboxValue = int(self.textbox.text())
        self.totalTime = textboxValue * 10
        return




if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = App()
    demo.show()

    sys.exit(app.exec_())