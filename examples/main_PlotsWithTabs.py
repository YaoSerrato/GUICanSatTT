import sys
import os
import signal
import random
import threading
import multiprocessing
import time
import psutil

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PlotsWithTabs_GUIcode import *
from matplotlib.animation import FuncAnimation
from itertools import count

from PyQt5.QtWidgets import QStyleFactory


#---------------- General Functions --------------------------
def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

#----------------------- Consumer --------------------------
class MyForm(QMainWindow):
# w = self
# w.ui = self.ui
    def __init__(self, queueGUI, producer_pid):
        super().__init__()

        self.index = 0
        self.xdata = []        
        self.ydata = []

        self.mutex = threading.Lock()
        self.flag = 1

        self.queueGUI = queueGUI
        self.producer_pid = producer_pid

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       # Here, all the graphical elements are created

        self.ui.pushButton_start.clicked.connect(self.Initializer)
        # self.ui.pushButton_stop.clicked.connect(self.Stopping)

    def Stopping(self):
        os.kill(self.producer_pid, signal.SIGTERM)
        self.tim.cancel()
        print("status producer: " + str(check_pid(self.producer_pid)))
        print(self.tim.isAlive)

    def Initializer(self):
        if self.flag:
            self.animate()
            self.flag = 0
            print("I have been pressed!")

    def animate(self):
        self.mutex.acquire()

        # print(threading.active_count())

        self.tim = threading.Timer(0.5,self.animate)
        self.tim.start() 

        # try:
        for i in range(0,self.queueGUI.qsize()):
            frame = self.queueGUI.get()
            self.ydata.append(frame[0])
            self.xdata.append(frame[1])       
        # except:
        #     pass

        # data = [random.random() for i in range(25)]
        self.ui.widget_graph_tab1.clearWG()

        self.ui.widget_graph_tab1.setWGtitle('Random generated numbers')
        self.ui.widget_graph_tab1.setWGxlabel('Sample [n]')
        self.ui.widget_graph_tab1.setWGylabel('Number [-]')
        self.ui.widget_graph_tab1.setWGylim(0, 1)
        self.ui.widget_graph_tab1.setWGxlim(max(0, self.xdata[-1] - 20), self.xdata[-1])
        self.ui.widget_graph_tab1.setWGgrid(True)

        self.ui.widget_graph_tab1.ax.plot(self.xdata, self.ydata)
        self.ui.widget_graph_tab1.draw()

        self.ui.lineEdit_serialRX.setText("Current tab is " + str(self.ui.tabWidget_graphs.currentIndex()))
        self.mutex.release()

def Plotter(queuePlotter, producer):
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))    # ['windowsvista', 'Windows', 'Fusion']

    w = MyForm(queuePlotter, producer)
    w.show()

    sys.exit(app.exec_())    

#----------------------- Producer --------------------------
def Producer(queueProducer):
    # time.sleep(20)
    cnt = 0
    while 1:
        num = random.random()
        cnt += 1
        queueProducer.put([num,cnt])
        print(f"The producer put {num} in the queue. Number {cnt}")
        time.sleep(.2)

#----------------------- Main --------------------------
if __name__=="__main__":
    # print(QStyleFactory.keys())

    queue = multiprocessing.Queue()

    processProducer = multiprocessing.Process(target = Producer, name = "processProducer", args=(queue,))    
    processProducer.start()

    processPlotter = multiprocessing.Process(target = Plotter, name = "processPlotter", args=(queue,processProducer.pid))
    processPlotter.start()
