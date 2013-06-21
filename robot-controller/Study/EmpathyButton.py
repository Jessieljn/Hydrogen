import random

from PyQt4 import QtGui

from Action import BaseAction
from Action import Motion
from Action import Stiffness
from EmpathyMotionList import EmpathyMotionList


class EmpathyButton(QtGui.QPushButton):
    INDEX_ACTIONS = 0
    INDEX_MOTION = 1

    _behaviours = []
    _motions = dict()

    def __init__(self, label):
        super(EmpathyButton, self).__init__(label)
        # The list list of action-motion.
        # action-motion contains list of actions and corresponding motion IDs
        self._list = dict()
        self._maxLevel = 0
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
<<<<<<< HEAD
        while not jlv in self._list:
            jlv -= 1# try to use less jittery version if we don't have corresponding version of actions
            #END while
        if jlv < 0:
            return [] # if there is no version of actions, return empty list
        #END if

=======
        motions = []
        level = jlv
        while len(motions) <= 0 and level >= 0:
            if level in self._list:
                if len(self._list[level][EmpathyButton.INDEX_MOTION]) > 0:
                    val = random.randint(0, len(self._list[level][EmpathyButton.INDEX_MOTION]) - 1)
                    motions.append(Stiffness(1.0))
                    motions.append(Motion(motion = self._list[level][EmpathyButton.INDEX_MOTION][val], blocking = False))
                #END if
            #END if
            level = level - 1
        #END while
>>>>>>> a5853cc68c96dabd1a29bc6e1c6f1b853eddef04
        actions = []
        level = jlv
        while len(actions) <= 0 and level >= 0:
            if level in self._list:
                if len(self._list[level][EmpathyButton.INDEX_ACTIONS]) > 0:
                    val = random.randint(0, len(self._list[level][EmpathyButton.INDEX_ACTIONS]) - 1)
                    actions = actions + self._list[level][EmpathyButton.INDEX_ACTIONS][val]
                #END if
            #END if
            level = level - 1
        #END while
        return motions + actions
    #END getRobotActions()

    def maxLevel(self):
        return self._maxLevel
    #END maxLevel()
#END class
