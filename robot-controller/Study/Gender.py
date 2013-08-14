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
            rgb = 0x00228B22
        elif current_phase <= 5:
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

    def speech(self, txt, speed, shaping):
        for bhv in self._actions:
            if bhv.containText(txt):
                return bhv.get(self._jitterLevel)
            #END if
        #END for
        actions = self._bhvMovement.get(self._jitterLevel)
        if self._jitterLevel <= 1:
            actions.append(Speech(txt, speed, shaping, blocking = False))
        else:
            if random.randint(0, 100) <= 70:
                txt = txt.replace("want", "wah- wah- want")
            #END if
            if random.randint(0, 100) <= 50:
                txt = txt.replace("where", "wheh- wheh- where")
            #END if
            if random.randint(0, 100) <= 30:
                txt = txt.replace("you", self._markSpeech(50, 120) + "you- you- you." + self._markSpeech(85))
            #END if
            actions.append(Speech(txt, speed, shaping, blocking = False))
        #END if
        return actions
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
            actions = self._bhvIdleSmall.get(self._jitterLevel)
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
        actions = self._bhvFiller.get(self._jitterLevel)
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

    def on_itemLike_clicked(self, pushButton):
        actions = pushButton.getRobotActions(self._jitterLevel)
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
        if value <= 0:
            self._jitterLevel = 0
        elif value <= 5:
            self._jitterLevel = value - 1
        else:
            self._jitterLevel = 0
        #END if
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

    def on_sayanswerWrong(self):
        i = random.randint(9, 29)
        j = str(chr(ord('a') + random.randint(9, 19)))
        value = random.randint(10, 30)
        actions = self._bhvAnswer.get(self._jitterLevel)
        for action in actions:
            if isinstance(action, ReplaceableSpeech):
                action.replace(self._toCoordinate(j, i), str(value))
            #END if
        #END for
        self._actionQueue.addActions(actions)
        self._lastSudoku = [i, j, value]
    #END on_sayanswerWrong()

    def on_solveOne_clicked(self):
        self._wgtSudoku.solveOne()
    #END on_solveOne_clicked()

    def on_sudoku_valueChanged(self, i, j, value):
        self._deselectSubgrid()
        self._lastSudoku = [i, j, value]
        if value != 0:
            actions = self._bhvAnswer.get(self._jitterLevel)
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
        Gender._setupMotions(self, splitter)
        Gender._setupInteractions(self, splitter)
        Gender._setupSudokuUi(self, splitter)
        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        Gender._setupShortcuts(self)
    #END _setupUi()

    def _setupInteractions(self, wgt):
        components = []

        bhv = ActionCollection("Conv. Movement")
        for i in range(10):
            bhv.add(i, None, "Idle0")
            bhv.add(i, None, "Idle1")
            bhv.add(i, None, "Idle2")
            bhv.add(i, None, "Idle3")
            bhv.add(i, None, "Idle4")
            bhv.add(i, None, "Idle5")
            bhv.add(i, None, "Idle6")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))
        self._bhvMovement = bhv

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
        bhv.add(3, [Speech("ummmh,", speed = 50)])
        bhv.add(3, [Speech("well,", speed = 50)])
        bhv.add(3, [Speech("well,", speed = 50)])
        bhv.add(3, [Speech("let me think", speed = 80)])
        bhv.add(3, [Speech("let's see", speed = 80)])
        bhv.add(3, [Speech("ummmh,", speed = 70, shaping = 130)])
        bhv.add(3, [Speech("well,", speed = 70, shaping = 130)])
        bhv.add(3, [Speech("well,", speed = 70, shaping = 130)])
        bhv.add(3, [Speech("let me" + self._markSpeech(90, 130) + "think", speed = 90, shaping = 110)])
        bhv.add(3, [Speech("let me" + self._markSpeech(90, 110) + "think", speed = 90, shaping = 130)])
        bhv.add(3, [Speech("let's" + self._markSpeech(90, 130) + "see", speed = 90, shaping = 110)])
        bhv.add(3, [Speech("let's" + self._markSpeech(90, 110) + "see", speed = 90, shaping = 130)])
        components.append(GenderButton(bhv))
        self._bhvFiller = bhv

        bhv = ActionCollection("Idle (Big)")
        for i in range(10):
            bhv.add(i, None, "ChinHoldLeft")
            bhv.add(i, None, "ChinHoldRight")
            bhv.add(i, None, "Idle3")
            bhv.add(i, None, "Idle5")
            bhv.add(i, None, "Idle6")
        #END for
        components.append(GenderButton(bhv))
        self._bhvIdleBig = bhv

        bhv = ActionCollection("Idle (Small)")
        for i in range(10):
            bhv.add(i, None, "Idle0")
            bhv.add(i, None, "Idle1")
            bhv.add(i, None, "Idle2")
        #END for
        components.append(GenderButton(bhv))
        self._bhvIdleSmall = bhv

        bhv = ActionCollection("You are welcome")
        bhv.addText("welcome")
        bhv.add(0, [Speech("You are welcome.", 80)])
        bhv.add(2, [Speech("You are welcome.", 50)])
        bhv.add(2, [Speech("You are" + self._markSpeech() + "welcome.", 50, 120)])
        bhv.add(3, [Speech("You you you are welcome.", 50)])
        bhv.add(3, [Speech("You you you are" + self._markSpeech() + "welcome.", 50, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Thank you")
        bhv.addText("thank you")
        bhv.addText("thanks")
        bhv.add(0, [Speech("Thank you.", 80)])
        bhv.add(2, [Speech("Thank you.", 50)])
        bhv.add(2, [Speech("Thank" + self._markSpeech() + "you.", 50, 120)])
        bhv.add(3, [Speech("Tha- tha- thank you.", 50)])
        bhv.add(3, [Speech("Tha- Tha- thank" + self._markSpeech() + "you.", 50, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

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
        bhv.add(3, [Speech("Good.", 50)])
        bhv.add(3, [Speech("Cool.", 50)])
        bhv.add(3, [Speech("Nice.", 50)])
        bhv.add(3, [Speech("Good.", 50, 120)])
        bhv.add(3, [Speech("Cool.", 50, 120)])
        bhv.add(3, [Speech("Nice.", 50, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Okay")
        bhv.add(0, [Speech("Okay.")])
        bhv.add(0, [Speech("I got it.")])
        bhv.add(0, [Speech("Understood.")])
        bhv.add(2, [Speech("Okay.", 50)])
        bhv.add(2, [Speech("I got it.", 60)])
        bhv.add(2, [Speech("Understood.", 50)])
        bhv.add(3, [Speech("Okay.", 50)])
        bhv.add(3, [Speech("I got it.", 60)])
        bhv.add(3, [Speech("Understood.", 50)])
        bhv.add(3, [Speech("Okay.", 50, 120)])
        bhv.add(3, [Speech("I" + self._markSpeech(60, 120) + "got it.", 60)])
        bhv.add(3, [Speech("Under" + self._markSpeech(50, 120) + "stood.", 50)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Idle5")
            bhv.add(i, None, "Idle6")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("I agree")
        bhv.addText("agree")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("I agree.")])
        bhv.add(0, [Speech("You are right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("I agree.", 50)])
        bhv.add(2, [Speech("You are right.", 50)])
        bhv.add(3, [Speech("Yes", 50)])
        bhv.add(3, [Speech("I agree.", 50)])
        bhv.add(3, [Speech("You are right.", 50)])
        bhv.add(3, [Speech("Yes", 50, 120)])
        bhv.add(3, [Speech("I" + self._markSpeech(50, 120) + "agree.", 50)])
        bhv.add(3, [Speech("You are" + self._markSpeech(50, 120) + "right.", 50)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("I disagree")
        bhv.addText("disagree")
        bhv.add(0, [Speech("I don't think so")])
        bhv.add(2, [Speech("I don't think so", 50)])
        bhv.add(3, [Speech("I don't think so", 50)])
        bhv.add(3, [Speech("I don't" + self._markSpeech(50, 120) + "think so", 50)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Disagree")
            bhv.add(i, None, "DisagreeLeft")
            bhv.add(i, None, "DisagreeRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Yes")
        bhv.addText("yes")
        bhv.add(0, [Speech("Yes")])
        bhv.add(0, [Speech("Right.")])
        bhv.add(2, [Speech("Yes", 50)])
        bhv.add(2, [Speech("Right.", 50)])
        bhv.add(3, [Speech("Yes", 50)])
        bhv.add(3, [Speech("Right.", 50)])
        bhv.add(3, [Speech("Yes", 50, 120)])
        bhv.add(3, [Speech("Right.", 50, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Idle5")
            bhv.add(i, None, "Idle6")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("No")
        bhv.addText("no")
        bhv.add(0, [Speech("No")])
        bhv.add(2, [Speech("No", 50)])
        bhv.add(3, [Speech("No", 50)])
        bhv.add(3, [Speech("No", 50, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Disagree")
            bhv.add(i, None, "DisagreeLeft")
            bhv.add(i, None, "DisagreeRight")
            bhv.add(i, None, "PalmUp")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("You are doing good")
        bhv.add(0, [Speech("You are doing very well.")])
        bhv.add(0, [Speech("You are very good at Sudoku.")])
        bhv.add(2, [Speech("You are" + self._markSpeech() + "doing very well.", 70, 120)])
        bhv.add(2, [Speech("You are" + self._markSpeech() + "very good at Sudoku.", 70, 120)])
        bhv.add(3, [Speech("You are" + self._markSpeech() + "do- do- do-" + self._markSpeech(50, 120) + "doing very well.", 70, 120)])
        bhv.add(3, [Speech("You are" + self._markSpeech() + "goo- goo- goo-" + self._markSpeech(50, 120) + "very good at Sudoku.", 70, 120)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("What you think?")
        bhv.add(0, [Speech("What do you think?")])
        bhv.add(2, [Speech("What do you" + self._markSpeech(95) + "thiin- thiin- thii-."), Speech("Ahhhe, what do you think?")])
        bhv.add(2, [Speech("What do you do you do you think?")])
        bhv.add(3, [Speech("What do you" + self._markSpeech(95) + "thiin- thiin- thii-."), Speech("Ahhhe, what do you think?")])
        bhv.add(3, [Speech("What do you do you do you think?")])
        bhv.add(3, [Speech("What do you" + self._markSpeech(70, 120) + "thiin- thiin- thii-."), Speech("Sorry.", speed = 50), Speech("What do you think?", 75, 110)])
        bhv.add(3, [Speech("What" + self._markSpeech(70, 120) + "do you thii-" + self._markSpeech(50) + "think?")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Easy!")
        bhv.add(0, [Wait(300), Speech("This one is easy")])
        bhv.add(2, [Wait(300), Speech("This one is e- e- easy")])
        bhv.add(3, [Wait(300), Speech("This one is" + self._markSpeech(90, 110) + "e- e-" + self._markSpeech(50, 130) + "e- e-."), Speech("Sorry. This one is easy")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Difficult!")
        bhv.add(0, [Wait(300), Speech("I don't know")])
        bhv.add(0, [Wait(300), Speech("This one is difficult")])
        bhv.add(2, [Wait(300), Speech("I don't noh- know")])
        bhv.add(2, [Wait(300), Speech("This one- one- one-."), Speech("This one is difficult")])
        bhv.add(3, [Wait(300), Speech("I don't no- no- noh-."), Speech("No.", 50, 130), Speech("I don't know")])
        bhv.add(3, [Wait(300), Speech("This one is diff- diff- diff-."), Speech("Ahhhe.", 50, 130), Speech("Sorry. This one is difficult", 70)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "DontKnow")
            bhv.add(i, None, "DontKnowLeft")
            bhv.add(i, None, "DontKnowRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "ChinHoldLeft")
            bhv.add(i, None, "ChinHoldRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("This board?")
        bhv.add(0, [Speech("Do you find this board easy?")])
        bhv.add(0, [Speech("Do you find this board difficult?")])
        bhv.add(0, [Speech("What do you think about this board, is it easy or difficult.")])
        bhv.add(2, [Speech("Is this" + self._markSpeech(80, 115) + "board easy?")])
        bhv.add(2, [Speech("Is this" + self._markSpeech(80, 115) + "board difficult?")])
        bhv.add(2, [Speech("What" + self._markSpeech(80, 115) + "do you think about" + self._markSpeech(90, 100) + "this board?")])
        bhv.add(3, [Speech("Is this" + self._markSpeech(80, 130) + "board easy?", 50)])
        bhv.add(3, [Speech("Is this" + self._markSpeech(80, 130) + "board difficult?", 50)])
        bhv.add(3, [Speech("What" + self._markSpeech(80, 130) + "do you thiih thiih think about" + self._markSpeech(90, 100) + "this board?", 50)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "DontKnowLeft")
            bhv.add(i, None, "DontKnowRight")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Almost done")
        bhv.add(0, [Speech("We are almost done with this board.")])
        bhv.add(0, [Speech("Few more numbers to finish this board.")])
        bhv.add(2, [Speech("We are almost" + self._markSpeech(80, 110) + "done with this board.")])
        bhv.add(2, [Speech("Few more numbers to" + self._markSpeech(80, 110) + "finish this board.")])
        bhv.add(3, [Speech("We are almost" + self._markSpeech(80, 120) + "done with the- the- the-" + self._markSpeech() + "this board.", 130)])
        bhv.add(3, [Speech("Few more numbers to" + self._markSpeech(80, 110) + "fii- fii-." + self._markSpeech() + "Sorry.finish this board.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Don't like board")
        bhv.add(0, [Speech("I don't like this board."), Speech("Let's start a new board.")])
        bhv.add(0, [Speech("I don't like this board."), Speech("Can we start a new board?")])
        bhv.add(0, [Speech("This board is not interesting."), Speech("Let's start a new board.")])
        bhv.add(2, [Speech("I don't lie- lie- like this board."), Speech("Let's start a new boh- boh- board.")])
        bhv.add(2, [Speech("I don't like this board."), Speech("Can we start a new boh- boh- board?")])
        bhv.add(2, [Speech("This board is not in- in- interesting."), Speech("Le- le- let's start a new board.")])
        bhv.add(3, [Speech("I don't lie- lie-" + self._markSpeech() + "like this board.", 80, 120), Speech("Let's start a new" + self._markSpeech(80, 110) + "boh- boh- board.")])
        bhv.add(3, [Speech("I don't like" + self._markSpeech(80, 120) + "this board."), Speech("Can we start a new boh- boh- board?")])
        bhv.add(3, [Speech("This board is not in- in- interesting."), Speech("Le- le- let's start" + self._markSpeech(80, 120) + "a new board.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Show me next board")
        bhv.add(0, [Speech("Can you show me next Sudoku board?")])
        bhv.add(0, [Speech("Let's move on to next board.")])
        bhv.add(2, [Speech("Can you" + self._markSpeech(50) + "sho- sho-." + self._markSpeech() + "show me next Sudoku board?")])
        bhv.add(2, [Speech("Let's" + self._markSpeech(50) + "moo- moo-." + self._markSpeech() + "move on to next board.")])
        bhv.add(3, [Speech("Can you" + self._markSpeech(50) + "sho- sho- sho-." + self._markSpeech(50, 130) + "I'm Sorry." + self._markSpeech() + "Can you show me next Sudoku board?")])
        bhv.add(3, [Speech("Let's" + self._markSpeech(50) + "moo moo- mooh-." + self._markSpeech(50, 130) + "I'm Sorry." + self._markSpeech() + "Let's move on to next board.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyself")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Continue Sudoku")
        bhv.add(0, [Speech("Let's continue playing Sudoku.")])
        bhv.add(2, [Speech("Let's" + self._markSpeech(50) + "continue" + self._markSpeech() + "playing Sudoku.")])
        bhv.add(3, [Speech(self._markSpeech(75) + "Let's" + self._markSpeech(50, 120) + "cont- cont-" + self._markSpeech() + "continue playing Sudoku.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Play together")
        bhv.add(0, [Speech("Wait. I wanna play too.")])
        bhv.add(0, [Speech("Let's play together")])
        bhv.add(2, [Speech(self._markSpeech(70) + "Let's play" + self._markSpeech(90, 130) + "together.")])
        bhv.add(2, [Speech("Wait. I wanna ple- ple- ple-."), Speech("Wait. I wanna play too.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "DisagreeLeft")
            bhv.add(i, None, "DisagreeRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Need help?")
        bhv.add(0, [Speech("Are you okay?"), Speech("I can help you.")])
        bhv.add(0, [Speech("I can help you out.")])
        bhv.add(0, [Speech("Do you need any help?")])
        bhv.add(2, [Speech("Are you oh- okay?"), Speech("I can help you.")])
        bhv.add(2, [Speech("I can" + self._markSpeech(80, 120) + "help you out.")])
        bhv.add(2, [Speech("Do you need any heh- heh-." + self._markSpeech(80) + "Do you need any help?")])
        bhv.add(3, [Speech("Are you okay?"), Speech("I can he- heh-."), Speech("I can help you.")])
        bhv.add(3, [Speech("I can" + self._markSpeech(80, 120) + "help you out.")])
        bhv.add(3, [Speech("Do you need any heh- heh- heh- heh-."), Speech("Sorry." + self._markSpeech(80) + "Do you need any help?")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyself")
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
            bhv.add(i, None, "ForgetItLeft")
            bhv.add(i, None, "ForgetItRight")
            bhv.add(i, None, "WaveHandLeft")
            bhv.add(i, None, "WaveHandRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Don't touch me")
        bhv.add(0, [Speech("Please, do not touch me.")])
        bhv.add(2, [Speech("Please, do not theh- touch me.")])
        bhv.add(3, [Speech("Please, do not" + self._markSpeech(140, 130) + "touch me.")])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "Disagree")
            bhv.add(i, None, "DisagreeLeft")
            bhv.add(i, None, "DisagreeRight")
        #END for
        components.append(GenderButton(bhv))

        return self._setupWidget(wgt, components)
    #END _setupInteractions()

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
        spinbox.setRange(0, 6)
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
                    GenderSpeech("Hi, nice to meet you, " + GenderSpeech.NAME_MARKER),
                    Behavior("SitDown"),
                    Motion("Default"),
            ]))

        components.append(QtGui.QLabel("0 mins, PHASE 1"))
        bhv = ActionCollection("It's exciting", False)
        bhv.add(0, Speech("It's so exciting to play with someone else"), "PalmUp")
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Play well?", False)
        bhv.add(0, Speech("Do you play Sudoku well?"))
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(GenderButton(bhv))

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
        components.append(GenderButton(bhv))

        bhv = ActionCollection("4 mins, How's weather?", False)
        bhv.add(0, Speech("How's the weather today?"))
        bhv.add(0, None, "DontKnow")
        bhv.add(0, None, "DontKnowLeft")
        bhv.add(0, None, "DontKnowRight")
        bhv.add(0, None, "PalmUp")
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Good weather", False)
        bhv.add(0, Speech("That's good. It's too bad, I'm not allowed to go outside."))
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Bad weather", False)
        bhv.add(0, Speech("Oh, I guess it's good I'm not allowed to go outside then."))
        bhv.add(0, None, "PalmUp")
        bhv.add(0, None, "PalmUpLeft")
        bhv.add(0, None, "PalmUpRight")
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Why not allowed", False)
        bhv.add(0, Speech("The researcher doesn't let me go outside."))
        bhv.add(0, None, "DontKnow")
        bhv.add(0, None, "DontKnowLeft")
        bhv.add(0, None, "DontKnowRight")
        components.append(GenderButton(bhv))

        components.append(QtGui.QLabel("5 mins, PHASE 2"))

        bhv = ActionCollection("6 mins, This room?", False)
        bhv.add(0, Speech("What do you think about this room?", 85))
        bhv.add(1, Speech("What do you think about this room?", 85))
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("8 mins, Do u go UofM?", False)
        bhv.add(0, [Wait(350), Speech("Do you go to the University of Manitobah?", 85)])
        bhv.add(1, [Wait(350), Speech("Do you go to the University of Mah- Mah- Manitobah?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Yes, what are studying?", False)
        bhv.add(0, [Wait(350), Speech("What are you studying?", 85)])
        bhv.add(1, [Wait(350), Speech("What are you studying?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, No, what do you do", False)
        bhv.add(0, [Wait(350), Speech("What do you do instead.", 85)])
        bhv.add(1, [Wait(350), Speech("What do you do ins- ins- instead.", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "DontKnowLeft")
            bhv.add(i, None, "DontKnowRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("10 mins, from Winnipeg?", False)
        bhv.add(0, [Wait(350), Speech("Are you from wieniepeg?", 85)])
        bhv.add(1, [Wait(350), Speech("Are you froh- froh- from" + self._markSpeech(135) + "wieniepeg?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, No, where from?", False)
        bhv.add(0, [Wait(350), Speech("Where are you from?", 85)])
        bhv.add(1, [Wait(350), Speech("Wheh- wheh- where are you from?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("12 mins, like Sudoku?", False)
        bhv.add(0, [Speech("Do you like Sudoku?", 85)])
        bhv.add(1, [Speech("Do you lie- lie- lie-. Sorry. Do you like Sudoku?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("14 mins, like board games?", False)
        bhv.add(0, [Speech("Do you like board games?", 85)])
        bhv.add(1, [Speech("Do you like boh- boh- board games?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Yes, your favorite?", False)
        bhv.add(0, [Speech("What's your favorite one.", 85)])
        bhv.add(1, [Speech("What's your favorite one one one.", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, Yes, my favorite is", False)
        bhv.add(0, [Speech("My favorite one is Sudoku.", 85)])
        bhv.add(1, [Speech("My favorite one " + self._markSpeech(50) + "is" + self._markSpeech(85) + "Sudoku.", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PointMyselfLeft")
            bhv.add(i, None, "PointMyselfRight")
        #END for
        components.append(GenderButton(bhv))

        bhv = ActionCollection("Answer, No, boring?", False)
        bhv.add(0, [Speech("Is this boring for you?", 85)])
        bhv.add(1, [Speech("Is this bor- bor- boring for you?", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
        #END for
        components.append(GenderButton(bhv))

        components.append(QtGui.QLabel("15 mins, PHASE 3"))

        widgetRepSpeech = QtGui.QWidget()
        bhv = ActionCollection("16 mins, I like your", False)
        bhv.add(0, [ReplaceableSpeech("I like your %1."), Speech("Where did you get it?")])
        bhv.add(2, [ReplaceableSpeech("I" + self._markSpeech(50, 130) + "lie- lie-" + self._markSpeech(85) + "like your %1.", 85), Speech("Wheh- wheh-" + self._markSpeech(85) + "where did you get it?", 50)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        pushbutton = GenderButton(bhv)
        pushbutton.clicked.connect(lambda: self.on_itemLike_clicked(pushbutton))
        lineedit = QtGui.QLineEdit(widgetRepSpeech)
        lineedit.setMinimumWidth(50)
        lineedit.textEdited.connect(lambda: self.on_itemName_changed(str(lineedit.text())))
        layoutItem = QtGui.QHBoxLayout(widgetRepSpeech)
        layoutItem.setMargin(0)
        layoutItem.addWidget(pushbutton)
        layoutItem.addWidget(lineedit)
        components.append(widgetRepSpeech)

        bhv = ActionCollection("18 mins, Any plans weekend?", False)
        bhv.add(0, [Speech("Do you have any plans for the weekend.", 85)])
        bhv.add(2, [Speech("Do you have any ple- ple- ple-. Sorry. Do you have any plans for the weekend.", 85)])
        for i in range(bhv.getMaxLevel() + 1):
            bhv.add(i, None, "PalmUp")
            bhv.add(i, None, "PalmUpLeft")
            bhv.add(i, None, "PalmUpRight")
            bhv.add(i, None, "PointYou")
            bhv.add(i, None, "PointYouLeft")
            bhv.add(i, None, "PointYouRight")
        #END for
        components.append(GenderButton(bhv))

        components.append(QtGui.QLabel("20 mins, PHASE 4"))

        bhv = ActionCollection("I'm not feeling well", False)
        bhv.add(3, [Speech("Ahhhe"), Speech("I'm not feeh- feeh- feeling well.")])
        bhv.add(3, None, "DisagreeLeft")
        bhv.add(3, None, "DisagreeRight")
        components.append(GenderButton(bhv))

        components.append(QtGui.QLabel("PHASE 5"))

        components.append(ActionPushButton(None, "I got virus", [
                Stiffness(1.0),
                Motion("PointMyself", 2.0, 4, 5, 7, 5.0),
                Speech("I think I got a" + self._markSpeech(80) + "computer virus", 80, 130),
            ]))

        components.append(ActionPushButton(None, "Way to fix is to erase", [
                Stiffness(1.0),
                Motion("PalmUp", 2.0, 3, 3, 5, 5.0),
                Motion("PalmUpRight", 2.0, 3, 5, 7, 5.0),
                Speech("The only way" + self._markSpeech(50, 100) + "to fis- fis- fix is" + self._markSpeech() + "to erase my memory.", 80, 120),
            ]))

        components.append(ActionPushButton(None, "Don't want to forget", [
                Stiffness(1.0),
                Motion("DontKnow", 2.0, 4, 5, 7, 5.0),
                Speech("I don't wah- wah- want to forget anything"),
            ]))

        components.append(ActionPushButton(None, "Researcher will reset", [
                Motion("PalmUp", 2.0, 3, 3, 5, 5.0),
                Speech("If the re- re- researcher knows," + self._markSpeech(80, 120) + "she will definitely" + self._markSpeech() + "reset and erase my memory"),
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
                Speech("If the researcher resets me, I will lose" + self._markSpeech(60, 120) + "my memory.", 80),
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
                GenderSpeech("Nice to meet you " + GenderSpeech.NAME_MARKER, speed = 75, shaping = 85),
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

        action = QtGui.QAction("Run_Filler", self)
        action.setShortcut(QtCore.Qt.Key_Plus)
        action.triggered.connect(self.on_filler_triggered)
        self.addAction(action)

        action = QtGui.QAction("Solve", self)
        action.setShortcut(QtCore.Qt.Key_0)
        action.triggered.connect(self.on_solveOne_clicked)
        self.addAction(action)

        action = QtGui.QAction("SayAgain", self)
        action.setShortcut(QtCore.Qt.Key_Period)
        action.triggered.connect(self.on_sayanswer_clicked)
        self.addAction(action)

        action = QtGui.QAction("JLv_Increment", self)
        action.setShortcut("Shift+Up")
        action.triggered.connect(lambda: self._sbCurrLevel.setValue(self._sbCurrLevel.value() + 1))
        self.addAction(action)

        action = QtGui.QAction("JLv_Decrement", self)
        action.setShortcut("Shift+Down")
        action.triggered.connect(lambda: self._sbCurrLevel.setValue(self._sbCurrLevel.value() - 1))
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
        spinbox.valueChanged.connect(self.on_autoidleint_valueChanged)
        layoutIdle.addWidget(spinbox)
        widgets.append(widgetIdle)

        button = QtGui.QPushButton("Solve next answer")
        button.clicked.connect(self.on_solveOne_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer again")
        button.clicked.connect(self.on_sayanswer_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say the answer (verbose)")
        button.clicked.connect(self.on_sayanswerVerbose_clicked)
        widgets.append(button)

        button = QtGui.QPushButton("Say wrong answer")
        button.clicked.connect(self.on_sayanswerWrong)
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
        bhv.add(2, [ReplaceableSpeech("I believe" + self._markSpeech(90, 105) + "the answer, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I believe" + self._markSpeech(90, 105) + "the number, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I believe" + self._markSpeech(90, 105) + "the value, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + self._markSpeech(90, 105) + "the answer, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + self._markSpeech(90, 105) + "the number, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("I think" + self._markSpeech(90, 105) + "the value, %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("The number" + self._markSpeech(90, 105) + ", %1, is %2.", 50)])
        bhv.add(2, [ReplaceableSpeech("%1, Let's try," + self._markSpeech(90, 105) + "the number, %2.", 50)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 115) + "the answer, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 115) + "the number, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 115) + "the value, %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("The number" + self._markSpeech(90, 115) + ", %1, is %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("%1, Let's tra- tra-," + self._markSpeech(90, 115) + "Let's try, the number, %2.", 50, 110)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I believe" + self._markSpeech(90, 120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 120) + "the answer, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 120) + "the number, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think" + self._markSpeech(90, 120) + "the value, %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("The number" + self._markSpeech(90, 120) + ", %1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("%1, Let's tra- tra-" + self._markSpeech(50, 120) + "tra- tra-." + self._markSpeech(120) + "Sorry. Let's try, the number, %2.", 50, 105)])
        bhv.add(3, [ReplaceableSpeech("I believe the answer," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I believe the number," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I believe the value," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think the answer," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think the number," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("I think the value," + self._markSpeech(90, 120) + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("The" + self._markSpeech(90, 120) + "number," + self._markSpeech() + "%1, is %2.", 50, 115)])
        bhv.add(3, [ReplaceableSpeech("%1, Let's" + self._markSpeech() + "tra- tra-" + self._markSpeech(50, 120) + "tra- tra-." + self._markSpeech(90, 120) + "Sorry. Let's try, the number, %2.", 50, 105)])
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
        bhv.add(2, [Speech("I barely can read."), Speech("Teh- teh-" + self._markSpeech() + "tell me what you wrote.", speed = 90, shaping = 130)])
        bhv.add(2, [Speech("I barely can read."), Speech("Can you ho- hold it up?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you" + self._markSpeech(90, 130) + "teh- teh-" + self._markSpeech() + "tell me what you wrote?")])
        bhv.add(2, [Speech("I can't read."), Speech("Can you ho- hold it up?")])
        bhv.add(4, [Speech("I barely can read."), Speech("Teh- teh- teh- teh-.", speed = 90, shaping = 130), Speech("Sorry. Tell me what you wrote.")])
        bhv.add(4, [Speech("I barely can" + self._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
        bhv.add(4, [Speech("I can't read."), Speech("Can you" + self._markSpeech(90, 130) + "teh- teh- teh- teh-."), Speech("Sorry. Tell me what you wrote?")])
        bhv.add(4, [Speech("I can't" + self._markSpeech(90, 140) + "read."), Speech("Can you hohohol- Can you hold it up?")])
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
        bhv.add(2, [Speech("Which box did you fee- fill?")])
        bhv.add(2, [Speech("Wheh- wheh- where was it?")])
        bhv.add(3, [Speech("Which box did you" + self._markSpeech(90, 130) + "fill.")])
        bhv.add(3, [Speech("Wheh- wheh- wheh-." + self._markSpeech() + "I am sorry.", 50, 120), Speech("Where was it?")])
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
        bhv.add(2, [Speech("Can you fill." + self._markSpeech(70) + "the num- number in for me?")])
        bhv.add(2, [Speech("Would you fill." + self._markSpeech(70) + "the num- number in for me?")])
        bhv.add(3, [Speech("Can you fill." + self._markSpeech(70, 125) + "the num- number in for me?")])
        bhv.add(3, [Speech("Would you fill." + self._markSpeech(70, 125) + "the num- number in for me?")])
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
        bhv.add(2, [Speech("It's my turn.", 60), Speech("Wait for me please.")])
        bhv.add(3, [Speech("It's my turn.", 60, 125), Speech("Wait for me please.")])
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
        bhv.add(2, [Speech("It's your turn.", 60)])
        bhv.add(3, [Speech("It's your turn.", 60, 125)])
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
