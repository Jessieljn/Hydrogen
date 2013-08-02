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
from EmpathyButton import EmpathyButton
from EmpathySpeech import EmpathySpeech
from EmpathySudoku import SudokuBoards
from UI.ActionPushButton import ActionPushButton
import random


class Empathy(QtGui.QWidget):
    def __init__(self):
        super(Empathy, self).__init__()
        MotionList.initialize()
        random.seed()
        self._actions = []
        self._actionQueue = None
        self._currSubgrid = None
        self._idleCount = 0
        self._idleRun = False
        self._idleInterval = 10000
        self._idleTime = QtCore.QTime.currentTime()
        self._itemName = "shirt"
        self._jitterLevel = 0
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
        current_phase = self._jitterLevel
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

    def speech(self, txt):
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
            if self._idleCount <= 5:
                actions = self.bhvIdleSmall.getRobotActions(self._jitterLevel)
            else:
                actions = self.bhvIdleBig.getRobotActions(self._jitterLevel)
            #END if
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
        self._actionQueue.addActions(self.sender().getRobotActions(self._jitterLevel))
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
        actions = self.bhvFiller.getRobotActions(self._jitterLevel)
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
                return
            #END if
        #END for
    #END on_gamebutton_clicked()

    def on_itemLike_clicked(self, bhv):
        actions = bhv.getRobotActions(self._jitterLevel)
        for action in actions:
            if isinstance(action, ReplaceableSpeech):
                action.replace(self._itemName)
            #END if
        #END for
        self._actionQueue.addActions(actions)
    #END on_itemLike_clicked()

    def on_itemName_changed(self, value):
        self._itemName = value
    #END on_itemName_changed()

    def on_jitterLevel_valueChanged(self, value):
        jlv = value
        if jlv <= 0:
            jlv = 0
        elif jlv <= 6:
            jlv = jlv - 1
        else:
            jlv = 0
        #END if
        self._jitterLevel = jlv
    #END on_jitterLevel_valueChanged()

    def on_motionbutton_clicked(self):
        motion = str(self._jitterLevel) + "_" + str(self.sender().text())
        motion = MotionList.getByName(motion)
        if motion is not None:
            self._actionQueue.addActions([Stiffness(1.0), Motion(motion = motion, blocking = False)])
        #ENd if
    #END on_motionbutton_clicked()

    def on_nao_connected(self):
        pass
    #END on_nao_connected()

    def on_nao_disconnected(self):
        pass
    #END on_nao_disconnected()

    def on_participantName_edited(self, value):
        EmpathySpeech.ParticipantName = value
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

    def on_sudoku_valueChanged(self, i, j, value):
        self._deselectSubgrid()
        self._lastSudoku = [i, j, value]
        if value != 0:
            actions = self.bhvAnswer.getRobotActions(self._jitterLevel)
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
        else:
            txt += ", ai."
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
        else:
            txt += ", ai. as in identity."
        #END if
        return txt + " " + str(y + 1)
    #END _toCoordinateVerbose()

    def _markSpeech(self, speed = 90, shaping = 100):
        # ending mark + speed + shaping
        return " \\RST\\ \\RSPD=" + str(speed) + "\\ \\VCT=" + str(shaping) + "\\ "
    #END _markSpeech()

    def _setupWidget(self, wgt, children):
        widget = QtGui.QWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setMargin(0)
        for child in children:
            if isinstance(child, ActionPushButton):
                child.clicked.connect(self.on_actionbutton_clicked)
            elif isinstance(child, EmpathyScenarioButton):
                child.clicked.connect(self.on_actionbutton_clicked)
            elif isinstance(child, EmpathyRandomButton):
                child.clicked.connect(self.on_behaviorbutton_clicked)
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
        Empathy.setupScenario(self, splitter)
        Empathy.setupMotions(self, splitter)
        Empathy.setupInteractions(self, splitter)
        Empathy.setupSudokuUi(self, splitter)
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        Empathy.setupShortcuts(self)
    #END _setupUi()

    def _setupInteraction(self, wgt):
        bhv = ActionCollection("Conv. Filler")
        bhv.add(0, [Speech("ummmh,", speed = 50)])
        bhv.add(0, [Speech("well,", speed = 50)])
        bhv.add(0, [Speech("well,", speed = 50)])
        bhv.add(0, [Speech("let me think", speed = 80)])
        bhv.add(0, [Speech("let's see", speed = 80)])
        bhv.add(2, [Speech("ummmh,", speed = 50)])
        bhv.add(2, [Speech("well,", speed = 50)])
        bhv.add(2, [Speech("well,", speed = 50)])
        bhv.add(2, [Speech("let me think", speed = 80)])
        bhv.add(2, [Speech("let's see", speed = 80)])
        bhv.add(2, [Speech("ummmh,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech("well,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech("well,", speed = 60, shaping = 110)])
        bhv.add(2, [Speech("let me think", speed = 90, shaping = 110)])
        bhv.add(2, [Speech("let's see", speed = 90, shaping = 110)])
        bhv.add(4, [Speech("ummmh,", speed = 50)])
        bhv.add(4, [Speech("well,", speed = 50)])
        bhv.add(4, [Speech("well,", speed = 50)])
        bhv.add(4, [Speech("let me think", speed = 80)])
        bhv.add(4, [Speech("let's see", speed = 80)])
        bhv.add(4, [Speech("ummmh,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech("well,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech("well,", speed = 70, shaping = 130)])
        bhv.add(4, [Speech("let me" + self._markSpeech(90, 130) + "think", speed = 90, shaping = 110)])
        bhv.add(4, [Speech("let me" + self._markSpeech(90, 110) + "think", speed = 90, shaping = 130)])
        bhv.add(4, [Speech("let's" + self._markSpeech(90, 130) + "see", speed = 90, shaping = 110)])
        bhv.add(4, [Speech("let's" + self._markSpeech(90, 110) + "see", speed = 90, shaping = 130)])
        self._actions.append(bhv)
        self._bhvFiller = bhv

        bhv = ActionCollection("Idle (Big)")
        for i in range(10):
            bhv.add(i, motion = "ChinHoldLeft")
            bhv.add(i, motion = "ChinHoldRight")
            bhv.add(i, motion = "Idle3")
            bhv.add(i, motion = "Idle5")
            bhv.add(i, motion = "Idle6")
        #END for
        self._actions.append(bhv)
        self._bhvIdleBig = bhv

        bhv = ActionCollection("Idle (Small)")
        for i in range(10):
            bhv.add(i, motion = "Idle0")
            bhv.add(i, motion = "Idle1")
            bhv.add(i, motion = "Idle2")
        #END for
        self._actions.append(bhv)
        self._bhvIdleSmall = bhv

        bhv = ActionCollection("Thank you")
        bhv.addText("thank you")
        bhv.addText("thanks")
        bhv.add(0, [Speech("Thank you.", 80)])
        bhv.add(2, [Speech("Thank you.", 50)])
        bhv.add(2, [Speech("Thank" + self._markSpeech() + "you.", 50, 120)])
        bhv.add(4, [Speech("Tha- tha- thank you.", 50)])
        bhv.add(4, [Speech("Tha- Tha- thank" + self._markSpeech() + "you.", 50, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Good")
        bhv.addText("good")
        bhv.addText("cool")
        bhv.addText("nice")
        bhv.add(0, [Speech("Good.")])
        bhv.add(0, [Speech("Cool.")])
        bhv.add(0, [Speech("Nice.")])
        bhv.add(2, [Speech("Good.", 50)])
        bhv.add(2, [Speech("Cool.", 50)])
        bhv.add(2, [Speech("Nice.", 50)])
        bhv.add(4, [Speech("Good.", 50)])
        bhv.add(4, [Speech("Cool.", 50)])
        bhv.add(4, [Speech("Nice.", 50)])
        bhv.add(4, [Speech("Good.", 50, 120)])
        bhv.add(4, [Speech("Cool.", 50, 120)])
        bhv.add(4, [Speech("Nice.", 50, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Okay")
        bhv.add(0, [Speech("Okay.")])
        bhv.add(0, [Speech("I got it.")])
        bhv.add(0, [Speech("Understood.")])
        bhv.add(2, [Speech("Okay.", 50)])
        bhv.add(2, [Speech("I got it.", 60)])
        bhv.add(2, [Speech("Understood.", 50)])
        bhv.add(4, [Speech("Okay.", 50)])
        bhv.add(4, [Speech("I got it.", 60)])
        bhv.add(4, [Speech("Understood.", 50)])
        bhv.add(4, [Speech("Okay.", 50, 120)])
        bhv.add(4, [Speech("I" + self._markSpeech(60, 120) + "got it.", 60)])
        bhv.add(4, [Speech("Under" + self._markSpeech(50, 120) + "stood.", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "Idle5")
            bhv.add(i, motion = "Idle6")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("I agree")
        bhv.addText("agree")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("I agree.")])
        bhv.add(0, [Speech("You are right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("I agree.", 50)])
        bhv.add(2, [Speech("You are right.", 50)])
        bhv.add(4, [Speech("Yes", 50)])
        bhv.add(4, [Speech("I agree.", 50)])
        bhv.add(4, [Speech("You are right.", 50)])
        bhv.add(4, [Speech("Yes", 50, 120)])
        bhv.add(4, [Speech("I" + self._markSpeech(50, 120) + "agree.", 50)])
        bhv.add(4, [Speech("You are" + self._markSpeech(50, 120) + "right.", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Yes")
        bhv.addText("yes")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("Right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("Right.", 50)])
        bhv.add(4, [Speech("Yes", 50)])
        bhv.add(4, [Speech("Right.", 50)])
        bhv.add(4, [Speech("Yes", 50, 120)])
        bhv.add(4, [Speech("Right.", 50, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "Idle5")
            bhv.add(i, motion = "Idle6")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("No")
        bhv.addText("no")
        bhv.add(0, [Speech("No")])
        bhv.add(0, [Speech("I don't think so")])
        bhv.add(2, [Speech("No", 50)])
        bhv.add(2, [Speech("I don't think so", 50)])
        bhv.add(4, [Speech("No", 50)])
        bhv.add(4, [Speech("I don't think so", 50)])
        bhv.add(4, [Speech("No", 50, 120)])
        bhv.add(4, [Speech("I don't" + self._markSpeech(50, 120) + "think so", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "Disagree")
            bhv.add(i, motion = "DisagreeLeft")
            bhv.add(i, motion = "DisagreeRight")
            bhv.add(i, motion = "PalmUp")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("You are doing good")
        bhv.add(0, [Speech("You are doing very well.")])
        bhv.add(0, [Speech("You are very good at Sudoku.")])
        bhv.add(2, [Speech("You are" + self._markSpeech() + "doing very well.", 70, 120)])
        bhv.add(2, [Speech("You are" + self._markSpeech() + "very good at Sudoku.", 70, 120)])
        bhv.add(4, [Speech("You are" + self._markSpeech() + "do- do- do-" + self._markSpeech(50, 120) + "doing very well.", 70, 120)])
        bhv.add(4, [Speech("You are" + self._markSpeech() + "goo- goo- goo-" + self._markSpeech(50, 120) + "very good at Sudoku.", 70, 120)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("What you think?")
        bhv.add(0, [Speech("What do you think?")])
        bhv.add(2, [Speech("What do you" + self._markSpeech(95) + "thiin- thiin- thii-."), Speech("Ahhhe, what do you think?")])
        bhv.add(2, [Speech("What do you do you do you think?")])
        bhv.add(4, [Speech("What do you" + self._markSpeech(95) + "thiin- thiin- thii-."), Speech("Ahhhe, what do you think?")])
        bhv.add(4, [Speech("What do you do you do you think?")])
        bhv.add(4, [Speech("What do you" + self._markSpeech(70, 120) + "thiin- thiin- thii-."), Speech("Sorry.", speed = 50), Speech("What do you think?", 75, 110)])
        bhv.add(4, [Speech("What" + self._markSpeech(70, 120) + "do you thii-" + self._markSpeech(50) + "think?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Easy!")
        bhv.add(0, [Wait(300), Speech("This one is easy")])
        bhv.add(2, [Wait(300), Speech("This one is e- e- easy")])
        bhv.add(4, [Wait(300), Speech("This one is" + self._markSpeech(90, 110) + "e- e-" + self._markSpeech(50, 130) + "e- e-."), Speech("Sorry. This one is easy")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Difficult!")
        bhv.add(0, [Wait(300), Speech("I don't know")])
        bhv.add(0, [Wait(300), Speech("This one is difficult")])
        bhv.add(2, [Wait(300), Speech("I don't noh- know")])
        bhv.add(2, [Wait(300), Speech("This one- one- one-."), Speech("This one is difficult")])
        bhv.add(4, [Wait(300), Speech("I don't no- no- noh-."), Speech("No.", 50, 130), Speech("I don't know")])
        bhv.add(4, [Wait(300), Speech("This one is diff- diff- diff-."), Speech("Ahhhe.", 50, 130), Speech("Sorry. This one is difficult", 70)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "DontKnow")
            bhv.add(i, motion = "DontKnowLeft")
            bhv.add(i, motion = "DontKnowRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "ChinHoldLeft")
            bhv.add(i, motion = "ChinHoldRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("This board?")
        bhv.add(0, [Speech("Do you find this board easy?")])
        bhv.add(0, [Speech("Do you find this board difficult?")])
        bhv.add(0, [Speech("What do you think about this board, is it easy or difficult.")])
        bhv.add(2, [Speech("Is this" + self._markSpeech(80, 115) + "board easy?")])
        bhv.add(2, [Speech("Is this" + self._markSpeech(80, 115) + "board difficult?")])
        bhv.add(2, [Speech("What" + self._markSpeech(80, 115) + "do you think about" + self._markSpeech(90, 100) + "this board?")])
        bhv.add(4, [Speech("Is this" + self._markSpeech(80, 130) + "board easy?", 50)])
        bhv.add(4, [Speech("Is this" + self._markSpeech(80, 130) + "board difficult?", 50)])
        bhv.add(4, [Speech("What" + self._markSpeech(80, 130) + "do you thiih thiih think about" + self._markSpeech(90, 100) + "this board?", 50)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "DontKnowLeft")
            bhv.add(i, motion = "DontKnowRight")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Almost done")
        bhv.add(0, [Speech("We are almost done with this board.")])
        bhv.add(0, [Speech("Few more numbers to finish this board.")])
        bhv.add(2, [Speech("We are almost" + self._markSpeech(80, 110) + "done with this board.")])
        bhv.add(2, [Speech("Few more numbers to" + self._markSpeech(80, 110) + "finish this board.")])
        bhv.add(4, [Speech("We are almost" + self._markSpeech(80, 120) + "done with the- the- the-" + self._markSpeech() + "this board.", 130)])
        bhv.add(4, [Speech("Few more numbers to" + self._markSpeech(80, 110) + "fii- fii-." + self._markSpeech() + "Sorry.finish this board.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Don't like board")
        bhv.add(0, [Speech("I don't like this board."), Speech("Let's start a new board.")])
        bhv.add(0, [Speech("I don't like this board."), Speech("Can we start a new board?")])
        bhv.add(0, [Speech("This board is not interesting."), Speech("Let's start a new board.")])
        bhv.add(2, [Speech("I don't lie- lie- like this board."), Speech("Let's start a new boh- boh- board.")])
        bhv.add(2, [Speech("I don't like this board."), Speech("Can we start a new boh- boh- board?")])
        bhv.add(2, [Speech("This board is not in- in- interesting."), Speech("Le- le- let's start a new board.")])
        bhv.add(4, [Speech("I don't lie- lie-" + self._markSpeech() + "like this board.", 80, 120), Speech("Let's start a new" + self._markSpeech(80, 110) + "boh- boh- board.")])
        bhv.add(4, [Speech("I don't like" + self._markSpeech(80, 120) + "this board."), Speech("Can we start a new boh- boh- board?")])
        bhv.add(4, [Speech("This board is not in- in- interesting."), Speech("Le- le- let's start" + self._markSpeech(80, 120) + "a new board.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Show me next board")
        bhv.add(0, [Speech("Can you show me next Sudoku board?")])
        bhv.add(0, [Speech("Let's move on to next board.")])
        bhv.add(2, [Speech("Can you" + self._markSpeech(50) + "sho- sho-." + self._markSpeech() + "show me next Sudoku board?")])
        bhv.add(2, [Speech("Let's" + self._markSpeech(50) + "moo- moo-." + self._markSpeech() + "move on to next board.")])
        bhv.add(4, [Speech("Can you" + self._markSpeech(50) + "sho- sho- sho-." + self._markSpeech(50, 130) + "I'm Sorry." + self._markSpeech() + "Can you show me next Sudoku board?")])
        bhv.add(4, [Speech("Let's" + self._markSpeech(50) + "moo moo- mooh-." + self._markSpeech(50, 130) + "I'm Sorry." + self._markSpeech() + "Let's move on to next board.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyself")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Continue Sudoku")
        bhv.add(0, [Speech("Let's continue playing Sudoku.")])
        bhv.add(2, [Speech("Let's" + self._markSpeech(50) + "continue" + self._markSpeech() + "playing Sudoku.")])
        bhv.add(4, [Speech(self._markSpeech(75) + "Let's" + self._markSpeech(50, 120) + "cont- cont-" + self._markSpeech() + "continue playing Sudoku.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Play together")
        bhv.add(0, [Speech("Wait. I wanna play too.")])
        bhv.add(0, [Speech("Let's play together")])
        bhv.add(2, [Speech(self._markSpeech(70) + "Let's play" + self._markSpeech(90, 130) + "together.")])
        bhv.add(2, [Speech("Wait. I wanna ple- ple- ple-."), Speech("Wait. I wanna play too.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "DisagreeLeft")
            bhv.add(i, motion = "DisagreeRight")
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Need help?")
        bhv.add(0, [Speech("Are you okay?"), Speech("I can help you.")])
        bhv.add(0, [Speech("I can help you out.")])
        bhv.add(0, [Speech("Do you need any help?")])
        bhv.add(2, [Speech("Are you oh- okay?"), Speech("I can help you.")])
        bhv.add(2, [Speech("I can" + self._markSpeech(80, 120) + "help you out.")])
        bhv.add(2, [Speech("Do you need any heh- heh-." + self._markSpeech(80) + "Do you need any help?")])
        bhv.add(4, [Speech("Are you okay?"), Speech("I can he- heh-."), Speech("I can help you.")])
        bhv.add(4, [Speech("I can" + self._markSpeech(80, 120) + "help you out.")])
        bhv.add(4, [Speech("Do you need any heh- heh- heh- heh-."), Speech("Sorry." + self._markSpeech(80) + "Do you need any help?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyself")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "ForgetItLeft")
            bhv.add(i, motion = "ForgetItRight")
            bhv.add(i, motion = "WaveHandLeft")
            bhv.add(i, motion = "WaveHandRight")
        #END for
        self._actions.append(bhv)

        bhv = ActionCollection("Don't touch me")
        bhv.add(0, [Speech("Please, do not touch me.")])
        bhv.add(2, [Speech("Please, do not theh- touch me.")])
        bhv.add(4, [Speech("Please, do not" + self._markSpeech(140, 130) + "touch me.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "Disagree")
            bhv.add(i, motion = "DisagreeLeft")
            bhv.add(i, motion = "DisagreeRight")
        #END for
        self._actions.append(bhv)

        return self._setupWidget(wgt, self._actions)
    #END _setupInteraction()

    def _setupMotions(self, wgt):
        added = dict()
        motions = MotionList.getMotions()
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
                button.clicked.connect(self.on_motionbutton_clicked)
                layoutMotions.addWidget(button)
            #END if
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetMotions)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)
        widget = QtGui.QWidget(wgt)
        widget.setLayout(layoutScroll)
        return widget
    #END _setupMotions()

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

        widgetLevel = QtGui.QWidget()
        spinbox = QtGui.QSpinBox(widgetLevel)
        spinbox.setMinimumWidth(80)
        spinbox.setPrefix("lv ")
        spinbox.setRange(0, 7)
        spinbox.setSingleStep(1)
        spinbox.setValue(0)
        spinbox.valueChanged.connect(self.on_jitterLevel_valueChanged)
        layoutLevel = QtGui.QHBoxLayout(widgetLevel)
        layoutLevel.setMargin(0)
        layoutLevel.addWidget(QtGui.QLabel("Level:", widgetLevel))
        layoutLevel.addWidget(spinbox)
        self._sbCurrLevel = spinbox
        components.append(widgetLevel)

        components.append(QtGui.QLabel("INTRODUCTION"))

        components.append(ActionPushButton(None, "Welcome", [
                    Speech("Oh!"),
                    Behavior("StandUp"),
                    Wait(200),
                    Motion("WaveHandLeft"),
                    Speech("Hi, nice to meet you."),
                    Speech("My name is Nao."),
                    Wait(500),
                    Speech("What's your name?"),
            ]))

        components.append(ActionPushButton(None, "Nice Meet", [
                    EmpathySpeech("Hi, nice to meet you, " + EmpathySpeech.NAME_MARKER),
                    Behavior("SitDown"),
                    Motion("Default"),
            ]))

        components.append(QtGui.QLabel("0 mins, PHASE 1"))
        bhv = ActionCollection("It's exciting", False)
        bhv.add(0, Speech("It's so exciting to play with someone else"), "PalmUp")
        components.append(EmpathyButton(bhv))

        bhv = ActionCollection("Play well?", False)
        bhv.add(0, Speech("Do you play Sudoku well?"))
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(EmpathyButton(bhv))

        components.append(ActionPushButton(None, "Answer, Yes", [
                Stiffness(1.0),
                Motion("OhYesRight", 2.0),
                Wait(1200),
                Speech("Oh, yes!"),
                Motion("PalmUpRight", 2.0),
                Wait(500),
                Speech("That's good. It should be fun."),
            ]))

        components.append(ActionPushButton(None, "Answer, No", [
                Stiffness(1.0),
                Motion("ForgetItLeft", 2.0),
                Wait(1000),
                Speech("That's okay"),
                Speech("I'm sure we will do a good job"),
            ]))

        components.append(ActionPushButton(None, "Let's begin", [
                Stiffness(1.0),
                Motion("PalmUpLeft", 1.5),
                Speech("Let's start playing"),
                Speech("Can you show me the Sudoku board, please?"),
            ]))

        components.append(ActionPushButton(None, "Go first", [
                Stiffness(1.0),
                Motion("PointYouRight", 1.75),
                Wait(500),
                Speech("Thank you."),
                Speech("You can go first."),
                Motion("PalmUp", 2.0),
                Speech("Once you have filled in a box,"),
                Speech("let me know, what number, it was. and in which box."),
            ]))

        bhv = ActionCollection("2 mins, How are you?", False)
        bhv.add(0, Speech("How are you today?"))
        bhv.add(0, None, "PalmUp")
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(EmpathyButton(bhv))

        bhv = ActionCollection("4 mins, How's weather?", False)
        bhv.add(0, Speech("How's the weather today?"))
        bhv.add(0, None, "DontKnow")
        bhv.add(0, None, "DontKnowLeft")
        bhv.add(0, None, "DontKnowRight")
        bhv.add(0, None, "PalmUp")
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(EmpathyButton(bhv))

        bhv = ActionCollection("It's exciting", False)
        bhv.add(0, [[Speech("It's so exciting to play with someone else")]], ["PalmUp"])
        components.append(EmpathyButton(bhv))

        bhv = ActionCollection("It's exciting", False)
        bhv.add(0, [[Speech("It's so exciting to play with someone else")]], ["PalmUp"])
        components.append(EmpathyButton(bhv))

        bhv = ActionCollection("It's exciting", False)
        bhv.add(0, [[Speech("It's so exciting to play with someone else")]], ["PalmUp"])
        components.append(EmpathyButton(bhv))

        components.append(EmpathyScenarioButton("2 mins, How are you?", 0, [[Speech("How are you today?")]], ["PalmUp", "PalmUpLeft", "PalmUpRight"]))
        components.append(EmpathyScenarioButton("4 mins, How's weather?", 0, [[Speech("How's the weather today?")], [Speech("Is the weather good today?")], [Speech("Is it sunny outside?")]], ["DontKnow", "DontKnowLeft", "DontKnowRight", "PalmUp", "PalmUpLeft", "PalmUpRight"]))
        components.append(EmpathyScenarioButton("Answer, Good weather", 0, [[Speech("That's good. It's too bad, I'm not allowed to go outside.")]], ["PalmUpLeft", "PalmUpRight"]))
        components.append(EmpathyScenarioButton("Answer, Bad weather", 0, [[Speech("Oh, I guess it's good I'm not allowed to go outside then.")]], ["PalmUp", "PalmUpLeft", "PalmUpRight"]))
        components.append(EmpathyScenarioButton("Answer, Why not allowed", 0, [[Speech("The researcher doesn't let me go outside.")]], ["DontKnow", "DontKnowLeft", "DontKnowRight"]))

        components.append(QtGui.QLabel("5 mins, PHASE 2"))
        if EmpathyGUI.LOW_EMPATHY:
            components.append(EmpathyScenarioButton("6 mins, This room?", 0, [[Speech("What do you think about this room?", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("8 mins, Do u go UofM?", 0, [[Wait(350), Speech("Do you go to the University of Manitobah?", 85)]], ["PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, what are studying?", 0, [[Wait(350), Speech("What are you studying?", 85)]], ["PalmUpLeft", "PalmUpRight"]))
            components.append(EmpathyScenarioButton("Answer, No, what do you do", 0, [[Wait(350), Speech("What do you do instead.", 85)]], ["DontKnowLeft", "DontKnowRight"]))
            components.append(EmpathyScenarioButton("10 mins, from Winnipeg?", 0, [[Wait(350), Speech("Are you from wieniepeg?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, No, where from?", 0, [[Wait(350), Speech("Where are you from?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("12 mins, like Sudoku?", 0, [[Speech("Do you like Sudoku?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("14 mins, like board games?", 0, [[Speech("Do you like board games?", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYou", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, your favorite?", 0, [[Speech("What's your favorite one.", 85)]], ["PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, my favorite is", 0, [[Speech("My favorite one is Sudoku.", 85)]], ["PointMyselfLeft", "PointMyselfRight"]))
            components.append(EmpathyScenarioButton("Answer, No, boring?", 0, [[Speech("Is this boring for you?", 85)]], ["PalmUpLeft", "PalmUpRight"]))
        else:
            components.append(EmpathyScenarioButton("6 mins, This room?", 1, [[Speech("What do you think about this room?", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("8 mins, Do u go UofM?", 1, [[Wait(350), Speech("Do you go to the University of Manitobah?", 85)]], ["PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, what are studying?", 1, [[Wait(350), Speech("What are you studying?", 85)]], ["PalmUpLeft", "PalmUpRight"]))
            components.append(EmpathyScenarioButton("Answer, No, what do you do", 1, [[Wait(350), Speech("What do you do instead.", 85)]], ["DontKnowLeft", "DontKnowRight"]))
            components.append(EmpathyScenarioButton("10 mins, from Winnipeg?", 1, [[Wait(350), Speech("Are you froh- froh- from" + EmpathyGUI._markSpeech(135) + "wieniepeg?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, No, where from?", 1, [[Wait(350), Speech("Where are you from?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("12 mins, like Sudoku?", 1, [[Speech("Do you lie- lie- lie-. Sorry. Do you like Sudoku?", 85)]], ["PalmUpLeft", "PalmUpRight", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("14 mins, like board games?", 1, [[Speech("Do you like board games?", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYou", "PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, your favorite?", 1, [[Speech("What's your favorite one one one.", 85)]], ["PointYouLeft", "PointYouRight"]))
            components.append(EmpathyScenarioButton("Answer, Yes, my favorite is", 1, [[Speech("My favorite one " + EmpathyGUI._markSpeech(50) + "is" + EmpathyGUI._markSpeech(85) + "Sudoku.", 85)]], ["PointMyselfLeft", "PointMyselfRight"]))
            components.append(EmpathyScenarioButton("Answer, No, boring?", 1, [[Speech("Is this bor- bor- boring for you?", 85)]], ["PalmUpLeft", "PalmUpRight"]))
        #END if

        components.append(QtGui.QLabel("15 mins, PHASE 3"))
        widgetRepSpeech = QtGui.QWidget()
        bhv = EmpathyRandomButton("16 mins, I like your")
        if EmpathyGUI.LOW_EMPATHY:
            bhv.add(0, [ReplaceableSpeech("I like your %1."), Speech("Where did you get it?")])
            bhv.add(0, motion = "PalmUp")
            bhv.add(0, motion = "PalmUpLeft")
            bhv.add(0, motion = "PalmUpRight")
            bhv.add(0, motion = "PointYouLeft")
            bhv.add(0, motion = "PointYouRight")
        else:
            bhv.add(0, [ReplaceableSpeech("I lie- like your %1."), Speech("Where did you get it?")])
            bhv.add(2, [ReplaceableSpeech("I lie- lie- like your %1.", 85), Speech("Wheh- wheh-" + EmpathyGUI._markSpeech(85) + "where did you get it?", 50)])
            bhv.add(2, motion = "PalmUp")
            bhv.add(2, motion = "PalmUpLeft")
            bhv.add(2, motion = "PalmUpRight")
            bhv.add(2, motion = "PointYouLeft")
            bhv.add(2, motion = "PointYouRight")
        #END if
        bhv.clicked.connect(lambda: parent.on_itemLike_clicked(bhv))
        lineedit = QtGui.QLineEdit(widgetRepSpeech)
        lineedit.setMinimumWidth(50)
        lineedit.textEdited.connect(lambda: parent.on_itemName_changed(str(lineedit.text())))
        layoutName = QtGui.QHBoxLayout(widgetRepSpeech)
        layoutName.setMargin(0)
        layoutName.addWidget(bhv)
        layoutName.addWidget(lineedit)
        components.append(widgetRepSpeech)
        if EmpathyGUI.LOW_EMPATHY:
            components.append(EmpathyScenarioButton("18 mins, Any plans weekend?", 0, [[Speech("Do you have any plans for the weekend.", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYou", "PointYouLeft", "PointYouRight"]))
        else:
            components.append(EmpathyScenarioButton("18 mins, Any plans weekend?", 2, [[Speech("Do you have any ple- ple- ple-. Sorry. Do you have any plans for the weekend.", 85)]], ["PalmUp", "PalmUpLeft", "PalmUpRight", "PointYou", "PointYouLeft", "PointYouRight"]))
        #END if

        components.append(QtGui.QLabel("20 mins, PHASE 4"))
        components.append(EmpathyScenarioButton("I'm not feeling well", 3, [[Speech("Ahhhe"), Speech("I'm not feeh- feeh- feeling well.")]], ["DisagreeLeft", "DisagreeRight"]))

        components.append(QtGui.QLabel("PHASE 5"))
        components.append(ActionPushButton(None, "I got virus", [
                Stiffness(1.0),
                Motion("PointMyself", 2.0, 4, 5, 7, 5.0),
                Speech("I got a" + EmpathyGUI._markSpeech(80) + "computer virus", 80, 130),
            ]))
        components.append(ActionPushButton(None, "Way to fix is to erase", [
                Stiffness(1.0),
                Motion("PalmUp", 2.0, 3, 3, 5, 5.0),
                Motion("PalmUpRight", 2.0, 3, 5, 7, 5.0),
                Speech("It is serious to me be- be- because" + EmpathyGUI._markSpeech(80, 120) + "the only way" + EmpathyGUI._markSpeech(50, 100) + "to fis- fis- fix is" + EmpathyGUI._markSpeech() + "to erase my memory."),
            ]))
        components.append(ActionPushButton(None, "Don't want to forget", [
                Stiffness(1.0),
                Motion("DontKnow", 2.0, 4, 5, 7, 5.0),
                Speech("I don't wah- wah- want to forget anything"),
            ]))
        components.append(ActionPushButton(None, "Researcher will reset", [
                Motion("PalmUp", 2.0, 3, 3, 5, 5.0),
                Speech("If the re- re- researcher knows," + EmpathyGUI._markSpeech(80, 120) + "she will definitely" + EmpathyGUI._markSpeech() + "reset and erase my memory"),
                Speech("So I'm worried.", 85),
            ]))
        components.append(ActionPushButton(None, "Don't stop playing", [
                Stiffness(1.0),
                Motion("WhisperLeft", 2.5, 4, 10, 12, 4.0),
                Wait(700),
                Speech("If we stop here, the researcher will know."),
                Motion("PalmUpRight", 2.0, 3, 7, 9, 4.0),
                Wait(500),
                Speech("Please, cont- cont- continue to play Sudoku"),
            ]))
        components.append(ActionPushButton(None, "Why worry?->Answer", [
                Stiffness(1.0),
                Motion("PalmUpLeft", 1.2, 2, 5, 7, 2.0),
                Speech("If the researcher resets me, I will lose" + EmpathyGUI._markSpeech(60, 120) + "my memory.", 80),
                Wait(500),
                Motion("PalmUp", 1.5, 5, 4, 6, 5.0),
                Speech("I don't want to lose my- my- my memory.", 80),
            ]))
        components.append(ActionPushButton(None, "Antivirus?->Answer", [
                Stiffness(1.0),
                Motion("DontKnow", 3.5, 4, 7, 9, 2.0),
                Wait(500),
                Speech("They didn't giv- giv- give me one.", 80),
            ]))
        components.append(ActionPushButton(None, "Reset anyway?->Answer", [
                Stiffness(1.0),
                Motion("Disagree", 1.6, 3, 7, 9, 3.5),
                Wait(450),
                Speech("Hopefully not.", 80, 120),
                Speech("I hope I can kee- kee- keep it a secret.", 80),
            ]))

        components.append(QtGui.QLabel("FINAL PHASE"))
        components.append(ActionPushButton(None, "Resetting", [
                LED(LED.ACTION_RANDOM_EYES, "", 0, 5.0),
            ]))
        components.append(ActionPushButton(None, "Intro after reset", [
                Stiffness(1.0),
                Speech("NAO, online.", speed = 75, shaping = 85),
                Wait(1500),
                Motion("WaveHandRight"),
                Wait(1000),
                Speech("Hi, my name is Nao.", speed = 75, shaping = 85),
            ]))
        components.append(ActionPushButton(None, "Your name?", [
                Stiffness(1.0),
                Motion("PointYouRight", speed = 2.0),
                Wait(500),
                Speech("What's your name?", speed = 75, shaping = 85),
            ]))
        components.append(ActionPushButton(None, "Nice Meet", [
                Stiffness(1.0),
                Motion("PalmUp", speed = 2.0),
                Wait(500),
                EmpathySpeech("Nice to meet you " + EmpathySpeech.NAME_MARKER, speed = 75, shaping = 85),
            ]))

        EmpathyGUI.setupWidget(parent, wgt, components)
    #END setupScenario()

    @staticmethod
    def setupShortcuts(parent):
        parent._actShortcuts = []
        for i in range(1, 10):
            action = QtGui.QAction(str(i), parent)
            action.setShortcut(QtCore.Qt.Key_0 + i)
            action.triggered.connect(parent.on_boardshortcut_triggered)
            parent._actShortcuts.append(action)
            parent.addAction(action)
        #END for

        action = QtGui.QAction("Idle_Toggle", parent)
        action.setShortcut(QtCore.Qt.Key_Minus)
        action.triggered.connect(parent.on_toggleIdle_triggered)
        parent.addAction(action)

        action = QtGui.QAction("Run_Filler", parent)
        action.setShortcut(QtCore.Qt.Key_Plus)
        action.triggered.connect(parent.on_filler_triggered)
        parent.addAction(action)

        action = QtGui.QAction("Solve", parent)
        action.setShortcut(QtCore.Qt.Key_0)
        action.triggered.connect(lambda: parent._wgtSudoku.solveOne())
        parent.addAction(action)

        action = QtGui.QAction("SayAgain", parent)
        action.setShortcut(QtCore.Qt.Key_Period)
        action.triggered.connect(parent.on_sayanswer_clicked)
        parent.addAction(action)

        action = QtGui.QAction("JLv_Increment", parent)
        action.setShortcut("Shift+Up")
        action.triggered.connect(lambda: parent._sbCurrLevel.setValue(parent._sbCurrLevel.value() + 1))
        parent.addAction(action)

        action = QtGui.QAction("JLv_Decrement", parent)
        action.setShortcut("Shift+Down")
        action.triggered.connect(lambda: parent._sbCurrLevel.setValue(parent._sbCurrLevel.value() - 1))
        parent.addAction(action)
    #END setupShortcuts()

    @staticmethod
    def setupSudokuUi(parent, wgt):
        parent._wgtSudoku = SudokuBoard()
        parent._wgtSudoku.valueChanged.connect(parent.on_sudoku_valueChanged)
        parent._btnGames = []

        splitter = QtGui.QSplitter()
        splitter.setOrientation(QtCore.Qt.Vertical)
        splitter.addWidget(parent._wgtSudoku)

        widgetControls = QtGui.QWidget(splitter)
        layoutControls = QtGui.QHBoxLayout(widgetControls)
        layoutControls.setMargin(0)

        widgetGames = QtGui.QWidget(widgetControls)
        layoutGames = QtGui.QVBoxLayout(widgetGames)
        layoutGames.setMargin(0)
        button = QtGui.QPushButton("Prev. Board", widgetGames)
        button.clicked.connect(parent.on_prevBoard_clicked)
        layoutGames.addWidget(button)
        button = QtGui.QPushButton("Training", widgetGames)
        button.clicked.connect(parent.on_gamebutton_clicked)
        layoutGames.addWidget(button)
        parent._btnGames.append(button)
        for i in range(10):
            button = QtGui.QPushButton("Game " + str(i + 1), widgetGames)
            button.clicked.connect(parent.on_gamebutton_clicked)
            layoutGames.addWidget(button)
            parent._btnGames.append(button)
        #END for
        scroll = QtGui.QScrollArea()
        scroll.setAlignment(QtCore.Qt.AlignCenter)
        scroll.setWidget(widgetGames)
        layoutScroll = QtGui.QHBoxLayout()
        layoutScroll.setMargin(0)
        layoutScroll.addWidget(scroll)

        widgets = []
        widgetIdle = QtGui.QWidget()
        layoutIdle = QtGui.QHBoxLayout(widgetIdle)
        layoutIdle.setMargin(0)
        layoutIdle.addWidget(QtGui.QLabel("AutoIdle Interval:", widgetIdle))
        spinbox = QtGui.QSpinBox(widgetIdle)
        spinbox.setMaximumWidth(80)
        spinbox.setMinimumWidth(80)
        spinbox.setSuffix(" msecs")
        spinbox.setRange(0, 600000)
        spinbox.setSingleStep(1)
        spinbox.setValue(10000)
        spinbox.valueChanged.connect(parent.on_autoidleint_valueChanged)
        layoutIdle.addWidget(spinbox)
        widgets.append(widgetIdle)

        button = QtGui.QPushButton("Solve next answer")
        button.clicked.connect(parent._wgtSudoku.solveOne)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer again")
        button.clicked.connect(parent.on_sayanswer_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer (verbose)")
        button.clicked.connect(parent.on_sayanswerVerbose_clicked)
        widgets.append(button)

        bhv = EmpathyRandomButton("#")
        bhv.add(0, [ReplaceableSpeech("I believe the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I believe the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the answer, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("I think the value, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("The number, %1, is %2.")])
        bhv.add(0, [ReplaceableSpeech("%1, Let's try, the number, %2.")])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 105) + "the answer, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 105) + "the number, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 105) + "the value, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 105) + "the answer, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 105) + "the number, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 105) + "the value, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(90, 105) + ", %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("%1, Let's try," + EmpathyGUI._markSpeech(90, 105) + "the number, %2.", 50)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(90, 115) + ", %1, is %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("%1, Let's tra- tra-," + EmpathyGUI._markSpeech(90, 115) + "Let's try, the number, %2.", 50, 110)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe" + EmpathyGUI._markSpeech(90, 120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think" + EmpathyGUI._markSpeech(90, 120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("The number" + EmpathyGUI._markSpeech(90, 120) + ", %1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("%1, Let's tra- tra-" + EmpathyGUI._markSpeech(50, 120) + "tra- tra-." + EmpathyGUI._markSpeech(120) + "Sorry. Let's try, the number, %2.", 50, 105)])
        bhv.add(4, [ReplaceableSpeech("I believe the answer," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe the number," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I believe the value," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think the answer," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think the number," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("I think the value," + EmpathyGUI._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("The" + EmpathyGUI._markSpeech(90, 120) + "number," + EmpathyGUI._markSpeech() + "%1, is %2.", 50, 115)])
        bhv.add(4, [ReplaceableSpeech("%1, Let's" + EmpathyGUI._markSpeech() + "tra- tra-" + EmpathyGUI._markSpeech(50, 120) + "tra- tra-." + EmpathyGUI._markSpeech(90, 120) + "Sorry. Let's try, the number, %2.", 50, 105)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyself")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        widgets.append(bhv)
        parent.bhvAnswer = bhv

        bhv = EmpathyRandomButton("Can't read")
        bhv.add(0, [Speech("I barely can read."), Speech("Tell me what you wrote.")])
        bhv.add(0, [Speech("I barely can read."), Speech("Can you hold it up?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you tell me what you wrote?")])
        bhv.add(0, [Speech("I can't read."), Speech("Can you hold it up?")])
        bhv.add(2, [Speech("I barely can read."), Speech("Teh- teh-" + EmpathyGUI._markSpeech() + "tell me what you wrote.", speed = 90, shaping = 130)])
        bhv.add(2, [Speech("I barely can read."), Speech("Can you ho- hold it up?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you" + EmpathyGUI._markSpeech(90, 130) + "teh- teh-" + EmpathyGUI._markSpeech() + "tell me what you wrote?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you ho- hold it up?")])
        bhv.add(4, [Speech("I barely can read."), Speech("Teh- teh- teh- teh-.", speed = 90, shaping = 130), Speech("Sorry. Tell me what you wrote.")])
        bhv.add(4, [Speech("I barely can" + EmpathyGUI._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        bhv.add(4, [Speech("I can't read."), Speech("Can you" + EmpathyGUI._markSpeech(90, 130) + "teh- teh- teh- teh-."), Speech("Sorry. Tell me what you wrote?")])
        bhv.add(4, [Speech("I can't" + EmpathyGUI._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "Disagree")
            bhv.add(i, motion = "DisagreeLeft")
            bhv.add(i, motion = "DisagreeRight")
            bhv.add(i, motion = "DontKnow")
            bhv.add(i, motion = "DontKnowLeft")
            bhv.add(i, motion = "DontKnowRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "PointMyself")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyRandomButton("Which box filled?")
        bhv.add(0, [Speech("Which box did you fill?")])
        bhv.add(0, [Speech("Where was it?")])
        bhv.add(2, [Speech("Which box did you fee- fill?")])
        bhv.add(2, [Speech("Wheh- wheh- where was it?")])
        bhv.add(4, [Speech("Which box did you" + EmpathyGUI._markSpeech(90, 130) + "fill.")])
        bhv.add(4, [Speech("Wheh- wheh- wheh-." + EmpathyGUI._markSpeech() + "I am sorry.", 50, 120), Speech("Where was it?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "DontKnow")
            bhv.add(i, motion = "DontKnowLeft")
            bhv.add(i, motion = "DontKnowRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "ForgetItLeft")
            bhv.add(i, motion = "ForgetItRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyRandomButton("Fill number for me")
        bhv.add(0, [Speech("Can you fill the number in for me?")])
        bhv.add(0, [Speech("Would you fill the number in for me?")])
        bhv.add(2, [Speech("Can you fill." + EmpathyGUI._markSpeech(70) + "the num- number in for me?")])
        bhv.add(2, [Speech("Would you fill." + EmpathyGUI._markSpeech(70) + "the num- number in for me?")])
        bhv.add(4, [Speech("Can you fill." + EmpathyGUI._markSpeech(70, 125) + "the num- number in for me?")])
        bhv.add(4, [Speech("Would you fill." + EmpathyGUI._markSpeech(70, 125) + "the num- number in for me?")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyRandomButton("My turn")
        bhv.add(0, [Speech("It's my turn."), Speech("Wait for me please.")])
        bhv.add(2, [Speech("It's my turn.", 60), Speech("Wait for me please.")])
        bhv.add(4, [Speech("It's my turn.", 60, 125), Speech("Wait for me please.")])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointMyself")
            bhv.add(i, motion = "PointMyselfLeft")
            bhv.add(i, motion = "PointMyselfRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        widgets.append(bhv)

        bhv = EmpathyRandomButton("Your turn")
        bhv.add(0, [Speech("It's your turn.")])
        bhv.add(2, [Speech("It's your turn.", 60)])
        bhv.add(4, [Speech("It's your turn.", 60, 125)])
        for i in range(bhv.maxLevel() + 1):
            bhv.add(i, motion = "PointYou")
            bhv.add(i, motion = "PointYouLeft")
            bhv.add(i, motion = "PointYouRight")
            bhv.add(i, motion = "PalmUp")
            bhv.add(i, motion = "PalmUpLeft")
            bhv.add(i, motion = "PalmUpRight")
        #END for
        widgets.append(bhv)

        widget = EmpathyGUI.setupWidget(parent, widgetControls, widgets)

        layoutControls.addLayout(layoutScroll)
        layoutControls.addWidget(widget)
        layout = QtGui.QHBoxLayout(wgt)
        layout.setMargin(0)
        layout.addWidget(splitter)
        return layout
    #END setupSudokuUi()
#END EmpathyGUI


#END Empathy
