from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from Action import ActionStart
from Action import Behavior
from Action import LED
from Action import Motion
from Action import ReplaceableSpeech
from Action import Speech
from Action import Stiffness
from Action import Wait
from ActionCollection import ActionCollection
from MotionList import MotionList
from GenderButton import GenderButton
from GenderSpeech import GenderSpeech
from EmpathySudoku import SudokuBoards
from UI.ActionPushButton import ActionPushButton
from UI.SudokuBoard import SudokuBoard
import random


class Gender(QtGui.QWidget):
    def __init__(self):
        super(Gender, self).__init__()
        MotionList.initialize()
        random.seed()
        self._actions = []
        self._actionQueue = None
        self._currSubgrid = None
        self._idleCount = 0
        self._idleRun = False
        self._idleInterval = 10000
        self._idleTime = QtCore.QTime.currentTime()
        self._lastSudoku = [0, 0, 0] # x y value
        self._nao = None
        self._prevBoard = list()
        for i in range(9):
            self._prevBoard.append(dict())
            for j in range(9):
                self._prevBoard[i][j] = 0
            #END for
        #END for
        self._setupUi()
    #END __init__()

    def __del__(self):
        MotionList.destroy()
    #END __del__()

    def LEDActive(self):
        self._nao.LEDrandomEyes(1.0, True)
    #END LEDActive()

    def LEDNormal(self):
        self._nao.LEDfadeRGB(LEDNames.Face, 0x00000000, 0.5, True)
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

    def speech(self, txt, speed, shaping):
        return None
    #END speech()

    def hideEvent(self, event):
        self._idleRun = False
        self.killTimer(self._timerID)
    #END hideEvent()

    def showEvent(self, event):
        self._timerID = self.startTimer(50)
    #END showEvent()

    def timerEvent(self, event):
        if self._idleRun and self._idleTime < QtCore.QTime.currentTime():
            actions = self._bhvIdleSmall.get(0)
            actions.append(ActionStart())
            if not self._actionQueue.isRunning() and self._actionQueue.rowCount(None) <= 0:
                self._actionQueue.addActions(actions)
                self._idleCount = (self._idleCount + 1) % 5
            #END if
            self._idleTime = QtCore.QTime.currentTime().addMSecs(self._idleInterval)
        #END if
    #END timerEvent()

    def on_actionbutton_clicked(self):
        self._actionQueue.addActions(self.sender().getRobotActions())
    #END on_actionbutton_clicked()

    def on_autoidleint_valueChanged(self, value):
        self._idleInterval = value
    #END on_autoidleint_valueChanged()

    def on_behaviorbutton_clicked(self):
        self._actionQueue.addActions(self.sender().getRobotActions(0))
    #END on_behaviorbutton_clicked()

    def on_boardshortcut_triggered(self):
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
    #END on_boardshortcut_triggered()

    def on_filler_triggered(self):
        actions = self._bhvFiller.get(0)
        actions.append(ActionStart())
        self._actionQueue.addActions(actions)
    #END on_filler_triggered()

    def on_gamebutton_clicked(self):
        self._deselectSubgrid()
        for index in range(len(self._btnGames)):
            if self.sender() == self._btnGames[index]:
                for i in range(9):
                    for j in range(9):
                        self._prevBoard[i][j] = self._wgtSudoku.get(i, j)
                        self._wgtSudoku.set(i, j, SudokuBoards[index][i][j])
                    #END for
                #END for
                self._wgtSudoku.resetLastCoordinate()
                return
            #END if
        #END for
    #END on_gamebutton_clicked()

    def on_nao_connected(self):
        pass
    #END on_nao_connected()

    def on_nao_disconnected(self):
        pass
    #END on_nao_disconnected()

    def on_participantName_edited(self, value):
        GenderSpeech.ParticipantName = value
    #END on_participantName_edited()

    def on_prevBoard_clicked(self):
        prevBoard = list()
        for i in range(9):
            prevBoard.append(dict())
            for j in range(9):
                prevBoard[i][j] = self._wgtSudoku.get(i, j)
                self._wgtSudoku.set(i, j, self._prevBoard[i][j])
            #END for
        #END for
        self._prevBoard = prevBoard
    #END on_prevBoard_clicked()

    def on_sayanswer_clicked(self):
        action = Speech(self._toCoordinate(self._lastSudoku[1], self._lastSudoku[0]) + ", " + str(self._lastSudoku[2]))
        self._actionQueue.addActions(action)
    #END on_sayanswer_clicked()

    def on_sayanswerVerbose_clicked(self):
        action = Speech(self._toCoordinateVerbose(self._lastSudoku[1], self._lastSudoku[0]) + ", " + str(self._lastSudoku[2]))
        self._actionQueue.addActions(action)
    #END on_sayanswerVerbose_clicked()

    def on_solveOne_clicked(self):
        self._wgtSudoku.solveOne()
    #END on_solveOne_clicked()

    def on_sudoku_valueChanged(self, i, j, value):
        self._deselectSubgrid()
        self._lastSudoku = [i, j, value]
        if value != 0:
            actions = self._bhvAnswer.get(0)
            for action in actions:
                if isinstance(action, ReplaceableSpeech):
                    action.replace(self._toCoordinate(j, i), str(value))
                #END if
            #END for
            self._actionQueue.addActions(actions)
        #END if
    #END on_sudoku_valueChanged()

    def on_toggleIdle_triggered(self):
        self._idleRun = not self._idleRun
        self._idleTime = 0
    #END on_toggleIdle_triggered()

    def _deselectSubgrid(self):
        if self._currSubgrid is not None:
            self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1])
            self._currSubgrid = None
        #END if
    #END _deselectSubgrid()

    def _toCoordinate(self, x, y):
        txt = "aet"
        if x == 0:
            txt += ", \\RST\\ \\RSPD=50\\ ay. \\RST\\ \\RSPD=90\\"
        elif x == 1:
            txt += ", bee,"
        elif x == 2:
            txt += ", see,"
        elif x == 3:
            txt += ", dee,"
        elif x == 4:
            txt += ", \\RST\\ \\RSPD=50\\ eeh. \\RST\\ \\RSPD=90\\"
        elif x == 5:
            txt += ", f,"
        elif x == 6:
            txt += ", geeh."
        elif x == 7:
            txt += ", h."
        elif x == 8:
            txt += ", ai."
        else:
            txt += ", " + str(x) + "."
        #END if
        return txt + " " + str(y + 1)
    #END _toCoordinate()

    def _toCoordinateVerbose(self, x, y):
        txt = "aet"
        if x == 0:
            txt += ", \\RST\\ \\RSPD=50\\ ay. \\RST\\ \\RSPD=90\\ as in ace."
        elif x == 1:
            txt += ", bee, as in basement."
        elif x == 2:
            txt += ", see, as in car."
        elif x == 3:
            txt += ", dee, as in dream."
        elif x == 4:
            txt += ", \\RST\\ \\RSPD=50\\ eeh. \\RST\\ \\RSPD=90\\ as in elephant."
        elif x == 5:
            txt += ", f, as in feel."
        elif x == 6:
            txt += ", geeh. as in genius."
        elif x == 7:
            txt += ", h. as in honeybee."
        elif x == 8:
            txt += ", ai. as in identity."
        else:
            txt += ", " + str(x) + "."
        #END if
        return txt + " " + str(y + 1)
    #END _toCoordinateVerbose()

    def _setupWidget(self, wgt, children):
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)
        for child in children:
            if isinstance(child, ActionPushButton):
                child.clicked.connect(self.on_actionbutton_clicked)
            elif isinstance(child, GenderButton):
                child.clicked.connect(self.on_behaviorbutton_clicked)
                bhv = child.getActionCollection()
                if bhv.hasText():
                    self._actions.append(bhv)
                #END if
            #END if
            layout.addWidget(child)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widget)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(wgt)
        widget.setLayout(layoutScroll)
        return widget
    #END _setupWidget()

    def _setupUi(self):
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        Gender._setupScenario(self, splitter)
        Gender._setupSudokuUi(self, splitter)
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        Gender._setupShortcuts(self)
    #END _setupUi()
    
    def _setupBehaviours(self):
        bhv = ActionCollection("Idle (Big)")
        for i in range(10):
            bhv.add(i, None, "ChinHoldLeft")
            bhv.add(i, None, "ChinHoldRight")
            bhv.add(i, None, "Idle3")
            bhv.add(i, None, "Idle5")
            bhv.add(i, None, "Idle6")
        #END for
        self._bhvIdleBig = bhv

        bhv = ActionCollection("Idle (Small)")
        for i in range(10):
            bhv.add(i, None, "Idle0")
            bhv.add(i, None, "Idle1")
            bhv.add(i, None, "Idle2")
        #END for
        self._bhvIdleSmall = bhv
        
        bhv = ActionCollection("Conv. Filler")
        bhv.add(0, [Speech("ummmh,", speed = 50)])
        bhv.add(0, [Speech("well,", speed = 50)])
        bhv.add(0, [Speech("well,", speed = 50)])
        bhv.add(0, [Speech("let me think", speed = 80)])
        bhv.add(0, [Speech("let's see", speed = 80)])
        self._bhvFiller = bhv
    #END _setupBehaviours()

    def _setupScenario(self, wgt):
        components = list()

        widgetName = QtGui.QWidget()
        lineeditName = QtGui.QLineEdit(widgetName)
        lineeditName.setMinimumWidth(80)
        lineeditName.textEdited.connect(lambda: self.on_participantName_edited(str(lineeditName.text())))
        layoutName = QtGui.QHBoxLayout(widgetName)
        layoutName.setMargin(0)
        layoutName.addWidget(QtGui.QLabel("Name:", widgetName))
        layoutName.addWidget(lineeditName)
        components.append(widgetName)

        components.append(QtGui.QLabel("INTRODUCTION"))

        components.append(ActionPushButton(None, "Welcome", [
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHandLeft"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
            ]))

        components.append(ActionPushButton(None, "Nice Meet", [
                    GenderSpeech("Hi, nice to meet you, " + GenderSpeech.NAME_MARKER),
                    Behavior("SitDown"),
                    Motion("Default"),
            ]))

        return self._setupWidget(wgt, components)
    #END _setupScenario()

    def _setupShortcuts(self):
        self._actShortcuts = []
        for i in range(1, 10):
            action = QtGui.QAction(str(i), self)
            action.setShortcut(QtCore.Qt.Key_0 + i)
            action.triggered.connect(self.on_boardshortcut_triggered)
            self._actShortcuts.append(action)
            self.addAction(action)
        #END for

        action = QtGui.QAction("Idle_Toggle", self)
        action.setShortcut(QtCore.Qt.Key_Minus)
        action.triggered.connect(self.on_toggleIdle_triggered)
        self.addAction(action)

        action = QtGui.QAction("Solve", self)
        action.setShortcut(QtCore.Qt.Key_0)
        action.triggered.connect(self.on_solveOne_clicked)
        self.addAction(action)

        action = QtGui.QAction("SayAgain", self)
        action.setShortcut(QtCore.Qt.Key_Period)
        action.triggered.connect(self.on_sayanswer_clicked)
        self.addAction(action)
    #END _setupShortcuts()

    def _setupSudokuUi(self, wgt):
        self._wgtSudoku = SudokuBoard()
        self._wgtSudoku.valueChanged.connect(self.on_sudoku_valueChanged)
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
        button = QtGui.QPushButton("Prev. Board", widgetGames)
        button.clicked.connect(self.on_prevBoard_clicked)
        layoutGames.addWidget(button)
        button = QtGui.QPushButton("Training", widgetGames)
        button.clicked.connect(self.on_gamebutton_clicked)
        layoutGames.addWidget(button)
        self._btnGames.append(button)
        for i in range(10):
            button = QtGui.QPushButton("Game " + str(i + 1), widgetGames)
            button.clicked.connect(self.on_gamebutton_clicked)
            layoutGames.addWidget(button)
            self._btnGames.append(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetGames)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)

        widgets = []
        button = QtGui.QPushButton("Solve next answer")
        button.clicked.connect(self.on_solveOne_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer again")
        button.clicked.connect(self.on_sayanswer_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer (verbose)")
        button.clicked.connect(self.on_sayanswerVerbose_clicked)
        widgets.append(button)

        bhv = ActionCollection("#", False)
        bhv.add(0, [ReplaceableSpeech("I believe the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("The number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("%1, Let's try, the number, %2.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyself")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        widgets.append(GenderButton(bhv))
        self._bhvAnswer = bhv

        bhv = ActionCollection("Can't read", False)
        bhv.add(0, [Speech("I barely can read."), Speech("Tell me what you wrote.")])
        bhv.add(0, [Speech("I barely can read."), Speech("Can you hold it up?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you tell me what you wrote?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you hold it up?")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Disagree")
            bhv.add(i, None, "DisagreeLeft")
            bhv.add(i, None, "DisagreeRight")
            bhv.add(i, None, "DontKnow")
            bhv.add(i, None, "DontKnowLeft")
            bhv.add(i, None, "DontKnowRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointMyself")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
        #END for
        widgets.append(GenderButton(bhv))

        bhv = ActionCollection("Which box filled?", False)
        bhv.add(0, [Speech("Which box did you fill?")])
        bhv.add(0, [Speech("Where was it?")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "DontKnow")
            bhv.add(i, None, "DontKnowLeft")
            bhv.add(i, None, "DontKnowRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "ForgetItLeft")
            bhv.add(i, None, "ForgetItRight")
        #END for
        widgets.append(GenderButton(bhv))

        bhv = ActionCollection("Fill number for me", False)
        bhv.add(0, [Speech("Can you fill the number in for me?")])
        bhv.add(0, [Speech("Would you fill the number in for me?")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        widgets.append(GenderButton(bhv))

        bhv = ActionCollection("My turn", False)
        bhv.add(0, [Speech("It's my turn."), Speech("Wait for me please.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyself")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        widgets.append(GenderButton(bhv))

        bhv = ActionCollection("Your turn", False)
        bhv.add(0, [Speech("It's your turn.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        widgets.append(GenderButton(bhv))

        widget = self._setupWidget(widgetControls, widgets)

        layoutControls.addLayout(layoutScroll)
        layoutControls.addWidget(widget)
        layout = QtGui.QHBoxLayout(wgt)
        layout.setMargin(0)
        layout.addWidget(splitter)
        return layout
    #END _setupSudokuUi()
#END Empathy
