import sys
import time
from gui_components  import *
from PyQt5.QtCore    import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, QApplication,
QLineEdit, QApplication, QPushButton, QWidget)

def main():
    app = QApplication(sys.argv)
    mainWin = mainWindow()
    sys.exit(app.exec_())

if __name__== "__main__":
    main()
