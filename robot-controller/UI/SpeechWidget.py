from PyQt4 import QtCore
from PyQt4 import QtGui
from SubmittableTextEdit import SubmittableTextEdit


##
# SpeechWidget.py
#
# Text to Speech.
##
class SpeechWidget(QtGui.QGroupBox):
    def __init__(self, parent):
        super(SpeechWidget, self).__init__(parent)
        self.setTitle("Text To Speech")

        self._message = SubmittableTextEdit(self)
        self._message.setMaximumHeight(85)
        self._message.textChanged.connect(self.textEditing)
        self._message.textSubmitted.connect(self._message.clear)
        self._message.textSubmitted.connect(lambda: self.textSubmitted(self._message.text()))
        self._message.inputCancelled.connect(self._message.clear)
        self._message.inputCancelled.connect(self.inputCancelled)

        self._btnSay = QtGui.QPushButton('Say')
        self._btnSay.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self._btnSay.setFixedWidth(100)
        self._btnSay.setMaximumHeight(85)
        self._btnSay.clicked.connect(self.on__message_textSubmitted)

        self._lVolume = QtGui.QLabel("Volume")
        self._sldVolume = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldVolume.setMaximumHeight(60)
        self._sldVolume.setRange(0, 100)
        self._sldVolume.setValue(85)
        self._sldVolume.valueChanged.connect(self.on__sldVolume_valueChanged)
        self._VolumeLabel = QtGui.QLabel(str(self._sldVolume.value()))

        self._lSpeed = QtGui.QLabel("Speed")
        self._sldSpeed = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldSpeed.setMaximumHeight(60)
        self._sldSpeed.setRange(50, 200)
        self._sldSpeed.setValue(90)
        self._sldSpeed.valueChanged.connect(self.on_sldSpeed_valueChanged)
        self._SpeedLabel = QtGui.QLabel(str(self._sldSpeed.value()))

        self._lShape = QtGui.QLabel("Shape")
        self._sldShape = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldShape.setMaximumHeight(60)
        self._sldShape.setRange(50, 150)
        self._sldShape.setValue(100)
        self._sldShape.valueChanged.connect(self.on_sldShape_valueChanged)
        self._ShapeLabel = QtGui.QLabel(str(self._sldShape.value()))

        layoutVolume = QtGui.QVBoxLayout()
        layoutVolume.addWidget(self._lVolume)
        layoutVolume.addWidget(self._sldVolume, 0, QtCore.Qt.AlignCenter)
        layoutVolume.addWidget(self._VolumeLabel)

        layoutSpeed = QtGui.QVBoxLayout()
        layoutSpeed.addWidget(self._lSpeed)
        layoutSpeed.addWidget(self._sldSpeed, 0, QtCore.Qt.AlignCenter)
        layoutSpeed.addWidget(self._SpeedLabel)

        layoutShape = QtGui.QVBoxLayout()
        layoutShape.addWidget(self._lShape)
        layoutShape.addWidget(self._sldShape, 0, QtCore.Qt.AlignCenter)
        layoutShape.addWidget(self._ShapeLabel)

        layoutMain = QtGui.QHBoxLayout(self)
        layoutMain.addWidget(self._message)
        layoutMain.addWidget(self._btnSay)
        layoutMain.addLayout(layoutVolume)
        layoutMain.addLayout(layoutSpeed)
        layoutMain.addLayout(layoutShape)
    #END __init__()

    def isSpeechTextEmpty(self):
        return str(self._message.toPlainText()) == ""
    #END isSpeechTextEmpty

    def getShaping(self):
        return self._sldShape.value()
    #END getShaping()

    def getSpeed(self):
        return self._sldSpeed.value()
    #END getSpeed()

    def setTextEditFocus(self):
        self._message.setFocus(QtCore.Qt.OtherFocusReason)
        self._message.grabKeyboard()
    #END setTextEditFocus()

    inputCancelled = QtCore.pyqtSignal()

    textEditing = QtCore.pyqtSignal()

    textSubmitted = QtCore.pyqtSignal(str)

    volumeChanged = QtCore.pyqtSignal(float)
    speedChanged = QtCore.pyqtSignal(float)
    shapeChanged = QtCore.pyqtSignal(float)

    def on__sldVolume_valueChanged(self, value):
        self.volumeChanged.emit(float(value) / 100)
        self._VolumeLabel.setText(str(value))
    #END on__sldVolume_valueChanged()

    def on_sldSpeed_valueChanged(self, value):
        self.speedChanged.emit(float(value) / 100)
        self._SpeedLabel.setText(str(value))
    #END on_sldSpeed_valueChanged()

    def on_sldShape_valueChanged(self, value):
        self.shapeChanged.emit(float(value) / 100)
        self._ShapeLabel.setText(str(value))
    #END on_sldShape_valueChanged()
#END SpeechWidget
