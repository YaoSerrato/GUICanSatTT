# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# This is a line added from origin.


from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 8

class Ui_Window_Dashboard(object):

    # Defines the graphical elements of the GUI
    def setupUi(self, Window_Dashboard):

        # Main widget Window_Dashboard
        Window_Dashboard.setObjectName("Window_Dashboard")
        Window_Dashboard.resize(1350, 670)
        Window_Dashboard.setMinimumSize(QtCore.QSize(1350, 670))
        Window_Dashboard.setMaximumSize(QtCore.QSize(1350, 670))
        Window_Dashboard.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon("D:\Semestre 11\TT2\SET\GUI\images\ground_station_icon.png")
        # icon.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window_Dashboard.setWindowIcon(icon)

        # centralwidget_dashboard
        self.centralwidget_dashboard = QtWidgets.QWidget(Window_Dashboard)
        self.centralwidget_dashboard.setObjectName("centralwidget_dashboard")

        # mainframe_dashboard
        self.mainframe_dashboard = QtWidgets.QFrame(self.centralwidget_dashboard)
        self.mainframe_dashboard.setGeometry(QtCore.QRect(5, 5, 1340, 660))
        self.mainframe_dashboard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_dashboard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_dashboard.setObjectName("mainframe_dashboard")

        # label_title
        self.label_title = QtWidgets.QLabel(self.mainframe_dashboard)
        self.label_title.setGeometry(QtCore.QRect(730, 10, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        # line_separator
        self.line_separator = QtWidgets.QFrame(self.mainframe_dashboard)
        self.line_separator.setGeometry(QtCore.QRect(10, 50, 1320, 3))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.line_separator.setFont(font)
        self.line_separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separator.setObjectName("line_separator")

        # groupBox_infomission
        self.groupBox_infomission = QtWidgets.QGroupBox(self.mainframe_dashboard)
        self.groupBox_infomission.setGeometry(QtCore.QRect(10, 60, 1320, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)
        self.groupBox_infomission.setFont(font)
        self.groupBox_infomission.setObjectName("groupBox_infomission")

        # label_pcknum
        self.label_pcknum = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_pcknum.setGeometry(QtCore.QRect(10, 30, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pcknum.setFont(font)
        self.label_pcknum.setObjectName("label_pcknum")

        # lineEdit_pcknum
        self.lineEdit_pcknum = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_pcknum.setGeometry(QtCore.QRect(190, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_pcknum.setFont(font)        
        self.lineEdit_pcknum.setReadOnly(True)
        self.lineEdit_pcknum.setObjectName("lineEdit_pcknum")

        # label_timemission
        self.label_timemission = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_timemission.setGeometry(QtCore.QRect(310, 30, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_timemission.setFont(font)
        self.label_timemission.setObjectName("label_timemission")

        # lineEdit_timemission
        self.lineEdit_timemission = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_timemission.setGeometry(QtCore.QRect(480, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_timemission.setFont(font)
        self.lineEdit_timemission.setReadOnly(True)
        self.lineEdit_timemission.setObjectName("lineEdit_timemission")

        # label_state
        self.label_state = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state.setGeometry(QtCore.QRect(610, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")

        # lineEdit_state_wait
        self.lineEdit_state_wait = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_state_wait.setGeometry(QtCore.QRect(680, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_state_wait.setFont(font)
        self.lineEdit_state_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state_wait.setReadOnly(True)
        self.lineEdit_state_wait.setObjectName("lineEdit_state_wait")

        # lineEdit_state_ascent
        self.lineEdit_state_ascent = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_state_ascent.setGeometry(QtCore.QRect(800, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_state_ascent.setFont(font)
        self.lineEdit_state_ascent.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state_ascent.setReadOnly(True)
        self.lineEdit_state_ascent.setObjectName("lineEdit_state_ascent")

        # lineEdit_state_parachute
        self.lineEdit_state_parachute = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_state_parachute.setGeometry(QtCore.QRect(920, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_state_parachute.setFont(font)
        self.lineEdit_state_parachute.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state_parachute.setReadOnly(True)
        self.lineEdit_state_parachute.setObjectName("lineEdit_state_parachute")

        # lineEdit_state_autorrotation
        self.lineEdit_state_autorrotation = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_state_autorrotation.setGeometry(QtCore.QRect(1040, 30, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_state_autorrotation.setFont(font)
        self.lineEdit_state_autorrotation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state_autorrotation.setReadOnly(True)
        self.lineEdit_state_autorrotation.setObjectName("lineEdit_state_autorrotation")

        # lineEdit_state_landing
        self.lineEdit_state_landing = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_state_landing.setGeometry(QtCore.QRect(1200, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_state_landing.setFont(font)
        self.lineEdit_state_landing.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_state_landing.setReadOnly(True)
        self.lineEdit_state_landing.setObjectName("lineEdit_state_landing")

        # label_dataframe
        self.label_dataframe = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_dataframe.setGeometry(QtCore.QRect(10, 78, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_dataframe.setFont(font)
        self.label_dataframe.setObjectName("label_dataframe")

        # lineEdit_dataframe
        self.lineEdit_dataframe = QtWidgets.QLineEdit(self.groupBox_infomission)
        self.lineEdit_dataframe.setGeometry(QtCore.QRect(150, 78, 1161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_dataframe.setFont(font)
        self.lineEdit_dataframe.setReadOnly(True)
        self.lineEdit_dataframe.setObjectName("lineEdit_dataframe")

        # groupBox_GPSdata
        self.groupBox_GPSdata = QtWidgets.QGroupBox(self.mainframe_dashboard)
        self.groupBox_GPSdata.setGeometry(QtCore.QRect(10, 183, 360, 171))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)
        self.groupBox_GPSdata.setFont(font)
        self.groupBox_GPSdata.setObjectName("groupBox_GPSdata")

        # formLayoutWidget
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_GPSdata)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 341, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_GPSdata = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_GPSdata.setContentsMargins(5, 5, 5, 5)
        self.formLayout_GPSdata.setObjectName("formLayout_GPSdata")

        # label_latitude
        self.label_latitude = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_latitude.setFont(font)
        self.label_latitude.setObjectName("label_latitude")
        self.formLayout_GPSdata.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_latitude)

        # lineEdit_latitude
        self.lineEdit_latitude = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_latitude.setFont(font)
        self.lineEdit_latitude.setText("")
        self.lineEdit_latitude.setReadOnly(True)
        self.lineEdit_latitude.setObjectName("lineEdit_latitude")
        self.formLayout_GPSdata.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_latitude)

        # label_longitude
        self.label_longitude = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_longitude.setFont(font)
        self.label_longitude.setObjectName("label_longitude")
        self.formLayout_GPSdata.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_longitude)

        # lineEdit_longitude
        self.lineEdit_longitude = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_longitude.setFont(font)
        self.lineEdit_longitude.setText("")
        self.lineEdit_longitude.setReadOnly(True)
        self.lineEdit_longitude.setObjectName("lineEdit_longitude")
        self.formLayout_GPSdata.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_longitude)

        # label_altitude
        self.label_altitude = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_altitude.setFont(font)
        self.label_altitude.setObjectName("label_altitude")
        self.formLayout_GPSdata.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_altitude)

        # lineEdit_altitude
        self.lineEdit_altitude = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_altitude.setFont(font)
        self.lineEdit_altitude.setText("")
        self.lineEdit_altitude.setReadOnly(True)
        self.lineEdit_altitude.setObjectName("lineEdit_altitude")
        self.formLayout_GPSdata.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_altitude)

        # label_numsat
        self.label_numsat = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_numsat.setFont(font)
        self.label_numsat.setObjectName("label_numsat")
        self.formLayout_GPSdata.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_numsat)

        # lineEdit_numsat
        self.lineEdit_numsat = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_numsat.setFont(font)
        self.lineEdit_numsat.setText("")
        self.lineEdit_numsat.setReadOnly(True)
        self.lineEdit_numsat.setObjectName("lineEdit_numsat")
        self.formLayout_GPSdata.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_numsat)

        # groupBox_telemetrydata
        self.groupBox_telemetrydata = QtWidgets.QGroupBox(self.mainframe_dashboard)
        self.groupBox_telemetrydata.setGeometry(QtCore.QRect(10, 364, 360, 271))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)
        self.groupBox_telemetrydata.setFont(font)
        self.groupBox_telemetrydata.setObjectName("groupBox_telemetrydata")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_telemetrydata)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 341, 221))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_telemetrydata = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_telemetrydata.setContentsMargins(5, 5, 5, 5)
        self.formLayout_telemetrydata.setObjectName("formLayout_telemetrydata")
        self.label_height = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_height.setFont(font)
        self.label_height.setObjectName("label_height")
        self.formLayout_telemetrydata.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_height)

        # lineEdit_height
        self.lineEdit_height = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_height.setFont(font)
        self.lineEdit_height.setText("")
        self.lineEdit_height.setReadOnly(True)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.formLayout_telemetrydata.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_height)
        
        # label_pressure
        self.label_pressure = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pressure.setFont(font)
        self.label_pressure.setObjectName("label_pressure")
        self.formLayout_telemetrydata.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pressure)
        
        # lineEdit_pressure
        self.lineEdit_pressure = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_pressure.setFont(font)
        self.lineEdit_pressure.setText("")
        self.lineEdit_pressure.setReadOnly(True)
        self.lineEdit_pressure.setObjectName("lineEdit_pressure")
        self.formLayout_telemetrydata.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pressure)
        
        # label_temperature
        self.label_temperature = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_temperature.setFont(font)
        self.label_temperature.setObjectName("label_temperature")
        self.formLayout_telemetrydata.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_temperature)
        
        # lineEdit_temperature
        self.lineEdit_temperature = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_temperature.setFont(font)
        self.lineEdit_temperature.setText("")
        self.lineEdit_temperature.setReadOnly(True)
        self.lineEdit_temperature.setObjectName("lineEdit_temperature")
        self.formLayout_telemetrydata.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_temperature)
        
        # label_rotorspeed
        self.label_rotorspeed = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_rotorspeed.setFont(font)
        self.label_rotorspeed.setObjectName("label_rotorspeed")
        self.formLayout_telemetrydata.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_rotorspeed)
        
        # lineEdit_rotorspeed
        self.lineEdit_rotorspeed = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_rotorspeed.setFont(font)
        self.lineEdit_rotorspeed.setText("")
        self.lineEdit_rotorspeed.setReadOnly(True)
        self.lineEdit_rotorspeed.setObjectName("lineEdit_rotorspeed")
        self.formLayout_telemetrydata.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_rotorspeed)
        
        # label_pitch
        self.label_pitch = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pitch.setFont(font)
        self.label_pitch.setObjectName("label_pitch")
        self.formLayout_telemetrydata.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_pitch)
        self.label_roll = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_roll.setFont(font)
        self.label_roll.setObjectName("label_roll")
        self.formLayout_telemetrydata.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_roll)
        self.label_azimut = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_azimut.setFont(font)
        self.label_azimut.setObjectName("label_azimut")
        self.formLayout_telemetrydata.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_azimut)
        
        # lineEdit_pitch
        self.lineEdit_pitch = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_pitch.setFont(font)
        self.lineEdit_pitch.setText("")
        self.lineEdit_pitch.setReadOnly(True)
        self.lineEdit_pitch.setObjectName("lineEdit_pitch")
        self.formLayout_telemetrydata.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pitch)
        
        # lineEdit_roll
        self.lineEdit_roll = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_roll.setFont(font)
        self.lineEdit_roll.setText("")
        self.lineEdit_roll.setReadOnly(True)
        self.lineEdit_roll.setObjectName("lineEdit_roll")
        self.formLayout_telemetrydata.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_roll)
        
        # lineEdit_azimut
        self.lineEdit_azimut = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lineEdit_azimut.setFont(font)
        self.lineEdit_azimut.setText("")
        self.lineEdit_azimut.setReadOnly(True)
        self.lineEdit_azimut.setObjectName("lineEdit_azimut")
        self.formLayout_telemetrydata.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_azimut)
        
        # tabWidget_plots
        self.tabWidget_plots = QtWidgets.QTabWidget(self.mainframe_dashboard)
        self.tabWidget_plots.setGeometry(QtCore.QRect(400, 183, 931, 411))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.tabWidget_plots.setFont(font)
        self.tabWidget_plots.setAccessibleName("")
        self.tabWidget_plots.setAutoFillBackground(False)
        self.tabWidget_plots.setObjectName("tabWidget_plots")

        # tab_height
        self.tab_height = QtWidgets.QWidget()
        self.tab_height.setObjectName("tab_height")
        self.WG_tabheight = CreateCanvas(parent=self.tab_height, width=10.5, height=3.5,dpi=100)
        self.WG_tabheight.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_height, "")

        # tab_pressure
        self.tab_pressure = QtWidgets.QWidget()
        self.tab_pressure.setObjectName("tab_pressure")
        self.WG_tabpressure = CreateCanvas(parent=self.tab_pressure, width=10.5, height=3.5,dpi=100)
        self.WG_tabpressure.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_pressure, "")

        # tab_temperature
        self.tab_temperature = QtWidgets.QWidget()
        self.tab_temperature.setObjectName("tab_temperature")
        self.WG_tabtemperature = CreateCanvas(parent=self.tab_temperature, width=10.5, height=3.5,dpi=100)
        self.WG_tabtemperature.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_temperature, "")

        # tab_rotorspeed
        self.tab_rotorspeed = QtWidgets.QWidget()
        self.tab_rotorspeed.setObjectName("tab_rotorspeed")
        self.WG_tabrotorspeed = CreateCanvas(parent=self.tab_rotorspeed, width=10.5, height=3.5,dpi=100)
        self.WG_tabrotorspeed.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_rotorspeed, "")

        # tab_orientation
        self.tab_orientation = QtWidgets.QWidget()
        self.tab_orientation.setObjectName("tab_orientation")
        self.WG_taborientation = CreateCanvas(parent=self.tab_orientation, width=10.5, height=3.5,dpi=100)
        self.WG_taborientation.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_orientation, "")

        # tab_GPS
        self.tab_GPS = QtWidgets.QWidget()
        self.tab_GPS.setObjectName("tab_GPS")
        self.WG_tabGPS = CreateCanvas(parent=self.tab_GPS, width=10.5, height=3.5,dpi=100)
        self.WG_tabGPS.move(-65,0)
        self.tabWidget_plots.addTab(self.tab_GPS, "")

        # pushButton_start
        self.pushButton_start = QtWidgets.QPushButton(self.mainframe_dashboard)
        self.pushButton_start.setGeometry(QtCore.QRect(410, 612, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")

        # pushButton_stop
        self.pushButton_stop = QtWidgets.QPushButton(self.mainframe_dashboard)
        self.pushButton_stop.setGeometry(QtCore.QRect(521, 612, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")

        # pushButton_continue
        self.pushButton_continue = QtWidgets.QPushButton(self.mainframe_dashboard)
        self.pushButton_continue.setGeometry(QtCore.QRect(1230, 612, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_continue.setFont(font)
        self.pushButton_continue.setObjectName("pushButton_continue")
        Window_Dashboard.setCentralWidget(self.centralwidget_dashboard)

        # label_finished                
        self.label_finished = QtWidgets.QLabel(self.mainframe_dashboard)
        self.label_finished.setGeometry(QtCore.QRect(800, 614, 300, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(50)
        self.label_finished.setFont(font)
        self.label_finished.setObjectName("label_finished")

        # label_state_wait
        self.label_state_wait = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state_wait.setGeometry(QtCore.QRect(680, 50, 113, 20))        
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state_wait.setFont(font)
        self.label_state_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state_wait.setObjectName("label_state_wait")

        # label_state_ascent
        self.label_state_ascent = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state_ascent.setGeometry(QtCore.QRect(800, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state_ascent.setFont(font)
        self.label_state_ascent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state_ascent.setObjectName("label_state_ascent")

        # label_state_parachute
        self.label_state_parachute = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state_parachute.setGeometry(QtCore.QRect(920, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state_parachute.setFont(font)
        self.label_state_parachute.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state_parachute.setObjectName("label_state_parachute")

        # label_state_autorrotation
        self.label_state_autorrotation = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state_autorrotation.setGeometry(QtCore.QRect(1040, 50, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state_autorrotation.setFont(font)
        self.label_state_autorrotation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state_autorrotation.setObjectName("label_state_autorrotation")

        # label_state_landing
        self.label_state_landing = QtWidgets.QLabel(self.groupBox_infomission)
        self.label_state_landing.setGeometry(QtCore.QRect(1200, 50, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_state_landing.setFont(font)
        self.label_state_landing.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state_landing.setObjectName("label_state_landing")

        self.retranslateUi(Window_Dashboard)
        self.tabWidget_plots.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window_Dashboard)

    def retranslateUi(self, Window_Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Window_Dashboard.setWindowTitle(_translate("Window_Dashboard", "Estación en Tierra"))
        self.label_title.setText(_translate("Window_Dashboard", "CanSat con sistema de descenso por autorrotación"))

        self.groupBox_infomission.setTitle(_translate("Window_Dashboard", "Información de la misión"))
        self.label_pcknum.setText(_translate("Window_Dashboard", "Número de paquete:"))
        self.label_timemission.setText(_translate("Window_Dashboard", "Tiempo de misión:"))
        self.label_state.setText(_translate("Window_Dashboard", "Estado:"))
        self.label_dataframe.setText(_translate("Window_Dashboard", "Trama recibida:"))

        self.groupBox_GPSdata.setTitle(_translate("Window_Dashboard", "Datos de GPS"))
        self.label_latitude.setText(_translate("Window_Dashboard", "Latitud:"))
        self.label_longitude.setText(_translate("Window_Dashboard", "Longitud:"))
        self.label_altitude.setText(_translate("Window_Dashboard", "Altitud:"))
        self.label_numsat.setText(_translate("Window_Dashboard", "N° Satélites:"))

        self.groupBox_telemetrydata.setTitle(_translate("Window_Dashboard", "Datos de telemetría"))
        self.label_height.setText(_translate("Window_Dashboard", "Altura [m]:"))
        self.label_pressure.setText(_translate("Window_Dashboard", "Presión [Pa]:"))
        self.label_temperature.setText(_translate("Window_Dashboard", "Temperatura [°C]:"))
        self.label_rotorspeed.setText(_translate("Window_Dashboard", "Velocidad rotor [rpm]:"))
        self.label_pitch.setText(_translate("Window_Dashboard", "Pitch [°]:"))
        self.label_roll.setText(_translate("Window_Dashboard", "Roll [°]:"))
        self.label_azimut.setText(_translate("Window_Dashboard", "Azimut [°]:"))

        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_height), _translate("Window_Dashboard", "Altura"))
        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_pressure), _translate("Window_Dashboard", "Presión"))
        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_temperature), _translate("Window_Dashboard", "Temperatura"))
        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_rotorspeed), _translate("Window_Dashboard", "Velocidad Rotor"))
        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_orientation), _translate("Window_Dashboard", "Orientación"))
        self.tabWidget_plots.setTabText(self.tabWidget_plots.indexOf(self.tab_GPS), _translate("Window_Dashboard", "GPS"))

        self.pushButton_start.setText(_translate("Window_Dashboard", "Iniciar"))
        self.pushButton_stop.setText(_translate("Window_Dashboard", "Terminar"))
        self.pushButton_continue.setText(_translate("Window_Dashboard", "Continuar"))
        self.label_finished.setText(_translate("Window_Dashboard", ""))

        self.label_state_wait.setText(_translate("Window_Dashboard", "Espera"))
        self.label_state_ascent.setText(_translate("Window_Dashboard", "Ascenso"))
        self.label_state_parachute.setText(_translate("Window_Dashboard", "Paracaídas"))
        self.label_state_autorrotation.setText(_translate("Window_Dashboard", "Autorrotación"))
        self.label_state_landing.setText(_translate("Window_Dashboard", "Aterrizaje"))

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
