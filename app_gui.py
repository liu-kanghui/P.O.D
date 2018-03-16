#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
# from Light import Lights
import detect_device_ip
import waterpump_server


''' this script is the pod application'''

Ui_MainWindow, QtBaseClass = uic.loadUiType("pod.ui")


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Open file
        # openFile = QtGui.QAction("&Open File", self)
        # self.ui.open_file_line_edit.clicke]d.connect(self.file_open)
        # self.ui.start_lights_button.clicked.connect(self.TurnOnOffLight)
        # self.ui.stop_lights_button.clicked.connect(self.TurnOffLight)
        self.ui.start_pumping_button.clicked.connect(self.TurnOnWaterPump)
        # self.ui.stop_pumping_button.clicked.connect(self.TurnOffWaterPump)

    def CalculateTax(self):
        price = int(self.ui.price_box.toPlainText())
        tax = (self.ui.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.ui.results_window.setText(total_price_string)

    # def TurnOnLight(self):
    #     connectedpiZeroHostDict = detect_device_ip.arp_scan()
    #     # assign all the pod to control light as hard on and off.
    #     # just for now testing.
    #     for name, host in connectedpiZeroHostDict.items():
    #         print(host)
    #         lightPattern = Lights('192.168.1.102')
    #         lightPattern.hardOnOffLED(1, 1, 120)
    #
    # def TurnOffLight(self):


    def TurnOnWaterPump(self):
        run_time = (self.ui.pump_run_time.value())
        delay_time = (self.ui.pump_delay_time.value())
        waterpump_server.pump_water('192.168.1.102', run_time, delay_time)

    def TurnOffWaterPump(self):
        run_time = 0
        delay_time = 0
        waterpump_server.pump_water('192.168.1.102', run_time, delay_time)

    # def file_open(self):
    #     name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
    #     file = open(name, 'r')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
