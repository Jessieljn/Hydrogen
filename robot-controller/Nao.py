from Definitions import LEDNames
from PyQt4 import QtCore, QtGui
from NaoCamera import NaoCamera
import naoqi
import socket


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
        self.speechProxy = None
        self._camera = None
        self.behaviorProxy = None
        self.motionProxy = None
    # END __init__()

    connected = QtCore.pyqtSignal()

    disconnected = QtCore.pyqtSignal()

    frameAvailable = QtCore.pyqtSignal(QtGui.QImage)

    def connect(self, ipAddress, port):
        self._naoBroker = naoqi.ALBroker("NaoBroker", "0.0.0.0", 0, ipAddress, port)

        print " > Loading Text To Speech..."
        self.speechProxy = naoqi.ALProxy("ALTextToSpeech")
        self.speechProxy.setVolume(0.85)
        print " > " + str(self.speechProxy)
        print " > Loading Camera..."
        self._camera = NaoCamera()
        self._camera.frameAvailable.connect(self.frameAvailable)
        self._camera.start()
        print " > " + str(self._camera.getCameraProxy())
        print " > Loading Behaviors..."
        self.behaviorProxy = naoqi.ALProxy("ALBehaviorManager")
        print " > " + str(self.behaviorProxy)
        print " > Loading Motion..."
        self.motionProxy = naoqi.ALProxy("ALMotion")
        print " > " + str(self.motionProxy)
        print " > Loading LEDs..."
        self.ledProxy = naoqi.ALProxy("ALLeds")
        print " > " + str(self.ledProxy)

        self._isConnected = True
        self.connected.emit()
        return True
    # END connect()

    def disconnect(self):
        self._camera.stop()
        self._camera = None
        self.speechProxy = None
        self.behaviorProxy = None
        self.motionProxy = None
        self.ledProxy = None
        self._isConnected = False
        self._naoBroker.shutdown()
        self._naoBroker = None
        self.disconnected.emit()
    # END disconnect()

    def isConnected(self):
        return self._isConnected
    # END isConnected()

    def makeJitter(self, bhvName, boxName, startFrame = 0, endFrame = -1, joints = []):
        data = ""
        data += "in=/home/nao/behaviors/" + bhvName + "/behavior.xar|"
        data += "out=/home/nao/behaviors/jitter/behavior.xar|"
        data += "box=" + boxName + "|"
        data += "start=" + str(startFrame) + "|"
        data += "end=" + str(endFrame) + "|"
        for j in joints:
            data += "joint=" + j[0] + "," + str(j[1]) + "," + str(j[2]) + "|"
        # END for

        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sck.connect((self._naoBroker.getIP(), self._naoBroker.getPort()))
            sck.send(data)
            # Disconnect Signal
            sck.send("\0")
        finally:
            sck.close()
    # END makeJitter

    def behavior(self, bhv):
        self.behaviorProxy.runBehavior(bhv)
    # END behavior()

    def say(self, msg):
        self.speechProxy.say(msg)
    # END say()

    def LEDNormal(self):
        self.postLEDsetIntensity(LEDNames.Face, 1.0)
        self.postLEDfadeRGB(LEDNames.Chest, 0x0000ff00, 0.5)
        self.postLEDfadeRGB(LEDNames.LeftEar, 0x00ff6100, 0.5)
        self.postLEDfadeRGB(LEDNames.RightEar, 0x00ff6100, 0.5)
    # END LEDNormal()

    def LEDfadeIntensity(self, name, intensity, seconds):
        self.ledProxy.fade(name, intensity, seconds)
    # END LEDfadeIntensity()

    def LEDfadeRGB(self, name, rgb, seconds):
        self.ledProxy.fadeRGB(name, rgb, seconds)
    # END LEDfadeRGB()

    def LEDsetIntensity(self, name, intensity):
        self.ledProxy.setIntensity(name, intensity)
    # END LEDsetIntensity()

    def LEDrandomEyes(self, duration):
        self.ledProxy.randomEyes(duration)
    # END LEDrandomEyes()

    def postBehavior(self, bhv):
        self.behaviorProxy.post.runBehavior(bhv)
    # END postBehavior()

    def postSay(self, msg):
        self.speechProxy.post.say(msg)
    # END postSay()

    def postLEDfadeIntensity(self, name, intensity, seconds):
        self.ledProxy.post.fade(name, intensity, seconds)
    # END postLEDfadeIntensity()

    def postLEDfadeRGB(self, name, rgb, seconds):
        self.ledProxy.post.fadeRGB(name, rgb, seconds)
    # END postLEDfadeRGB()

    def postLEDsetIntensity(self, name, intensity):
        self.ledProxy.post.setIntensity(name, intensity)
    # END postLEDsetIntensity()

    def postLEDrandomEyes(self, duration):
        self.ledProxy.post.randomEyes(duration)
    # END postLEDrandomEyes()

    def tiltHeadUp(self):
        self.motionProxy.changeAngles("HeadPitch", -0.20, 0.10)
    # END tiltHeadUp()

    def tiltHeadDown(self):
        self.motionProxy.changeAngles("HeadPitch", 0.20, 0.10)
    # END tiltHeadDown()

    def turnHeadLeft(self):
        self.motionProxy.changeAngles("HeadYaw", 0.20, 0.10)
    # END turnHeadLeft()

    def turnHeadRight(self):
        self.motionProxy.changeAngles("HeadYaw", -0.20, 0.10)
    # END turnHeadRight()

    def setCameraResolution(self, value):
        self._camera.setResolution(value)
    # END setCameraResolution()

    def setCameraSource(self, value):
        self._camera.setParam(value)
    # END setCameraSource()

    def setStiffness(self, stiffness):
        self.motionProxy.setStiffnesses("Body", stiffness)
    # END setStiffness()

    def setVolume(self, volume):
        self.speechProxy.setVolume(volume)
    # END setVolume()
# END Nao
