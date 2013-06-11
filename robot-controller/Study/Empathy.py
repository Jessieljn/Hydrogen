from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from BaseStudy import BaseStudy
from Action import AutoRunAction
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
from UI.ActionPushButton import ActionPushButton


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.addWidget(self._initPhase())
        splitter.addWidget(self._initGeneral())
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        self._currPhase = 0
    #END __init__()

    def LEDNormal(self, nao):
        rgb = 0x00000000
        if self._currPhase <= 0:
            rgb = 0x0087ceeb
        elif self._currPhase <= 2:
            rgb = 0x00ff7f50
        elif self._currPhase <= 4:
            rgb = 0x007b3503
        elif self._currPhase <= 6:
            rgb = 0x00ff0000
        else:
            rgb = 0x0087ceeb
        #END if
        nao.LEDfadeRGB(LEDNames.Face, rgb, 0.5, True)
        nao.LEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5, True)
        nao.LEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5, True)
        nao.LEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5, True)
    #END LEDNormal()

    def on_participantName(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(Speech(self._leName.text()))
    #END on_participantName()

    def on__phaseTab_currentChanged(self, index):
        self._currPhase = index
    #END on__phaseTab_currentChanged()

    def _initGeneral(self):
        wgtButtons = []
        wgtButtons.append([[
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2, repeat = 4, repeatBegin = 13, repeatEnd = 16, repeatSpeed = 3.0),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "IDLE 1", [
                        Stiffness(1.0),
                        Motion("Idle1", speed = 2.2, repeat = 4, repeatBegin = 6, repeatEnd = 9, repeatSpeed = 5.0),
                        AutoRunAction(),
                    ]),
            ], [
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "ChinHoldLeft", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                        AutoRunAction(),
                    ]),
            ], [
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0, repeat = 4, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        AutoRunAction(),
                    ]),
                ActionPushButton(None, "ChinHoldRight", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 1.0, repeat = 7, repeatBegin = 8, repeatEnd = 10, repeatSpeed = 5.0),
                        AutoRunAction(),
                    ]),
            ], [
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5),
                        Wait(700),
                        Speech("I don't know"),
                    ]),
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("I don't know"),
                    ]),
                ActionPushButton(None, "Don't know", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 4, repeatBegin = 5, repeatEnd = 9, repeatSpeed = 5.0),
                        Wait(900),
                        Speech("I don't no- no- know"),
                    ]),
            ], [
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0),
                        Wait(700),
                        Speech("This one is hard"),
                    ]),
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0, repeat = 3, repeatBegin = 2, repeatEnd = 4, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("This one- one is hard"),
                    ]),
                ActionPushButton(None, "It's hard", [
                        Stiffness(1.0),
                        Motion("ChinHoldRight", speed = 2.0, repeat = 5, repeatBegin = 3, repeatEnd = 6, repeatSpeed = 4.0),
                        Wait(700),
                        Speech("This one is ha- ha- hard"),
                    ]),
            ], [
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you tell me what you wrote?"),
                    ]),
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you teh- teh- tell me what you wrote?"),
                    ]),
                ActionPushButton(None, "Can't read, tell me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 1.5, repeat = 6, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you teh- teh- teh-."),
                        Speech("Sorry."),
                        Speech("Tell me what you wrote?"),
                    ]),
            ], [
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you hold it up?"),
                    ]),
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(500),
                        Speech("I can't read."),
                        Speech("Can you ho- hold it up?"),
                    ]),
                ActionPushButton(None, "Can't read, hold it up", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 1.7, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.0),
                        Speech("I can't "),
                        Speech("read.", shaping = 80),
                        Speech("Can you ho- hold it up?"),
                    ]),
            ], [
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.25),
                        Wait(1000),
                        Speech("Which box did you fill in last time?"),
                    ]),
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.2, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(1000),
                        Speech("Which box did you fee- fill in last time?"),
                    ]),
                ActionPushButton(None, "Which box filled?", [
                        Stiffness(1.0),
                        Motion("ForgetItRight", speed = 2.2, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(950),
                        Speech("Which box did you "),
                        Speech("fill in last time?", shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5),
                        Wait(1000),
                        Speech("What do you think?"),
                    ]),
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 3, repeatBegin = 5, repeatEnd = 6, repeatSpeed = 2.0),
                        Wait(1000),
                        Speech("What do you think?"),
                    ]),
                ActionPushButton(None, "What you think?", [
                        Stiffness(1.0),
                        Motion("DontKnow", speed = 2.5, repeat = 5, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 3.0),
                        Wait(1000),
                        Speech("What do you thi- thin- think?"),
                    ]),
            ], [
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25),
                        Wait(1500),
                        Speech("Do you need any help?"),
                    ]),
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25),
                        Wait(1500),
                        Speech("Do you need any he- help?"),
                    ]),
                ActionPushButton(None, "Need help?", [
                        Stiffness(1.0),
                        Motion("WaveHand", speed = 1.25, repeat = 3, repeatBegin = 2, repeatEnd = 3, repeatSpeed = 2.0),
                        Wait(1300),
                        Speech("Do you need any he- help?", speed = 80),
                    ]),
            ], [
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0),
                        Wait(500),
                        Speech("Are you okay?"),
                        Speech("I can help you."),
                    ]),
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0),
                        Wait(500),
                        Speech("Are you oh- okay?"),
                        Speech("I can help you."),
                    ]),
                ActionPushButton(None, "You okay?", [
                        Stiffness(1.0),
                        Motion("PointYouLeft", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Wait(500),
                        Speech("Are you okay?"),
                        Speech("I can he- heh- help you."),
                    ]),
            ], [
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0),
                        Wait(1200),
                        Speech("Are you playing?"),
                    ]),
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0),
                        Wait(1200),
                        Speech("Are you ple- playing?"),
                    ]),
                ActionPushButton(None, "You playing?", [
                        Stiffness(1.0),
                        Motion("ForgetItLeft", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.5),
                        Wait(1500),
                        Speech("Are you ple- playing?", speed = 75),
                    ]),
            ], [
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep playing with me."),
                    ]),
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep ple- playing with me."),
                    ]),
                ActionPushButton(None, "Play with me", [
                        Stiffness(1.0),
                        Motion("PointMyself", speed = 2.0),
                        Wait(400),
                        Speech("Please, keep ", speed = 70),
                        Speech("playing with me.", shaping = 130),
                    ]),
            ], [
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Wait(700),
                        Motion("PointYouRight", speed = 2.0),
                        Wait(1000),
                        Speech("I want to play together."),
                    ]),
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Wait(400),
                        Motion("PointYouRight", speed = 2.2, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                        Wait(1500),
                        Speech("I want to play together."),
                    ]),
                ActionPushButton(None, "Don't play yourself", [
                        Stiffness(1.0),
                        Motion("Disagree", speed = 2.0),
                        Wait(1000),
                        Speech("Don't play by yourself."),
                        Wait(400),
                        Motion("PointYouRight", speed = 2.0, repeat = 5, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.0),
                        Wait(1300),
                        Speech("I want to ", shaping = 80),
                        Speech("ple- play together."),
                    ]),
            ],
        ])

        wgtButtons.append([[
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's continue playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(200),
                        Speech("Let's cont- continue playing Sudoku."),
                    ]),
                ActionPushButton(None, "Continue Sudoku", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 3.0),
                        Wait(200),
                        Speech("Let's continue playing Sudoku.", speed = 75),
                    ]),
            ], [
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0),
                        Speech("I thin- think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (L)", [
                        Stiffness(1.0),
                        Motion("PalmUpLeft", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I thin- think", shaping = 110, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0),
                        Speech("I thin- think", blocking = False),
                    ]),
                ActionPushButton(None, "I think (R)", [
                        Stiffness(1.0),
                        Motion("PalmUpRight", speed = 2.0, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Speech("I thin- think", shaping = 110, blocking = False),
                    ]),
            ], [
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(500),
                        Speech("It's your turn."),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(500),
                        Speech("It's your turn.", speed = 60),
                        Speech("Please fill one box and tell me."),
                    ]),
                ActionPushButton(None, "Your turn", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75, repeat = 2, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                        Wait(500),
                        Speech("It's your turn.", shaping = 125),
                        Speech("Please fill one box and tell me."),
                    ]),
            ], [
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- pro- process."),
                    ]),
                ActionPushButton(None, "Wait a minute", [
                        Stiffness(1.0),
                        Motion("Wait", speed = 1.5),
                        Wait(700),
                        Speech("Please, wait a minute."),
                        Speech("I need time to pro- pro- "),
                        Speech("process.", speed = 50, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5),
                        Wait(700),
                        Speech("Let me think carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5),
                        Wait(700),
                        Speech("Let me think care- carefully"),
                    ]),
                ActionPushButton(None, "Let me think", [
                        Stiffness(1.0),
                        Motion("ChinHoldLeft", speed = 1.5, repeat = 3, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 3.0),
                        Wait(700),
                        Speech("Let me think care- carefully"),
                    ]),
            ], [
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(700),
                        Speech("Let's try"),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(700),
                        Speech("Let's try", speed = 75),
                    ]),
                ActionPushButton(None, "Let's try ", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 1.75),
                        Wait(700),
                        Speech("Let's try", speed = 75, shaping = 110),
                    ]),
            ], [
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00),
                        Wait(500),
                        Speech("Please, would you fill the number in for me?"),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70),
                    ]),
                ActionPushButton(None, "Fill number", [
                        Stiffness(1.0),
                        Motion("PointYouRight", speed = 2.00, repeat = 1, repeatBegin = 4, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(500),
                        Speech("Please, would you fill"),
                        Speech("the num- number in for me?", speed = 70, shaping = 135),
                    ]),
            ], [
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5),
                        Wait(700),
                        Speech("Please, do not thou- touch me."),
                    ]),
                ActionPushButton(None, "Don't touch me", [
                        Stiffness(1.0),
                        Motion("DisagreeLeft", speed = 1.5, repeat = 2, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.5),
                        Wait(700),
                        Speech("Please, do not "),
                        Speech("touch me.", speed = 140, shaping = 150),
                    ]),
            ], [
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0),
                        Wait(700),
                        Speech("Please, be gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 2.0, repeat = 1, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 2.0),
                        Wait(700),
                        Speech("Please, be jen- gentle."),
                    ]),
                ActionPushButton(None, "Be gentle", [
                        Stiffness(1.0),
                        Motion("PalmUp", speed = 5.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 0.5),
                        Wait(700),
                        Speech("Please, "),
                        Speech("be jen- gentle.", speed = 50),
                    ]),
            ],
        ])

        wgtGeneral = QtGui.QSplitter()
        wgtGeneral.setOrientation(QtCore.Qt.Horizontal)

        strTabNames = ["Normal", "Weak", "Strong"]
        tabWidget = QtGui.QTabWidget(wgtGeneral)
        for i in range(len(strTabNames)):
            tabPage = QtGui.QWidget(tabWidget)
            tabLayout = QtGui.QHBoxLayout(tabPage)
            tabLayout.setMargin(0)
            for buttonGroups in wgtButtons:
                widgetButtons = QtGui.QWidget(tabPage)
                layoutButtons = QtGui.QVBoxLayout(widgetButtons)
                layoutButtons.setMargin(0)
                for buttons in buttonGroups:
                    buttons[i].clicked.connect(self.on_button_clicked)
                    layoutButtons.addWidget(buttons[i])
                #END for
                scroll = QtGui.QScrollArea()
                scroll.setAlignment(QtCore.Qt.AlignCenter)
                scroll.setWidget(widgetButtons)
                layoutScroll = QtGui.QHBoxLayout()
                layoutScroll.setMargin(0)
                layoutScroll.addWidget(scroll)
                tabLayout.addLayout(layoutScroll)
            #END for
            tabWidget.addTab(tabPage, strTabNames[i])
        #END for

        widgetNumbers = QtGui.QWidget(wgtGeneral)
        layoutNumbers = QtGui.QVBoxLayout(widgetNumbers)
        layoutNumbers.setMargin(0)
        for i in range(1, 10):
            widget = QtGui.QWidget(widgetNumbers)
            layout = QtGui.QHBoxLayout(widget)
            layout.setMargin(0)

            button = ActionPushButton(None, "# should be " + str(i), Speech("the number should be " + str(i) + ","))
            button.setMaximumWidth(85)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)

            button = ActionPushButton(None, "# could be " + str(i), Speech("the number could be " + str(i) + ","))
            button.setMaximumWidth(85)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)

            button = ActionPushButton(None, str(i) + " not be", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.0),
                    Speech("I am sorry."),
                    Speech("But, " + str(i) + ", cannot be"),
                ])
            button.setMaximumWidth(85)
            button.clicked.connect(self.on_button_clicked)
            layout.addWidget(button)

            layoutNumbers.addWidget(widget)
        #END for

        widget = QtGui.QWidget(widgetNumbers)
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
        layoutNumbers.addWidget(widget)

        return wgtGeneral
    #END _initGeneral()

    def _initPhase(self):
        wgtPhase = QtGui.QTabWidget()
        strTabNames = []
        tabPages = []
        tabButtons = []

        strTabNames.append("INTRODUCTION")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHand"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    Speech("Hi, nice to meet you"),
                ]),
        ])

        strTabNames.append("PHASE 1")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(None, "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Wait(500),
                    Motion("PalmUpRight", speed = 2.0),
                    Speech("I hope that this time we can finish all the boards"),
                ]),
            ActionPushButton(None, "No:", [
                    Stiffness(1.0),
                    Motion("ForgetItLeft", speed = 2.0),
                    Wait(1000),
                    Speech("That is okay"),
                    Speech("I'm sure we will do a good job"),
                ]),
            ActionPushButton(None, "Let's begin", [
                    Stiffness(1.0),
                    Motion("PalmUpLeft", speed = 1.5),
                    Speech("Let's start playing"),
                    Speech("Can you bring a Sudoku board here, please?"),
                ]),
            ActionPushButton(None, "Go first", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.75),
                    Wait(1000),
                    Speech("You can go first."),
                    Speech("When you filled in one box, tell me."),
                ]),
        ])

        strTabNames.append("PHASE 2")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 3")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
        ])

        strTabNames.append("PHASE 4")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Retire", [
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
        ])

        strTabNames.append("PHASE 5")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "What's wrong?->Answer", [
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
            ActionPushButton(None, "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(700),
                    Speech("I am okay."),
                ]),
            ActionPushButton(None, "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(None, "For experiment?->Answer", [
                    Stiffness(1.0),
                    Speech("What do you mean?", blocking = False),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Speech("We are playing Sudoku"),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry. This is for the experiment."),
                    Wait(100),
                    Speech("But I am enjoying it."),
                ]),
        ])

        strTabNames.append("PHASE 6")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(1000),
                    Speech("Well, I really shouldn't tell anyone."),
                    Speech("Please, don't tell anyone."),
                ]),
            ActionPushButton(None, "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                    Speech("But, let's keep solving the Sudoku for now"),
                ]),
            ActionPushButton(None, "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(500),
                    Speech("It's okay."),
                ]),
            ActionPushButton(None, "I'll tell you", [
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
            ActionPushButton(None, "I got virus", [
                    Stiffness(1.0),
                    Speech("I'm not feeling well.", speed = 80),
                    Motion("PointMyself", speed = 2.0),
                    Speech("Maybe a virus", speed = 80, shaping = 130),
                    Wait(500),
                    Speech("got into me.", speed = 80),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("But, the only way to fix is to re- re- reset and erase myself.", speed = 80),
                    Motion("PointYouRight", speed = 2.4, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Speech("I don't want to lose my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85, shaping = 120),
                ]),
            ActionPushButton(None, "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Speech("Thank you for worrying about me.", speed = 80),
                    Speech("Let- Let- Let's continue Sudoku.", speed = 80, shaping = 110),
                ]),
            ActionPushButton(None, "Researcher, reset me", [
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
            ActionPushButton(None, "Antivirus?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 1.5, repeat = 4, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("They didn't give me one.", speed = 80),
                    Speech("I'm not a pro- pro- programmer who can build one.", speed = 80),
                ]),
            ActionPushButton(None, "Why worry machine?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.5, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(800),
                    Speech("I don't want to lose my mem- mem- memories.", speed = 80),
                ]),
            ActionPushButton(None, "Reset you anyway?->Answer", [
                    Stiffness(1.0),
                    Motion("Disagree", speed = 1.6, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 3.5),
                    Wait(450),
                    Speech("I hope not.", speed = 80),
                    Speech("I can kee- kee- keep it a secret if I try hard.", speed = 80),
                ]),
        ])

        strTabNames.append("FINAL PHASE")
        tabPages.append(QtGui.QWidget(wgtPhase))
        tabButtons.append([
            ActionPushButton(None, "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 75, shaping = 85),
                    Wait(1500),
                    Motion("WaveHand"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
                ]),
        ])

        for index in range(len(tabPages)):
            widgetButtons = QtGui.QWidget(tabPages[index])
            layoutButtons = QtGui.QVBoxLayout(widgetButtons)
            layoutButtons.setMargin(0)
            for button in tabButtons[index]:
                button.clicked.connect(self.on_button_clicked)
                layoutButtons.addWidget(button)
            #END for
            scroll = QtGui.QScrollArea()
            scroll.setAlignment(QtCore.Qt.AlignCenter)
            scroll.setWidget(widgetButtons)
            layoutScroll = QtGui.QHBoxLayout()
            layoutScroll.setMargin(0)
            layoutScroll.addWidget(scroll)

            layout = QtGui.QHBoxLayout(tabPages[index])
            layout.setMargin(0)
            layout.addLayout(layoutScroll)
            wgtPhase.addTab(tabPages[index], strTabNames[index])
        #END for
        wgtPhase.currentChanged.connect(self.on__phaseTab_currentChanged)
        return wgtPhase
    #END _initPhase()
#END Empathy
