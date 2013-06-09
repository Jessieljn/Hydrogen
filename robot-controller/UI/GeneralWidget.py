from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import AutoRunAction
from Action import BaseAction
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from ActionPushButton import ActionPushButton
from Nao import NaoMotionList


##
# GeneralWidget.py
#
# Creates the General Widget in the GUI
##
class GeneralWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(GeneralWidget, self).__init__(parent)

        ##################################################
        # General Speech
        ##################################################
        self._speechs = [ \
                ActionPushButton(None, "Hello", Speech("Hello")),
                ActionPushButton(None, "Thanks", Speech("Thank you")),
                ActionPushButton(None, "Sorry", Speech("I'm sorry")),
                ActionPushButton(None, "Good", Speech("Good!")),
                ActionPushButton(None, "Okay", Speech("Okay")),
                ActionPushButton(None, "Yes", Speech("Yes")),
                ActionPushButton(None, "No", Speech("No")),
                ActionPushButton(None, "Hmmm", Speech("Heum,")),
                None,
                ActionPushButton(None, "Louder", Speech("Please speak louder")),
                ActionPushButton(None, "Say again?", Speech("Could you say one more time?")),
                ActionPushButton(None, "Repeat?", Speech("Would you like me to repeat that?")),
                ActionPushButton(None, "Understood?", Speech("Do you understand?")),
                ActionPushButton(None, "Don't Understand", Speech("I don't understand")),
                ActionPushButton(None, "Greeting", Speech("Hello, my name is NAO, nice to meet you")),
                ActionPushButton(None, "End Experiment", Speech("Thank you for participating in our experiment")),
            ]

        self._grpSpeech = QtGui.QGroupBox(self)
        self._grpSpeech.setTitle("General Speech")
        layoutSpeech = QtGui.QVBoxLayout(self._grpSpeech)
        layoutSpeech.setMargin(6)
        layoutSpeech.addSpacing(3)
        widget = QtGui.QWidget(self._grpSpeech)
        layout = QtGui.QHBoxLayout(widget)
        layout.setMargin(0)
        for item in self._speechs:
            if item is None:
                layoutSpeech.addWidget(widget)
                widget = QtGui.QWidget(self._grpSpeech)
                layout = QtGui.QHBoxLayout(widget)
                layout.setMargin(0)
            else:
                item.setParent(widget)
                item.clicked.connect(self.on_runSpeech_clicked)
                layout.addWidget(item)
            #END if
        #END for
        layoutSpeech.addWidget(widget)

        ##################################################
        # General Motions
        ##################################################
        self._grpBehaviors = QtGui.QGroupBox(self)
        self._grpBehaviors.setTitle("Behaviors & Motions")

        wgtBehavior = QtGui.QWidget(self._grpBehaviors)
        self._cbBehaviors = QtGui.QComboBox(wgtBehavior)
        self._cbBehaviors.setMinimumWidth(120)
        self._btnRunBhv = QtGui.QPushButton("Run", wgtBehavior)
        self._btnRunBhv.clicked.connect(self.on_runBehavior_clicked)
        layoutBehavior = QtGui.QHBoxLayout(wgtBehavior)
        layoutBehavior.setMargin(0)
        layoutBehavior.addWidget(self._cbBehaviors)
        layoutBehavior.addWidget(self._btnRunBhv)

        wgtMotion = QtGui.QWidget(self._grpBehaviors)
        self._cbMotions = QtGui.QComboBox(wgtMotion)
        for i in range(NaoMotionList.length()):
            self._cbMotions.addItem(NaoMotionList.get(i).name())
        #END for
        self._cbMotionSpeed = QtGui.QComboBox(wgtMotion)
        self._cbMotionSpeed.addItems(["x" + str(value / 100.0) for value in range(25, 301, 25)])
        self._cbMotionSpeed.setCurrentIndex(3)
        self._btnRunMotion = QtGui.QPushButton("Run", wgtMotion)
        self._btnRunMotion.clicked.connect(self.on_runMotion_clicked)

        layoutMotionList = QtGui.QHBoxLayout()
        layoutMotionList.setMargin(0)
        layoutMotionList.addWidget(self._cbMotions)
        layoutMotionList.addWidget(self._cbMotionSpeed)
        layoutMotionList.addWidget(self._btnRunMotion)

        self._cbMotionRepeatCount = QtGui.QComboBox(wgtMotion)
        self._cbMotionRepeatCount.addItems([str(value) for value in range(25)])
        self._cbMotionRepeatSpeed = QtGui.QComboBox(wgtMotion)
        self._cbMotionRepeatSpeed.addItems(["x" + str(value / 100.0) for value in range(25, 301, 25)])
        self._cbMotionRepeatSpeed.setCurrentIndex(3)
        self._cbMotionRepeatBegin = QtGui.QComboBox(wgtMotion)
        self._cbMotionRepeatBegin.addItems([str(value) for value in range(100)])
        self._cbMotionRepeatEnd = QtGui.QComboBox(wgtMotion)
        self._cbMotionRepeatEnd.addItems([str(value) for value in range(100)])

        layoutMotionRepeat = QtGui.QHBoxLayout()
        layoutMotionRepeat.setMargin(0)
        layoutMotionRepeat.addWidget(QtGui.QLabel("Repeat ", wgtMotion))
        layoutMotionRepeat.addWidget(self._cbMotionRepeatCount)
        layoutMotionRepeat.addWidget(QtGui.QLabel("times ", wgtMotion))
        layoutMotionRepeat.addWidget(self._cbMotionRepeatSpeed)
        layoutMotionRepeat.addWidget(QtGui.QLabel("key frame(s) from", wgtMotion))
        layoutMotionRepeat.addWidget(self._cbMotionRepeatBegin)
        layoutMotionRepeat.addWidget(QtGui.QLabel(" to", wgtMotion))
        layoutMotionRepeat.addWidget(self._cbMotionRepeatEnd)

        layoutMotion = QtGui.QVBoxLayout(wgtMotion)
        layoutMotion.setMargin(0)
        layoutMotion.addLayout(layoutMotionList)
        layoutMotion.addLayout(layoutMotionRepeat)

        layoutBehavior = QtGui.QHBoxLayout(self._grpBehaviors)
        layoutBehavior.setMargin(6)
        layoutBehavior.addSpacing(10)
        layoutBehavior.addWidget(wgtBehavior, 0, QtCore.Qt.AlignCenter)
        layoutBehavior.addWidget(wgtMotion, 0, QtCore.Qt.AlignCenter)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._grpSpeech)
        layoutMain.addWidget(self._grpBehaviors)
    #END __init__()

    playAction = QtCore.pyqtSignal(BaseAction)

    def init_behaviorList(self, nao):
        self._cbBehaviors.clear()
        self._cbBehaviors.addItems(nao.getInstalledBehaviors())
        self._cbBehaviors.setCurrentIndex(0)
    #END init_behaviorList()

    def on_runBehavior_clicked(self):
        self.playAction.emit(Stiffness(1.0))
        self.playAction.emit(Behavior(self._cbBehaviors.currentText(), blocking = False))
        self.playAction.emit(AutoRunAction())
    #END on_runBehavior_clicked()

    def on_runMotion_clicked(self):
        speed = float(self._cbMotionSpeed.currentText()[1:])
        repeatBegin = int(self._cbMotionRepeatBegin.currentText())
        repeatEnd = int(self._cbMotionRepeatEnd.currentText())
        repeatCount = int(self._cbMotionRepeatCount.currentText())
        repeatSpeed = float(self._cbMotionRepeatSpeed.currentText()[1:])
        self.playAction.emit(Stiffness(1.0))
        self.playAction.emit(Motion(self._cbMotions.currentText(), speed, repeatCount, repeatBegin, repeatEnd, repeatSpeed, blocking = False))
        self.playAction.emit(AutoRunAction())
    #END on_runMotion_clicked()

    def on_runSpeech_clicked(self):
        for action in self.sender().getRobotActions():
            self.playAction.emit(action)
        #END for
        self.playAction.emit(AutoRunAction())
    #END on_runSpeech_clicked()
#END GeneralWidget
