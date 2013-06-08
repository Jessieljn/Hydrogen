from BaseAction import BaseAction
from Nao import NaoMotionList


class Motion(BaseAction):
    def __init__(self, motionName):
        super(Motion, self).__init__()
        self._motionName = str(motionName)
    #END __init__()

    def execute(self, nao):
        motion = NaoMotionList.getMotion(self._motionName)
        if motion is not None:
            nao.motion(motion)
        #END if
    #END execute()

    def actionToString(self):
        return "Motion"
    #END actionToString()

    def paramToString(self):
        return self._motionName
    #END paramToString()
#END class
