from NaoMotionDisagreeGesture import NaoMotionDisagreeGesture


class NaoMotionList():
    _motions = list()

    @staticmethod
    def initialize():
        NaoMotionList._motions.append(NaoMotionDisagreeGesture())
    #END initialize()

    @staticmethod
    def destroy():
        NaoMotionList._motions = list()
    #END destroy()

    @staticmethod
    def getMotion(name):
        for motion in NaoMotionList._motions:
            if motion.name() == name:
                return motion
            #END if
        #END for
        return None
    #END getMotion()
#END class
