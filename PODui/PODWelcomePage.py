import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PODCreateNewExperiment import createNew
from PODViewExperiment import viewExperiment
from PODAbout import about

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.init_ui()

    def init_ui(self):
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
        self.viewExperimentButton.clicked.connect(self.openViewWindow)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText('Create New \nExperiment')
        self.createButton.move(15, 150)
        self.createButton.resize(150, 60);
        self.createButton.setStyleSheet("background-color:#FFFFFF")
        self.createButton.setFont(self.buttonFont)
        self.createButton.clicked.connect(self.openCreateNewWindow)

        self.aboutButton = QtWidgets.QPushButton(self)
        self.aboutButton.setText('About P.O.D.')
        self.aboutButton.move(15, 220)
        self.aboutButton.resize(150, 60);
        self.aboutButton.setStyleSheet("background-color:#FFFFFF")
        self.aboutButton.setFont(self.buttonFont)
        self.aboutButton.clicked.connect(self.openAboutWindow)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.move(15, 290)
        self.exitButton.resize(150, 60);
        self.exitButton.setStyleSheet("background-color:#FFFFFF")
        self.exitButton.setFont(self.buttonFont)
        self.exitButton.clicked.connect(self.close)

        self.show()
        sys.exit(app.exec_())

    def openCreateNewWindow(self):
        self.hide()
        self.dialog = createNew()
        self.dialog.show()

    def openViewWindow(self):
        self.hide()
        self.dialog = viewExperiment()
        self.dialog.show()

    def openAboutWindow(self):
        self.hide()
        self.dialog = about()
        self.dialog.show()

    def showSelf(self):
        self.show()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
