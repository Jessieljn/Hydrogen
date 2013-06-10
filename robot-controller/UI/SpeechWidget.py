from PyQt4 import QtCore
from PyQt4 import QtGui
from FocusableTextEdit import FocusableTextEdit


##
# SpeechWidget.py
#
# Text to Speech.
##
class SpeechWidget(QtGui.QGroupBox):
    def __init__(self, parent):
        super(SpeechWidget, self).__init__(parent)
        self.setTitle("Text To Speech")

        self._message = FocusableTextEdit(self)
        self._message.setMaximumHeight(85)
        self._message.textChanged.connect(self.on__message_textChanged)
        self._message.textSubmitted.connect(self.on__message_textSubmitted)
        self._message.inputCancelled.connect(self.on__message_inputCancelled)

        self._btnSay = QtGui.QPushButton('Say')
        self._btnSay.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self._btnSay.setFixedWidth(100)
        self._btnSay.setMaximumHeight(85)
        self._btnSay.clicked.connect(self.on__message_textSubmitted)

        self._lVolume = QtGui.QLabel("Volume")
        self._sldVolume = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldVolume.setMaximumHeight(60)
        self._sldVolume.setRange(0, 100)
        self._sldVolume.setValue(50)
        self._sldVolume.valueChanged.connect(self.on__sldVolume_valueChanged)

        self._lSpeed = QtGui.QLabel("Speed")
        self._sldSpeed = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldSpeed.setMaximumHeight(60)
        self._sldSpeed.setRange(0, 100)
        self._sldSpeed.setValue(50)
        self._sldSpeed.valueChanged.connect(self.on_sldSpeed_valueChanged)

        self._lShape = QtGui.QLabel("Shape")
        self._sldShape = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldShape.setMaximumHeight(60)
        self._sldShape.setRange(0, 100)
        self._sldShape.setValue(50)
        self._sldShape.valueChanged.connect(self.on_sldShape_valueChanged)

        layoutVolume = QtGui.QVBoxLayout()
        layoutVolume.addWidget(self._lVolume)
        layoutVolume.addWidget(self._sldVolume, 0, QtCore.Qt.AlignCenter)

        layoutSpeed = QtGui.QVBoxLayout()
        layoutSpeed.addWidget(self._lSpeed)
        layoutSpeed.addWidget(self._sldSpeed, 0, QtCore.Qt.AlignCenter)

        layoutShape = QtGui.QVBoxLayout()
        layoutShape.addWidget(self._lShape)
        layoutShape.addWidget(self._sldShape, 0, QtCore.Qt.AlignCenter)

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

    def setTextEditFocus(self):
        self._message.setFocus(QtCore.Qt.OtherFocusReason)
        self._message.grabKeyboard()
    #END setTextEditFocus()

    textEditing = QtCore.pyqtSignal()
    textInputCancelled = QtCore.pyqtSignal()
    textSubmitted = QtCore.pyqtSignal(str)
    volumeChanged = QtCore.pyqtSignal(float)
    speedChanged = QtCore.pyqtSignal(float)
    shapeChanged = QtCore.pyqtSignal(float)

    def on__message_textChanged(self):
        self.textEditing.emit()
    #END on__message_textChanged()

    def on__message_textSubmitted(self):
        self.textSubmitted.emit(self._message.toPlainText())
        self._message.clear()
    #END on__message_textSubmitted()

    def on__message_inputCancelled(self):
        self._message.clear()
        self.textInputCancelled.emit()
    #END on__message_inputCancelled()

    def on__sldVolume_valueChanged(self, value):
        self.volumeChanged.emit(float(value) / 100)
    #END on__sldVolume_valueChanged()

    def on_sldSpeed_valueChanged(self, value):
        self.speedChanged.emit(float(value) / 100)
    #END on_sldSpeed_valueChanged()

    def on_sldShape_valueChanged(self, value):
        self.shapeChanged.emit(float(value) / 100)
    #END on_sldShape_valueChanged()
#END class