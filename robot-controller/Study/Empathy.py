from PyQt4 import QtGui
from Action.Behavior import Behavior
from Action.Speech import Speech
from UI.ActionPushButton import ActionPushButton


class Empathy(QtGui.QWidget):
    def __init__(self):
        super(Empathy, self).__init__()
        self._actionQueue = None

        self.chinScratch = ActionPushButton(self, "Scratch Chin", Behavior("chinScratch"))
        self.chinScratch.execute.connect(self.on_actionReceived)

        self.pointLeft = ActionPushButton(self, "Left Hand Point", Behavior("leftHandPointing"))
        self.pointLeft.execute.connect(self.on_actionReceived)

        self.pointRight = ActionPushButton(self, "Right Hand Point", Behavior("rightHandPointing"))
        self.pointRight.execute.connect(self.on_actionReceived)

        self.scratchHead = ActionPushButton(self, "Scratch Head", Behavior("shakeHand"))
        self.scratchHead.execute.connect(self.on_actionReceived)

        self.numsAre = ActionPushButton(self, "#s are", Speech("Possible numbers are"))
        self.numsAre.execute.connect(self.on_actionReceived)

        self.numIs = ActionPushButton(self, "# is", Speech("Possible number is"))
        self.numIs.execute.connect(self.on_actionReceived)

        self.numAnd = ActionPushButton(self, "And", Speech("And"))
        self.numAnd.execute.connect(self.on_actionReceived)

        self.numOne = ActionPushButton(self, "1: One", Speech("One"))
        self.numOne.execute.connect(self.on_actionReceived)

        self.numTwo = ActionPushButton(self, "2: Two", Speech("Two"))
        self.numTwo.execute.connect(self.on_actionReceived)

        self.numThree = ActionPushButton(self, "3: Three", Speech("Three"))
        self.numThree.execute.connect(self.on_actionReceived)

        self.numFour = ActionPushButton(self, "4: Four", Speech("Four"))
        self.numFour.execute.connect(self.on_actionReceived)

        self.numFive = ActionPushButton(self, "5: Five", Speech("Five"))
        self.numFive.execute.connect(self.on_actionReceived)

        self.numSix = ActionPushButton(self, "6: Six", Speech("Six"))
        self.numSix.execute.connect(self.on_actionReceived)

        self.numSeven = ActionPushButton(self, "7: Seven", Speech("Seven"))
        self.numSeven.execute.connect(self.on_actionReceived)

        self.numEight = ActionPushButton(self, "8: Eight", Speech("Eight"))
        self.numEight.execute.connect(self.on_actionReceived)

        self.numNine = ActionPushButton(self, "9: Nine", Speech("Nine"))
        self.numNine.execute.connect(self.on_actionReceived)

        self.cwPurposeGoal = ActionPushButton(self, "Purpose->Goal", Speech("Purpose, hmmm. Goal?"))
        self.cwPurposeGoal.execute.connect(self.on_actionReceived)

        self.cwPurposeAim = ActionPushButton(self, "Purpose->Aim", Speech("Oh, how about aim?"))
        self.cwPurposeAim.execute.connect(self.on_actionReceived)

        hbox1 = QtGui.QVBoxLayout()
        hbox2 = QtGui.QVBoxLayout()

        hbox1.addWidget(self.chinScratch)
        hbox1.addWidget(self.scratchHead)
        hbox1.addWidget(self.pointRight)
        hbox1.addWidget(self.pointLeft)

        hbox2.addWidget(self.numsAre)
        hbox2.addWidget(self.numIs)
        hbox2.addWidget(self.numAnd)
        hbox2.addWidget(self.numOne)
        hbox2.addWidget(self.numTwo)
        hbox2.addWidget(self.numThree)
        hbox2.addWidget(self.numFour)
        hbox2.addWidget(self.numFive)
        hbox2.addWidget(self.numSix)
        hbox2.addWidget(self.numSeven)
        hbox2.addWidget(self.numEight)
        hbox2.addWidget(self.numNine)
        hbox2.addWidget(self.cwPurposeGoal)
        hbox2.addWidget(self.cwPurposeAim)

        layout = QtGui.QHBoxLayout(self)
        layout.addLayout(hbox1)
        layout.addLayout(hbox2)
    #END __init__()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    #END on_actionReceived()
#END Empathy
