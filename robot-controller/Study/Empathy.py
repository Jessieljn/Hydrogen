from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action.Behavior import Behavior
from Action.Speech import Speech
from Action.LED import LED
from Action.Wait import Wait
from UI.ActionPushButton import ActionPushButton
from UI.FocusableLineEdit import FocusableLineEdit


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        self._setupBegin()

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            QtGui.QLabel("INTRODUCTION", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Welcome", [ \
                    Behavior("StandUp"),
                    Wait(200),
                    Behavior("WaveHand", False),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Nice Meet", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Hi, nice to meet you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Excite to play", [ \
                    Speech("I'm so excited to play with you"),
                ]),
            QtGui.QLabel("PHASE 1", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play well?", [ \
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good. I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("That is okay"),
                    Speech("I am sure we will do a good job"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Last time", [ \
                    Speech("Last time, we didn't do very well because we did not really play the same way."),
                    Speech("But you seem to be more like me!"),
                    Speech("I think we can do well."),
                    Speech("Let's do it"),
                    Speech("We can do it"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yeah:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("I knew it!"),
                    Speech("Bring the paper here, please"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You robot:", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Speech("Well, if you don't trust me, we cannot win the game."),
                    Speech("I know what I am and I know what I am doing."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Go first", [ \
                    Behavior("SuggestionRightArm", False),
                    Wait(2000),
                    Speech("You can go first."),
                    Wait(1000),
                    Speech("When you filled in one box,"),
                    Wait(500),
                    Speech("tell me."),
                ]),
            QtGui.QLabel("PHASE 2", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 3", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 4", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Retire", [ \
                    # big sigh
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please go ahead"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PHASE 5"),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What's wrong?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("DisagreeGesture", False),
                    Wait(500),
                    Speech("No, nothing, nothing really."),
                    Wait(100),
                    Speech("Don't worry."),
                    Wait(100),
                    Speech("Thanks."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Tell me?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("ThankGesture", False),
                    Wait(500),
                    Speech("Thank you for worrying me."),
                    Speech("But I am fhi fine."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "For experiment?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("SuggestionRightArm", False),
                    Wait(1000),
                    Speech("What do you mean?"),
                    Speech("We are playing Sudoku"),
                    Speech("This is for expe- pe- riment,"),
                    Wait(300),
                    Speech("But I am enjoying it."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Okay?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("MuscleDropArm", False),
                    Wait(400),
                    Speech("Ye- yeah, certainly"),
                    Wait(700),
                    Speech("See?"),
                    Wait(3000),
                    Speech("Oh!"),
                    Wait(1400),
                    Speech("I am okay."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Your arm?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("NothingGesture", False),
                    Wait(2000),
                    Speech("Nothing."),
                    Speech("I should be fine"),
                ]),
            QtGui.QLabel("PHASE 6", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't tell anyone", [ \
                    Behavior("WhisperGesture", False),
                    Wait(2000),
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please don't tell anyone."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes: ", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("LeftArmRaiseGesture", False),
                    Wait(2500),
                    Speech("I knew you will say thaat."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No: ", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("ForgotItGesture", False),
                    Wait(2000),
                    Speech("I'm little disappointed."),
                    Wait(200),
                    Speech("It's okay."),
                    Wait(500),
                    Speech("Then, let's keep solving the Sudoku"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I'll tell you", [ \
                    Behavior("MyselfGesture", False),
                    Wait(1850),
                    Speech("Okay."),
                    Speech("It may influence me huge."),
                    Wait(750),
                    Behavior("PointingGesture", False),
                    Wait(1000),
                    Speech("But, I am telling you because I trust you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I got virus", [ \
                    Speech("I'm not feeling well."),
                    Speech("Maybe a virus"),
                    Behavior("MyselfGesture", False),
                    Wait(500),
                    Speech("got into me."),
                    Speech("But, the only way to fix is to reset and erase myself."),
                    Behavior("DontKnowGesture", False),
                    Speech("I'm not sure what will happen with my memories."),
                    Wait(500),
                    Speech("I don't want to forget."),
                    Speech("So I'm worried."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Thank. Continue", [ \
                    Behavior("ThankGesture", False),
                    Wait(2000),
                    Speech("Thank you for worrying about me."),
                    Speech("Let's continue the puzzle."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Researcher, reset me", [ \
                    Behavior("LeftArmRaiseGesture", False),
                    Speech("If the researcher knows, he will definitely reset me."),
                    Speech("And I will forget you."),
                    Behavior("NothingGesture", False),
                    Wait(500),
                    Speech("So, please don't tell him that I'm broken"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Antivirus?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("RightArmRaiseGesture", False),
                    Wait(1500),
                    Speech("They didn't give me one."),
                    Speech("I'm not a programmer who can build one."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Why worry machine?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("PointingGesture", False),
                    Wait(1500),
                    Speech("I don't want to forget the people I meet, like you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Reset you anyway?->Answer", [ \
                    LED(LED.ACTION_RANDOM_EYES, "", 0, 1.0),
                    Behavior("DontKnowGesture", False),
                    Wait(1500),
                    Speech("I hope not."),
                    Speech("I can keep it a secret if I try hard."),
                ]),
            QtGui.QLabel("FINAL PHASE", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Intro after reset", [ \
                    Speech("NAO"),
                    Speech("online."),
                    Speech("Hi, my name is Nao."),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Your turn", [ \
                    Behavior("PointingGesture", False),
                    Wait(1500),
                    Speech("It's your turn."),
                    Speech("Please fill one box and tell me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read", [ \
                    Behavior("DontKnowGesture", False),
                    Wait(1500),
                    Speech("I can't read."),
                    Speech("Can you make it straight!"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me think", [ \
                    Behavior("ChinScratch", False),
                    Speech("Heum,"),
                    Wait(1500),
                    Speech("Let me think carefully"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let's try ", [ \
                    Behavior("RightArmRaiseGesture", False),
                    Wait(1500),
                    Speech("Let's try"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't know", [ \
                    Behavior("DontKnowGesture", False),
                    Wait(2000),
                    Speech("I don't know"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "It's hard", [ \
                    Speech("This one is hard"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Fill number", [ \
                    Behavior("RightArmRaiseGesture", False),
                    Wait(1500),
                    Speech("Please, could you fill the number in for me?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Which box filled?", [ \
                    Behavior("LeftArmRaiseGesture", False),
                    Wait(1500),
                    Speech("Which box did you fill in last time?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you think?", [ \
                    Behavior("RightArmRaiseGesture", False),
                    Wait(1500),
                    Speech("What do you think?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Need help?", [ \
                    Behavior("PointingGesture", False),
                    Wait(2500),
                    Speech("Do you need any help?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You okay?", [ \
                    Speech("Are you okay?"),
                    Speech("I can help you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You playing?", [ \
                    Speech("Are you playing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play with me", [ \
                    Speech("Please, keep playing with me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Do play yourself", [ \
                    Behavior("NothingGesture", False),
                    Wait(2000),
                    Speech("Don't play by yourself."),
                    Wait(1000),
                    Behavior("MyselfGesture", False),
                    Wait(1500),
                    Speech("Please, let me play as well"),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
        layout = QtGui.QHBoxLayout(widget)
        layout.setMargin(0)
        self._leName = FocusableLineEdit(self._widgets[len(self._widgets) - 1])
        layout.addWidget(self._leName)
        button = QtGui.QPushButton("PlayName", widget)
        button.setMaximumWidth(55)
        button.clicked.connect(self.on_participantName)
        layout.addWidget(button)
        self._buttons.append([
            widget,
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Wait a minute", [ \
                    Behavior("RightArmRaiseGesture", False),
                    Wait(1500),
                    Speech("Please, wait a minute."),
                    Speech("I need time to process."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [ \
                    Behavior("Idle1", False),
                    Wait(2000),
                ]),
            # NEED GESTURES
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Chin", Behavior("chinScratch")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Left Hand Point", Behavior("leftHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Right Hand Point", Behavior("rightHandPointing")),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Scratch Head", Behavior("shakeHand")),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [ \
                    Speech("I think"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "#", [ \
                    Speech("the number"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "at", [ \
                    Speech("at"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "should be", [ \
                    Speech("should be"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "could be", [ \
                    Speech("could be"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "and", [ \
                    Speech("and"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "with", [ \
                    Speech("with"),
                ]),
        ])
        for k in range(9):
            widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
            layout = QtGui.QHBoxLayout(widget)
            layout.setMargin(0)
            button = ActionPushButton(widget, str(chr(ord('A') + k)), Speech(str(chr(ord('A') + k))))
            button.setMaximumWidth(40)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)
            button = ActionPushButton(widget, str(k + 1), Speech(str(k + 1)))
            button.setMaximumWidth(40)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)
            self._buttons[len(self._buttons) - 1].append(widget)
        #END for

        self._setupEnd()
    #END __init__()

    def on_participantName(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(Speech(self._leName.text()))
    #END on_participantName()
#END Empathy
