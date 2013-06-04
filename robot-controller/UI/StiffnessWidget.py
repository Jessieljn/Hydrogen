from PyQt4 import QtCore, QtGui


##
# StiffnessWidget.py
#
# Sets the stiffness of the NAO.
##
class StiffnessWidget(QtGui.QGroupBox):
    def __init__(self, parent):
        super(StiffnessWidget, self).__init__(parent)
        self.setTitle("Stiffness")

        self._rdbtnOff = QtGui.QRadioButton("Off")
        self._rdbtnOff.setChecked(True)
        self._rdbtnLow = QtGui.QRadioButton("Low")
        self._rdbtnMed = QtGui.QRadioButton("Med")
        self._rdbtnHigh = QtGui.QRadioButton("High")

        self._btnGrp = QtGui.QButtonGroup()
        self._btnGrp.addButton(self._rdbtnOff)
        self._btnGrp.addButton(self._rdbtnLow)
        self._btnGrp.addButton(self._rdbtnMed)
        self._btnGrp.addButton(self._rdbtnHigh)
        self._btnGrp.buttonClicked.connect(self.on_btnGrp_buttonClicked)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.addWidget(self._rdbtnOff)
        layoutMain.addWidget(self._rdbtnLow)
        layoutMain.addWidget(self._rdbtnMed)
        layoutMain.addWidget(self._rdbtnHigh)
    #END __init__()

    stiffnessChanged = QtCore.pyqtSignal(float)

    def on_btnGrp_buttonClicked(self, button):
        if button == self._rdbtnOff:
            self.stiffnessChanged.emit(0.0)
        elif button == self._rdbtnLow:
            self.stiffnessChanged.emit(0.25)
        elif button == self._rdbtnMed:
            self.stiffnessChanged.emit(0.5)
        elif button == self._rdbtnHigh:
            self.stiffnessChanged.emit(1.0)
        #END if
    #END on__btnGrp_buttonClicked()
#END class
