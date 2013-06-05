from PyQt4 import QtGui
from Action.Behavior import Behavior
from Action.Speech import Speech
from UI.BehaviorPushButton import BehaviorPushButton
from UI.SpeechPushButton import SpeechPushButton


class Empathy(QtGui.QWidget):
    def __init__(self):
        super(Empathy, self).__init__()
        self._actionQueue = None

        self.chinScratch = BehaviorPushButton(self, "Scratch Chin", "chinScratch")
        self.chinScratch.execute.connect(self.on__BehaviorButton_clicked)

        self.pointLeft = BehaviorPushButton(self, "Left Hand Point", "leftHandPointing")
        self.pointLeft.execute.connect(self.on__BehaviorButton_clicked)

        self.pointRight = BehaviorPushButton(self, "Right Hand Point", "rightHandPointing")
        self.pointRight.execute.connect(self.on__BehaviorButton_clicked)

        self.scratchHead = BehaviorPushButton(self, "Scratch Head", "shakeHand")
        self.scratchHead.execute.connect(self.on__BehaviorButton_clicked)

        self.numsAre = SpeechPushButton(self, "#s are", "Possible numbers are")
        self.numsAre.execute.connect(self.on__SpeechButton_clicked)

        self.numIs = SpeechPushButton(self, "# is", "Possible number is")
        self.numIs.execute.connect(self.on__SpeechButton_clicked)

        self.numAnd = SpeechPushButton(self, "And", "And")
        self.numAnd.execute.connect(self.on__SpeechButton_clicked)

        self.numOne = SpeechPushButton(self, "1: One", "One")
        self.numOne.execute.connect(self.on__SpeechButton_clicked)

        self.numTwo = SpeechPushButton(self, "2: Two", "Two")
        self.numTwo.execute.connect(self.on__SpeechButton_clicked)

        self.numThree = SpeechPushButton(self, "3: Three", "Three")
        self.numThree.execute.connect(self.on__SpeechButton_clicked)

        self.numFour = SpeechPushButton(self, "4: Four", "Four")
        self.numFour.execute.connect(self.on__SpeechButton_clicked)

        self.numFive = SpeechPushButton(self, "5: Five", "Five")
        self.numFive.execute.connect(self.on__SpeechButton_clicked)

        self.numSix = SpeechPushButton(self, "6: Six", "Six")
        self.numSix.execute.connect(self.on__SpeechButton_clicked)

        self.numSeven = SpeechPushButton(self, "7: Seven", "Seven")
        self.numSeven.execute.connect(self.on__SpeechButton_clicked)

        self.numEight = SpeechPushButton(self, "8: Eight", "Eight")
        self.numEight.execute.connect(self.on__SpeechButton_clicked)

        self.numNine = SpeechPushButton(self, "9: Nine", "Nine")
        self.numNine.execute.connect(self.on__SpeechButton_clicked)

        self.cwPurposeGoal = SpeechPushButton(self, "Purpose->Goal", "Purpose, hmmm. Goal?")
        self.cwPurposeGoal.execute.connect(self.on__SpeechButton_clicked)

        self.cwPurposeAim = SpeechPushButton(self, "Purpose->Aim", "Oh, how about aim?")
        self.cwPurposeAim.execute.connect(self.on__SpeechButton_clicked)

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

    def on__BehaviorButton_clicked(self, motion):
        self._actionQueue.enqueue(Behavior(motion))
    #END on__BehaviorButton_clicked()

    def on__SpeechButton_clicked(self, speech):
        self._actionQueue.enqueue(Speech(speech))
    #END on__SpeechButton_clicked()
#END Empathy
