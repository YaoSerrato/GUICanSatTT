# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotDisplay_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 8

class Ui_DisplayPlots_Window(object):
    def setupUi(self, DisplayPlots_Window):
        DisplayPlots_Window.setObjectName("DisplayPlots_Window")
        DisplayPlots_Window.resize(1350, 670)
        DisplayPlots_Window.setMinimumSize(QtCore.QSize(1350, 670))
        DisplayPlots_Window.setMaximumSize(QtCore.QSize(1350, 670))
        self.centralwidget_displayplots = QtWidgets.QWidget(DisplayPlots_Window)
        self.centralwidget_displayplots.setObjectName("centralwidget_displayplots")
        self.label_title = QtWidgets.QLabel(self.centralwidget_displayplots)
        self.label_title.setGeometry(QtCore.QRect(730, 10, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.line_separator = QtWidgets.QFrame(self.centralwidget_displayplots)
        self.line_separator.setGeometry(QtCore.QRect(10, 50, 1320, 3))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.line_separator.setFont(font)
        self.line_separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separator.setObjectName("line_separator")
        self.label_pcknum = QtWidgets.QLabel(self.centralwidget_displayplots)
        self.label_pcknum.setGeometry(QtCore.QRect(30, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pcknum.setFont(font)
        self.label_pcknum.setObjectName("label_pcknum")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget_displayplots)
        self.comboBox.setGeometry(QtCore.QRect(30, 95, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget_displayplots)
        self.pushButton.setGeometry(QtCore.QRect(270, 95, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget_displayplots)
        self.pushButton_2.setGeometry(QtCore.QRect(1200, 95, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        DisplayPlots_Window.setCentralWidget(self.centralwidget_displayplots)

        self.retranslateUi(DisplayPlots_Window)
        QtCore.QMetaObject.connectSlotsByName(DisplayPlots_Window)

    def retranslateUi(self, DisplayPlots_Window):
        _translate = QtCore.QCoreApplication.translate
        DisplayPlots_Window.setWindowTitle(_translate("DisplayPlots_Window", "MainWindow"))
        self.label_title.setText(_translate("DisplayPlots_Window", "CanSat con sistema de descenso por autorrotación"))
        self.label_pcknum.setText(_translate("DisplayPlots_Window", "Parámetro:"))
        self.pushButton.setText(_translate("DisplayPlots_Window", "Graficar"))
        self.pushButton_2.setText(_translate("DisplayPlots_Window", "Cerrar"))

class CreateCanvas(FigureCanvas):
    # self = widget_graph_XXXX
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)        

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                            QtWidgets.QSizePolicy.Expanding,
                            QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def setWGtitle(self, title):
        self.ax.set_title(title)

    def setWGxlabel(self, label):
        self.ax.set_xlabel(label)

    def setWGylabel(self, label):
        self.ax.set_ylabel(label)
    
    def setWGylim(self, ymin, ymax):
        self.ax.set_ylim(ymin, ymax)

    def setWGxlim(self, xmin, xmax):
        self.ax.set_xlim(xmin, xmax)
    
    def setWGgrid(self, gridEnabler):
        self.ax.grid(gridEnabler)

    def clearWG(self):
        self.ax.cla()
