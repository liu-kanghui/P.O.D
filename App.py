#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from Light import Lights
import DetectDevice

''' this script is the pod application'''

Ui_MainWindow, QtBaseClass = uic.loadUiType("pod.ui")


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        connectedDevicesIP = DetectDevice.arpScan()
        # assign all the pod to control light as hard on and off.
        # just for now testing.
        for ip in connectedDevicesIP:
            lightPattern = Lights(ip)
            lightPattern.hardOnOffLED(1, 1, 120)
        self.ui.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        L = Lights()
        for i in range(100, 255):
            L.runLights(i)
        price = int(self.ui.price_box.toPlainText())
        tax = (self.ui.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.ui.results_window.setText(total_price_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
