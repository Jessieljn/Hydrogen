from PyQt4 import QtGui
from Action import BaseAction
from Action import Motion
from Action import Stiffness
from Action import WaitMotion
from EmpathyMotionList import EmpathyMotionList
import random


class EmpathyButton(QtGui.QPushButton):
    INDEX_ACTIONS = 0
    INDEX_MOTION = 1

    INDEX_FILLER = 0
    INDEX_BIG_IDLE = 1
    INDEX_SMALL_IDLE = 2
    INDEX_SUDOKU_ANSWER = 3

    _behaviours = []
    _motions = dict()

    def __init__(self, label, idle = False):
        super(EmpathyButton, self).__init__(label)
        # The list list of action-motion.
        # action-motion contains list of actions and corresponding motion IDs
        self._list = dict()
        self._maxLevel = 0
        self._idle = idle
        random.seed()
    #END __init__()

    def add(self, jlv, actions = None, motion = None):
        if not jlv in self._list:
            self._list[jlv] = [[], []]
            self._maxLevel = max(self._maxLevel, jlv)
        #END if
        if actions is not None:
            if isinstance(actions, BaseAction):
                actions = [actions]
            #END if
            self._list[jlv][EmpathyButton.INDEX_ACTIONS].append(actions)
        #END if
        if motion is not None:
            motion = EmpathyMotionList.getByName(motion)
            if motion is not None:
                self._list[jlv][EmpathyButton.INDEX_MOTION].append(motion)
            #END if
        #END if
    #END add()

    def getRobotActions(self, jlv):
        while not jlv in self._list:
            jlv = jlv - 1 # try to use less jittery version if we don't have corresponding version of actions
        #END while
        if jlv < 0:
            return [] # if there is no version of actions, return empty list
        #END if

        actions = []
        if len(self._list[jlv][EmpathyButton.INDEX_MOTION]) > 0:
            val = random.randint(0, len(self._list[jlv][EmpathyButton.INDEX_MOTION]) - 1)
            actions.append(Stiffness(1.0))
            actions.append(Motion(motion = self._list[jlv][EmpathyButton.INDEX_MOTION][val], blocking = False))
            if self._idle:
                pass
                #actions.append(WaitMotion())
            #END if
        #END if
        if len(self._list[jlv][EmpathyButton.INDEX_ACTIONS]) > 0:
            val = random.randint(0, len(self._list[jlv][EmpathyButton.INDEX_ACTIONS]) - 1)
            actions = actions + self._list[jlv][EmpathyButton.INDEX_ACTIONS][val]
        #END if
        return actions
    #END getRobotActions()

    def maxLevel(self):
        return self._maxLevel
    #END maxLevel()
#END class
