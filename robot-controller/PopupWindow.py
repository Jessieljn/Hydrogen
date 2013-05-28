from PyQt4 import QtGui
from PyQt4 import QtCore
from ConnectionWinClass import ConnectionWin
import Nao


##
# Popup.py
#
# Popup window for the connection class.
#
# TODO: Add on click connect for connection window.
##
class Popup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Connection Window')
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))

        self.connection = ConnectionWin

        self.conB = QtGui.QPushButton('Connect', self)
        self.ip = QtGui.QLineEdit('140.193.228.26', self)
        self.port = QtGui.QLineEdit('9559', self)

        self.dialogLabel = QtGui.QLabel("<qt> Please visit <a href = http://www.google.ca>Google</a>to search.</qt>", self)
        self.connect(self.dialogLabel, QtCore.SIGNAL("linkActivated(QString)"), self.OpenURL)

        self.conB.clicked.connect(self.passToMain)

        self.ip.move(105, 10)
        self.port.move(105, 30)
    #END __init__()

    def paintEvent(self, e):
        dc = QtGui.QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)
    #END paintEvent

    def doit(self):
        print "Opening Window"
        self.w = Popup()
        self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.w.show()
    #END doit

    def passToMain(self):
        li = [self.ip.displayText(), self.port.displayText()]
        self.nao.tryConnect(li)
        self.close()

    def OpenURL(self, URL):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(URL))
#END Popup