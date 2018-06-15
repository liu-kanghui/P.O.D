#!/bin/python3

# import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import calendar
import time


class start(QMainWindow):
    def __init__(self):
        super(start, self).__init__(None)
        self.home = home()

    def toHome(self):
        self.home.show()
        self.hide()

class home(QMainWindow):
    def __init__(self):
        super(home, self).__init__(None)
        self.setupUi()
        self.viewExperimentButton.clicked.connect(self.toViewExperimentWindow)
        self.createButton.clicked.connect(self.toCreateWindow)
        self.aboutButton.clicked.connect(self.toAboutWindow)
        self.viewExperimentWindow = viewExperimentWindow(self)
        self.createWindow = createWindow(self)
        self.aboutWindow = aboutWindow(self)


    def setupUi(self):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.setStyleSheet("background-color:#98FB98");

        # labels
        # Image logo
        self.podLogo = QtWidgets.QLabel(self)
        self.originalpixmap = QtGui.QPixmap('podLogo1.png')
        self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.podLogo.setPixmap(self.adjustedPixmap)
        self.podLogo.move(15, 10)
        # Background label
        self.menuLabel = QtWidgets.QLabel(self)
        self.menuLabel.setGeometry(QtCore.QRect(180, 0, 730, 500))
        self.menuLabel.setStyleSheet("background-color:#FFFFFF")
        # Welcome Label
        self.welcomeLabel = QtWidgets.QLabel(self)
        self.welcomeLabel.setText('Welcome to P.O.D')
        self.welcomeLabel.move(250, 140)
        self.welcomeFont = QtGui.QFont("Times", 32, QtGui.QFont.Bold)
        self.welcomeLabel.setFont(self.welcomeFont)
        self.welcomeLabel.setStyleSheet("background-color:#FFFFFF")
        # pod label
        self.podLabel = QtWidgets.QLabel(self)
        self.podLabel.setText('Plant Observation Device')
        self.podLabel.move(300, 190)
        self.podFont = QtGui.QFont("Times", 18)
        self.podLabel.setFont(self.podFont)
        self.podLabel.setStyleSheet("background-color:#FFFFFF")
        # #98FB98
        self.podbackLabel = QtWidgets.QLabel(self)
        self.podbackLabel.setGeometry(QtCore.QRect(200, 200, 0, 0))
        self.podbackLabel.setStyleSheet("background-color:#98FB98")

        # Button font
        self.buttonFont = QtGui.QFont("Helvetica", 12)

        # BUTTONS
        self.viewExperimentButton = QtWidgets.QPushButton(self)
        self.viewExperimentButton.setText('View \nExperiments')
        self.viewExperimentButton.move(15, 80)
        self.viewExperimentButton.resize(150, 60);
        self.viewExperimentButton.setStyleSheet("background-color:#FFFFFF")
        self.viewExperimentButton.setFont(self.buttonFont)
        # self.viewExperimentButton.clicked.connect(self.openViewWindow)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Create New \nExperiment')
        self.createButton.move(15, 150)
        self.createButton.resize(150, 60);
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        # self.createButton.clicked.connect(self.openCreateNewWindow)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.aboutButton.setText('About P.O.D.')
        self.aboutButton.move(15, 220)
        self.aboutButton.resize(150, 60);
        self.aboutButton.setStyleSheet("background-color:#FFFFFF")
        self.aboutButton.setFont(self.buttonFont)
        # self.aboutButton.clicked.connect(self.openAboutWindow)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(15, 290)
        self.exitButton.resize(150, 60);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.show()

    def toViewExperimentWindow(self):
        self.viewExperimentWindow.show()
        self.hide()
        self.setEnabled(False)
        self.viewExperimentWindow.setEnabled(True)

    def toCreateWindow(self):
        self.createWindow.show()
        self.hide()
        self.setEnabled(False)
        self.createWindow.setEnabled(True)

    def toAboutWindow(self):
        self.aboutWindow.show()
        self.hide()
        self.setEnabled(False)
        self.aboutWindow.setEnabled(True)

    def reEnable(self):
        self.setEnabled(True)

class viewExperimentWindow(QMainWindow):
    def __init__(self, home):
        super(viewExperimentWindow, self).__init__(home)
        self.home = home
        self.setupUi()
        self.backButton.clicked.connect(self.toHome)

    def setupUi(self):
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

        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setText('Go Back')
        self.backButton.move(480, 300)
        self.backButton.resize(100, 40);
        self.backButton.setStyleSheet("background-color:#FFFFFF")
        self.backButton.setFont(self.buttonFont)
        # self.backButton.clicked.connect(self.goBack())

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
        self.tableWidget.resize(625, 205)
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


    def toHome(self):
        self.home.show()
        self.home.setEnabled(True)
        self.hide()


class createWindow(QMainWindow):
    def __init__(self, home):
        super(createWindow, self).__init__(home)
        self.home = home
        self.setupUi()
        self.backButton.clicked.connect(self.toHome)

    def setupUi(self):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.setStyleSheet("background-color:#FFFFFF");

        # labels
        # Background label
        self.menuLabel = QtWidgets.QLabel(self)
        self.menuLabel.setGeometry(QtCore.QRect(0, 0, 175, 70))
        self.menuLabel.setStyleSheet("background-color:#98FB98")

        self.podbackLabel = QtWidgets.QLabel(self)
        self.podbackLabel.setGeometry(QtCore.QRect(175, 0, 600, 70))
        self.podbackLabel.setStyleSheet("background-color:#FFFFFF")
        # Image logo
        self.podLogo = QtWidgets.QLabel(self)
        self.originalpixmap = QtGui.QPixmap('podLogo1.png')
        self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.podLogo.setPixmap(self.adjustedPixmap)
        self.podLogo.setStyleSheet("background-color:#98FB98")
        self.podLogo.move(15, 10)
        # Create new experiment labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('Create New Experiment')
        self.createNewLabel.move(250, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")

        self.inputFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        # Experiment name
        self.experimentNameLabel = QtWidgets.QLabel(self)
        self.experimentNameLabel.setText('Experiment Name:')
        self.experimentNameLabel.move(15, 90)
        self.experimentNameLabel.setFont(self.inputFont)
        # experiment name textbox
        self.experimentNameTextBox = QtWidgets.QLineEdit(self)
        self.experimentNameTextBox.move(150, 90)
        self.experimentNameTextBox.resize(150,25)
        self.experimentNameTextBox.setStyleSheet("background-color:#FFFFFF")

        # Group name
        # self.groupNameLabel = QtWidgets.QLabel(self)
        # self.groupNameLabel.setText('Group Name:')
        # self.groupNameLabel.move(15, 120)
        # self.groupNameLabel.setFont(self.inputFont)
        # # group name textbox
        # self.groupNameTextBox = QtWidgets.QLineEdit(self)
        # self.groupNameTextBox.move(150, 120)
        # self.groupNameTextBox.resize(150,25)
        # self.groupNameTextBox.setStyleSheet("background-color:#FFFFFF")

        # # POD Number
        # self.PODNumLabel = QtWidgets.QLabel(self)
        # self.PODNumLabel.setText('P.O.D. Number:')
        # self.PODNumLabel.move(15, 120)
        # self.PODNumLabel.setFont(self.inputFont)
        # # POD number textbox
        # self.PODNumberTextBox = QtWidgets.QLineEdit(self)
        # self.PODNumberTextBox.move(150, 120)
        # self.PODNumberTextBox.resize(150,25)
        # self.PODNumberTextBox.setStyleSheet("background-color:#FFFFFF")

        # Start Experiment Time
        self.startTimeLabel = QtWidgets.QLabel(self)
        self.startTimeLabel.setText('Start Time:')
        self.startTimeLabel.move(320, 90)
        self.startTimeLabel.setFont(self.inputFont)
        # End Time
        self.endTimeLabel = QtWidgets.QLabel(self)
        self.endTimeLabel.setText('End Time:')
        self.endTimeLabel.move(320, 120)
        self.endTimeLabel.setFont(self.inputFont)

        # Pictures per day label
        self.pictureLabel = QtWidgets.QLabel(self)
        self.pictureLabel.setText('Pictures per day:')
        self.pictureLabel.move(15, 180)
        self.pictureLabel.setFont(self.inputFont)

        # Pictures per day
        self.picturesPerDay = QtWidgets.QSpinBox(self)
        self.picturesPerDay.move(140, 180)

        # Button font
        self.buttonFont = QtGui.QFont("Helvetica", 12)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(70, 300)
        self.exitButton.resize(100, 40);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Add Group')
        self.createButton.move(210, 300)
        self.createButton.resize(100, 40)
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        self.createButton.clicked.connect(self.openAddGroup)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Create')
        self.createButton.move(480, 300)
        self.createButton.resize(100, 40);
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        self.createButton.clicked.connect(self.createExperiment)

        self.startDate = QtWidgets.QDateEdit(self)
        self.startDate.setDisplayFormat("MMM d yyyy")
        self.startDate.setDate(QtCore.QDate.currentDate())
        self.startDate.move(420, 90)

        self.startTime = QtWidgets.QTimeEdit(self)
        self.startTime.setDisplayFormat('hh:mm AP')
        self.startTime.move(540, 90)

        self.endDate = QtWidgets.QDateEdit(self)
        self.endDate.setDisplayFormat("MMM d yyyy")
        self.endDate.setDate(QtCore.QDate.currentDate())
        self.endDate.move(420, 120)

        self.endTime = QtWidgets.QTimeEdit(self)
        self.endTime.setDisplayFormat('hh:mm AP')
        self.endTime.move(540, 120)

        # Water Cycle label
        self.waterCycleLabel = QtWidgets.QLabel(self)
        self.waterCycleLabel.setText('Water Cycle (Hours):')
        self.waterCycleLabel.move(15, 120)
        self.waterCycleLabel.setFont(self.inputFont)

        # Watering Time label
        self.waterTimeLabel = QtWidgets.QLabel(self)
        self.waterTimeLabel.setText('Watering Time (Seconds):')
        self.waterTimeLabel.move(15, 150)
        self.waterTimeLabel.setFont(self.inputFont)

        # Water number textbox
        self.waterTime = QtWidgets.QTimeEdit(self)
        self.waterTime.setDisplayFormat('hh')
        self.waterTime.move(200, 120)

        # Water number textbox
        self.wateringTime = QtWidgets.QTimeEdit(self)
        self.wateringTime.setDisplayFormat('ss')
        self.wateringTime.move(200, 150)

        # light label
        self.waterCycleLabel = QtWidgets.QLabel(self)
        self.waterCycleLabel.setText('Input CSV file for Lights:')
        self.waterCycleLabel.move(320, 150)
        self.waterCycleLabel.setFont(self.inputFont)

        self.csvFileTextBox = QtWidgets.QLineEdit(self)
        self.csvFileTextBox.move(405, 180)
        self.csvFileTextBox.resize(180, 25)
        self.csvFileTextBox.setStyleSheet("background-color:#D3D3D3")
        self.csvFileTextBox.setDisabled(True)

        # Light error label
        self.lightErrorLabel = QtWidgets.QLabel(self)
        self.lightErrorLabel.setText('Light Error:')
        self.lightErrorLabel.move(320, 210)
        self.lightErrorLabel.setFont(self.inputFont)

        # Light error
        self.lightError = QtWidgets.QSpinBox(self)
        self.lightError.setMaximum(1000)
        self.lightError.move(410, 210)

        # Light error label
        self.tempErrorLabel = QtWidgets.QLabel(self)
        self.tempErrorLabel.setText('Temperature Error:')
        self.tempErrorLabel.move(15, 240)
        self.tempErrorLabel.setFont(self.inputFont)

        # Temperature Cycle label
        self.tempCycleLabel = QtWidgets.QLabel(self)
        self.tempCycleLabel.setText('Temperature Cycle (Min):')
        self.tempCycleLabel.move(15, 210)
        self.tempCycleLabel.setFont(self.inputFont)

        # temp error
        self.tempCycle = QtWidgets.QSpinBox(self)
        self.tempCycle.setMaximum(1000)
        self.tempCycle.move(200, 210)

        # temp error
        self.tempError = QtWidgets.QSpinBox(self)
        self.tempError.setMaximum(1000)
        self.tempError.move(165, 240)

        self.browseButton = QtWidgets.QPushButton(self)
        self.browseButton.setText('Browse')
        self.browseButton.move(323, 182)
        self.browseButton.resize(80, 20);
        self.browseButton.setStyleSheet("background-color:#FFFFFF")
        self.browseButton.setFont(self.buttonFont)
        self.browseButton.clicked.connect(self.openCSVFile)

        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setText('Go Back')
        self.backButton.move(340, 300)
        self.backButton.resize(100, 40);
        self.backButton.setStyleSheet("background-color:#FFFFFF")
        self.backButton.setFont(self.buttonFont)

    def openAddGroup(self):
        self.hide()
        self.dialog = addGroup()
        self.dialog.show()

    def openCSVFile(self):
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        self.file = QtCore.QFileInfo(self.path).fileName()
        # print(self.file)
        self.csvFileTextBox.setStyleSheet("background-color:#FFFFFF")
        self.csvFileTextBox.setText(self.file)

    def createExperiment(self):
        with open("currentExperiments/" + self.experimentNameTextBox.text() + ".csv", 'w') as self.f:
            # start time
            self.f.write("exp_start "+ str(calendar.timegm(time.strptime(self.endDate.date().toString("MMM d, yyyy") + ' @ ' + self.endTime.time().toString("hh:mm:ss") + ' UTC', '%b %d, %Y @ %H:%M:%S UTC'))) + "\n")
            # print(calendar.timegm(time.strptime(self.startDate.date().toString("MMM d, yyyy") + ' @ ' + self.startTime.time().toString("hh:mm:ss") + ' UTC', '%b %d, %Y @ %H:%M:%S UTC')))
            # print(calendar.timegm(time.strptime(self.endDate.date().toString("MMM d, yyyy") + ' @ ' + self.endTime.time().toString("hh:mm:ss") + ' UTC', '%b %d, %Y @ %H:%M:%S UTC')))
            # experiment duration
            self.f.write("exp_duration " + str(calendar.timegm(time.strptime(self.endDate.date().toString("MMM d, yyyy") + ' @ ' + self.endTime.time().toString("hh:mm:ss") + ' UTC', '%b %d, %Y @ %H:%M:%S UTC')) - calendar.timegm(time.strptime(self.startDate.date().toString("MMM d, yyyy") + ' @ ' + self.startTime.time().toString("hh:mm:ss") + ' UTC', '%b %d, %Y @ %H:%M:%S UTC'))))
            self.f.write('\n')
            # csv file
            self.f.write("csv_filename " + self.file)
            self.f.write('\n')
            # water delay
            self.f.write("water_delay " + self.waterTime.time().toString("hh") + "\n")
            # water duration
            self.f.write("water_duration " + self.wateringTime.time().toString("ss") + "\n")
            # light delay
            self.f.write("lightsensor_delay " + "2\n")
            # light error
            self.f.write("lightsensor_error " + str(self.lightError.value()) + "\n")
            # temp delay
            self.f.write("tempsensor_delay " + str(self.tempCycle.value()) + "\n")
            # temp error
            self.f.write("tempsensor_error " + str(self.tempError.value()) + "\n")
            # photo delay
            self.f.write("picture_delay " + str(int(24 / self.picturesPerDay.value())))

    def toHome(self):
        self.home.show()
        self.home.setEnabled(True)
        self.hide()

class aboutWindow(QMainWindow):
    def __init__(self, home):
        super(aboutWindow, self).__init__(home)
        self.home = home
        self.setupUi()
        self.backButton.clicked.connect(self.toHome)


    def setupUi(self):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.podbackLabel = QtWidgets.QLabel(self)
        self.podbackLabel.setGeometry(QtCore.QRect(175, 0, 600, 70))
        self.podbackLabel.setStyleSheet("background-color:#FFFFFF")
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
        # Create new experiment labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('About P.O.D')
        self.createNewLabel.move(300, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")

        # About Paragraph
        self.aboutPodLabel = QtWidgets.QLabel(self)
        self.aboutPodLabel.setText('      Dr. Ben Miner from the Biology department at Western Washington University\nwants to know how different lighting patterns affect the growth of a specific type of plant.\nIn order to determine the effects of variable lighting on these plants, an experiment\nmust be conducted using our POD devices.')
        self.aboutPodLabel.move(25, 75)
        self.paragraphFont = QtGui.QFont("Times", 12)
        self.aboutPodLabel.setFont(self.paragraphFont)
        self.aboutPodLabel.resize(600, 100);
        # Second About Paragraph
        self.secondAboutPodLabel = QtWidgets.QLabel(self)
        self.secondAboutPodLabel.setText('      The PODs will use software interacting with sensors on a Raspberry Pi to adjust\nlighting, water plants and document the growth of each plant. By the end of this project, we\nshould be able to find out how various lighting patterns can change the growth\nof these plants.')
        self.secondAboutPodLabel.move(25, 150)
        self.secondAboutPodLabel.setFont(self.paragraphFont)
        self.secondAboutPodLabel.resize(600, 100);
        # Button font
        self.buttonFont = QtGui.QFont("Helvetica", 12)
        # Exit Button
        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(70, 290)
        self.exitButton.resize(100, 40);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setText('Go Back')
        self.backButton.move(480, 290)
        self.backButton.resize(100, 40);
        self.backButton.setStyleSheet("background-color:#FFFFFF")
        self.backButton.setFont(self.buttonFont)

    def toHome(self):
        self.home.show()
        self.home.setEnabled(True)
        self.hide()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = start()
    sys.exit(app.exec_())
