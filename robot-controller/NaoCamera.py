from Definitions import Camera, CameraResolution, VIDEO_SUBSCRIBE_NAME
from PyQt4 import QtCore, QtGui
import naoqi


class NaoCamera(QtCore.QObject):
    THREAD_SLEEP_INTERVAL = 3
    CAMERA_PARAM_SELECT = 18

    def __init__(self):
        super(NaoCamera, self).__init__()
        self._thread = None
        self._interval = 1000 / 30
        self._running = False
        self._cameraProxy = None
        self._cameraProxyID = None
    #END __init__()

    frameAvailable = QtCore.pyqtSignal(QtGui.QImage)

    def start(self):
        if self._thread is None:
            self._running = True
            self._thread = QtCore.QThread()
            self.moveToThread(self._thread)
            self.connect(self._thread, QtCore.SIGNAL("started()"), self._process);
            self._thread.connect(self, QtCore.SIGNAL("deleteLater()"), self.deleteLater);
            self._cameraProxy = naoqi.ALProxy("ALVideoDevice")
            self._cameraProxy.setParam(NaoCamera.CAMERA_PARAM_SELECT, Camera.Top)
            self._cameraProxyID = self._cameraProxy.subscribe(VIDEO_SUBSCRIBE_NAME, CameraResolution.QVGA, 11, 20)
            self._thread.start()
        #END if
    #END start()

    def stop(self):
        if self._thread is not None:
            self._old = self._thread
            self._running = False
            self._thread.wait(1000)
            self._thread.quit()
            self._thread = None
        #END if
        if self._cameraProxy is not None:
            if self._cameraProxyID is not None:
                self._cameraProxy.unsubscribe(self._cameraProxyID)
                self._cameraProxyID = None
            #END if
            self._cameraProxy = None
        #END if
    #END stop()

    def getCameraProxy(self):
        return self._cameraProxy
    #END getCameraProxy()

    def setCameraResolution(self, value):
        self._cameraProxy.setResolution(self.cameraProxyID, value)
    #END setCameraResolution()

    def setCameraSource(self, value):
        self._cameraProxy.setParam(NaoCamera.CAMERA_PARAM_SELECT, value)
    #END setCameraSource()

    def _process(self):
        while self._running:
            end = QtCore.QTime.currentTime().addMSecs(self._interval)
            rawFrame = self._cameraProxy.getImageRemote(self._cameraProxyID)
            frame = QtGui.QImage(rawFrame[6], rawFrame[0], rawFrame[1], QtGui.QImage.Format_RGB888)
            self.frameAvailable.emit(frame)
            while self._running and QtCore.QTime.currentTime() < end:
                QtCore.QThread.msleep(NaoCamera.THREAD_SLEEP_INTERVAL)
            #END while
        #END while
        self._running = False
    #END _process()
#END class
