from PyQt4 import QtGui
from Action.Behavior import Behavior
from UI.BehaviorPushButton import BehaviorPushButton


class Empathy(QtGui.QWidget):
    def __init__(self, parent, actionQueue):
        super(Empathy, self).__init__(parent)
        self._actionQueue = actionQueue

        self.chinScratch = BehaviorPushButton(self, "Scratch Chin", "chinScratch")
        self.chinScratch.execute.connect(self.on__BehaviorButton_clicked)

        self.pointLeft = BehaviorPushButton(self, "Left Hand Point", "leftHandPointing")
        self.pointLeft.execute.connect(self.on__BehaviorButton_clicked)

        self.pointRight = BehaviorPushButton(self, "Right Hand Point", "rightHandPointing")
        self.pointRight.execute.connect(self.on__BehaviorButton_clicked)

        self.scratchHead = BehaviorPushButton(self, "Scratch Head", "shakeHand")
        self.scratchHead.execute.connect(self.on__BehaviorButton_clicked)

        hbox1 = QtGui.QVBoxLayout()
        hbox2 = QtGui.QVBoxLayout()

        hbox1.addWidget(self.chinScratch)
        hbox1.addWidget(self.scratchHead)
        hbox1.addWidget(self.pointRight)
        hbox1.addWidget(self.pointLeft)

        layout = QtGui.QHBoxLayout(self)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
    #END __init__()

    def on__BehaviorButton_clicked(self, motion):
        self._actionQueue.enqueue(Behavior(motion))
    #END on__BehaviorButton_clicked()
#END Empathy
