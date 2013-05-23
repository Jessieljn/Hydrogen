from PyQt4 import QtGui
from PyQt4 import QtCore


class Popup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Connection Window')
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))

    def paintEvent(self, e):
        dc = QtGui.QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)

    def doit(self):
        print "Opening Window"
        self.w = Popup()
        self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
        self.w.show()