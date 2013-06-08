from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action import Behavior
from Action import Speech
from UI.ActionPushButton import ActionPushButton


class General(BaseStudy):
    def __init__(self):
        super(General, self).__init__()
        self._setupBegin()

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Introduction", [ \
                    Speech("Thanks for coming in. Please remember that you can leave at"
                           " any time. If you have any specific questions about the "
                           "tasks, please hold them until after the experiment is "
                           "complete; I will be happy to answer any of your questions "
                           "afterwards. If you are uncomfortable with this, please "
                           "remember that you can leave at any time. The cash "
                           "honorarium is yours to keep even if you choose not to "
                           "continue to the end."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Demographics", [ \
                    Speech("Before we begin, please open the blue folder in "
                           "front of you. Inside, you will find a demographics "
                           "questionnaire. Please fill it out and let me know "
                           "when you are finished."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Sit Down", [ \
                    Speech("Thank you. Please take a seat at the computer to my right."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You're Welcome", [ \
                    Speech("You are welcome"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Head Nodding", [ \
                    Behavior("headNod"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Head", [ \
                    Behavior("scratchHeadRight"),
                ]),
        ])

        self._setupEnd()
    #END __init__()
#END class
