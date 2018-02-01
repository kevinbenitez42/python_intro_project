from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, QApplication,
    QLineEdit, QApplication, QPushButton, QWidget, QInputDialog, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

import image_processing
import urllib.request
import shutil
import os

class loadButton(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)


class mainWindow(QMainWindow, QWidget):

    stringinit = " "
    imageProcessor = image_processing.ImageProcessor()
    def __init__(self):

        super().__init__()
        self.line = QLineEdit('', self)
        self.button = loadButton('load', self)
        self.button2 = loadButton('load url', self)
        self.menuBar = self.menuBar()
        self.impMenu  = QMenu('import image', self)
        self.impAct   = QAction('take picture', self)
        self.impAct2  = QAction('directory select', self)

        self.initUI()

    def updateAndDisplay(self):

            image = self.imageProcessor.getImage(self.line.text())
            print(self.line.text())
            if self.imageProcessor.isInDirectory(
               self.imageProcessor.returnImage()):
               self.line.setText('')
               self.line.setText(image + ' has been loaded!')
               self.imageProcessor.displayImage()
            else:
               self.line.setText('Error: file not found')

    def fileDialog(self):
         self.openFileNameDialog()


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileName(self,"select files", "",
                   "All Files (*);;Python Files (*.py)", options=options)
        self.line.setText(files)
        print(files)

    def loadUrl(self):

        url = self.line.text()
        filename = 'downloadimage'
        urllib.request.urlretrieve(url, filename)
        self.imageProcessor.setImage(filename)
        self.imageProcessor.setImageDirectory(filename)
        self.line.setText('')
        self.line.setText(filename + ' has been loaded!')
        self.imageProcessor.displayImage()

    def initUI(self):

        self.line.setDragEnabled(True)
        self.line.move(5,35)
        self.line.resize(380,30)


        self.button.clicked.connect(self.updateAndDisplay)
        self.button.move(390,35)

        self.button2.clicked.connect(self.loadUrl)
        self.button2.move(495, 35)

        self.impMenu.addAction(self.impAct)
        self.impMenu.addAction(self.impAct2)
        self.menuBar.addMenu(self.impMenu)

        self.impAct.triggered.connect(self.fileDialog)
        self.impAct2.triggered.connect(self.fileDialog)

        self.setGeometry(500, 500, 600, 75)
        self.setWindowTitle('Menu')
        self.show()
