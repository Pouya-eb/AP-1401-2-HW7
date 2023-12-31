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
        self.btnStart.clicked.connect(self.start)
        self.btnSetTimer.clicked.connect(self.set)

        self.btnResume.clicked.connect(self.resume)
        self.btnResume.hide()

        self.btnPause.clicked.connect(self.pause)
        self.btnPause.hide()

        self.timer = QBasicTimer()
        self.step = 0
        self.totalTime = 100

        self.lcd.hide()

    def set(self):
        textboxValue = int(self.textbox.text())
        self.totalTime = textboxValue * 10
        return

    def start(self):
        self.step = 0
        self.progressBar.setValue(0)
        self.lcd.show()
        self.progressBar.show()
        self.btnResume.show()
        self.btnPause.show()
        self.resume()

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()

    def resume(self):
        self.timer.start(self.totalTime, self)
    
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.progressBar.hide()
            return

        self.step += 1
        self.progressBar.setValue(self.step)
        self.lcd.display(self.step)

    def mousePressEvent(self, event):
        if event.button() == 1:
            
            cursor = QCursor()
            curserPos = cursor.pos()
            curserX = curserPos.x()
            curserY = curserPos.y()

            windowPos =  self.pos()
            windowX = windowPos.x()
            windowY = windowPos.y()

            lcdPos = self.lcd.size()
            lcdX = lcdPos.width()
            lcdY = lcdPos.height()

            realX = curserX - windowX - 30 - floor(lcdX/2)
            realY = curserY - windowY - 30 - floor(lcdY/2)

            conditionX = (0 < realX) and (realX < 401)
            conditionY = (0 < realY) and (realY < 401)

            xMove = floor(realX / 51)
            yMove = floor(realY / 51)

            if(conditionX and conditionY):
                self.start()
                self.lcd.move(xMove * 51, yMove * 51)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = App()
    demo.show()

    sys.exit(app.exec_())