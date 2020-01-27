# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigCanSatDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
# This is a comment made from origin.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_InitialCanSatConfig(object):
    
    # Defines the graphical elements of the GUI
    def setupUi(self, Dialog_ConfigCanSat):
        
        # Main widget Dialog_ConfigCanSat
        Dialog_ConfigCanSat.setObjectName("Dialog_ConfigCanSat")
        Dialog_ConfigCanSat.resize(400, 336)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog_ConfigCanSat.setFont(font)

        # progressBar_configuring
        self.progressBar_configuring = QtWidgets.QProgressBar(Dialog_ConfigCanSat)
        self.progressBar_configuring.setGeometry(QtCore.QRect(20, 250, 360, 23))
        self.progressBar_configuring.setProperty("value", 24)
        self.progressBar_configuring.setObjectName("progressBar_configuring")

        # label_configuring
        self.label_configuring = QtWidgets.QLabel(Dialog_ConfigCanSat)
        self.label_configuring.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label_configuring.setObjectName("label_configuring")

        # textEdit_msgsconfig
        self.textEdit_msgsconfig = QtWidgets.QTextEdit(Dialog_ConfigCanSat)
        self.textEdit_msgsconfig.setGeometry(QtCore.QRect(20, 50, 360, 180))
        self.textEdit_msgsconfig.setObjectName("textEdit_msgsconfig")

        # pushButton_acceptconfig
        self.pushButton_acceptconfig = QtWidgets.QPushButton(Dialog_ConfigCanSat)
        self.pushButton_acceptconfig.setGeometry(QtCore.QRect(305, 295, 75, 23))
        self.pushButton_acceptconfig.setObjectName("pushButton_acceptconfig")

        # Labeling GUI elements
        self.retranslateUi(Dialog_ConfigCanSat)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ConfigCanSat)

    # Labels all GUI elements
    def retranslateUi(self, Dialog_ConfigCanSat):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ConfigCanSat.setWindowTitle(_translate("Dialog_ConfigCanSat", "Configurando CanSat"))
        self.label_configuring.setText(_translate("Dialog_ConfigCanSat", "Configurando..."))
        self.pushButton_acceptconfig.setText(_translate("Dialog_ConfigCanSat", "Aceptar"))
