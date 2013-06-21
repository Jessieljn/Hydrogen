from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Behavior
from Action import Motion
from Action import Stiffness
from Nao import NaoMotionList


class MovementWidget(QtGui.QGroupBox):
    def __init__(self, parent):
        super(MovementWidget, self).__init__(parent)
        self.setTitle("Movement")
        self._actionQueue = None
        self._nao = None
        self._settingStiffness = False

        self._cbBehaviors = QtGui.QComboBox()
        self._cbBehaviors.setMinimumWidth(120)
        self._btnRunBhv = QtGui.QPushButton("Run")
        self._btnRunBhv.clicked.connect(self.on_runBehavior_clicked)
        layoutBehavior = QtGui.QHBoxLayout()
        layoutBehavior.setMargin(0)
        layoutBehavior.addWidget(self._cbBehaviors)
        layoutBehavior.addWidget(self._btnRunBhv)

        self._cbMotions = QtGui.QComboBox()
        for i in range(NaoMotionList.length()):
            self._cbMotions.addItem(NaoMotionList.get(i).name())
        #END for
        self._cbMotionSpeed = QtGui.QComboBox()
        self._cbMotionSpeed.addItems(["x" + str(value / 100.0) for value in range(10, 501, 10)])
        self._cbMotionSpeed.setCurrentIndex(9)
        self._btnRunMotion = QtGui.QPushButton("Run")
        self._btnRunMotion.clicked.connect(self.on_runMotion_clicked)

        layoutMotionList = QtGui.QHBoxLayout()
        layoutMotionList.setMargin(0)
        layoutMotionList.addWidget(self._cbMotions)
        layoutMotionList.addWidget(self._cbMotionSpeed)
        layoutMotionList.addWidget(self._btnRunMotion)

        self._cbMotionRepeatCount = QtGui.QComboBox()
        self._cbMotionRepeatCount.addItems([str(value) for value in range(26)])
        self._cbMotionRepeatSpeed = QtGui.QComboBox()
        self._cbMotionRepeatSpeed.addItems(["x" + str(value / 100.0) for value in range(10, 501, 10)])
        self._cbMotionRepeatSpeed.setCurrentIndex(9)
        self._cbMotionRepeatBegin = QtGui.QComboBox()
        self._cbMotionRepeatBegin.addItems([str(value) for value in range(100)])
        self._cbMotionRepeatEnd = QtGui.QComboBox()
        self._cbMotionRepeatEnd.addItems([str(value) for value in range(100)])

        layoutMotionRepeat1 = QtGui.QHBoxLayout()
        layoutMotionRepeat1.setMargin(0)
        layoutMotionRepeat1.addWidget(QtGui.QLabel("Repeat "))
        layoutMotionRepeat1.addWidget(self._cbMotionRepeatCount)
        layoutMotionRepeat1.addWidget(QtGui.QLabel("times "))
        layoutMotionRepeat1.addWidget(self._cbMotionRepeatSpeed)
        layoutMotionRepeat2 = QtGui.QHBoxLayout()
        layoutMotionRepeat2.setMargin(0)
        layoutMotionRepeat2.addWidget(QtGui.QLabel("frame(s) from"))
        layoutMotionRepeat2.addWidget(self._cbMotionRepeatBegin)
        layoutMotionRepeat2.addWidget(QtGui.QLabel(" to"))
        layoutMotionRepeat2.addWidget(self._cbMotionRepeatEnd)

        layoutMotion = QtGui.QVBoxLayout()
        layoutMotion.setMargin(0)
        layoutMotion.addLayout(layoutMotionList)
        layoutMotion.addLayout(layoutMotionRepeat1)
        layoutMotion.addLayout(layoutMotionRepeat2)

        layoutControl = QtGui.QVBoxLayout()
        layoutControl.setMargin(0)
        layoutControl.addLayout(layoutBehavior)
        layoutControl.addLayout(layoutMotion)

        self._lStiffness = QtGui.QLabel("Stiffness")
        self._lStiffness.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self._sldStiffness = QtGui.QSlider(QtCore.Qt.Vertical)
        self._sldStiffness.setPageStep(5)
        self._sldStiffness.setRange(0, 100)
        self._sldStiffness.setSingleStep(1)
        self._sldStiffness.setValue(0)
        self._sldStiffness.valueChanged.connect(self.on_sldStiffness_valueChanged)
        self._lStiffnessValue = QtGui.QLabel(str(self._sldStiffness.value()))
        self._lStiffnessValue.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)

        layoutStiffness = QtGui.QVBoxLayout()
        layoutStiffness.setMargin(0)
        layoutStiffness.addWidget(self._lStiffness, 0, QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layoutStiffness.addWidget(self._sldStiffness, 0, QtCore.Qt.AlignHCenter)
        layoutStiffness.addWidget(self._lStiffnessValue, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)

        layoutMain = QtGui.QHBoxLayout(self)
        layoutMain.addLayout(layoutControl)
        layoutMain.addLayout(layoutStiffness)
    #END __init__()

    stiffnessChanged = QtCore.pyqtSignal(float)

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self.on_nao_connected)
            self._nao.disconnected.disconnect(self.on_nao_disconnected)
            self._nao.stiffnessChanged.disconnect(self.on_nao_stiffnessChanged)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self.on_nao_connected)
            self._nao.disconnected.connect(self.on_nao_disconnected)
            self._nao.stiffnessChanged.connect(self.on_nao_stiffnessChanged)
        #END if
    #END setNao()

    def on_nao_connected(self):
        self._cbBehaviors.addItems(self._nao.getInstalledBehaviors())
        self._cbBehaviors.setCurrentIndex(0)
    #END on_nao_connected()

    def on_nao_disconnected(self):
        self._cbBehaviors.clear()
    #END on_nao_disconnected()

    def on_nao_stiffnessChanged(self, value):
        self._settingStiffness = True
        self._sldStiffness.setValue(value * 100)
        self._settingStiffness = False
    #END on_nao_stiffnessChanged()

    def on_runBehavior_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(Behavior(self._cbBehaviors.currentText(), blocking = False))
        #END if
    #END on_runBehavior_clicked()

    def on_runMotion_clicked(self):
        if self._actionQueue is not None:
            speed = float(self._cbMotionSpeed.currentText()[1:])
            repeatBegin = int(self._cbMotionRepeatBegin.currentText())
            repeatEnd = int(self._cbMotionRepeatEnd.currentText())
            repeatCount = int(self._cbMotionRepeatCount.currentText())
            repeatSpeed = float(self._cbMotionRepeatSpeed.currentText()[1:])
            self._actionQueue.addActions([
                    Stiffness(1.0),
                    Motion(self._cbMotions.currentText(), speed, repeatCount, repeatBegin, repeatEnd, repeatSpeed, blocking = False),
                ])
        #END if
    #END on_runMotion_clicked()

    def on_sldStiffness_valueChanged(self, value):
        self._lStiffnessValue.setText(str(value))
        if not self._settingStiffness:
            self._nao.setStiffness(float(value) / 100)
        #END if
    #END on_sldStiffness_valueChanged()
#END StiffnessWidget
