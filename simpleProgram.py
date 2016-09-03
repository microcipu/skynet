#!/usr/bin/env python3

# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100, title='Default'):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.suptitle(title)

        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass



class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self, data):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], data, 'r')
        self.draw()

class ApplicationWindow(QtWidgets.QMainWindow):
    pret = 0
    sc = 0
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QGridLayout(self.main_widget)
        self.sc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='sc')
        self.dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='dc')
        self.pret = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='pret')
        self.val = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='val')
        self.profit = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='profit')
        self.test = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100, title='test')

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_plot)
        timer.start(10)

        l.addWidget(self.sc, 0, 1)
        l.addWidget(self.dc, 0, 2)
        l.addWidget(self.pret, 0, 3)
        l.addWidget(self.val, 1, 1)
        l.addWidget(self.profit, 1, 2)
        l.addWidget(self.test, 1, 3)


        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def update_plot(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.pret.update_figure(l)
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        pass

    def fileQuit(self):

        self.close()

    def closeEvent(self, comenzi):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About", "About")


class inputdialogdemo(QWidget):
    def __init__(self, parent=None):
        super(inputdialogdemo, self).__init__(parent)

        layout = QFormLayout()
        self.btn = QPushButton("Choose Product")
        self.btn.clicked.connect(self.getItem)

        self.le = QLineEdit()
        layout.addRow(self.btn, self.le)
        self.btn1 = QPushButton("Get price")
        self.btn1.clicked.connect(self.getprice)

        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)
        self.btn2 = QPushButton("Enter an discount")
        self.btn2.clicked.connect(self.getdiscount)

        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.le3 = QLineEdit()
        self.le3.setReadOnly(True)
        self.le3.setText(str('test categorie'))
        self.la3 = QLabel()
        self.la3.setText(str('Category'))
        layout.addRow(self.la3,self.le3)

        self.le4 = QLineEdit()
        self.le4.setReadOnly(True)
        self.le4.setText(str('test availability'))
        self.la4 = QLabel()
        self.la4.setText(str('Availability'))
        layout.addRow(self.la4, self.le4)

        self.le5 = QLineEdit()
        self.le5.setReadOnly(True)
        self.le5.setText(str('test rating'))
        self.la5 = QLabel()
        self.la5.setText(str('Rating'))
        layout.addRow(self.la5, self.le5)

        self.le6 = QLineEdit()
        self.le6.setReadOnly(True)
        self.le6.setText(str('test reviews'))
        self.la6 = QLabel()
        self.la6.setText(str('Reviews'))
        layout.addRow(self.la6, self.le6)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog")

    def getItem(self):
        items = ("iphone 6", "laptop dell", "masina de tuns iarba", "rucsac")

        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of products", items, 0, False)

        if ok and item:
            self.le.setText(item)

    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

        if ok:
            self.le1.setText(str(text))

    def getprice(self):
        num, ok = QInputDialog.getInt(self, "Price input dialog", "enter a price")

        if ok:
            self.le1.setText(str(num))

    def getdiscount(self):
        num, ok = QInputDialog.getInt(self, "Discount input dialog", "enter a discount value")

        if ok:
            self.le2.setText(str(num))

app = QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()

ex = inputdialogdemo()
ex.show()
sys.exit(app.exec_())
#qApp.exec_()