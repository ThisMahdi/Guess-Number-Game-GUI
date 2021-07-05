# A Simple Code By ThisMahdi | Telegram : @Thisismahdi

# Imports Here
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QMessageBox
from PyQt5 import QtGui
from PyQt5 import uic
import random
import sys


__version__ = '1'
__author__ = 'Mahdi Yaghoubi'

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\page1.ui', self)
        self.enter.clicked.connect(self.page2)
        link = "<a style='text-decoration: none; color:white;' href='https://github.com/ThisMahdi/'>By Mahdi Yaghoubi</a>"
        self.mahdi.setText(link)


    def page2(self):
        global name
        name = self.name.text()
        if name == "":
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Enter Your Name.")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            # showing msg box
            x = msg.exec_()
        else:
            print(f"name entered as {name}")
            page2 = Page2()
            widget.addWidget(page2)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\page2.ui', self)
        self.welcome.setText(f"Welcome {name}")
        self.start.clicked.connect(self.ischecked)

    def ischecked(self):
        if not self.easy.isChecked() and not self.normal.isChecked() and not self.hard.isChecked():
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Select Difficulty First.")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            # showing msg box
            x = msg.exec_()
        else:
            self.page3()

    def page3(self):
        page3 = Page3()
        widget.addWidget(page3)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        if self.easy.isChecked():
            global random_number
            random_number = random.randint(0, 100)
            # print(random_number)
            print("easy selected")
        elif self.normal.isChecked():
            random_number = random.randint(100, 999)
            # print(random_number)
            print("normal selected")
        elif self.hard.isChecked():
            random_number = random.randint(1000, 9999)
            # print(random_number)
            print("hard selected")
        else:
            pass


class Page3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('uis\page3.ui', self)
        self.check.clicked.connect(self.input_number)
        self.onlyint = QIntValidator()
        self.number.setValidator(self.onlyint)


    def input_number(self):
        number = self.number.text()
        if number == "":
            msg = QMessageBox()
            msg.setWindowTitle(" ")
            msg.setText("Please Enter Number First.")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            # showing msg box
            x = msg.exec_()
        else:
            self.random_number()

    def random_number(self):
        number = self.number.text()
        if int(number) < random_number:
            msg = QMessageBox()
            msg.setWindowTitle(":( | Guess < Number")
            msg.setText("""Your GUESS is LOWER than the number!
Try again...""")
            msg.setWindowIcon(QtGui.QIcon("icon\.png"))
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            # showing msg box
            x = msg.exec_()
        elif int(number) > random_number:
            msg = QMessageBox()
            msg.setWindowTitle(":( | Guess > Number")
            msg.setText("""Your GUESS is HIGHER than the number!
Try again...""")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            # showing msg box
            x = msg.exec_()
        elif int(number) == random_number:
            msg = QMessageBox()
            msg.setWindowTitle("=)))))))) | Guess = Number")
            msg.setText("""Congrats!!
You Guess The Number Correctly ;)""")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Close)
            msg.setDefaultButton(QMessageBox.Close)
            # showing msg box
            x = msg.exec_()
            sys.exit()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("WTF?")
            msg.setText("ERROR :| IDK!")
            msg.setWindowIcon(QtGui.QIcon("icon\logo.png"))
            msg.setStandardButtons(QMessageBox.Close)
            msg.setDefaultButton(QMessageBox.Close)
            # showing msg box
            x = msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    widget.setWindowIcon(QtGui.QIcon("icon\logo.png"))
    widget.setWindowTitle("Guess The Number!")
    widget.setStyleSheet('background-color:#05445E;')
    page1 = Page1()
    widget.addWidget(page1)
    widget.setFixedHeight(135)
    widget.setFixedWidth(500)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing...")

        
# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
