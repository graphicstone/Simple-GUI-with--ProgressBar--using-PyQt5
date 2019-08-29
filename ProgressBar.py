import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QMessageBox, QCheckBox, QRadioButton, QGridLayout
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer, QSize
from PyQt5 import QtGui, QtCore

class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setMinimumSize(QSize(300, 150)) 
        self.setWindowTitle("Select option")

        self.b = QCheckBox("Android",self)
        self.b.stateChanged.connect(self.clickBox)
        self.b.setGeometry(20, 20, 320, 40)

        self.b = QCheckBox("iOS",self)
        self.b.stateChanged.connect(self.clickBox)
        self.b.setGeometry(20, 50, 320, 40)

        self.btn = QPushButton('Submit', self)
        self.btn.clicked.connect(self.submitClickBox)
        self.btn.setGeometry(200, 100, 50, 35)

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')

    def submitClickBox(self, state):
        self.close()

class MainWindow(QMainWindow):
    ct = 0
    def __init__(self):
        QMainWindow.__init__(self)
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)

        self.setMinimumSize(QSize(1000, 500))    
        self.setWindowTitle("Upload Files") 

        oImage = QImage("ewe.png")
        sImage = oImage.scaled(QSize(1000,500))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        

        self.pLabel = QLabel(self)
        self.pLabel.setText('Project Address:')
        self.pLabel.move(200, 95)
        self.pLine = QLineEdit(self)
        self.pLine.setGeometry(300, 95, 400, 35)

        self.uiLable = QLabel(self)
        self.uiLable.setText('UI Address:')
        self.uiLable.move(200, 180)
        self.uiLine = QLineEdit(self)
        self.uiLine.setGeometry(300, 180, 400, 35)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(200, 300, 600, 35)

        self.btn = QPushButton('Upload', self)
        self.btn.clicked.connect(self.clickMethod)
        self.btn.setGeometry(600, 415, 150, 35)

        self.Nextbtn = QPushButton('Next', self)
        self.Nextbtn.clicked.connect(self.nextWindow)
        self.dialog = Second(self)
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

    def nextWindow(self):
        self.ct = self.ct + 1
        self.dialog.show()
        self.Nextbtn.setText('Finish')
        if(self.ct == 2):
            self.close()

    def timerEvent(self, e):
      
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Files Uploaded')
            self.Nextbtn.setEnabled(True)
            return

        # if self.step == 60:
        #     self.timer.stop()  

        self.step = self.step + 10
        self.pbar.setValue(self.step)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
