import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("P.O.D.")

        # far down on page, far left on page, width, height
        self.setGeometry(325, 100, 650, 400)

        # self.setStyleSheet("background-color:#CGCGCG");

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
        # Add Group labels
        self.createNewLabel = QtWidgets.QLabel(self)
        self.createNewLabel.setText('Add Group')
        self.createNewLabel.move(320, 15)
        self.createFont = QtGui.QFont("Times", 24, QtGui.QFont.Bold)
        self.createNewLabel.setFont(self.createFont)
        self.createNewLabel.setStyleSheet("background-color:#FFFFFF")
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

        editBox = QLineEdit('Drag this', self)
        editBox.setDragEnabled(True)
        editBox.move(10, 10)
        editBox.resize(100,32)

        button = CustomLabel('Drop here.', self)
        button.resize(200,100)
        button.setStyleSheet("background-color:white")
        button.move(130,15)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

class CustomLabel(QLabel):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
