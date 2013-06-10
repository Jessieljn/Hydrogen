from Definitions import LEDNames
from PyQt4 import QtCore
from NaoCamera import NaoCamera
from NaoMotion import NaoMotion
from NaoMotionList import NaoMotionList
import naoqi


##
# Nao.py
#
# Connection to the NAO
##
class Nao(QtCore.QObject):
    def __init__(self):
        super(Nao, self).__init__()
        self._isConnected = False
        self._naoBroker = None
        self._camera = NaoCamera()
        self._behaviorProxy = None
        self._motionProxy = None
        self._speechProxy = None
        self._ledProxy = None
        self._stiffness = 0.0
        NaoMotionList.initialize()
    # END __init__()

    def __del__(self):
        NaoMotionList.destroy()
    # END __del__()

    connected = QtCore.pyqtSignal()

    disconnected = QtCore.pyqtSignal()

    def connect(self, ipAddress, port):
        self._naoBroker = naoqi.ALBroker("NaoBroker", "0.0.0.0", 0, ipAddress, port)

        print " > Loading Text To Speech..."
        self._speechProxy = naoqi.ALProxy("ALTextToSpeech")
        self._speechProxy.setVolume(0.85)
        print " > " + str(self._speechProxy)
        print " > Loading Camera..."
        self._camera.start()
        print " > " + str(self._camera.getCameraProxy())
        print " > Loading Behaviors..."
        self._behaviorProxy = naoqi.ALProxy("ALBehaviorManager")
        print " > " + str(self._behaviorProxy)
        print " > Loading Motion..."
        self._motionProxy = naoqi.ALProxy("ALMotion")
        print " > " + str(self._motionProxy)
        print " > Loading LEDs..."
        self._ledProxy = naoqi.ALProxy("ALLeds")
        print " > " + str(self._ledProxy)

        self._isConnected = True
        self.connected.emit()
        return True
    # END connect()

    def disconnect(self):
        self._isConnected = False
        self._camera.stop()
        self._ledProxy = None
        self._speechProxy = None
        self._motionProxy = None
        self._behaviorProxy = None
        self._naoBroker.shutdown()
        self._naoBroker = None
        self.disconnected.emit()
    # END disconnect()

    def isConnected(self):
        return self._isConnected
    # END isConnected()

    def getCamera(self):
        return self._camera
    # END getCamera()

    def getInstalledBehaviors(self):
        return self._behaviorProxy.getInstalledBehaviors()
    # END getInstalledBehaviors()

    def behavior(self, bhv, post):
        if not post:
            self._behaviorProxy.runBehavior(bhv)
        else:
            self._behaviorProxy.post.runBehavior(bhv)
        #END if
    # END behavior()

    def motion(self, motion, post):
        proxy = naoqi.ALProxy("ALMotion")
        if not post:
            if motion.getMethod() == NaoMotion.METHOD_BEZIER:
                proxy.angleInterpolationBezier(motion.getNames(), motion.getTimes(), motion.getKeys());
            else:
                proxy.angleInterpolation(motion.getNames(), motion.getKeys(), motion.getTimes(), True);
            #END if
        else:
            if motion.getMethod() == NaoMotion.METHOD_BEZIER:
                proxy.post.angleInterpolationBezier(motion.getNames(), motion.getTimes(), motion.getKeys());
            else:
                proxy.post.angleInterpolation(motion.getNames(), motion.getKeys(), motion.getTimes(), True);
            #END if
        #END if
    # END motion()

    def say(self, msg, post):
        if not post:
            self._speechProxy.say(msg)
        else:
            self._speechProxy.post.say(msg)
        #END if
    # END say()

    def LEDNormal(self):
        self.LEDsetIntensity(LEDNames.Face, 1.0, True)
        self.LEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5, True)
        self.LEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5, True)
        self.LEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5, True)
    # END LEDNormal()

    def LEDfadeIntensity(self, name, intensity, seconds, post):
        if not post:
            self._ledProxy.fade(name, intensity, seconds)
        else:
            self._ledProxy.post.fade(name, intensity, seconds)
        #END if
    # END LEDfadeIntensity()

    def LEDfadeRGB(self, name, rgb, seconds, post):
        if not post:
            self._ledProxy.fadeRGB(name, rgb, seconds)
        else:
            self._ledProxy.post.fadeRGB(name, rgb, seconds)
        #END if
    # END LEDfadeRGB()

    def LEDsetIntensity(self, name, intensity, post):
        if not post:
            self._ledProxy.setIntensity(name, intensity)
        else:
            self._ledProxy.post.setIntensity(name, intensity)
        #END if
    # END LEDsetIntensity()

    def LEDrandomEyes(self, duration, post):
        if not post:
            self._ledProxy.randomEyes(duration)
        else:
            self._ledProxy.post.randomEyes(duration)
        #END if
    # END LEDrandomEyes()

    def tiltHeadUp(self):
        self._motionProxy.changeAngles("HeadPitch", -0.20, 0.10)
    # END tiltHeadUp()

    def tiltHeadDown(self):
        self._motionProxy.changeAngles("HeadPitch", 0.20, 0.10)
    # END tiltHeadDown()

    def turnHeadLeft(self):
        self._motionProxy.changeAngles("HeadYaw", 0.20, 0.10)
    # END turnHeadLeft()

    def turnHeadRight(self):
        self._motionProxy.changeAngles("HeadYaw", -0.20, 0.10)
    # END turnHeadRight()

    def setStiffness(self, stiffness):
        if self._stiffness < stiffness:
            if stiffness > 1.0:
                stiffness = 1.0
            #END if
            while self._stiffness < stiffness:
                self._stiffness = self._stiffness + 0.05
                if self._stiffness > 1.0:
                    self._stiffness = 1.0
                #END if
                self._motionProxy.setStiffnesses("Body", self._stiffness)
            #END while
        else:
            if stiffness < 0.0:
                stiffness = 0.0
            #END if
            while self._stiffness > stiffness:
                self._stiffness = self._stiffness - 0.05
                if self._stiffness < 0.0:
                    self._stiffness = 0.0
                #END if
                self._motionProxy.setStiffnesses("Body", self._stiffness)
            #END while
        #END if
    # END setStiffness()

    def setVolume(self, volume):
        self._speechProxy.setVolume(volume)
    # END setVolume()
# END Nao
