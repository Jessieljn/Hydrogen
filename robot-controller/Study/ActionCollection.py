from PyQt4 import QtCore
from Action import BaseAction
from Action import Motion
from Action import Stiffness
from MotionList import MotionList
from Nao import NaoMotion
import random


class ActionCollection(QtCore.QObject):
    INDEX_ACTIONS = 0
    INDEX_MOTION = 1

    def __init__(self, name = "", insert_sequence = False):
        super(ActionCollection, self).__init__()
        self._name = name
        self._inSeq = insert_sequence
        self._list = dict() # list of actions and motions
        self._maxLevel = 0 # max level in the list
        self._text = list() # text to replace say module's behavior
    #END __init__()

    def add(self, level, actions = None, motions = None, insert_sequence = None):
        if insert_sequence is None:
            insert_sequence = self._inSeq
        #END if
        if not level in self._list:
            self._maxLevel = max(self._maxLevel, level)
            self._list[level] = [[], []]
        #END if

        if actions is not None:
            if isinstance(actions, BaseAction):
                actions = [actions]
            #END if
            if insert_sequence:
                if len(self._list[level][ActionCollection.INDEX_ACTIONS]) <= 0:
                    self._list[level][ActionCollection.INDEX_ACTIONS].append([])
                #END if
                self._list[level][ActionCollection.INDEX_ACTIONS][-1] += actions
            else:
                self._list[level][ActionCollection.INDEX_ACTIONS].append(actions)
            #END if
        #END if

        if motions is not None:
            if isinstance(motions, str):
                motions = [Motion(motion = MotionList.getByName(str(level) + "_" + motions), blocking = False)]
            elif isinstance(motions, NaoMotion):
                motions = [Motion(motion = motions, blocking = False)]
            #END if
            if insert_sequence:
                if len(self._list[level][ActionCollection.INDEX_MOTION]) <= 0:
                    self._list[level][ActionCollection.INDEX_MOTION].append([])
                #END if
                self._list[level][ActionCollection.INDEX_MOTION][-1] += motions
            else:
                self._list[level][ActionCollection.INDEX_MOTION].append(motions)
            #END if
        #END if
    #END add()

    def addText(self, value):
        self._text.append(value.lower())
    #END addText()

    def containText(self, value):
        value = value.lower()
        for sz in self._text:
            if sz == value:
                return True
            #END if
        #END for
        return False
    #END containText()

    def get(self, level):
        motions = []
        curr = level
        while len(motions) <= 0 and curr >= 0:
            if curr in self._list and len(self._list[curr][ActionCollection.INDEX_MOTION]) > 0:
                val = random.randint(0, len(self._list[curr][ActionCollection.INDEX_MOTION]) - 1)
                motions.append(Stiffness(1.0))
                motions += self._list[curr][ActionCollection.INDEX_MOTION][val]
            #END if
            curr -= 1
        #END while
        actions = []
        curr = level
        while len(actions) <= 0 and curr >= 0:
            if curr in self._list and len(self._list[curr][ActionCollection.INDEX_ACTIONS]) > 0:
                val = random.randint(0, len(self._list[curr][ActionCollection.INDEX_ACTIONS]) - 1)
                actions += self._list[curr][ActionCollection.INDEX_ACTIONS][val]
            #END if
            curr -= 1
        #END while
        return motions + actions
    #END get()

    def getInsertSequence(self):
        return self._inSeq
    #END getInsertSequence()

    def getMaxLevel(self):
        return self._maxLevel
    #END getMaxLevel()

    def getName(self):
        return self._name
    #END getName()

    def setInsertSequence(self, value):
        self._inSeq = value
    #END setInsertSequence()
#END class
