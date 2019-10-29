# Main file

# ****************************************************************************************************************************************  #
# Imports
# ***************************************************************************************************************************************** #
import sys
import os
import glob

import serial

import csv

import time

import string

import random

from multiprocessing import Queue, Process
import threading

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QStyleFactory, QFileDialog, QMessageBox, QMainWindow

# Imports of GUI codes
from ConfigurationWindow_Dialog_GUIcode import *
from InitialCanSatConfig_Dialog_GUIcode import *
from Dashboard_Window_GUIcode import *

# ***************************************************************************************************************************************** #
# Classes
# ***************************************************************************************************************************************** #

# -----------------------------------------------------------------------------------------------------------------------------------------
# Configuration dialog class
class clsConfigurationDialog(QDialog):
    def __init__(self):
        # Calling parent constructor
        super().__init__()

        # Initializing instance variables

        self.inst_flagdirectory = False
        self.inst_flagfilename = False
        self.inst_flagCOM = False

        self.inst_msgbox = QMessageBox()

        # Creating graphical environment
        self.uiclsConfigurationDialog = Ui_Dialog_ConfigurationWindow()
        self.uiclsConfigurationDialog.setupUi(self)
        self.show()

        self.uiclsConfigurationDialog.pushButton_accept.setDisabled(True)

        # Calling configuration methods
        self.mthSearchPorts()

        # Managing signals & slots
        self.uiclsConfigurationDialog.pushButton_cancel.clicked.connect(self.slotCloseWindow)
        self.uiclsConfigurationDialog.pushButton_selectdirectory.clicked.connect(self.slotEnterDirectoryCSV)
        self.uiclsConfigurationDialog.pushButton_accept.clicked.connect(self.slotAccept)
        self.uiclsConfigurationDialog.pushButton_configCanSat.clicked.connect(self.slotConfigureCanSat)
        self.uiclsConfigurationDialog.lineEdit_filename.textEdited.connect(self.slotVerifyFilename)

    def slotConfigureCanSat(self):
        if self.uiclsConfigurationDialog.comboBox_COMport.currentIndex() == 0:            
            self.inst_msgbox.setIcon(QMessageBox.Warning)
            self.inst_msgbox.setWindowTitle("Error puerto COM")
            self.inst_msgbox.setText("No hay puerto COM seleccionado.")
            self.inst_msgbox.setInformativeText('')
            self.inst_msgbox.exec_()
        else:            
            # Here I call an instance from the class related to the initial commands sent to CanSat            
            self.uiclsConfigurationDialog.pushButton_accept.setDisabled(False)
            self.uiclsConfigurationDialog.pushButton_configCanSat.setDisabled(True)

        # self.ui.pushButton_accept.setDisabled(False)

    def slotCloseWindow(self):
        self.close()

    def slotVerifyFilename(self):        
        for c in self.uiclsConfigurationDialog.lineEdit_filename.text():
            if c in string.whitespace:
                self.inst_msgbox.setIcon(QMessageBox.Warning)
                self.inst_msgbox.setText("¡Advertencia!")
                self.inst_msgbox.setWindowTitle("Espacio detectado") 
                self.inst_msgbox.setInformativeText('El nombre de archivo no puede incluir espacios en blanco.')
                self.inst_msgbox.exec_()
            elif c in string.punctuation:
                self.inst_msgbox.setIcon(QMessageBox.Warning)
                self.inst_msgbox.setText("¡Advertencia!")
                self.inst_msgbox.setWindowTitle("Caracter inválido") 
                self.inst_msgbox.setInformativeText('El nombre de archivo contiene un caracter inválido.')
                self.inst_msgbox.exec_()                

    def slotEnterDirectoryCSV(self):
        self.inst_pathdir = QFileDialog.getExistingDirectory(parent = self, caption = 'Seleccionar directorio donde guardar el archivo .csv')
        self.uiclsConfigurationDialog.lineEdit_directorypath.setText(self.inst_pathdir)

    def slotAccept(self):                       
        if len(self.uiclsConfigurationDialog.lineEdit_directorypath.text()) == 0:
            self.inst_flagdirectory = True            
        else:
            self.inst_flagdirectory = False
        
        if len(self.uiclsConfigurationDialog.lineEdit_filename.text()) == 0:
            self.inst_flagfilename = True            
        else:
            self.inst_flagfilename = False

        if self.uiclsConfigurationDialog.comboBox_COMport.currentIndex() == 0:
            self.inst_flagCOM = True            
        else:
            self.inst_flagCOM = False
        
        if self.inst_flagdirectory or self.inst_flagfilename or self.inst_flagCOM:
            self.inst_msgbox.setIcon(QMessageBox.Warning)
            self.inst_msgbox.setText("¡Advertencia!")
            self.inst_msgbox.setWindowTitle("¡Advertencia!") 
            self.inst_msgbox.setInformativeText('Campos faltantes: \n' + self.inst_flagfilename*' -Nombre de archivo\n' + self.inst_flagdirectory*' -Directorio\n' + self.inst_flagCOM*' -Puerto COM')
            self.inst_msgbox.exec_()
        else:
            self.inst_pathcsv = self.inst_pathdir + '/' + self.uiclsConfigurationDialog.lineEdit_filename.text() + '.csv'
            self.close()
            extdefCreateProcesses(self.uiclsConfigurationDialog.comboBox_COMport.currentText(), self.inst_pathcsv)            

    def mthSearchPorts(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()                
                self.uiclsConfigurationDialog.comboBox_COMport.addItem(port)
            except (OSError, serial.SerialException):
                pass

# External methods called in clsConfigurationDialog class
def extdefCreateProcesses(argdef_COMport, argdef_pathcsv):
    queue_data = Queue()

    # Creating Plotter Process
    process_plotter = Process(target = ProcessPlotter, name = 'process_plotter', args = (queue_data, argdef_pathcsv))
    process_plotter.start()

    # Creating Producer Process
    process_producer = Process(target = ProcessProducer, name = 'process_producer', args = (queue_data, argdef_COMport))
    process_producer.start()

    process_plotter.join()
    process_producer.join()
    # here I create the queues

# -----------------------------------------------------------------------------------------------------------------------------------------
# Dashboard class
class clsDashboardWindow(QMainWindow):
    def __init__(self, argcls_queuedata, argcls_pathcsv):
        # Calling parent constructor
        super().__init__()

        # Initializing instance variables
        self.inst_queueDashboard = argcls_queuedata
        
        self.inst_csvfile = open(argcls_pathcsv, mode = 'at', newline = '')
        self.inst_csvwriter = csv.writer(self.inst_csvfile, delimiter = ',')

        self.inst_mutex = threading.Lock()        

        self.inst_initflag = True

        self.inst_pcknum = []
        self.inst_missiontime = []
        self.inst_pitch = []
        self.inst_roll = []
        self.inst_azimuth = []
        self.inst_pressure = []        
        self.inst_temperature = []
        self.inst_height = []
        self.inst_numsat = []
        self.inst_latitude = []
        self.inst_longitude = []
        self.inst_altitude = []
        self.inst_rotorspeed = []
        self.inst_state = []

        # Creating graphical environment
        self.uiclsDashboardWindow = Ui_Window_Dashboard()
        self.uiclsDashboardWindow.setupUi(self)
        self.show()

        self.uiclsDashboardWindow.pushButton_continue.setDisabled(True)

        self.inst_plotWG = [self.uiclsDashboardWindow.WG_tabheight,
                        self.uiclsDashboardWindow.WG_tabpressure,
                        self.uiclsDashboardWindow.WG_tabtemperature,
                        self.uiclsDashboardWindow.WG_tabrotorspeed,
                        self.uiclsDashboardWindow.WG_taborientation,
                        self.uiclsDashboardWindow.WG_tabGPS]

        # Calling configuration methods

        # Managing signals & slots
        self.uiclsDashboardWindow.pushButton_start.clicked.connect(self.slotInitializer)
        self.uiclsDashboardWindow.pushButton_stop.clicked.connect(self.slotCloseDashboard)
    
    def slotInitializer(self):
        if self.inst_initflag:
            self.mthDisplay()
            self.inst_initflag = False

    def slotCloseDashboard(self):
        self.close()
        self.inst_csvfile.close()
    
    def mthDisplay(self):
        # Locking thread
        self.inst_mutex.acquire()

        # Creating timer thread for getting data from inst_queueDashboard and plotting/displaying it
        self.inst_timerplot = threading.Timer(1.0, self.mthDisplay)
        self.inst_timerplot.start()

        try:
            # Getting data from inst_queueDashboard
            for _ in range(0, self.inst_queueDashboard.qsize()):
                dataframe = self.inst_queueDashboard.get()
                
                self.inst_pcknum.append(dataframe[0])
                self.inst_missiontime.append(dataframe[1])
                self.inst_pitch.append(dataframe[2])
                self.inst_roll.append(dataframe[3])
                self.inst_azimuth.append(dataframe[4])
                self.inst_pressure.append(dataframe[5])
                self.inst_temperature.append(dataframe[6])
                self.inst_height.append(dataframe[7])
                self.inst_numsat.append(dataframe[8])
                self.inst_latitude.append(dataframe[9])
                self.inst_longitude.append(dataframe[10])
                self.inst_altitude.append(dataframe[11])
                self.inst_rotorspeed.append(dataframe[12])
                self.inst_state.append(dataframe[13])

                dataframestr = list(map(str,dataframe))
                self.inst_csvwriter.writerow(dataframestr)
                # self.inst_csvfile.close()

            # Displaying values in LineEdits
            self.uiclsDashboardWindow.lineEdit_dataframe.setText(str(dataframe))
            self.uiclsDashboardWindow.lineEdit_pcknum.setText(str(self.inst_pcknum[-1]))
            self.uiclsDashboardWindow.lineEdit_timemission.setText(str(self.inst_missiontime[-1]))
            self.uiclsDashboardWindow.lineEdit_pitch.setText(str(self.inst_pitch[-1]))
            self.uiclsDashboardWindow.lineEdit_roll.setText(str(self.inst_roll[-1]))
            self.uiclsDashboardWindow.lineEdit_azimut.setText(str(self.inst_azimuth[-1]))
            self.uiclsDashboardWindow.lineEdit_pressure.setText(str(self.inst_pressure[-1]))
            self.uiclsDashboardWindow.lineEdit_temperature.setText(str(self.inst_temperature[-1]))                        
            self.uiclsDashboardWindow.lineEdit_height.setText(str(self.inst_height[-1]))
            self.uiclsDashboardWindow.lineEdit_numsat.setText(str(self.inst_numsat[-1]))
            self.uiclsDashboardWindow.lineEdit_latitude.setText(str(self.inst_latitude[-1]))
            self.uiclsDashboardWindow.lineEdit_longitude.setText(str(self.inst_longitude[-1]))
            self.uiclsDashboardWindow.lineEdit_altitude.setText(str(self.inst_altitude[-1]))
            self.uiclsDashboardWindow.lineEdit_rotorspeed.setText(str(self.inst_rotorspeed[-1]))

            # Colouring state field
            # self.mthColourState(self.inst_state[-1])

            # Plotting
            if self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 0:
                self.mthPlot(0, 'ALtura', 'Tiempo [s]', 'Altura [m]', self.inst_missiontime, self.inst_height, 'bo--')

            elif self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 1:
                self.mthPlot(1, 'Presión barmétrica', 'Tiempo [s]', 'Presión [Pa]', self.inst_missiontime, self.inst_pressure, 'ks--')

            elif self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 2:
                self.mthPlot(2, 'Temperatura exterior', 'Tiempo [s]', 'Temperatura [°C]', self.inst_missiontime, self.inst_temperature, 'r^--')

            elif self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 3:
                self.mthPlot(3, 'Velocidad del rotor', 'Tiempo [s]', 'Velocidad [rpm]', self.inst_missiontime, self.inst_rotorspeed, 'mp--')

            elif self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 4:
                self.mthPlotOrientation(4, 'Orientación del CanSat', 'Tiempo [s]', 'Orientación [°]', self.inst_missiontime, self.inst_pitch, self.inst_roll, self.inst_azimuth)

            elif self.uiclsDashboardWindow.tabWidget_plots.currentIndex() == 5:
                self.mthPlotGPS(5, 'Posición de GPS', 'Latitud [°]', 'Longitud [°]', self.inst_latitude, self.inst_longitude, 'ko--')
            
        except:
            pass

        self.inst_mutex.release()
    
    def mthPlot(self, numplot, argmth_title, argmth_xlabel, argmth_ylabel, argmth_xdata, argmth_ydata, argmth_style):
        self.inst_plotWG[numplot].clearWG()

        self.inst_plotWG[numplot].setWGtitle(argmth_title)
        self.inst_plotWG[numplot].setWGxlabel(argmth_xlabel)
        self.inst_plotWG[numplot].setWGylabel(argmth_ylabel)
        self.inst_plotWG[numplot].setWGxlim(max(0, argmth_xdata[-1]-10), argmth_xdata[-1])
        self.inst_plotWG[numplot].setWGgrid(True)

        self.inst_plotWG[numplot].ax.plot(argmth_xdata, argmth_ydata, argmth_style, linewidth = 2, markersize = 8)
        self.inst_plotWG[numplot].draw()

    def mthPlotOrientation(self, numplot, argmth_title, argmth_xlabel, argmth_ylabel, argmth_xdata, argmth_pitch, argmth_roll, argmth_az):
        self.inst_plotWG[numplot].clearWG()

        self.inst_plotWG[numplot].setWGtitle(argmth_title)
        self.inst_plotWG[numplot].setWGxlabel(argmth_xlabel)
        self.inst_plotWG[numplot].setWGylabel(argmth_ylabel)
        self.inst_plotWG[numplot].setWGylim(-180, 180)
        self.inst_plotWG[numplot].setWGxlim(max(0, argmth_xdata[-1]-10), argmth_xdata[-1])
        self.inst_plotWG[numplot].setWGgrid(True)

        self.inst_plotWG[numplot].ax.plot(argmth_xdata, argmth_pitch, 'bo--', label = 'Pitch', linewidth = 2, markersize = 8)
        self.inst_plotWG[numplot].ax.plot(argmth_xdata, argmth_roll, 'rs--', label = 'Roll', linewidth = 2, markersize = 8)
        self.inst_plotWG[numplot].ax.plot(argmth_xdata, argmth_az, 'k^--', label = 'Azimuth', linewidth = 2, markersize = 8)
        self.inst_plotWG[numplot].ax.legend()
        self.inst_plotWG[numplot].draw()

    def mthPlotGPS(self, numplot, argmth_title, argmth_xlabel, argmth_ylabel, argmth_xdata, argmth_ydata, argmth_style):
        self.inst_plotWG[numplot].clearWG()

        self.inst_plotWG[numplot].setWGtitle(argmth_title)
        self.inst_plotWG[numplot].setWGxlabel(argmth_xlabel)
        self.inst_plotWG[numplot].setWGylabel(argmth_ylabel)
        self.inst_plotWG[numplot].setWGxlim(-90, 90)
        self.inst_plotWG[numplot].setWGylim(0, 360)
        self.inst_plotWG[numplot].setWGgrid(True)

        self.inst_plotWG[numplot].ax.plot(argmth_xdata, argmth_ydata, argmth_style, linewidth = 2, markersize = 8)
        self.inst_plotWG[numplot].draw()

    def mthColourState(self, argmth_state):
        self.uiclsDashboardWindow.lineEdit_state_wait.setStyleSheet('background-color: white')
        self.uiclsDashboardWindow.lineEdit_state_ascent.setStyleSheet('background-color: white')
        self.uiclsDashboardWindow.lineEdit_state_parachute.setStyleSheet('background-color: white')
        self.uiclsDashboardWindow.lineEdit_state_autorrotation.setStyleSheet('background-color: white')
        self.uiclsDashboardWindow.lineEdit_state_landing.setStyleSheet('background-color: white')        

        if argmth_state == 1:
            self.uiclsDashboardWindow.lineEdit_state_wait.setStyleSheet('background-color: yellow')            
        elif argmth_state == 2:
            self.uiclsDashboardWindow.lineEdit_state_ascent.setStyleSheet('background-color: yellow')
        elif argmth_state == 3:
            self.uiclsDashboardWindow.lineEdit_state_parachute.setStyleSheet('background-color: yellow')
        elif argmth_state == 4:
            self.uiclsDashboardWindow.lineEdit_state_autorrotation.setStyleSheet('background-color: yellow')
        elif argmth_state == 5:
            self.uiclsDashboardWindow.lineEdit_state_landing.setStyleSheet('background-color: yellow')


# ***************************************************************************************************************************************** #
# Processes
# ***************************************************************************************************************************************** #

# Plotter
def ProcessPlotter(argdef_queuePlotter, argdef_CSV):    
    app_dashboard = QApplication(sys.argv)
    app_dashboard.setStyle(QStyleFactory.create('Fusion'))

    objclsDashboardWindow_Dashboard = clsDashboardWindow(argdef_queuePlotter, argdef_CSV)

    sys.exit(app_dashboard.exec_())

# Producer
def ProcessProducer(argdef_queueProducer, argdef_COM):
    ser = serial.Serial(argdef_COM, 115200, timeout = 1)
    flagserial = True

    while flagserial:
        try:
            line = ser.readline().decode('UTF-8')
            splitline = line.split(',')

            if len(splitline) == 14:
                splitline[13] = splitline[13].strip('\n')
                numframe = list(map(float,splitline))                
                argdef_queueProducer.put(numframe)
                print("Put: " + str(numframe))
        except serial.SerialException:
            # There is no new data from serial port
            ser.close()
            flagserial = False            

  

# ***************************************************************************************************************************************** #
# Main
# ***************************************************************************************************************************************** #
if __name__ == "__main__":
    app_main = QApplication(sys.argv)
    app_main.setStyle(QStyleFactory.create('Fusion'))    # ['windowsvista', 'Windows', 'Fusion']

    objclsConfigurationDialog_ConfigurationWindow = clsConfigurationDialog()
    
    sys.exit(app_main.exec_())