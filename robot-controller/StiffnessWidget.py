from PyQt4 import QtGui

class StiffnessWidget (QtGui.QGroupBox):
    def __init__(self, nao, parent):
        super(StiffnessWidget, self).__init__()
        self.setTitle("Stiffness")
        self.nao = nao

        self.buttons = QtGui.QButtonGroup()

        self.off = QtGui.QRadioButton("Off")
        self.low = QtGui.QRadioButton("Low")
        self.med = QtGui.QRadioButton("Med")
        self.high = QtGui.QRadioButton("High")

        self.buttons.addButton(self.off)
        self.buttons.addButton(self.low)
        self.buttons.addButton(self.med)
        self.buttons.addButton(self.high)

        self.off.setChecked(True)

        self.buttons.buttonClicked.connect(self.setStiffness)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.off)
        layout.addWidget(self.low)
        layout.addWidget(self.med)
        layout.addWidget(self.high)

        self.setLayout(layout)

    def setStiffness(self, button):
        if button == self.off:
            self.nao.setStiffness(0.0)
        elif button == self.low:
            self.nao.setStiffness(0.25)
        elif button == self.med:
            self.nao.setStiffness(0.5)
            pass
        elif button == self.high:
            self.nao.setStiffness(1.0)
