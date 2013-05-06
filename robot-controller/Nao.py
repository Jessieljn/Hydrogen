import naoqi
from PyQt4 import QtCore
from PyQt4 import QtGui

DEFAULT_IP = '130.179.30.44'
DEFAULT_PORT = 9559

CAMERA_PARAM = 18
TOP_CAMERA = 0
BOTTOM_CAMERA = 1
BOTH_CAMERAS = 2


class Nao(QtCore.QObject):

    #Signals
    connected_signal = QtCore.pyqtSignal()
    disconnected_signal = QtCore.pyqtSignal()
    newFrame_cam1_signal = QtCore.pyqtSignal(QtGui.QImage)
    newFrame_cam2_signal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, cameraWidget = None):
        super(Nao, self).__init__()

        self.is_connected = False
        self.speechProxy = None
        self.cameraProxy = None
        self.behaviorProxy = None
        self.motionProxy = None
        self.timerID = None
        self.cameraWidget = cameraWidget
        self.cameraSource = TOP_CAMERA
    #END __init__()

    def connect(self, IP = DEFAULT_IP, port = DEFAULT_PORT):
        print " > Loading Text To Speech..."
        self.speechProxy = naoqi.ALProxy("ALTextToSpeech", IP, port)
        print " > " + str(self.speechProxy)
        self.speechProxy.setVolume(0.6)
        print " > Loading Camera..."
        self.cameraProxy = naoqi.ALProxy("ALVideoDevice", IP, port)
        print " > " + str(self.cameraProxy)
        print " > Loading Behaviors..."
        self.behaviorProxy = naoqi.ALProxy("ALBehaviorManager", IP, port)
        print " > " + str(self.behaviorProxy)
        print " > Loading Motion..."
        self.motionProxy = naoqi.ALProxy("ALMotion", IP, port)
        print " > " + str(self.motionProxy)
        print " > Loading LEDs..."
        self.ledProxy = naoqi.ALProxy("ALLeds", IP, port)
        print " > " + str(self.ledProxy)

        self.is_connected = True
        self.connected_signal.emit()
        return True
    #END connect()

    def startCamera(self):
        self.cameraProxyID = self.cameraProxy.subscribe("controller", 0, 11, 20)
        self.cameraProxy.setParam(CAMERA_PARAM, TOP_CAMERA)
        self.timerID = self.startTimer(1000/30)
    #END startCamera

    def stopCamera(self):
        if self.timerID != None:
            self.killTimer(self.timerID)
            self.timerID = None
            self.cameraProxy.unsubscribe(self.cameraProxyID)
        #END if
    #END stopCamera()

    def say(self, msg):
        self.speechProxy.post.say(msg)
    #END say()

    def disconnect(self):
        self.stopCamera()

        self.cameraProxy = None
        self.speechProxy = None
        self.behaviorProxy = None
        self.motionProxy = None
        self.ledProxy = None
        self.is_connected = False
        self.disconnected_signal.emit()
    #END disconnect()

    def isConnected(self):
        return self.is_connected
    #END isConnected()

    def timerEvent(self, event):
        if self.cameraWidget != None:
            source = self.cameraWidget.getCameraSource()

            if source == TOP_CAMERA:
                self.cameraProxy.setParam(CAMERA_PARAM, TOP_CAMERA)
            #END if
            elif source == BOTTOM_CAMERA:
                self.cameraProxy.setParam(CAMERA_PARAM, BOTTOM_CAMERA)
            #END elif

            self.rawFrame = self.cameraProxy.getImageRemote(self.cameraProxyID)
            self.frame = QtGui.QImage(self.rawFrame[6], self.rawFrame[0], self.rawFrame[1], QtGui.QImage.Format_RGB888)
            self.cameraWidget.setImage(self.frame)
        #END if
    #END timerEvent()

    def standUp(self):
        self.behaviorProxy.post.runBehavior("StandUp")
    #END standUp()

    def sitDown(self):
        self.behaviorProxy.post.runBehavior("SitDown")
        pass
    #END sitDown()

    def tiltHeadUp(self):
        self.motionProxy.changeAngles("HeadPitch", -0.20, 0.10)
    #END tiltHeadUp()

    def tiltHeadDown(self):
        self.motionProxy.changeAngles("HeadPitch", 0.20, 0.10)
    #END tiltHeadDown()

    def turnHeadLeft(self):
        self.motionProxy.changeAngles("HeadYaw", 0.20, 0.10)
    #END turnHeadLeft()

    def turnHeadRight(self):
        self.motionProxy.changeAngles("HeadYaw", -0.20, 0.10)
    #END turnHeadRight()

    def prod1(self):
        self.behaviorProxy.post.runBehavior("Prod1")
    #END prod1

    def prod2(self):
        self.behaviorProxy.post.runBehavior("Prod2")
    #END prod2

    def prod3(self):
        self.behaviorProxy.post.runBehavior("Prod3")
    #END prod3

    def prod4(self):
        self.behaviorProxy.post.runBehavior("Prod4")
    #END prod4

    def setVolume(self, volume):
        self.speechProxy.setVolume(volume)
    #END setVolume()

    def setLEDsNormal(self):
        self.ledProxy.post.fadeRGB("ChestLeds", 0x0000ff00, 0.5)
        self.ledProxy.post.setIntensity("FaceLeds", 1.0)
        self.ledProxy.post.fadeRGB("LeftEarLeds", 0x00ff6100, 0.5)
        self.ledProxy.post.fadeRGB("RightEarLeds", 0x00ff6100, 0.5)
    #END setLEDsNormal()

    def setLEDsProcessing(self):
        self.ledProxy.post.fadeRGB("ChestLeds", 0x00ff0000, 0.5)
        self.ledProxy.post.fadeRGB("FaceLeds", 0x00ffa500, 0.5)
        self.ledProxy.post.fadeRGB("LeftEarLeds", 0x00ffa500, 0.5)
        self.ledProxy.post.fadeRGB("RightEarLeds", 0x00ffa500, 0.5)

        #Sets the intensity of the LEDs.
        #self.ledProxy.post.setIntensity("ChestLeds", 1.0)
    #END setLEDsProcessing()

    def introduce(self):
        self.behaviorProxy.post.runBehavior("Introduce")
    #END introduce()

    def setStiffness(self, stiffness):
        self.motionProxy.setStiffnesses("Body", stiffness)
    #END setStiffness()

    def taiChi(self):
        self.behaviorProxy.post.runBehavior("TaiChi")
    #END taiChi()
#END Nao