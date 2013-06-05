from PyQt4 import QtCore, QtGui


class AboutWindow(QtGui.QDialog):
    def __init__(self, parent):
        super(AboutWindow, self).__init__(parent)

        self._label0 = QtGui.QLabel("NAO Robotic Controller", self)

        self._label1 = QtGui.QLabel("<qt><a href=http://www.hci.cs.umanitoba.ca>Human Computer Interaction "
                                    "Laboratory, University of Manitoba</a></qt>", self)
        self._label1.linkActivated.connect(self.OpenURL)

        self._btnOkay = QtGui.QPushButton('Okay', self)
        self._btnOkay.setMaximumWidth(120)
        self._btnOkay.clicked.connect(self.on__btnOkay_triggered)

        self._layoutGrid = QtGui.QVBoxLayout(self)
        self._layoutGrid.setContentsMargins(10, 10, 10, 10)
        self._layoutGrid.setSpacing(6)
        self._layoutGrid.addWidget(self._label0, 0, QtCore.Qt.AlignCenter)
        self._layoutGrid.addWidget(self._label1, 0, QtCore.Qt.AlignCenter)
        self._layoutGrid.addWidget(self._btnOkay, 0, QtCore.Qt.AlignCenter)

        self.setFixedSize(500, 100)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle('About')
    #END __init__()

    def OpenURL(self, URL):
        QtGui.QDesktopServices().openUrl(QtCore.QUrl(URL))
    #END OpenURL()

    def on__btnOkay_triggered(self):
        self.setResult(QtGui.QDialog.Accepted)
        self.accept()
        self.close()
    #END on__btnOkay_triggered()
#END AboutWindow