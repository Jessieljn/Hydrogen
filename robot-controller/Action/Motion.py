from BaseAction import BaseAction
from Nao import NaoMotionList


class Motion(BaseAction):
    def __init__(self, motionName, speed = 1.0, repeat = 0, repeatBegin = 0, repeatEnd = -1, blocking = False):
        super(Motion, self).__init__()
        self._motionName = str(motionName)
        if speed <= 0:
            self._speed = 0.0001
        elif speed >= 3.0:
            self._speed = 3.0
        else:
            self._speed = speed
        #END if
        self._repeat = int(repeat)
        self._repeatBegin = int(repeatBegin)
        self._repeatEnd = int(repeatEnd)
        self._blocking = blocking
    #END __init__()

    def execute(self, nao):
        motion = NaoMotionList.find(self._motionName)
        if motion is not None:
            if self._speed != 1.0:
                motion = motion.applySpeed(self._speed)
            #END if
            if self._repeat > 0:
                motion = motion.applyRepeat(self._repeatBegin, self._repeatEnd, self._repeat)
            #END if
            nao.motion(motion, self._blocking)
        #END if
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
            ret = ret + " repeating key frames from " + str(self._repeatBegin) + " to " + str(self._repeatEnd) + " " + str(self._repeat) + " times"
        #END if
        return ret
    #END paramToString()
#END class
