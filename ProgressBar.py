import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    flag = False
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1000, 500))    
        self.setWindowTitle("Add address") 

        self.pLabel = QLabel(self)
        self.pLabel.setText('Project Address:')
        self.pLine = QLineEdit(self)

        self.pLine.move(300, 95)
        self.pLine.resize(400, 35)
        self.pLabel.move(200, 95)

        self.uiLable = QLabel(self)
        self.uiLable.setText('UI Address:')
        self.uiLine = QLineEdit(self)

        self.uiLine.move(300, 180)
        self.uiLine.resize(400, 35)
        self.uiLable.move(200, 180)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(200, 300, 600, 35)

        self.btn = QPushButton('Upload', self)
        self.btn.clicked.connect(self.clickMethod)
        self.btn.setGeometry(600, 415, 150, 35)

        self.Nextbtn = QPushButton('Next', self)
        self.Nextbtn.clicked.connect(self.clickMethod)
        self.Nextbtn.setGeometry(800, 415, 150, 35)  
        self.Nextbtn.setEnabled(False)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.show()

    def clickMethod(self):
        if len(self.pLine.text()) == 0 or len(self.uiLine.text()) == 0:
            QMessageBox.about(self, "Error", "Empty Field")
        else:
            if self.timer.isActive():
                self.timer.stop()
                self.btn.setText('Start')
            else:
                self.timer.start(100, self)
                self.btn.setText('Stop')
        print('Project Address: ' + self.pLine.text())
        print('UI Address: ' + self.uiLine.text())

    def timerEvent(self, e):
      
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Files Uploaded')
            self.Nextbtn.setEnabled(True)
            return

        if self.step == 60:
            self.timer.stop()  

        self.step = self.step + 10
        self.pbar.setValue(self.step)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
