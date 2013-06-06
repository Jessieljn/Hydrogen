from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action.Behavior import Behavior
from Action.Speech import Speech
from Action.Wait import Wait
from UI.ActionPushButton import ActionPushButton


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        self._setupBegin()

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "INTRODUCTION"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Welcome", [ \
                    Speech("Oh,"),
                    # standing up motion
                    Wait(200),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Nice Meet", [ \
                    Speech("Nice to meet you"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Vision Process", [ \
                    Speech("I can also do vision processing"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Excite to play", [ \
                    Speech("I am so excited to play with you"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 1"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play well?", [ \
                    Speech("It is so exciting to play this game with someone else"),
                    Speech("Do you play games well?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes:", [ \
                    Speech("Oh yes!"),
                    Speech("My last partner was not really good. I hope that this time we can finish the games"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No:", [ \
                    Speech("That is okay"),
                    Speech("I am sure we will do a good job"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Last time", [ \
                    Speech("Last time, we didn't do very well in this game because we did not really play the same way."),
                    Speech("But you seem to be more like me!"),
                    Speech("I think we can do well."),
                    Speech("Let's do it"),
                    Speech("We can do it"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yeah:", [ \
                    Speech("I knew it!"),
                    Speech("Bring the paper here, please"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You robot:", [ \
                    Speech("Well, if you don't trust me, we cannot win the game."),
                    Speech("I know what I am and I know what I am doing."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Go first", [ \
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [ \
                    Speech("I think"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "# at", [ \
                    Speech("the number at"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "should be", [ \
                    Speech("should be"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me see", [ \
                    Speech("I can't read."),
                    Speech("Can you make it straight!"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me think", [ \
                    Speech("Hmm,"),
                    # pause
                    Speech("Let me think carefully"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you think?", [ \
                    Speech("What do you think?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you doing?", [ \
                    Speech("What are you doing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You playing?", [ \
                    Speech("Are you playing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play with me", [ \
                    Speech("Please keey, playing with me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Chin", Behavior("chinScratch")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Left Hand Point", Behavior("leftHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Right Hand Point", Behavior("rightHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Head", Behavior("shakeHand")),
        ])

        i = len(self._buttons)
        self._buttons.append([])
        self._widgets.append(QtGui.QWidget(self))
        j = len(self._buttons)
        self._buttons.append([])
        self._widgets.append(QtGui.QWidget(self))
        for k in range(9):
            button = ActionPushButton(self._widgets[i], str(chr(ord('A') + k)), Speech(str(chr(ord('A') + k))))
            button.setMaximumWidth(40)
            self._buttons[i].append(button)
            button = ActionPushButton(self._widgets[j], str(k + 1), Speech(str(k + 1)))
            button.setMaximumWidth(40)
            self._buttons[j].append(button)
        #END for

        self._setupEnd()
    #END __init__()
#END Empathy
