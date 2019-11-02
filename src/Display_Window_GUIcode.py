# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotDisplay_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 8

class Ui_DisplayPlots_Window(object):
    # Creating graphical environment
    def setupUi(self, DisplayPlots_Window):

        # Configuring main widget DisplayPlots_Window
        DisplayPlots_Window.setObjectName("DisplayPlots_Window")
        DisplayPlots_Window.resize(1350, 670)
        DisplayPlots_Window.setMinimumSize(QtCore.QSize(1350, 670))
        DisplayPlots_Window.setMaximumSize(QtCore.QSize(1350, 670))

        # centralwidget_displayplots
        self.centralwidget_displayplots = QtWidgets.QWidget(DisplayPlots_Window)
        self.WG_plotarea = CreateCanvas(parent = self.centralwidget_displayplots, width = 12.90, height = 5.4, dpi = 100)
        self.WG_plotarea.setWGgrid(True)
        self.WG_toolbar = NavigationToolbar(self.WG_plotarea, self.WG_plotarea)
        self.WG_plotarea.move(30,110)
        self.centralwidget_displayplots.setObjectName("centralwidget_displayplots")

        # label_title
        self.label_title = QtWidgets.QLabel(self.centralwidget_displayplots)
        self.label_title.setGeometry(QtCore.QRect(730, 10, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        # line_separator
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

        # label_parameter
        self.label_parameter = QtWidgets.QLabel(self.centralwidget_displayplots)
        self.label_parameter.setGeometry(QtCore.QRect(30, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_parameter.setFont(font)
        self.label_parameter.setObjectName("label_parameter")

        # comboBox_parameter
        self.comboBox_parameter = QtWidgets.QComboBox(self.centralwidget_displayplots)
        self.comboBox_parameter.setGeometry(QtCore.QRect(130, 70, 221, 22))
        self.comboBox_parameter.setObjectName("comboBox_parameter")

        # pushButton_plot
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget_displayplots)
        self.pushButton_plot.setGeometry(QtCore.QRect(370, 70, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton_plot.setFont(font)
        self.pushButton_plot.setObjectName("pushButton_plot")

        # pushButton_close
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget_displayplots)
        self.pushButton_close.setGeometry(QtCore.QRect(1200, 70, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_plot_2")

        DisplayPlots_Window.setCentralWidget(self.centralwidget_displayplots)

        self.retranslateUi(DisplayPlots_Window)
        QtCore.QMetaObject.connectSlotsByName(DisplayPlots_Window)

    # Labeling all GUI elements
    def retranslateUi(self, DisplayPlots_Window):
        _translate = QtCore.QCoreApplication.translate
        DisplayPlots_Window.setWindowTitle(_translate("DisplayPlots_Window", "MainWindow"))
        self.label_title.setText(_translate("DisplayPlots_Window", "CanSat con sistema de descenso por autorrotación"))
        self.label_parameter.setText(_translate("DisplayPlots_Window", "Parámetro:"))
        self.pushButton_plot.setText(_translate("DisplayPlots_Window", "Graficar"))
        self.pushButton_close.setText(_translate("DisplayPlots_Window", "Cerrar"))

# Plotter class
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
