from PyQt4 import QtCore
from PyQt4 import QtGui


###
# AboutWindow.py
#
# Creates an about window with a link to the HCI Website.
###
class AboutWindow(QtGui.QDialog):
    def __init__(self, parent):
        super(AboutWindow, self).__init__(parent)

        self._label0 = QtGui.QLabel("NAO Robotic Controller", self)
        self._label1 = QtGui.QLabel("<qt><a href=http://www.hci.cs.umanitoba.ca>Human Computer Interaction "
                                    "Laboratory, University of Manitoba</a></qt>", self)
        self._label1.linkActivated.connect(self.OpenURL)

        self._btnClose = QtGui.QPushButton('Close', self)
        self._btnClose.setMaximumWidth(120)
        self._btnClose.clicked.connect(self.on__btnClose_triggered)

        self._layoutGrid = QtGui.QVBoxLayout(self)
        self._layoutGrid.setContentsMargins(10, 10, 10, 10)
        self._layoutGrid.setSpacing(6)
        self._layoutGrid.addWidget(self._label0, 0, QtCore.Qt.AlignCenter)
        self._layoutGrid.addWidget(self._label1, 0, QtCore.Qt.AlignCenter)
        self._layoutGrid.addWidget(self._btnClose, 0, QtCore.Qt.AlignCenter)

        self.setFixedSize(500, 100)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('About')
    #END __init__()

    def OpenURL(self, URL):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(URL))
    #END OpenURL()

    def on__btnClose_triggered(self):
        self.setResult(QtGui.QDialog.Accepted)
        self.accept()
        self.close()
    #END on__btnOkay_triggered()
#END AboutWindow.py