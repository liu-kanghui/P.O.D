import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets

class viewExperiment(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui(self)

    def init_ui(self, *args):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.setStyleSheet("background-color:#FFFFFF");
        #98FB98

        # Create new experiment labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('View Experiments')
        self.createNewLabel.move(300, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")

        # labels
        # Background label
        self.menuLabel = QtWidgets.QLabel(self)
        self.menuLabel.setGeometry(QtCore.QRect(0, 0, 175, 70))
        self.menuLabel.setStyleSheet("background-color:#98FB98")
        # Image logo
        self.podLogo = QtWidgets.QLabel(self)
        self.originalpixmap = QtGui.QPixmap('podLogo1.png')
        self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.podLogo.setPixmap(self.adjustedPixmap)
        self.podLogo.setStyleSheet("background-color:#98FB98")
        self.podLogo.move(15, 10)

        # Button font
        self.buttonFont = QtGui.QFont("Helvetica", 12)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(70, 300)
        self.exitButton.resize(100, 40);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.currDir = 0
        # print(os.getcwd() + "/currentExperiments")
        self.directory = os.fsencode(os.getcwd() + "/currentExperiments")
        # print(self.directory)
        self.dirlist = os.listdir(self.directory) # dir is your directory path
        self.number_files = len(self.dirlist)
        # print(self.number_files)

        self.tableWidget = QtWidgets.QTableWidget(self)
        # set row count
        self.tableWidget.setRowCount(self.number_files)
        # set column count
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setHorizontalHeaderLabels(('Experiment Name', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Water Delay', 'Water Duration', 'Light Delay', 'Light Error', 'Temp Delay', 'Temp Error', 'Photo Delay', 'CSV File'))
        self.tableWidget.move(10, 75)
        self.tableWidget.resize(625, 275)
        self.tableWidget.setColumnWidth(0, 150)
        # # simple version for working with CWD
        # print(len([self.name for self.name in os.listdir('.') if os.path.isfile(self.name)]))


        for self.file in os.listdir(self.directory):
               self.filename = os.fsdecode(self.file)
               # print(self.filename)
               with open("currentExperiments/" + self.filename, "r") as self.fileInput:
                  self.reader = csv.reader(self.fileInput)
                  self.fileContents = list(self.reader)
                  # print(str(self.fileContents[0]).strip('[]'))
                  self.tableWidget.setItem(self.currDir, 5, QtWidgets.QTableWidgetItem(str(self.fileContents[3]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 6, QtWidgets.QTableWidgetItem(str(self.fileContents[4]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 7, QtWidgets.QTableWidgetItem(str(self.fileContents[5]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 8, QtWidgets.QTableWidgetItem(str(self.fileContents[6]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 9, QtWidgets.QTableWidgetItem(str(self.fileContents[7]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 10, QtWidgets.QTableWidgetItem(str(self.fileContents[8]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 11, QtWidgets.QTableWidgetItem(str(self.fileContents[9]).strip("[]").strip("''")))
                  # self.tableWidget.setItem(self.currDir, 12, QtWidgets.QTableWidgetItem(str(self.fileContents[11]).strip("[]").strip("''")))
                  self.tableWidget.setItem(self.currDir, 12, QtWidgets.QTableWidgetItem(str(self.fileContents[2]).strip("[]").strip("''")))

                  self.currDir = self.currDir + 1

        self.show()
