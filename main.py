from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtGui
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
from deneme2 import Ui_MainWindow
import numpy as np

angle=0
class deneme(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()#sınıflardan nesne oluşturmak için
        self.ui.setupUi(self)
        self.ui2=Canvas()

        ##############################################################################################################
        self.ui.horizontalSlider.setMinimum(100)
        self.ui.horizontalSlider.setMaximum(2000)
        self.ui.horizontalSlider.setSingleStep(1)
        self.ui.horizontalSlider.valueChanged.connect(self.slider1)

        self.ui.horizontalSlider_2.setMinimum(4)
        self.ui.horizontalSlider_2.setMaximum(24)
        self.ui.horizontalSlider_2.setSingleStep(0.2)
        self.ui.horizontalSlider_2.valueChanged.connect(self.slider2)

        palette = self.ui.lcdNumber_2.palette()
        palette.setColor(palette.Light, QtGui.QColor(1, 0, 0))
        self.ui.lcdNumber_2.setPalette(palette)
        self.ui.lcdNumber.setPalette(palette)
        self.ui.lcdNumber_3.setPalette(palette)

        self.MyUI()

    def slider1(self):

        # self.horizontalSlider_2.setValue(int(self.horizontalSlider.value()))
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        global angle
        angle = self.ui.horizontalSlider.value()
        self.MyUI()



    def slider2(self):
        self.ui.lcdNumber_2.display(self.ui.horizontalSlider_2.value())




    def MyUI(self):
        canvas = Canvas(self, width=4, height=3)
        canvas.move(330, 5)
        print("deneme")




class Canvas(FingureCanvas):

    def __init__(self, parent=None, width=18, height=18, dpi=80):


        fig = Figure(figsize=(width, height), dpi=dpi)
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        print(angle)
        self.plot()

    def plot(self):
        x = [150, 1]
        cols = ["lightgrey", "k"]
        ax = self.figure.add_subplot(111)
        ax.pie(x, colors=cols, startangle=angle, radius=1.55)





uygulama=QApplication([])
pencere=deneme()
pencere.show()
uygulama.exec_()
