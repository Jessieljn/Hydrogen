from BaseAction import BaseAction
from Nao import NaoMotionList


class Motion(BaseAction):
    def __init__(self, motionName = "", speed = 1.0, repeat = 0, repeatBegin = 0, repeatEnd = -1, repeatSpeed = 1.0,
                 motion = None, blocking = False):
        super(Motion, self).__init__()
        self._motionName = str(motionName)
        self._speed = float(speed)
        self._repeat = int(repeat)
        self._repeatBegin = int(repeatBegin)
        self._repeatEnd = int(repeatEnd)
        self._repeatSpeed = float(repeatSpeed)
        self._motion = motion
        self._blocking = blocking
        if self._motion is None:
            self._motion = NaoMotionList.find(self._motionName)
            if self._speed != 1.0:
                self._motion = self._motion.applySpeed(self._speed)
            #END if
            if self._repeat > 0:
                self._motion = self._motion.applyRepeat(self._repeatBegin, self._repeatEnd, self._repeat,
                                                        self._repeatSpeed)
            #END if
        else:
            self._motionName = "[Predefined] " + self._motion.name()
        #END if
    #END __init__()

    def execute(self, nao):
        nao.motion(self._motion, not self._blocking)
    #END execute()

    def actionToString(self):
        return "Motion"
    #END actionToString()

    def paramToString(self):
        ret = self._motionName
        if self._speed != 1.0:
            ret = ret + " x" + str(self._speed)
        #END if
        if self._repeat > 0:
            ret += " repeating key frames "
            if self._repeatSpeed != 1.0:
                ret = ret + " x" + str(self._repeatSpeed) + " "
            #END if
            ret = ret + str(self._repeat) + " times" + " from " + str(self._repeatBegin) + " to " + str(self._repeatEnd)
        #END if
        return ret
    #END paramToString()
#END Motion.py