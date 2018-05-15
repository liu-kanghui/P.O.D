import sys
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets

class InitialCard(QtWidgets.QLabel):
    def __init__(self, text, parent):
        super(InitialCard, self).__init__(text, parent)
        self.setAutoFillBackground(True)
        self.setFrameStyle(QtWidgets.QFrame.WinPanel|QtWidgets.QFrame.Sunken)
        newFont = QtGui.QFont("MsReferenceSansSerif", 10)
        newFont.setBold(False)
        self.setFont(newFont)
        self.setMinimumSize(90, 25)
        self.setMaximumHeight(30)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.mimeText=self.text()

    def mouseMoveEvent(self, event):
        if not self.text():
            return
        mimeData = QtCore.QMimeData()
        mimeData.setText(self.mimeText)
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction, QtCore.Qt.CopyAction)

class CardsDropWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(CardsDropWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.contentsVLO = QtWidgets.QVBoxLayout()
        self.contentsVLO.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.contentsVLO)


    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            cardSource=event.source()
            cardText=cardSource.text()
            if not cardSource in self.children():
                newCard = InitialCard(cardText, self)
                self.contentsVLO.addWidget(newCard)
                cardSource.clear()
            else:
                event.ignore()
        else:
            event.ignore()

class addGroup(QtWidgets.QWidget):
    # def __init__(self):
    #     super().__init__()
    #
    #     self.init_ui(self)
    #
    # def init_ui(self, *args):
    #     self.setWindowTitle("P.O.D.")
    #
    #     # far down on page, far left on page, width, height
    #     self.setGeometry(325, 100, 650, 400)
    #
    #     # self.setStyleSheet("background-color:#CGCGCG");
    #
    #     # labels
    #     # Background label
    #     self.menuLabel = QtWidgets.QLabel(self)
    #     self.menuLabel.setGeometry(QtCore.QRect(0, 0, 175, 70))
    #     self.menuLabel.setStyleSheet("background-color:#98FB98")
    #
    #     self.podbackLabel = QtWidgets.QLabel(self)
    #     self.podbackLabel.setGeometry(QtCore.QRect(175, 0, 600, 70))
    #     self.podbackLabel.setStyleSheet("background-color:#FFFFFF")
    #     # Image logo
    #     self.podLogo = QtWidgets.QLabel(self)
    #     self.originalpixmap = QtGui.QPixmap('podLogo1.png')
    #     self.adjustedPixmap = self.originalpixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
    #     self.podLogo.setPixmap(self.adjustedPixmap)
    #     self.podLogo.setStyleSheet("background-color:#98FB98")
    #     self.podLogo.move(15, 10)
    #     # Add Group labels
    #     self.createNewLabel = QtWidgets.QLabel(self)
    #     self.createNewLabel.setText('Add Group')
    #     self.createNewLabel.move(320, 15)
    #     self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
    #     self.createNewLabel.setFont(self.createFont)
    #     self.createNewLabel.setStyleSheet("background-color:#FFFFFF")
    #
    #     self.inputFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
    #     # Experiment name
    #     self.addToCurrGroupLabel = QtWidgets.QLabel(self)
    #     self.addToCurrGroupLabel.setText('Add to Current Group:')
    #     self.addToCurrGroupLabel.move(15, 90)
    #     self.addToCurrGroupLabel.setFont(self.inputFont)
    #
    #     self.tableWidget = QtWidgets.QTableWidget(self)
    #     # set row count
    #     self.tableWidget.setRowCount(4)
    #     # set column count
    #     self.tableWidget.setColumnCount(2)
    #     self.tableWidget.setHorizontalHeaderLabels(('Available POD', 'Group'))
    #     self.tableWidget.move(10, 75)
    #     self.tableWidget.resize(630, 150)
    #     self.tableWidget.setColumnWidth(0, 310)
    #     self.tableWidget.setColumnWidth(1, 310)
    #
    #     # print(os.getcwd() + "/currentExperiments")
    #     self.directory = os.fsencode(os.getcwd() + "/currentExperiments")
    #     # print(self.directory)
    #     self.var = 0
    #     for self.file in os.listdir(self.directory):
    #            self.filename = os.fsdecode(self.file)
    #            # print(self.filename)
    #            with open("currentExperiments/" + self.filename, "r") as self.fileInput:
    #               self.reader = csv.reader(self.fileInput)
    #               self.fileContents = list(self.reader)
    #               self.tableWidget.setItem(self.var, 0, QtWidgets.QTableWidgetItem(str(self.fileContents[2]).strip("[]").strip("''")))
    #               self.tableWidget.setItem(self.var, 1, QtWidgets.QTableWidgetItem(str(self.fileContents[1]).strip('[]').strip("''")))
    #               self.var = self.var + 1
    #
    #     # Button font
    #     self.buttonFont = QtGui.QFont("Helvetica", 12)
    #
    #     self.exitButton = QtWidgets.QPushButton(self)
    #     self.exitButton.setText('Exit')
    #     self.exitButton.move(70, 300)
    #     self.exitButton.resize(100, 40);
    #     self.exitButton.setStyleSheet("background-color:#FFFFFF")
    #     self.exitButton.setFont(self.buttonFont)
    #     self.exitButton.clicked.connect(self.close)
    #
    #     self.show()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        self.setStyleSheet("background-color:white");

        self.label=InitialCard("Group", self)
        self.lineEdit=QtWidgets.QLineEdit("Create a New Group Here")
        self.lineEdit.selectAll()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = CardsDropWidget(self.scrollArea)
        self.scrollArea.setMinimumWidth(150)
        self.scrollArea.setWidget(self.scrollContent)
        self.dialogueLayout=QtWidgets.QHBoxLayout()
        self.labelLayout=QtWidgets.QVBoxLayout()
        self.labelLayout.addWidget(self.label)
        self.labelLayout.addWidget(self.lineEdit)
        self.labelLayout.addStretch()
        self.dialogueLayout.addWidget(self.scrollArea)
        self.dialogueLayout.addLayout(self.labelLayout)
        self.setLayout(self.dialogueLayout)
        self.setMinimumSize(300, 150)
        self.lineEdit.returnPressed.connect(self.createCardTxt_fn)

    def createCardTxt_fn(self):
        cardTxt=self.lineEdit.text()
        self.label.setText(cardTxt)
