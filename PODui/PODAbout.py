import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
# from PODWelcomePage import showSelf

class about(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui(self)

    def init_ui(self, *args):
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
        self.backButton.setText('Back')
        self.backButton.move(480, 290)
        self.backButton.resize(100, 40);
        self.backButton.setStyleSheet("background-color:#FFFFFF")
        self.backButton.setFont(self.buttonFont)
        # self.backButton.clicked.connect(self.back)
        self.show()
    #
    # def back(self):
    #     self.hide()
    #     showSelf()
