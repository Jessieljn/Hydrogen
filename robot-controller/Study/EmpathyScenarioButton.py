from PyQt4 import QtGui
from Action import Motion
from Action import Stiffness
from EmpathyMotionList import EmpathyMotionList
import random


class EmpathyScenarioButton(QtGui.QPushButton):
    def __init__(self, label, jlv, actions, motions):
        super(EmpathyScenarioButton, self).__init__(label)
        self._actions = actions
        self._motions = []
        self._jlv = jlv
        for motion in motions:
            motion = EmpathyMotionList.getByName(str(jlv) + "_" + motion)
            if motion is not None:
                self._motions.append(motion)
            #END if
        #END for
    #END __init__()

    def getRobotActions(self):
        actions = []
        if len(self._motions) > 0:
            val = random.randint(0, len(self._motions) - 1)
            actions.append(Stiffness(1.0))
            actions.append(Motion(motion = self._motions[val], blocking = False))
        #END if
        if len(self._actions) > 0:
            val = random.randint(0, len(self._actions) - 1)
            actions = actions + self._actions[val]
        #END if
        return actions
    #END getRobotActions()
#END EmpathyScenarioButton.py