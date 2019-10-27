# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotsWithTabs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 8


class Ui_MainWindow(object):
    # Aquí MainWindow = w
    # Aquí self = w.ui

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 510)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # -----------------------------------------------------------------------------------------------------------------------------------
        
        self.tabWidget_graphs = QtWidgets.QTabWidget(self.centralwidget)        
        self.tabWidget_graphs.setGeometry(QtCore.QRect(30, 20, 741, 431))
        self.tabWidget_graphs.setObjectName("tabWidget_graphs")

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.widget_graph_tab1 = CreateCanvas(self.tab_1, width=7, height=3.8)
        self.widget_graph_tab1.move(10,10)
        self.widget_graph_tab1.setObjectName("widget_graph_tab1")
        self.tabWidget_graphs.addTab(self.tab_1, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_graphs.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_graphs.addTab(self.tab_3, "")

        # -----------------------------------------------------------------------------------------------------------------------------------

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(30, 470, 75, 23))
        self.pushButton_start.setObjectName("pushButton_start")

        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(650, 470, 75, 23))
        self.pushButton_stop.setObjectName("pushButton_stop")

        self.lineEdit_serialRX = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_serialRX.setGeometry(QtCore.QRect(250, 470, 311, 21))
        self.lineEdit_serialRX.setObjectName("lineEdit_serialRX")        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_graphs.setCurrentIndex(0)        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plots within Tabs"))
        self.tabWidget_graphs.setTabText(self.tabWidget_graphs.indexOf(self.tab_1), _translate("MainWindow", "Height"))
        self.tabWidget_graphs.setTabText(self.tabWidget_graphs.indexOf(self.tab_2), _translate("MainWindow", "Pressure"))
        self.tabWidget_graphs.setTabText(self.tabWidget_graphs.indexOf(self.tab_3), _translate("MainWindow", "Orientation"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.lineEdit_serialRX.setText(_translate("MainWindow", ""))


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
