from PyQt4 import QtGui
from PyQt4 import QtCore


class AboutWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('About')
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))

        self.dialogLabel0 = QtGui.QLabel("NAO Robotic Controller", self)
        self.dialogLabel0.move(200, 10)

        self.dialogLabel1 = QtGui.QLabel("<qt><a href=http://www.hci.cs.umanitoba.ca>Human Computer Interaction "
                                         "Laboratory, University of Manitoba</a></qt>", self)
        self.dialogLabel1.move(100, 40)

        self.connect(self.dialogLabel1, QtCore.SIGNAL("linkActivated(QString)"), self.OpenURL)
    #END __init__()

    def doit(self):
        print "Opening Window"
        self.w = AboutWindow()
        self.w.setGeometry(QtCore.QRect(100, 100, 500, 100))
        self.w.show()
    #END doit

    def OpenURL(self, URL):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(URL))
    #END OpenURL
#END AboutWindow