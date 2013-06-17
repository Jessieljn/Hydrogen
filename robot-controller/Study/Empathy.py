from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from Action import ActionStart
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from Action import Wait
from EmpathyBehaviorButton import EmpathyBehaviorButton
from EmpathySpeech import EmpathySpeech
from UI.ActionPushButton import ActionPushButton
from UI.SudokuBoard import SudokuBoard


class Empathy(QtGui.QWidget):
    def __init__(self):
        super(Empathy, self).__init__()
        EmpathyBehaviorButton.initialize()
        self._setupUi()
        self._actionQueue = None
        self._currSubgrid = None
        self._idleCount = 0
        self._idleRun = False
        self._nao = None
        self._last = [0, 0, 0]
        self._games = [[
                # Training board
                [0, 7, 8, 4, 9, 0, 1, 3, 5],
                [9, 1, 5, 8, 0, 6, 7, 0, 4],
                [3, 2, 4, 7, 1, 5, 0, 9, 8],
                [5, 0, 6, 3, 7, 4, 9, 1, 2],
                [1, 0, 7, 6, 2, 8, 0, 5, 0],
                [4, 0, 2, 9, 5, 1, 8, 6, 7],
                [0, 4, 9, 0, 6, 3, 5, 0, 1],
                [8, 5, 3, 1, 4, 9, 2, 7, 6],
                [2, 0, 1, 5, 8, 0, 3, 0, 9],
            ], [ # Game 1
                [0, 3, 0, 8, 0, 0, 0, 0, 0],
                [9, 0, 5, 6, 0, 0, 7, 0, 0],
                [0, 0, 1, 0, 9, 3, 2, 0, 0],
                [8, 0, 6, 5, 0, 0, 0, 0, 0],
                [0, 4, 0, 0, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 7, 2, 3, 0, 6, 9, 5, 0],
                [0, 1, 9, 4, 8, 7, 0, 6, 0],
                [3, 6, 8, 2, 5, 9, 0, 1, 0],
            ], [ # Game 2
                [1, 5, 0, 0, 0, 0, 9, 2, 4],
                [0, 0, 4, 0, 0, 0, 7, 0, 6],
                [0, 0, 0, 0, 0, 0, 3, 8, 5],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 2, 0, 3, 0, 0, 0, 6, 0],
                [0, 0, 6, 7, 0, 0, 4, 0, 3],
                [0, 0, 2, 4, 0, 0, 5, 3, 1],
                [0, 0, 7, 2, 0, 3, 6, 9, 8],
                [0, 8, 3, 0, 0, 1, 2, 4, 0],
            ], [ # Game 3
                [8, 0, 0, 0, 0, 2, 4, 3, 6],
                [3, 0, 0, 0, 7, 0, 9, 0, 2],
                [0, 0, 0, 1, 0, 0, 7, 8, 5],
                [0, 0, 0, 0, 8, 3, 0, 5, 4],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5, 0, 0, 3, 7, 9],
                [0, 2, 0, 0, 9, 0, 6, 4, 7],
                [0, 4, 0, 8, 0, 0, 1, 9, 0],
                [1, 0, 0, 4, 0, 0, 5, 2, 8],
            ], [ # Game 4
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [9, 0, 0, 1, 3, 7, 0, 0, 6],
                [0, 0, 7, 0, 0, 9, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [5, 0, 6, 4, 0, 2, 0, 0, 0],
                [1, 2, 3, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 2, 3, 8, 4, 0],
                [2, 9, 8, 7, 4, 1, 3, 6, 0],
                [7, 0, 0, 6, 8, 5, 2, 9, 0],
            ], [ # Game 5
                [0, 7, 0, 4, 0, 0, 6, 0, 3],
                [0, 0, 0, 0, 0, 0, 8, 0, 0],
                [4, 6, 5, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 7, 3, 0, 0, 0, 0],
                [5, 0, 4, 0, 0, 0, 0, 0, 0],
                [8, 4, 3, 6, 5, 1, 9, 0, 2],
                [9, 0, 6, 3, 2, 7, 0, 0, 4],
                [2, 1, 7, 0, 4, 8, 3, 0, 6],
            ], [ # Game 6
                [0, 0, 0, 9, 3, 8, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [3, 4, 6, 0, 2, 7, 0, 0, 0],
                [6, 3, 0, 8, 9, 1, 2, 0, 5],
                [0, 0, 1, 0, 4, 5, 0, 0, 7],
                [2, 0, 0, 0, 0, 3, 0, 0, 8],
                [9, 0, 0, 0, 7, 2, 3, 0, 0],
                [4, 0, 2, 3, 5, 6, 1, 0, 0],
                [0, 0, 0, 4, 8, 9, 0, 0, 0],
            ], [ # Game 7
                [0, 3, 0, 9, 7, 5, 6, 0, 0],
                [0, 0, 0, 1, 8, 0, 9, 0, 0],
                [8, 0, 1, 4, 6, 3, 0, 0, 0],
                [0, 0, 0, 2, 3, 7, 0, 6, 0],
                [0, 0, 9, 5, 1, 6, 0, 4, 0],
                [0, 7, 0, 0, 9, 4, 2, 1, 0],
                [0, 8, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 6, 2, 1, 0, 0, 0],
                [1, 0, 6, 7, 5, 0, 0, 0, 0],
            ], [ # Game 8
                [6, 0, 5, 0, 2, 1, 0, 0, 8],
                [9, 0, 7, 5, 3, 8, 4, 0, 2],
                [2, 8, 3, 6, 4, 7, 9, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 8, 6, 2, 0, 0, 0],
                [3, 0, 8, 0, 9, 0, 0, 0, 0],
                [0, 0, 6, 0, 0, 0, 7, 0, 0],
                [0, 0, 0, 2, 1, 0, 8, 0, 0],
                [0, 5, 0, 4, 0, 9, 2, 0, 0],
            ], [ # Game 9
                [0, 5, 0, 0, 0, 0, 9, 0, 0],
                [8, 6, 4, 9, 0, 0, 0, 0, 5],
                [3, 9, 1, 2, 7, 0, 6, 0, 8],
                [7, 0, 8, 0, 5, 0, 0, 0, 0],
                [5, 2, 3, 4, 0, 1, 0, 0, 0],
                [0, 4, 0, 0, 0, 0, 0, 0, 0],
                [9, 8, 2, 0, 0, 0, 0, 0, 0],
                [4, 3, 5, 6, 8, 0, 0, 0, 0],
                [1, 7, 0, 0, 0, 4, 8, 0, 0],
            ], [ # Game 10
                [0, 6, 0, 3, 7, 0, 9, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 8, 9, 0, 0, 7],
                [9, 0, 0, 6, 3, 4, 7, 0, 0],
                [4, 0, 0, 8, 0, 1, 0, 0, 0],
                [1, 0, 8, 7, 9, 5, 2, 0, 0],
                [0, 0, 0, 1, 5, 0, 0, 7, 8],
                [0, 0, 0, 9, 4, 7, 5, 0, 2],
                [0, 0, 0, 2, 6, 8, 0, 0, 4],
            ]]
    #END __init__()

    def __del__(self):
        EmpathyBehaviorButton.destroy()
    #END __del__()

    def LEDActive(self):
        self._nao.LEDrandomEyes(1.0, True)
    #END LEDActive()

    def LEDNormal(self):
        current_phase = self._sbCurrLevel.value()
        rgb = 0x00000000
        if current_phase <= 1:
            rgb = 0x0087ceeb
        elif current_phase <= 2:
            rgb = 0x0000FF7F
        elif current_phase <= 3:
            rgb = 0x003CB371
        elif current_phase <= 4:
            rgb = 0x00008B45
        elif current_phase <= 5:
            rgb = 0x00228B22
        elif current_phase <= 6:
            rgb = 0x0000ff00
        else:
            rgb = 0x0087ceeb
        #END if
        self._nao.LEDfadeRGB(LEDNames.Face, rgb, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5, True)
        self._nao.LEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5, True)
    #END LEDNormal()

    def getJitterLevel(self):
        jlv = self._sbCurrLevel.value()
        if jlv <= 0:
            jlv = 0
        elif jlv <= 6:
            jlv = jlv - 1
        else:
            jlv = 0
        #END if
        return jlv
    #END getJitterLevel()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self._on_nao_connected)
            self._nao.disconnected.disconnect(self._on_nao_disconnected)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self._on_nao_connected)
            self._nao.disconnected.connect(self._on_nao_disconnected)
        #END if
    #END setNao()

    def hideEvent(self, event):
        self._idleRun = False
        self.killTimer(self._timerID)
    #END hideEvent()

    def showEvent(self, event):
        self._timerID = self.startTimer(10000)
    #END showEvent()

    def timerEvent(self, event):
        if self._idleRun:
            if self._idleCount <= 5:
                actions = EmpathyBehaviorButton.getBehavior(EmpathyBehaviorButton.INDEX_SMALL_IDLE).getRobotActions(self.getJitterLevel())
            else:
                actions = EmpathyBehaviorButton.getBehavior(EmpathyBehaviorButton.INDEX_BIG_IDLE).getRobotActions(self.getJitterLevel())
            #END if
            actions.append(ActionStart())
            if not self._actionQueue.isRunning() and self._actionQueue.rowCount(None) <= 0:
                self._actionQueue.addActions(actions)
                self._idleCount = (self._idleCount + 1) % 5
            #END if
        #END if
    #END timerEvent()

    def _on_actionbutton_clicked(self):
        self._actionQueue.addActions(self.sender().getRobotActions())
    #END _on_actionbutton_clicked()

    def _on_behaviorbutton_clicked(self):
        self._actionQueue.addActions(self.sender().getRobotActions(self.getJitterLevel()))
    #END _on_behaviorbutton_clicked()

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

    def _on_filler_triggered(self):
        actions = EmpathyBehaviorButton.getBehavior(EmpathyBehaviorButton.INDEX_FILLER).getRobotActions(self.getJitterLevel())
        actions.append(ActionStart())
        self._actionQueue.addActions(actions)
    #END _on_filler_triggered()

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

    def _on_motionbutton_clicked(self):
        motion = str(self.getJitterLevel()) + "_" + str(self.sender().text())
        motion = EmpathyBehaviorButton.getMotionByName(motion)
        if motion is not None:
            self._actionQueue.addActions([Stiffness(1.0), Motion(motion = motion, blocking = False)])
        #ENd if
    #END _on_motionbutton_clicked()

    def _on_nao_connected(self):
        pass
    #END _on_nao_connected()

    def _on_nao_disconnected(self):
        pass
    #END _on_nao_disconnected()

    def _on_participantName_edited(self):
        EmpathySpeech.ParticipantName = str(self._participantName.text())
    #END _on_participantName_edited()

    def _on_sayanswer_clicked(self):
        action = Speech(self._toCoordinate(self._last[1], self._last[0]) + ", " + str(self._last[2]))
        self._actionQueue.addActions(action)
    #END _on_sayanswer_clicked()

    def _on_solveone_clicked(self):
        self._wgtSudoku.solveOne()
    #END _on_solveone_clicked()

    def _on_sudoku_valueChanged(self, i, j, value):
        if self._currSubgrid is not None:
            self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1])
            self._currSubgrid = None
        #END if
        self._last = [i, j, value]
        if value != 0:
            actions = EmpathyBehaviorButton.getBehavior(EmpathyBehaviorButton.INDEX_SUDOKU_ANSWER).getRobotActions(self.getJitterLevel())
            actions.append(Speech(self._toCoordinate(j, i) + ", " + str(value)))
            self._actionQueue.addActions(actions)
        #END if
    #END _on_sudoku_valueChanged()

    def _on_toggleIdle_triggered(self):
        self._idleRun = not self._idleRun
    #END _on_toggleIdle_triggered()

    def _toCoordinate(self, x, y):
        txt = "aet "
        if x == 0:
            txt = txt + "ay"
        elif x == 1:
            txt = txt + "bee"
        elif x == 2:
            txt = txt + "see"
        elif x == 3:
            txt = txt + "d"
        elif x == 4:
            txt = txt + "e"
        elif x == 5:
            txt = txt + "f"
        elif x == 6:
            txt = txt + "g"
        elif x == 7:
            txt = txt + "h"
        else:
            txt = txt + "ayi"
        #END if
        return txt + " " + str(y + 1)
    #END _toCoordinate()

    def _setupUi(self):
        #=======================================================================
        # Shortcuts
        #=======================================================================
        self._actShortcuts = []
        for i in range(1, 10):
            action = QtGui.QAction(str(i), self)
            action.setShortcut(QtCore.Qt.Key_0 + i)
            action.triggered.connect(self._on_boardshortcut_triggered)
            self._actShortcuts.append(action)
            self.addAction(action)
        #END for

        action = QtGui.QAction("Idle_Toggle", self)
        action.setShortcut(QtCore.Qt.Key_Minus)
        action.triggered.connect(self._on_toggleIdle_triggered)
        self.addAction(action)

        action = QtGui.QAction("Run_Filler", self)
        action.setShortcut(QtCore.Qt.Key_Plus)
        action.triggered.connect(self._on_filler_triggered)
        self.addAction(action)

        action = QtGui.QAction("Solve", self)
        action.setShortcut(QtCore.Qt.Key_0)
        action.triggered.connect(self._on_solveone_clicked)
        self.addAction(action)

        action = QtGui.QAction("SayAgain", self)
        action.setShortcut(QtCore.Qt.Key_Period)
        action.triggered.connect(self._on_sayanswer_clicked)
        self.addAction(action)

        action = QtGui.QAction("JLv_Increment", self)
        action.setShortcut("Shift+Up")
        action.triggered.connect(lambda: self._sbCurrLevel.setValue(self._sbCurrLevel.value() + 1))
        self.addAction(action)

        action = QtGui.QAction("JLv_Decrement", self)
        action.setShortcut("Shift+Down")
        action.triggered.connect(lambda: self._sbCurrLevel.setValue(self._sbCurrLevel.value() - 1))
        self.addAction(action)

        #=======================================================================
        # Widgets
        #=======================================================================
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)

        added = dict()
        motions = EmpathyBehaviorButton.getMotions()
        for i in range(len(motions)):
            motions[i] = motions[i][2:]
        #END for
        motions = sorted(motions)
        widgetMotions = QtGui.QWidget()
        layoutMotions = QtGui.QVBoxLayout(widgetMotions)
        layoutMotions.setMargin(0)
        for name in motions:
            if not name in added:
                added[name] = True
                button = QtGui.QPushButton(name, widgetMotions)
                button.clicked.connect(self._on_motionbutton_clicked)
                layoutMotions.addWidget(button)
            #END if
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
            if str(button.text()) == "\\CUT\\":
                scroll = QtGui.QScrollArea()
                scroll.setAlignment(QtCore.Qt.AlignCenter)
                scroll.setWidget(widgetBehaviors)
                layoutScroll = QtGui.QHBoxLayout()
                layoutScroll.setMargin(0)
                layoutScroll.addWidget(scroll)
                widget = QtGui.QWidget(splitter)
                widget.setLayout(layoutScroll)

                widgetBehaviors = QtGui.QWidget()
                layoutBehaviors = QtGui.QVBoxLayout(widgetBehaviors)
                layoutBehaviors.setMargin(0)
            else:
                button.clicked.connect(self._on_behaviorbutton_clicked)
                layoutBehaviors.addWidget(button)
            #END if
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
                    Motion("WaveHandLeft"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
                ]),
            ActionPushButton(None, "Nice Meet", [
                    EmpathySpeech("Hi, nice to meet you, \\NAME\\"),
                    Behavior("SitDown"),
                    Motion("Default"),
                ]),

            QtGui.QLabel("PHASE 1"),
            ActionPushButton(None, "Play well?", [
                    Stiffness(1.0),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(600),
                    Speech("It's so exciting to play with someone else"),
                    Motion("PalmUp", speed = 2.0),
                    Speech("Do you play Sudoku well?"),
                ]),
            ActionPushButton(None, "Yes:", [
                    Stiffness(1.0),
                    Motion("OhYesRight", speed = 2.0),
                    Wait(1200),
                    Speech("Oh, yes!"),
                    Speech("My last partner was not really good.", blocking = False),
                    Motion("PalmUpRight", speed = 2.0),
                    Wait(500),
                    Motion("PalmUpLeft", speed = 2.0),
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
                    Speech("Ahhhe"),
                    Motion("DisagreeRight", speed = 2.0, repeat = 3, repeatBegin = 5, repeatEnd = 7, repeatSpeed = 5.0),
                    Wait(600),
                    Speech("I can't ple- ple- play anymore."),
                ]),
            ActionPushButton(None, "Go ahead", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 2.2),
                    Motion("PointYouRight", speed = 2.2, repeat = 4, repeatBegin = 5, repeatEnd = 8, repeatSpeed = 3.0),
                    Wait(750),
                    Speech("I need some rest, please "),
                    Speech("\\RST\\ \\RSPD=150\\ go-, go-, go-, \\RST\\ \\RSPD=90\\ go ahead"),
                ]),

            QtGui.QLabel("PHASE 5"),
            ActionPushButton(None, "Okay?->Answer", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Wait(700),
                    Speech("Ye- Ye- yeah, certainly"),
                    Wait(500),
                    Speech("I am okay."),
                ]),
            ActionPushButton(None, "What's wrong?->Answer", [
                    Stiffness(1.0),
                    Motion("Wait", speed = 2.0),
                    Speech("No, nothing, nothing really."),
                    Wait(700),
                    Motion("PalmUpLeft", speed = 2.0, repeat = 3, repeatBegin = 3, repeatEnd = 5, repeatSpeed = 3.0),
                    Speech("Don't worry."),
                ]),
            ActionPushButton(None, "Tell me?->Answer", [
                    Stiffness(1.0),
                    Speech("Thank you for worrying about me.", blocking = False),
                    Motion("ForgetItRight", speed = 1.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 5.0),
                    Speech("But I am fhi- fhi- fine."),
                ]),
            ActionPushButton(None, "For experiment?->Answer", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 1.6, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 3.0),
                    Wait(100),
                    Speech("We are playing Sudoku"),
                    Motion("PalmUp", speed = 2.0),
                    Speech("This is for the expe- expe- expe-."),
                    Speech("Sorry."),
                    Motion("PointYouLeft", speed = 2.5),
                    Wait(500),
                    Speech("This is for the experiment."),
                ]),

            QtGui.QLabel("PHASE 6"),
            ActionPushButton(None, "Don't tell anyone", [
                    Stiffness(1.0),
                    Motion("WhisperLeft", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 4.0),
                    Wait(700),
                    Speech("Well, I really shouldn't teh- teh- tell anyone."),
                    Motion("PalmUpRight", speed = 2.0, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 4.0),
                    Wait(500),
                    Speech("Please, don't tell any- any- any-. Ahhhe, anyone."),
                ]),
            ActionPushButton(None, "Yes: ", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.5, repeat = 4, repeatBegin = 10, repeatEnd = 12, repeatSpeed = 2.0),
                    Wait(850),
                    Speech("Thank you for your kai- kai- kindness."),
                    Motion("PalmUpLeft", speed = 2.0, repeat = 3, repeatBegin = 6, repeatEnd = 7, repeatSpeed = 3.5),
                    Wait(500),
                    Speech("But, let's keep so- so- solving the Sudoku for now"),
                ]),
            ActionPushButton(None, "No: ", [
                    Stiffness(1.0),
                    Motion("ForgetItRight", speed = 2.2, repeat = 4, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
                    Wait(500),
                    Speech("It's oh- oh- okay."),
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
                ]),
            ActionPushButton(None, "Reset to fix", [
                    Stiffness(1.0),
                    Motion("DontKnow", speed = 2.3, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("The only way to fix is to re- re- reset and erase myself.", speed = 80),
                ]),
            ActionPushButton(None, "My memories", [
                    Stiffness(1.0),
                    Motion("PointYouRight", speed = 2.2, repeat = 3, repeatBegin = 7, repeatEnd = 9, repeatSpeed = 2.0),
                    Speech("I'm not sure what will happen with my- my- my memories.", speed = 80),
                    Motion("PalmUp", speed = 1.5, repeat = 5, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
                    Speech("I don't want to lose my- my- my memories.", speed = 80),
                    Speech("So I'm worried.", speed = 85, shaping = 120),
                ]),
            ActionPushButton(None, "Thank. Continue", [
                    Stiffness(1.0),
                    Motion("PalmUp", speed = 1.8, repeat = 4, repeatBegin = 9, repeatEnd = 11, repeatSpeed = 2.0),
                    Motion("PointYouRight", speed = 2.2, repeat = 3, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 2.0),
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
                    Motion("PalmUp", speed = 1.5, repeat = 5, repeatBegin = 4, repeatEnd = 6, repeatSpeed = 5.0),
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
                    Motion("WaveHandRight"),
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
            #END if
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
        self._wgtSudoku.valueChanged.connect(self._on_sudoku_valueChanged)
        self._btnGames = []

        splitter = QtGui.QSplitter()
        splitter.setOrientation(QtCore.Qt.Vertical)
        splitter.addWidget(self._wgtSudoku)

        widgetControls = QtGui.QWidget(splitter)
        layoutControls = QtGui.QHBoxLayout(widgetControls)
        layoutControls.setMargin(0)

        widgetGames = QtGui.QWidget(widgetControls)
        layoutGames = QtGui.QVBoxLayout(widgetGames)
        layoutGames.setMargin(0)
        button = QtGui.QPushButton("Training", widgetGames)
        button.clicked.connect(self._on_gamebutton_clicked)
        layoutGames.addWidget(button)
        self._btnGames.append(button)
        for i in range(10):
            button = QtGui.QPushButton("Game " + str(i + 1), widgetGames)
            button.clicked.connect(self._on_gamebutton_clicked)
            layoutGames.addWidget(button)
            self._btnGames.append(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetGames)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        layoutControls.addLayout(layoutScroll)

        widgetExtra = QtGui.QWidget(widgetControls)
        layoutExtra = QtGui.QVBoxLayout(widgetExtra)
        layoutExtra.setMargin(0)

        widgetName = QtGui.QWidget(widgetExtra)
        layoutName = QtGui.QHBoxLayout(widgetName)
        layoutName.setMargin(0)
        layoutName.addWidget(QtGui.QLabel("Name:", widgetName))
        self._participantName = QtGui.QLineEdit(widgetName)
        self._participantName.setMaximumWidth(80)
        self._participantName.setMinimumWidth(80)
        self._participantName.textEdited.connect(self._on_participantName_edited)
        layoutName.addWidget(self._participantName)
        layoutExtra.addWidget(widgetName)

        widgetLevel = QtGui.QWidget(widgetExtra)
        layoutLevel = QtGui.QHBoxLayout(widgetLevel)
        layoutLevel.setMargin(0)
        layoutLevel.addWidget(QtGui.QLabel("Level:", widgetLevel))
        self._sbCurrLevel = QtGui.QSpinBox(widgetLevel)
        self._sbCurrLevel.setMaximumWidth(80)
        self._sbCurrLevel.setMinimumWidth(80)
        self._sbCurrLevel.setPrefix("lv ")
        self._sbCurrLevel.setRange(0, 7)
        self._sbCurrLevel.setSingleStep(1)
        self._sbCurrLevel.setValue(0)
        layoutLevel.addWidget(self._sbCurrLevel)
        layoutExtra.addWidget(widgetLevel)

        button = QtGui.QPushButton("Solve next answer")
        button.clicked.connect(self._on_solveone_clicked)
        layoutExtra.addWidget(button)

        button = QtGui.QPushButton("Say the answer again")
        button.clicked.connect(self._on_sayanswer_clicked)
        layoutExtra.addWidget(button)

        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetExtra)
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
