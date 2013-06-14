from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from BaseStudy import BaseStudy
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
from EmpathyBehaviorButton import EmpathyBehaviorButton
from UI.ActionPushButton import ActionPushButton
from UI.SudokuBoard import SudokuBoard


class Empathy(BaseStudy):
    def __init__(self):
        super(Empathy, self).__init__()
        EmpathyBehaviorButton.initialize()
        self._setupUi()
        self._actionQueue = None
        self._nao = None
        self._timerID = self.startTimer(1000)
    #END __init__()

    def __del__(self):
        self.killTimer(self._timerID)
        EmpathyBehaviorButton.destroy()
    #END __del__()

    def LEDActive(self):
        if self._nao is not None:
            self._nao.LEDrandomEyes(1.0, True)
        #END if
    #END LEDActive()

    def LEDNormal(self):
        rgb = 0x00000000
        if self._currPhase <= 1:
            rgb = 0x0087ceeb
        elif self._currPhase <= 2:
            rgb = 0x0000FF7F
        elif self._currPhase <= 3:
            rgb = 0x003CB371
        elif self._currPhase <= 4:
            rgb = 0x00008B45
        elif self._currPhase <= 5:
            rgb = 0x00228B22
        elif self._currPhase <= 6:
            rgb = 0x0000ff00
        else:
            rgb = 0x0087ceeb
        #END if
        self._nao.LEDfadeRGB(LEDNames.Face, rgb, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5, True)
    #END LEDNormal()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self.on_nao_connected)
            self._nao.disconnected.disconnect(self.on_nao_disconnected)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self.on_nao_connected)
            self._nao.disconnected.connect(self.on_nao_disconnected)
        #END if
    #END setNao()

    def _on_actionbutton_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END _on_actionbutton_clicked()

    def _on_boardshortcut_triggered(self):
        for action in self._actShortcuts:
            if self.sender() == action:
                intValue = int(action.text()) - 1
                if self._currSubgrid is None:
                    # selecting subgrid
                    x = intValue % 3
                    y = 2 - (intValue / 3)
                    self._currSubgrid = [y, x]
                    self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1], QtGui.QColor(0, 255, 0))
                else:
                    # selecting cell
                    x = (self._currSubgrid[1] * 3) + (intValue % 3)
                    y = (self._currSubgrid[0] * 3) + (2 - (intValue / 3))
                    self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1])
                    self._wgtSudoku.focus(y, x)
                    self._currSubgrid = None
                #END if
                return
            #END if
        #END for
    #END _on_boardshortcut_triggered()

    def _on_gamebutton_clicked(self):
        if self._currSubgrid is not None:
            self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1])
            self._currSubgrid = None
        #END if
        for index in range(len(self._btnGames)):
            if self.sender() == self._btnGames[index]:
                for i in range(9):
                    for j in range(9):
                        self._wgtSudoku.set(i, j, self._games[index][i][j])
                    #END for
                #END for
                return
            #END if
        #END for
    #END _on_gamebutton_clicked()

    def _on_nao_connected(self):
        pass
    #END _on_nao_connected()

    def _on_nao_disconnected(self):
        pass
    #END _on_nao_disconnected()

    def _on_solveone_clicked(self):
        if self._currSubgrid is not None:
            self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1])
            self._currSubgrid = None
        #END if
    #END _on_solveone_clicked()

    def timerEvent(self, event):
        pass
    #END timerEvent()

    def _setupUi(self):
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)

        widgetMotions = QtGui.QWidget()
        layoutMotions = QtGui.QVBoxLayout(widgetMotions)
        layoutMotions.setMargin(0)
        for i in range(EmpathyBehaviorButton.lengthMotions()):
            keyValue = EmpathyBehaviorButton.getMotion(i)
            button = ActionPushButton(None, keyValue[0], [Stiffness(1.0), keyValue[1]])
            button.clicked.connect(self.on_button_clicked)
            layoutMotions.addWidget(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetMotions)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(splitter)
        widget.setLayout(layoutScroll)

        widgetBehaviors = QtGui.QWidget()
        layoutBehaviors = QtGui.QVBoxLayout(widgetBehaviors)
        layoutBehaviors.setMargin(0)
        for i in range(EmpathyBehaviorButton.lengthBehaviors()):
            button = EmpathyBehaviorButton.getBehavior(i)
            button.clicked.connect(self.on_button_clicked)
            layoutBehaviors.addWidget(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetBehaviors)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(splitter)
        widget.setLayout(layoutScroll)

        widget = QtGui.QWidget(splitter)
        widget.setLayout(self._setupScenarioUi())

        widget = QtGui.QWidget(splitter)
        widget.setLayout(self._setupSudokuUi())

        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
    #END _setupUi

    def _setupScenarioUi(self):
        components = [
            QtGui.QLabel("INTRODUCTION"),
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

            QtGui.QLabel("PHASE 1"),
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

            QtGui.QLabel("PHASE 2"),

            QtGui.QLabel("PHASE 3"),

            QtGui.QLabel("PHASE 4"),
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

            QtGui.QLabel("PHASE 5"),
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

            QtGui.QLabel("PHASE 6"),
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

            QtGui.QLabel("FINAL PHASE"),
            ActionPushButton(None, "Intro after reset", [
                    Stiffness(1.0),
                    Speech("NAO, online.", speed = 75, shaping = 85),
                    Wait(1500),
                    Motion("WaveHand"),
                    Wait(1000),
                    Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
                ]),
        ]

        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)
        for comp in components:
            if isinstance(comp, ActionPushButton):
                comp.clicked.connect(self._on_actionbutton_clicked)
            layout.addWidget(comp)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widget)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        return layoutScroll
    #END _setupScenarioUi()

    def _setupSudokuUi(self):
        self._wgtSudoku = SudokuBoard()
        self._actShortcuts = []
        self._btnGames = [
                QtGui.QPushButton("Game Q"),
                QtGui.QPushButton("Game W"),
                QtGui.QPushButton("Game E"),
                QtGui.QPushButton("Game R"),
                QtGui.QPushButton("Game T"),
                QtGui.QPushButton("Game Y"),
                QtGui.QPushButton("Game U"),
                QtGui.QPushButton("Game I"),
                QtGui.QPushButton("Game O"),
                QtGui.QPushButton("Game P"),
            ]
        self._games = [[
                [6, 0, 0, 0, 0, 0, 2, 0, 5],
                [0, 0, 1, 0, 4, 0, 6, 0, 0],
                [2, 0, 5, 0, 7, 8, 9, 0, 3],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 9, 0, 3, 0, 6],
                [0, 0, 7, 0, 2, 3, 1, 5, 0],
                [0, 0, 0, 7, 6, 2, 0, 0, 0],
                [0, 0, 6, 3, 0, 0, 7, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]]
        self._currSubgrid = None

        for i in range(1, 10):
            action = QtGui.QAction(str(i), self)
            action.setShortcut(QtCore.Qt.Key_0 + i)
            action.triggered.connect(self._on_boardshortcut_triggered)
            self._actShortcuts.append(action)
            self.addAction(action)
        #END for

        splitter = QtGui.QSplitter()
        splitter.setOrientation(QtCore.Qt.Vertical)
        splitter.addWidget(self._wgtSudoku)

        widgetControls = QtGui.QWidget(splitter)
        layoutControls = QtGui.QHBoxLayout(widgetControls)
        layoutControls.setMargin(0)

        widget = QtGui.QWidget(widgetControls)
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)
        for button in self._btnGames:
            button.clicked.connect(self._on_gamebutton_clicked)
            layout.addWidget(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widget)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        layoutControls.addLayout(layoutScroll)

        widget = QtGui.QWidget(widgetControls)
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)

        button = QtGui.QPushButton("Say next answer")
        button.clicked.connect(self._on_solveone_clicked)
        layout.addWidget(button)

        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widget)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        layoutControls.addLayout(layoutScroll)

        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        return layout
    #END _setupSudokuUi()
#END Empathy
