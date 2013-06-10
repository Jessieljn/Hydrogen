from PyQt4 import QtCore
from PyQt4 import QtGui
from BaseStudy import BaseStudy
from Action import AutoRunAction
from Action import Behavior
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
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHand"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Nice Meet", [
                    Speech("Hi, nice to meet you"),
                ]),
            # practice session
            QtGui.QLabel("PHASE 1", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Wait(500),
                    Motion("PalmUpRight", speed = 2.0),
                    Speech("I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No:", [
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1000),
                    Speech("That is okay"),
                    Speech("I'm sure we will do a good job"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let's begin", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5),
                    Speech("Let's start playing"),
                    Speech("Can you bring a Sudoku board here, please?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Go first", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(1000),
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
            QtGui.QLabel("PHASE 2", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 3", self._widgets[len(self._widgets) - 1]),
            QtGui.QLabel("PHASE 4", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Retire", [
                    Stiffness(1.0),
                    Motion("DisagreeRight", speed = 1.5),
                    Wait(300),
                    Speech("Ahhhe"),
                    Wait(1000),
                    Motion("PointYouRight", speed = 1.5, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(500),
                    Speech("I can't play anymore."),
                    Speech("I need some rest, please "),
                    Speech("go-, go-, go-, go ahead"),
                ]),
            QtGui.QLabel("PHASE 5", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What's wrong?->Answer", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 1.5),
                    Wait(400),
                    Speech("No, nothing, nothing really."),
                    Wait(700),
                    Motion("PalmUpLeft", speed = 2.0),
                    Speech("Don't worry."),
                    Wait(100),
                    Speech("Thanks."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(700),
                    Speech("I am okay."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "For experiment?->Answer", [
                    Stiffness(1.0),
                    Speech("What do you mean?", blocking = False),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Speech("We are playing Sudoku"),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry. This is for the experiment."),
                    Wait(100),
                    Speech("But I am enjoying it."),
                ]),
            QtGui.QLabel("PHASE 6", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(1000),
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please, don't tell anyone."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                    Speech("But, let's keep solving the Sudoku for now"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("It's okay."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I'll tell you", [
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("Ahhhe", speed = 60),
                    Wait(1000),
                    Speech("It may inf- inf- influence me huge."),
                    Wait(750),
                    Motion("PointYouLeft", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("But, I will teh- teh- tell you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "I got virus", [
                    Stiffness(1.0),
                    Speech("I'm not feeling well.", speed = 80),
                    Motion("PointMyself", speed = 2.0),
                    Speech("Maybe a virus", speed = 80),
                    Wait(500),
                    Speech("got into me.", speed = 80),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("But, the only way to fix is to re- re- reset and erase myself.", speed = 80),
                    Motion("PointYouRight", speed = 2.4, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Speech("I don't want to lose my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Speech("Thank you for worrying about me.", speed = 80),
                    Speech("Let- Let- Let's continue Sudoku.", speed = 80),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Researcher, reset me", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.2, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("If the researcher knows, she will definitely reset me.", speed = 80),
                    Wait(1500),
                    Motion("DisagreeRight", speed = 3.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("So, please.", speed = 80),
                    Wait(250),
                    Speech("Don't tell her that I'm bro- bro- broken.", speed = 80),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Antivirus?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 1.5, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("They didn't give me one.", speed = 80),
                    Speech("I'm not a pro- pro- programmer who can build one.", speed = 80),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Why worry machine?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(800),
                    Speech("I don't want to lose my mem- mem- memories.", speed = 80),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Reset you anyway?->Answer", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 1.6, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(450),
                    Speech("I hope not.", speed = 80),
                    Speech("I can kee- kee- keep it a secret if I try hard.", speed = 80),
                ]),
            QtGui.QLabel("FINAL PHASE", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 80, shaping = 70),
                    Wait(1500),
                    Motion("WaveHand"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 80, shaping = 70),
                ]),
        ])

        self._widgets.append(QtGui.QWidget(self))
        self._buttons.append([
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Your turn", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(500),
                    Speech("It's your turn."),
                    Speech("Please fill one box and tell me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read, hold it up", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0),
                    Wait(500),
                    Speech("I can't read."),
                    Speech("Can you hold it up?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Can't read, tell me", [
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 1.5),
                    Wait(500),
                    Speech("I can't read."),
                    Speech("Can you tell me what you wrote?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let me think", [
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.5),
                    Wait(700),
                    Speech("Heum, let me think carefully"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Let's try ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(700),
                    Speech("Let's try"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Fill number", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.00),
                    Wait(500),
                    Speech("Please, would you fill the number in for me?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't know", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.5),
                    Wait(700),
                    Speech("I don't know"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "It's hard", [
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 2.0),
                    Wait(700),
                    Speech("This one is hard"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Which box filled?", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.25),
                    Wait(1000),
                    Speech("Which box did you fill in last time?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "What you think?", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.5),
                    Wait(1000),
                    Speech("What do you think?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Continue Sudoku", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.0),
                    Wait(200),
                    Speech("Let's continue playing Sudoku."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Need help?", [
                    Stiffness(1.0),
                    Motion("WaveHand", speed = 1.25),
                    Wait(1500),
                    Speech("Do you need any help?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You okay?", [
                    Stiffness(1.0),
                    Motion("PointYouLeft", speed = 2.0),
                    Wait(500),
                    Speech("Are you okay?"),
                    Speech("I can help you."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "You playing?", [
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1200),
                    Speech("Are you playing?"),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Play with me", [
                    Stiffness(1.0),
                    Motion("PointMyself", speed = 2.0),
                    Wait(400),
                    Speech("Please, keep playing with me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't play yourself", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 2.0),
                    Wait(1000),
                    Speech("Don't play by yourself."),
                    Wait(700),
                    Motion("PointYouRight", speed = 2.0),
                    Wait(1000),
                    Speech("I want to play together."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Don't touch me", [
                    Stiffness(1.0),
                    Motion("DisagreeLeft", speed = 1.5),
                    Wait(700),
                    Speech("Please, do not touch me."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Be gentle", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.0, repeat = 1, repeatBegin = 0, repeatEnd = 7, repeatSpeed = 5.0),
                    Wait(700),
                    Speech("Please, be gentle."),
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
            ActionPushButton(self._widgets[len(self._widgets) - 1], "Wait a minute", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 1.5),
                    Wait(700),
                    Speech("Please, wait a minute."),
                    Speech("I need time to process."),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldR)", [
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0),
                    AutoRunAction(),
                ]),
            QtGui.QLabel("Jitter Weak Version", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0, repeat = 4, repeatBegin = 13, repeatEnd = 16, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            QtGui.QLabel("Jitter Strong Version", self._widgets[len(self._widgets) - 1]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE 1", [
                    Stiffness(1.0),
                    Motion("Idle1", speed = 1.0, repeat = 4, repeatBegin = 6, repeatEnd = 9, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [
                    Stiffness(1.0),
                    Motion("ChinHoldLeft", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "IDLE (ChinHoldL)", [
                    Stiffness(1.0),
                    Motion("ChinHoldRight", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PalmUpLeft", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 11, repeatSpeed = 3.0),
                    AutoRunAction(),
                ]),
            ActionPushButton(self._widgets[len(self._widgets) - 1], "PalmUpRight", [
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
        button = ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [
                Stiffness(1.0),
                Motion("PalmUpLeft", speed = 2.0),
                Speech("I think", blocking = False),
            ])
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        button = ActionPushButton(self._widgets[len(self._widgets) - 1], "I think", [
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
        layoutSubgrids = [
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
