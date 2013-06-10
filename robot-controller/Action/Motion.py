from BaseAction import BaseAction
from Nao import NaoMotionList


class Motion(BaseAction):
    def __init__(self, motionName, speed = 1.0, repeat = 0, repeatBegin = 0, repeatEnd = -1, repeatSpeed = 1.0, blocking = False):
        super(Motion, self).__init__()
        self._motionName = str(motionName)
        self._speed = float(speed)
        self._repeat = int(repeat)
        self._repeatBegin = int(repeatBegin)
        self._repeatEnd = int(repeatEnd)
        self._repeatSpeed = float(repeatSpeed)
        self._blocking = blocking
    #END __init__()

    def execute(self, nao):
        motion = NaoMotionList.find(self._motionName)
        if motion is not None:
            if self._speed != 1.0:
                motion = motion.applySpeed(Motion.speedToTimeModifier(self._speed))
            #END if
            if self._repeat > 0:
                motion = motion.applyRepeat(self._repeatBegin, self._repeatEnd, self._repeat, Motion.speedToTimeModifier(self._repeatSpeed))
            #END if
            nao.motion(motion, not self._blocking)
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
            ret += " repeating key frames "
            if self._repeatSpeed != 1.0:
                ret = ret + " x" + str(self._repeatSpeed) + " "
            #END if
            ret = ret + str(self._repeat) + " times" + " from " + str(self._repeatBegin) + " to " + str(self._repeatEnd)
        #END if
        return ret
    #END paramToString()

    @staticmethod
    def speedToTimeModifier(speed):
        if speed <= 0.0:
            # slowest
            return 5.0
        elif speed < 1.0:
            # slower
            return 5.0 * speed
        elif speed > 1.0:
            # faster
            return 1.0 / speed
        else:
            return speed
        #END if
    #END _speedToTimeModifier()
#END class
