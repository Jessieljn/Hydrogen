from PyQt4 import QtGui
from Action.Speech import Speech
from UI.ActionPushButton import ActionPushButton


class General(QtGui.QWidget):
    def __init__(self):
        super(General, self).__init__()
        self._actionQueue = None

        self.intro = ActionPushButton(self, "Introduction", Speech("Thanks for coming in. Please remember that you can leave at"
                                                           " any time. If you have any specific questions about the "
                                                           "tasks, please hold them until after the experiment is "
                                                           "complete; I will be happy to answer any of your questions "
                                                           "afterwards. If you are uncomfortable with this, please "
                                                           "remember that you can leave at any time. The cash "
                                                           "honorarium is yours to keep even if you choose not to "
                                                           "continue to the end."))
        self.intro.execute.connect(self.on_actionReceived)

        self.demographics = ActionPushButton(self, "Demographics", Speech("Before we begin, please open the blue folder in "
                                                                  "front of you. Inside, you will find a demographics "
                                                                  "questionnaire. Please fill it out and let me know "
                                                                  "when you are finished."))
        self.demographics.execute.connect(self.on_actionReceived)

        self.sitDown = ActionPushButton(self, "Sit Down", Speech("Thank you. Please take a seat at the computer to my right."))
        self.sitDown.execute.connect(self.on_actionReceived)

        self.welcome = ActionPushButton(self, "You're Welcome", Speech("You are welcome"))
        self.welcome.execute.connect(self.on_actionReceived)

        self.nod = ActionPushButton(self, "Head Nodding", Speech("headNod"))
        self.nod.execute.connect(self.on_actionReceived)

        self.scratch = ActionPushButton(self, "Scratch Head", Speech("scratchHeadRight"))
        self.scratch.execute.connect(self.on_actionReceived)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.intro)
        layout.addWidget(self.demographics)
        layout.addWidget(self.sitDown)
        layout.addWidget(self.welcome)
        layout.addWidget(self.nod)
        layout.addWidget(self.scratch)
    #END __init__()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def on_actionReceived(self, action):
        self._actionQueue.enqueue(action)
    #END on_actionReceived()
#END class
