from Definitions import Camera, Direction
from PyQt4 import QtCore, QtGui


##
# CameraWidget.py
#
# Creates a camera widget in the GUI.
# Allows for switching between the top and bottom camera, as well as rotation of the camera.
##
class CameraWidget(QtGui.QGroupBox):
    def __init__(self, parent, naoCamera):
        super(CameraWidget, self).__init__(parent)
        self.setTitle("Camera")

        self._wgtImage = QtGui.QWidget(self)
        self._wgtImage.setMinimumSize(320, 240)
        self._lCamera = QtGui.QLabel(self._wgtImage)
        self._lCamera.setAlignment(QtCore.Qt.AlignCenter)
        self._lCamera.setFrameStyle(QtGui.QFrame.Panel)
        layoutCamera = QtGui.QHBoxLayout(self._wgtImage)
        layoutCamera.setMargin(0)
        layoutCamera.addWidget(self._lCamera, 0, QtCore.Qt.AlignCenter)

        self._wgtButtons = QtGui.QWidget(self)
        self._wgtButtons.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        self._btnUp = QtGui.QPushButton("^", self._wgtButtons)
        self._btnUp.setFixedSize(25, 25)
        self._btnUp.clicked.connect(self.on__btnUp_clicked)
        self._btnDown = QtGui.QPushButton("v", self._wgtButtons)
        self._btnDown.setFixedSize(25, 25)
        self._btnDown.clicked.connect(self.on__btnDown_clicked)
        self._btnLeft = QtGui.QPushButton("<", self._wgtButtons)
        self._btnLeft.setFixedSize(25, 25)
        self._btnLeft.clicked.connect(self.on__btnLeft_clicked)
        self._btnRight = QtGui.QPushButton(">", self._wgtButtons)
        self._btnRight.setFixedSize(25, 25)
        self._btnRight.clicked.connect(self.on__btnRight_clicked)
        layoutButtons = QtGui.QGridLayout(self._wgtButtons)
        layoutButtons.setContentsMargins(10, 10, 10, 10)
        layoutButtons.setSpacing(6)
        layoutButtons.addWidget(self._btnUp, 1, 2, 1, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layoutButtons.addWidget(self._btnLeft, 2, 1, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        layoutButtons.addWidget(self._btnRight, 2, 3, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        layoutButtons.addWidget(self._btnDown, 3, 2, 1, 1, QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)

        self._wgtCamSel = QtGui.QWidget(self)
        self._wgtCamSel.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        self._rdbtnTopCamera = QtGui.QRadioButton("Top", self._wgtCamSel)
        self._rdbtnTopCamera.setChecked(True)
        self._rdbtnBottomCamera = QtGui.QRadioButton("Bottom", self._wgtCamSel)
        self._btnGrpCamera = QtGui.QButtonGroup()
        self._btnGrpCamera.addButton(self._rdbtnTopCamera)
        self._btnGrpCamera.addButton(self._rdbtnBottomCamera)
        self._btnGrpCamera.buttonClicked.connect(self.on__btnGrpCamera_buttonClicked)
        layoutCamSel = QtGui.QHBoxLayout(self._wgtCamSel)
        layoutCamSel.setMargin(0)
        layoutCamSel.addWidget(self._rdbtnTopCamera, 0, QtCore.Qt.AlignCenter)
        layoutCamSel.addWidget(self._rdbtnBottomCamera, 0, QtCore.Qt.AlignCenter)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(3)
        layoutMain.addWidget(self._wgtImage)
        layoutMain.addWidget(self._wgtButtons)
        layoutMain.addWidget(self._wgtCamSel)

        self._naoCamera = naoCamera
        self._timerID = self.startTimer(1000 / 60)
        self.setDefaultImage()
    #END __init__()

    def __del__(self):
        self.killTimer(self._timerID)
    #END __del__()

    cameraChanged = QtCore.pyqtSignal(int)

    moveHead = QtCore.pyqtSignal(int)

    def setDefaultImage(self):
        self._lCamera.setPixmap(QtGui.QPixmap('images/image.png'))
    #END setDefaultImage()

    def on__btnUp_clicked(self):
        self.moveHead.emit(Direction.Up)
    #END on__btnUp_clicked()

    def on__btnDown_clicked(self):
        self.moveHead.emit(Direction.Down)
    #END on__btnDown_clicked()

    def on__btnLeft_clicked(self):
        self.moveHead.emit(Direction.Left)
    #END on__btnLeft_clicked()

    def on__btnRight_clicked(self):
        self.moveHead.emit(Direction.Right)
    #END on__btnRight_clicked()

    def on__btnGrpCamera_buttonClicked(self, button):
        if button == self._rdbtnTopCamera:
            self.cameraChanged.emit(Camera.Top)
        elif button == self._rdbtnBottomCamera:
            self.cameraChanged.emit(Camera.Bottom)
        #END if
    #END on__btnGrpCamera_buttonClicked()

    def resizeEvent(self, event):
        self._lCamera.setFixedSize(self._wgtImage.size())
    #END resizeEvent()

    def timerEvent(self, event):
        image = self._naoCamera.frame()
        if image is not None:
            image = QtGui.QPixmap.fromImage(image)
            image = image.scaled(self._lCamera.size(), QtCore.Qt.KeepAspectRatio)
            self._lCamera.setPixmap(image)
        #END if
    #END timerEvent()
#END CameraWidget
