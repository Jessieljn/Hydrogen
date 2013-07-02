from PyQt4 import QtCore
from PyQt4 import QtGui
from Definitions import LEDNames
from Action import ActionStart
from Action import Motion
from Action import ReplaceableSpeech
from Action import Speech
from Action import Stiffness
from EmpathyMotionList import EmpathyMotionList
from EmpathySpeech import EmpathySpeech
from EmpathySudoku import SudokuBoards
from EmpathyGUI import EmpathyGUI
import random


class Empathy(QtGui.QWidget):
    def __init__(self):
        super(Empathy, self).__init__()
        EmpathyMotionList.initialize()
        random.seed()
        self._actionQueue = None
        self._currSubgrid = None
        self._idleCount = 0
        self._idleRun = False
        self._idleInterval = 10000
        self._idleTime = QtCore.QTime.currentTime()
        self._itemName = "shirt"
        self._jitterLevel = 0
        self._lastSudoku = [0, 0, 0]  # x y value
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
        EmpathyMotionList.destroy()
    #END __del__()

    def LEDActive(self):
        self._nao.LEDrandomEyes(1.0, True)
    #END LEDActive()

    def LEDNormal(self):
        current_phase = self._jitterLevel
        # noinspection PyUnusedLocal
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

    # noinspection PyUnusedLocal
    def hideEvent(self, event):
        self._idleRun = False
        self.killTimer(self._timerID)
    #END hideEvent()

    # noinspection PyUnusedLocal
    def showEvent(self, event):
        self._timerID = self.startTimer(50)
    #END showEvent()

    # noinspection PyUnusedLocal
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
                    self._wgtSudoku.highlightSubgrid(self._currSubgrid[0], self._currSubgrid[1],
                                                     QtGui.QColor(0, 255, 0))
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
            jlv -= 1
        else:
            jlv = 0
        #END if
        self._jitterLevel = jlv
    #END on_jitterLevel_valueChanged()

    def on_motionbutton_clicked(self):
        motion = str(self._jitterLevel) + "_" + str(self.sender().text())
        motion = EmpathyMotionList.getByName(motion)
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
        action = Speech(self._toCoordinateVerbose(self._lastSudoku[1], self._lastSudoku[0]) + ", "
                        + str(self._lastSudoku[2]))
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

    def _setupUi(self):
        splitter = QtGui.QSplitter(self)
        splitter.setOrientation(QtCore.Qt.Horizontal)

        layout = QtGui.QHBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(splitter)
        EmpathyGUI.setupShortcuts(self)
    #END _setupUi()
#END Empathy