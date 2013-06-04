from PyQt4 import QtGui
from Action.Behavior import Behavior
from Action.Speech import Speech
from UI.BehaviorPushButton import BehaviorPushButton
from UI.SpeechPushButton import SpeechPushButton


class General(QtGui.QWidget):
    def __init__(self, parent, actionQueue):
        super(General, self).__init__(parent)
        self._actionQueue = actionQueue

        self.intro = SpeechPushButton(self, "Introduction", "Thanks for coming in. Please remember that you can leave at"
                                                           " any time. If you have any specific questions about the "
                                                           "tasks, please hold them until after the experiment is "
                                                           "complete; I will be happy to answer any of your questions "
                                                           "afterwards. If you are uncomfortable with this, please "
                                                           "remember that you can leave at any time. The cash "
                                                           "honorarium is yours to keep even if you choose not to "
                                                           "continue to the end.")
        self.intro.execute.connect(self.on__SpeechButton_clicked)

        self.demographics = SpeechPushButton(self, "Demographics", "Before we begin, please open the blue folder in "
                                                                  "front of you. Inside, you will find a demographics "
                                                                  "questionnaire. Please fill it out and let me know "
                                                                  "when you are finished.")
        self.demographics.execute.connect(self.on__SpeechButton_clicked)

        self.sitDown = SpeechPushButton(self, "Sit Down", "Thank you. Please take a seat at the computer to my right.")
        self.sitDown.execute.connect(self.on__SpeechButton_clicked)

        self.welcome = SpeechPushButton(self, "You're Welcome", "You are welcome")
        self.welcome.execute.connect(self.on__SpeechButton_clicked)

        self.nod = BehaviorPushButton(self, "Head Nodding", "headNod")
        self.nod.execute.connect(self.on__BehaviorButton_clicked)

        self.scratch = BehaviorPushButton(self, "Scratch Head", "scratchHeadRight")
        self.scratch.execute.connect(self.on__BehaviorButton_clicked)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.intro)
        layout.addWidget(self.demographics)
        layout.addWidget(self.sitDown)
        layout.addWidget(self.welcome)
        layout.addWidget(self.nod)
        layout.addWidget(self.scratch)
    #END __init__()

    def on__BehaviorButton_clicked(self, motion):
        self._actionQueue.enqueue(Behavior(motion))
    #END on__BehaviorButton_clicked()

    def on__SpeechButton_clicked(self, speech):
        self._actionQueue.enqueue(Speech(speech))
    #END on__SpeechButton_clicked()
#END class
