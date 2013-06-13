from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import Behavior
from Action import Motion
from Action import Speech
from Action import Stiffness
from Nao import NaoMotionList
from UI.ActionPushButton import ActionPushButton


class BaseStudy(QtGui.QWidget):
    def __init__(self):
        super(BaseStudy, self).__init__()
        self._actionQueue = None
        self._nao = None
        self._widgets = None
        self._buttons = None
        self._cbBehaviors = None
    #END __init__()

    def _setupUi(self, general_panel = True, custom_widget = None):
        wgtGeneral = None
        if general_panel:
            wgtGeneral = QtGui.QWidget()
            wgtGeneral.setMinimumHeight(180)

            ##################################################
            # General Speech
            ##################################################
            self._speechs = [
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
                ActionPushButton(None, "Say again?", Speech("Can you say one more time?")),
                ActionPushButton(None, "Repeat?", Speech("Would you like me to repeat that?")),
                ActionPushButton(None, "Understood?", Speech("Do you understand?")),
                ActionPushButton(None, "Don't Understand", Speech("I don't understand")),
                ActionPushButton(None, "Greeting", Speech("Hello, my name is NAO, nice to meet you")),
                ActionPushButton(None, "End Experiment", Speech("Thank you for participating in our experiment")),
            ]

            self._grpSpeech = QtGui.QGroupBox(wgtGeneral)
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
            self._grpBehaviors = QtGui.QGroupBox(wgtGeneral)
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
            self._cbMotionSpeed.addItems(["x" + str(value / 100.0) for value in range(10, 501, 10)])
            self._cbMotionSpeed.setCurrentIndex(9)
            self._btnRunMotion = QtGui.QPushButton("Run", wgtMotion)
            self._btnRunMotion.clicked.connect(self.on_runMotion_clicked)

            layoutMotionList = QtGui.QHBoxLayout()
            layoutMotionList.setMargin(0)
            layoutMotionList.addWidget(self._cbMotions)
            layoutMotionList.addWidget(self._cbMotionSpeed)
            layoutMotionList.addWidget(self._btnRunMotion)

            self._cbMotionRepeatCount = QtGui.QComboBox(wgtMotion)
            self._cbMotionRepeatCount.addItems([str(value) for value in range(26)])
            self._cbMotionRepeatSpeed = QtGui.QComboBox(wgtMotion)
            self._cbMotionRepeatSpeed.addItems(["x" + str(value / 100.0) for value in range(10, 501, 10)])
            self._cbMotionRepeatSpeed.setCurrentIndex(9)
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

            layoutMain = QtGui.QVBoxLayout(wgtGeneral)
            layoutMain.setMargin(0)
            layoutMain.addWidget(self._grpSpeech)
            layoutMain.addWidget(self._grpBehaviors)
        #END if

        wgtButtons = None
        if self._widgets is not None and self._buttons is not None:
            wgtButtons = QtGui.QWidget()
            layout = QtGui.QHBoxLayout(wgtButtons)
            layout.setMargin(0)
            for i in range(len(self._widgets)):
                layoutButtons = QtGui.QVBoxLayout(self._widgets[i])
                layoutButtons.setMargin(0)
                for button in self._buttons[i]:
                    if isinstance(button, ActionPushButton):
                        button.clicked.connect(self.on_button_clicked)
                    #END if
                    layoutButtons.addWidget(button)
                #END for
                scroll = QtGui.QScrollArea()
                scroll.setAlignment(QtCore.Qt.AlignCenter)
                scroll.setWidget(self._widgets[i])
                layoutScroll = QtGui.QHBoxLayout()
                layoutScroll.setMargin(0)
                layoutScroll.addWidget(scroll)
                layout.addLayout(layoutScroll)
            #END for
        #END if

        if wgtGeneral is not None or wgtButtons is not None or custom_widget is not None:
            splitter = QtGui.QSplitter(self)
            splitter.setOrientation(QtCore.Qt.Vertical)
            layout = QtGui.QHBoxLayout(self)
            layout.setMargin(0)
            layout.addWidget(splitter)
            if wgtGeneral is not None:
                wgtGeneral.setParent(splitter)
            #END if
            if wgtButtons is not None:
                wgtButtons.setParent(splitter)
            #END if
            if custom_widget is not None:
                custom_widget.setParent(splitter)
            #END if
        #END if
    #END _setupUi()

    def LEDActive(self):
        if self._nao is not None:
            self._nao.LEDrandomEyes(1.0, True)
        #END if
    #END LEDActive()

    def LEDNormal(self):
        if self._nao is not None:
            self._nao.LEDNormal()
        #END if
    #END LEDNormal()

    def setActionQueue(self, actionQueue):
        self._actionQueue = actionQueue
    #END setActionQueue()

    def setNao(self, nao):
        if self._nao is not None:
            self._nao.connected.disconnect(self.on_nao_connected)
            self._nao.disconnected.disconnect(self.on_nao_disconnected)
        #END if
        self._nao = nao
        if self._nao is not None:
            self._nao.connected.connect(self.on_nao_connected)
            self._nao.disconnected.connect(self.on_nao_disconnected)
        #END if
    #END setNao()

    def on_button_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_button_clicked()

    def on_nao_connected(self):
        if self._cbBehaviors is not None:
            self._cbBehaviors.addItems(self._nao.getInstalledBehaviors())
            self._cbBehaviors.setCurrentIndex(0)
        #END if
    #END on_nao_connected()

    def on_nao_disconnected(self):
        if self._cbBehaviors is not None:
            self._cbBehaviors.clear()
        #END if
    #END on_nao_disconnected()

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

    def on_runSpeech_clicked(self):
        if self._actionQueue is not None:
            self._actionQueue.addActions(self.sender().getRobotActions())
        #END if
    #END on_runSpeech_clicked()
#END BaseStudy
