# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_ConfigurationWindow(object):

    # Defines the graphical elements of the GUI
    def setupUi(self, Dialog_ConfigurationWindow):

        # Main widget Dialog_ConfigurationWindow
        Dialog_ConfigurationWindow.setObjectName("Dialog_ConfigurationWindow")
        Dialog_ConfigurationWindow.resize(750, 440)
        Dialog_ConfigurationWindow.setMinimumSize(QtCore.QSize(750, 440))
        Dialog_ConfigurationWindow.setMaximumSize(QtCore.QSize(750, 440))
        icon = QtGui.QIcon('D:\Semestre 11\TT2\SET\GUI\images\config_icon.png')
        # icon.addPixmap(QtGui.QPixmap("images/config_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_ConfigurationWindow.setWindowIcon(icon)
        Dialog_ConfigurationWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        # frame_main
        self.frame_main = QtWidgets.QFrame(Dialog_ConfigurationWindow)
        self.frame_main.setGeometry(QtCore.QRect(5, 5, 740, 430))
        self.frame_main.setStyleSheet("border-color: rgb(0,0,0);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")

        # label_ipnlogo
        self.label_ipnlogo = QtWidgets.QLabel(self.frame_main)
        self.label_ipnlogo.setGeometry(QtCore.QRect(70, 20, 71, 101))
        self.label_ipnlogo.setText("")
        # self.label_ipnlogo.setPixmap(QtGui.QPixmap("D:\Semestre 11\TT2\SET\GUI\images\ipn_logo_small.jpg"))
        self.label_ipnlogo.setObjectName("label_ipnlogo")

        # label_TTname1
        self.label_TTname1 = QtWidgets.QLabel(self.frame_main)
        self.label_TTname1.setGeometry(QtCore.QRect(160, 40, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_TTname1.setFont(font)
        self.label_TTname1.setObjectName("label_TTname1")

        # label_TTname2
        self.label_TTname2 = QtWidgets.QLabel(self.frame_main)
        self.label_TTname2.setGeometry(QtCore.QRect(250, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_TTname2.setFont(font)
        self.label_TTname2.setObjectName("label_TTname2")

        # label_upiitalogo
        self.label_upiitalogo = QtWidgets.QLabel(self.frame_main)
        self.label_upiitalogo.setGeometry(QtCore.QRect(560, 30, 101, 91))
        self.label_upiitalogo.setText("")
        # self.label_upiitalogo.setPixmap(QtGui.QPixmap("D:\Semestre 11\TT2\SET\GUI\images\upiita_logo_small.png"))
        self.label_upiitalogo.setObjectName("label_upiitalogo")

        # line_separator
        self.line_separator = QtWidgets.QFrame(self.frame_main)
        self.line_separator.setGeometry(QtCore.QRect(110, 140, 521, 16))
        self.line_separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separator.setObjectName("line_separator")

        # groupBox_csv
        self.groupBox_csv = QtWidgets.QGroupBox(self.frame_main)
        self.groupBox_csv.setGeometry(QtCore.QRect(30, 160, 671, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_csv.setFont(font)
        self.groupBox_csv.setObjectName("groupBox_csv")

        # formLayoutWidget
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_csv)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 641, 76))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        # formLayout_csv
        self.formLayout_csv = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_csv.setContentsMargins(10, 10, 10, 10)
        self.formLayout_csv.setObjectName("formLayout_csv")

        # label_filename
        self.label_filename = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_filename.setFont(font)
        self.label_filename.setObjectName("label_filename")
        self.formLayout_csv.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_filename)

        # lineEdit_filename
        self.lineEdit_filename = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_filename.setFont(font)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.formLayout_csv.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_filename)

        # pushButton_selectdirectory
        self.pushButton_selectdirectory = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_selectdirectory.setFont(font)
        self.pushButton_selectdirectory.setObjectName("pushButton_selectdirectory")
        self.formLayout_csv.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_selectdirectory)

        # lineEdit_directorypath
        self.lineEdit_directorypath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_directorypath.setReadOnly(True)
        self.lineEdit_directorypath.setObjectName("lineEdit_directorypath")
        self.formLayout_csv.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_directorypath)

        # groupBox_serial
        self.groupBox_serial = QtWidgets.QGroupBox(self.frame_main)
        self.groupBox_serial.setGeometry(QtCore.QRect(30, 290, 671, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_serial.setFont(font)
        self.groupBox_serial.setObjectName("groupBox_serial")

        # horizontalLayoutWidget
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_serial)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 641, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        # horizontalLayout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # label_selectport
        self.label_selectport = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selectport.setFont(font)
        self.label_selectport.setObjectName("label_selectport")
        self.horizontalLayout.addWidget(self.label_selectport)

        # comboBox_COMport
        self.comboBox_COMport = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_COMport.setFont(font)
        self.comboBox_COMport.setObjectName("comboBox_COMport")
        self.comboBox_COMport.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_COMport)

        # pushButton_accept
        self.pushButton_accept = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_accept.setGeometry(QtCore.QRect(530, 390, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_accept.setFont(font)
        self.pushButton_accept.setObjectName("pushButton_accept")

        # pushButton_cancel
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_cancel.setGeometry(QtCore.QRect(620, 390, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        # pushButton_configCanSat
        self.pushButton_configCanSat = QtWidgets.QPushButton(self.frame_main)
        self.pushButton_configCanSat.setGeometry(QtCore.QRect(30, 390, 140, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_configCanSat.setFont(font)
        self.pushButton_configCanSat.setObjectName("pushButton_configCanSat")

        # Labeling GUI elements
        self.retranslateUi(Dialog_ConfigurationWindow)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ConfigurationWindow)

    # Labels all GUI elements
    def retranslateUi(self, Dialog_ConfigurationWindow):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ConfigurationWindow.setWindowTitle(_translate("Dialog_ConfigurationWindow", "Configuración"))
        self.label_TTname1.setText(_translate("Dialog_ConfigurationWindow", "CanSat con sistema de descenso"))
        self.label_TTname2.setText(_translate("Dialog_ConfigurationWindow", "por autorrotación"))
        self.groupBox_csv.setTitle(_translate("Dialog_ConfigurationWindow", "Archivo .csv"))
        self.label_filename.setText(_translate("Dialog_ConfigurationWindow", "Nombre de archivo:"))
        self.pushButton_selectdirectory.setText(_translate("Dialog_ConfigurationWindow", "Seleccionar directorio"))
        self.groupBox_serial.setTitle(_translate("Dialog_ConfigurationWindow", "Comunicación serial"))
        self.label_selectport.setText(_translate("Dialog_ConfigurationWindow", "Seleccionar puerto COM:"))
        self.comboBox_COMport.setItemText(0, _translate("Dialog_ConfigurationWindow", "Ninguno"))
        self.pushButton_accept.setText(_translate("Dialog_ConfigurationWindow", "Aceptar"))
        self.pushButton_cancel.setText(_translate("Dialog_ConfigurationWindow", "Cancelar"))
        self.pushButton_configCanSat.setText(_translate("Dialog_ConfigurationWindow", "Configurar CanSat"))
