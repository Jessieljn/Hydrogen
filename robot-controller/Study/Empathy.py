from PyQt4 import QtCore
from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action import AutoRunAction
from Action import Behavior
from Action import LED
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
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
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHand"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Nice Meet", [ \
                    Speech("Hi, nice to meet you"),
                ]),
            # practice session
            QtGui.QLabel("PHASE 1", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play well?", [ \
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes:", [ \
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Wait(500),
                    Motion("PalmUpRight", speed = 2.0),
                    Speech("I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No:", [ \
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1000),
                    Speech("That is okay"),
                    Speech("I'm sure we will do a good job"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let's begin", [ \
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5),
                    Speech("Let's start playing"),
                    Speech("Can you bring a Sudoku board here, please?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Go first", [ \
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(1000),
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
            QtGui.QLabel("PHASE 2", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 3", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 4", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Retire", [ \
                    Stiffness(1.0),
                    Motion("DisagreeRight", speed = 1.5),
                    Wait(300),
                    Speech("Ahhhe"),
                    Wait(1000),
                    Motion("PointYouRight", speed = 1.5, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(500),
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please go ahead"),
                ]),
            QtGui.QLabel("PHASE 5", self._widgets[len(self._widgets) - 1]),
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
                    Speech("This is for the expe- expe- expe-. Sorry, this is for the experiment"),
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
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(500),
                    Speech("It's your turn."),
                    Speech("Please fill one box and tell me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read, hold it up", [ \
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0),
                    Wait(500),
                    Speech("I can't read."),
                    Speech("Can you hold it up?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read, tell me", [ \
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 1.5),
                    Wait(500),
                    Speech("I can't read."),
                    Speech("Can you tell me what you wrote?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me think", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.5),
                    Wait(700),
                    Speech("Heum, let me think carefully"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let's try ", [ \
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(700),
                    Speech("Let's try"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't know", [ \
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.5),
                    Wait(700),
                    Speech("I don't know"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "It's hard", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 2.0),
                    Wait(700),
                    Speech("This one is hard"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Fill number", [ \
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.00),
                    Wait(500),
                    Speech("Please, would you fill the number in for me?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Which box filled?", [ \
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.25),
                    Wait(1000),
                    Speech("Which box did you fill in last time?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you think?", [ \
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.5),
                    Wait(1000),
                    Speech("What do you think?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Need help?", [ \
                    Stiffness(1.0),
                    Motion("WaveHand", speed = 1.25),
                    Wait(1500),
                    Speech("Do you need any help?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You okay?", [ \
                    Stiffness(1.0),
                    Motion("PointYouLeft", speed = 2.0),
                    Wait(500),
                    Speech("Are you okay?"),
                    Speech("I can help you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You playing?", [ \
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1200),
                    Speech("Are you playing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play with me", [ \
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 2.0),
                    Wait(400),
                    Speech("Please, keep playing with me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Do play yourself", [ \
                    Stiffness(1.0),
                    Motion("Disagree", speed = 2.0),
                    Wait(1000),
                    Speech("Don't play by yourself."),
                    Wait(700),
                    Motion("PointYouRight", speed = 2.0),
                    Wait(1000),
                    Speech("I want to play together."),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
        layout = QtGui.QHBoxLayout(widget)
        layout.setMargin(0)
        self._leName = FocusableLineEdit(self._widgets[len(self._widgets) - 1])
        self._leName.setMaximumWidth(80)
        layout.addWidget(self._leName)
        button = QtGui.QPushButton("PlayName", widget)
        button.setMaximumWidth(55)
        button.clicked.connect(self.on_participantName)
        layout.addWidget(button)
        self._buttons.append([
            widget,
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Wait a minute", [ \
                    Stiffness(1.0),
                    Motion("Wait", speed = 1.5),
                    Wait(700),
                    Speech("Please, wait a minute."),
                    Speech("I need time to process."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [ \
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldR)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0),
                    AutoRunAction(),
                ]),
            QtGui.QLabel("Jitter Weak Version", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [ \
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0, repeat = 4, repeatBegin = 13, repeatEnd = 16, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            QtGui.QLabel("Jitter Strong Version", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [ \
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0, repeat = 4, repeatBegin = 6, repeatEnd = 9, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [ \
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PalmUpLeft", [ \
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 11, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PalmUpRight", [ \
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 11, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([])

        widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
        layout = QtGui.QHBoxLayout(widget)
        layout.setMargin(0)
        button = ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [ \
                Stiffness(1.0),
                Motion("PalmUpLeft", speed = 2.0),
                Speech("I think", blocking = False),
            ])
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        button = ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [ \
                Stiffness(1.0),
                Motion("PalmUpRight", speed = 2.0),
                Speech("I think", blocking = False),
            ])
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        self._buttons[len(self._buttons) - 1].append(widget)

        for i in range(1, 10):
            widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
            layout = QtGui.QHBoxLayout(widget)
            layout.setMargin(0)
            button = ActionPushButton(self._widgets[len(self._widgets) - 1], "# should be " + str(i), Speech("the number should be " + str(i) + ","))
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)
            button = ActionPushButton(self._widgets[len(self._widgets) - 1], "# could be " + str(i), Speech("the number could be " + str(i) + ","))
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)
            self._buttons[len(self._buttons) - 1].append(widget)
        #END for

        widget = QtGui.QWidget(self._widgets[len(self._widgets) - 1])
        layout = QtGui.QGridLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setMargin(0)
        layout.setHorizontalSpacing(6)
        layout.setVerticalSpacing(6)
        layoutSubgrids = [ \
            [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
            [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
            [QtGui.QGridLayout(), QtGui.QGridLayout(), QtGui.QGridLayout()],
        ]
        for i in range(3):
            for j in range(3):
                layoutSubgrids[i][j].setContentsMargins(0, 0, 0, 0)
                layoutSubgrids[i][j].setMargin(0)
                layoutSubgrids[i][j].setHorizontalSpacing(0)
                layoutSubgrids[i][j].setVerticalSpacing(0)
                for x in range(3):
                    for y in range(3):
                        text = str(chr(ord('A') + (j * 3 + x))) + str(i * 3 + y + 1)
                        button = ActionPushButton(widget, text, Speech("aet " + text, speed = 70))
                        button.setMaximumWidth(35)
                        button.clicked.connect(self.on_button_clicked)
                        layoutSubgrids[i][j].addWidget(button, y, x, 1, 1, QtCore.Qt.AlignCenter)
                    #END for
                #END for
                layout.addLayout(layoutSubgrids[i][j], i, j)
            #END for
        #END for
        self._buttons[len(self._buttons) - 1].append(widget)

        self._setupEnd()
    #END __init__()

    def on_participantName(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(Speech(self._leName.text()))
    #END on_participantName()
#END Empathy
