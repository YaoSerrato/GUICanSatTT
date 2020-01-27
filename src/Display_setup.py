# This is an arbitrary change.
# Second comment done on develop branch.
# This is an added comment from origin
# Another change made in develop.
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

        self.uiclsDisplay.comboBox_parameter.addItems(['None','MUSE','Kasabian','Lady Gaga','The Beatles','Billie Elish','Green Day'])        

        self.show()

        # Managing signals & slots
        self.uiclsDisplay.comboBox_parameter.currentIndexChanged.connect(self.slotItemSelectedChanged)

    def slotItemSelectedChanged(self):
        print(self.uiclsDisplay.comboBox_parameter.currentIndex())
        print(self.uiclsDisplay.comboBox_parameter.currentText())

if __name__=="__main__":
    app_display = QApplication(sys.argv)
    app_display.setStyle(QStyleFactory.create('Fusion'))    # ['windowsvista', 'Windows', 'Fusion']

    objclsDisplay_Plotter = clsDisplay()
    
    sys.exit(app_display.exec_())