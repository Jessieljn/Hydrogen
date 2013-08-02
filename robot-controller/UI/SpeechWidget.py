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
        self._szLastText = ""

        self._message = SubmittableTextEdit(self)
        self._message.textChanged.connect(self.textEditing)
        self._message.textSubmitted.connect(lambda: self.textSubmitted.emit(self.getText()))
        self._message.textSubmitted.connect(self._message.clear)
        self._message.inputCancelled.connect(self.inputCancelled)
        self._message.inputCancelled.connect(self._message.clear)

        self._lVolume = QtGui.QLabel("Volume")
        self._lVolume.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self._sldVolume = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldVolume.setPageStep(5)
        self._sldVolume.setRange(0, 100)
        self._sldVolume.setSingleStep(1)
        self._sldVolume.setValue(85)
        self._sldVolume.valueChanged.connect(self.on__sldVolume_valueChanged)
        self._VolumeLabel = QtGui.QLabel(str(self._sldVolume.value()))
        self._VolumeLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)

        self._lSpeed = QtGui.QLabel("Speed")
        self._lSpeed.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self._sldSpeed = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldSpeed.setPageStep(5)
        self._sldSpeed.setRange(50, 200)
        self._sldSpeed.setSingleStep(1)
        self._sldSpeed.setValue(90)
        self._sldSpeed.valueChanged.connect(self.on__sldSpeed_valueChanged)
        self._SpeedLabel = QtGui.QLabel(str(self._sldSpeed.value()))
        self._SpeedLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)

        self._lShape = QtGui.QLabel("Shape")
        self._lShape.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self._sldShape = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldShape.setPageStep(5)
        self._sldShape.setRange(50, 150)
        self._sldShape.setSingleStep(1)
        self._sldShape.setValue(100)
        self._sldShape.valueChanged.connect(self.on__sldShape_valueChanged)
        self._ShapeLabel = QtGui.QLabel(str(self._sldShape.value()))
        self._ShapeLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)

        layoutVolume = QtGui.QVBoxLayout()
        layoutVolume.setMargin(0)
        layoutVolume.addWidget(self._lVolume, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layoutVolume.addWidget(self._sldVolume, 0, QtCore.Qt.AlignHCenter)
        layoutVolume.addWidget(self._VolumeLabel, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)

        layoutSpeed = QtGui.QVBoxLayout()
        layoutSpeed.setMargin(0)
        layoutSpeed.addWidget(self._lSpeed, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layoutSpeed.addWidget(self._sldSpeed, 0, QtCore.Qt.AlignHCenter)
        layoutSpeed.addWidget(self._SpeedLabel, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)

        layoutShape = QtGui.QVBoxLayout()
        layoutShape.setMargin(0)
        layoutShape.addWidget(self._lShape, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layoutShape.addWidget(self._sldShape, 0, QtCore.Qt.AlignHCenter)
        layoutShape.addWidget(self._ShapeLabel, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)

        btnSay = QtGui.QPushButton('Say')
        btnSay.setFixedSize(120, 30)
        btnSay.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        btnSay.clicked.connect(lambda: self.textSubmitted.emit(self.getText()))
        btnSay.clicked.connect(self._message.clear)

        btnRepeat = QtGui.QPushButton('Repeat')
        btnRepeat.setFixedSize(120, 30)
        btnRepeat.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        btnRepeat.clicked.connect(lambda: self.textSubmitted.emit(self.getLastText()))

        layoutOptions = QtGui.QHBoxLayout()
        layoutOptions.setMargin(0)
        layoutOptions.addLayout(layoutVolume)
        layoutOptions.addLayout(layoutSpeed)
        layoutOptions.addLayout(layoutShape)

        layoutControls = QtGui.QVBoxLayout()
        layoutControls.setMargin(0)
        layoutControls.addLayout(layoutOptions)
        layoutControls.addWidget(btnSay, 0, QtCore.Qt.AlignHCenter)
        layoutControls.addWidget(btnRepeat, 1, QtCore.Qt.AlignHCenter)

        layoutMain = QtGui.QHBoxLayout(self)
        layoutMain.addWidget(self._message)
        layoutMain.addLayout(layoutControls)
    #END __init__()

    inputCancelled = QtCore.pyqtSignal()

    shapeChanged = QtCore.pyqtSignal(float)

    speedChanged = QtCore.pyqtSignal(float)

    textEditing = QtCore.pyqtSignal()

    textSubmitted = QtCore.pyqtSignal(str)

    volumeChanged = QtCore.pyqtSignal(float)

    def getShaping(self):
        return self._sldShape.value()
    #END getShaping()

    def getSpeed(self):
        return self._sldSpeed.value()
    #END getSpeed()

    def getLastText(self):
        return self._szLastText
    #END getLastText()

    def getText(self):
        self._szLastText = str(self._message.toPlainText())
        return self._szLastText
    #END getText()

    def isTextEmpty(self):
        return len(str(self._message.toPlainText())) <= 0
    #END isTextEmpty()

    def setInputFocus(self):
        self._message.setFocus(QtCore.Qt.OtherFocusReason)
    #END setInputFocus()

    def setText(self, text):
        self._message.setPlainText(text)
    #END setText()

    def on__sldShape_valueChanged(self, value):
        self._ShapeLabel.setText(str(value))
        self.shapeChanged.emit(float(value) / 100)
    #END on__sldShape_valueChanged()

    def on__sldSpeed_valueChanged(self, value):
        self._SpeedLabel.setText(str(value))
        self.speedChanged.emit(float(value) / 100)
    #END on__sldSpeed_valueChanged()

    def on__sldVolume_valueChanged(self, value):
        self._VolumeLabel.setText(str(value))
        self.volumeChanged.emit(float(value) / 100)
    #END on__sldVolume_valueChanged()
#END SpeechWidget
