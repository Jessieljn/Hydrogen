from Definitions import Camera, CameraResolution, VIDEO_SUBSCRIBE_NAME
from PyQt4 import QtCore, QtGui
import naoqi
import socket


##
# Nao.py
#
# Connection to the NAO
##
class Nao(QtCore.QObject):
    CAMERA_PARAM_SELECT = 18

    def __init__(self):
        super(Nao, self).__init__()
        self._isConnected = False
        self._naoBroker = None
        self.speechProxy = None
        self.cameraProxy = None
        self.behaviorProxy = None
        self.motionProxy = None
        self.timerID = None
    # END __init__()

    connected = QtCore.pyqtSignal()

    disconnected = QtCore.pyqtSignal()

    frameAvailable = QtCore.pyqtSignal(QtGui.QImage)

    def testing(self):
        print "testing"

    def connect(self, ipAddress, port):
        self._naoBroker = naoqi.ALBroker("NaoBroker", "0.0.0.0", 0, ipAddress, port)

        print " > Loading Text To Speech..."
        self.speechProxy = naoqi.ALProxy("ALTextToSpeech")
        self.speechProxy.setVolume(0.85)
        print " > " + str(self.speechProxy)
        print " > Loading Camera..."
        self.cameraProxy = naoqi.ALProxy("ALVideoDevice")
        print " > " + str(self.cameraProxy)
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
        self.stopCamera()
        self.cameraProxy = None
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

    def startCamera(self):
        self.cameraProxyID = self.cameraProxy.subscribe(VIDEO_SUBSCRIBE_NAME, CameraResolution.VGA, 11, 20)
        self.cameraProxy.setParam(Nao.CAMERA_PARAM_SELECT, Camera.Top)
        self.timerID = self.startTimer(1000 / 30)
    # END startCamera()

    def stopCamera(self):
        if self.timerID is not None:
            self.killTimer(self.timerID)
            self.timerID = None
            self.cameraProxy.unsubscribe(self.cameraProxyID)
        # END if
    # END stopCamera()

    def setCameraResolution(self, value):
        self.cameraProxy.setResolution(self.cameraProxyID, value)
    # END setCameraResolution()

    def setCameraSource(self, value):
        self.cameraProxy.setParam(Nao.CAMERA_PARAM_SELECT, value)
    # END setCameraSource()

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

    def postBehavior(self, bhv):
        self.behaviorProxy.post.runBehavior(bhv)
    # END postBehavior()

    def postSay(self, msg):
        self.speechProxy.post.say(msg)
    # END postSay()

    def timerEvent(self, event):
        self.rawFrame = self.cameraProxy.getImageRemote(self.cameraProxyID)
        self.frame = QtGui.QImage(self.rawFrame[6], self.rawFrame[0], self.rawFrame[1], QtGui.QImage.Format_RGB888)
        self.frameAvailable.emit(self.frame)
    # END timerEvent()

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

    def setLEDsNormal(self):
        self.ledProxy.post.fadeRGB("ChestLeds", 0x0000ff00, 0.5)
        self.ledProxy.post.setIntensity("FaceLeds", 1.0)
        self.ledProxy.post.fadeRGB("LeftEarLeds", 0x00ff6100, 0.5)
        self.ledProxy.post.fadeRGB("RightEarLeds", 0x00ff6100, 0.5)
    # END setLEDsNormal()

    def setLEDsProcessing(self):
        self.ledProxy.post.fadeRGB("ChestLeds", 0x00ff0000, 0.5)
        self.ledProxy.post.fadeRGB("FaceLeds", 0x00ffa500, 0.5)
        self.ledProxy.post.fadeRGB("LeftEarLeds", 0x00ffa500, 0.5)
        self.ledProxy.post.fadeRGB("RightEarLeds", 0x00ffa500, 0.5)

        # Sets the intensity of the LEDs.
        # self.ledProxy.post.setIntensity("ChestLeds", 1.0)
    # END setLEDsProcessing()

    def setStiffness(self, stiffness):
        self.motionProxy.setStiffnesses("Body", stiffness)
    # END setStiffness()

    def setVolume(self, volume):
        self.speechProxy.setVolume(volume)
    # END setVolume()
# END Nao
