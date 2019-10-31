import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStyleFactory, QApplication

from Display_Window_GUIcode import *

class clsDisplay(QMainWindow):
    def __init__(self):
        # Calling parent constructor
        super().__init__()

        # Creating graphical environment
        self.uiclsDisplay = Ui_DisplayPlots_Window()
        self.uiclsDisplay.setupUi(self)
        self.show()

if __name__=="__main__":
    app_display = QApplication(sys.argv)
    app_display.setStyle(QStyleFactory.create('Fusion'))    # ['windowsvista', 'Windows', 'Fusion']

    objclsDisplay_Plotter = clsDisplay()
    
    sys.exit(app_display.exec_())