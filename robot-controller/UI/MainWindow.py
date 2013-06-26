from Definitions import Direction
from PyQt4 import QtCore
from PyQt4 import QtGui
from Action import ActionModel
from Action import Speech
from Nao import Nao
from Study import Study
from AboutWindow import AboutWindow
from ActionListWidget import ActionListWidget
from CameraWidget import CameraWidget
from ConnectDialog import ConnectDialog
from MovementWidget import MovementWidget
from SpeechWidget import SpeechWidget
<<<<<<< HEAD
=======
from TimerWidget import TimerWidget
>>>>>>> 77033acf0220a7e608edc1ce38e8f67c8b19d535


##
# MainWindow.py
#
# Puts all the widgets together in one windows.
##
class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # noinspection PyCallingNonCallable
        self._nao = Nao()
        self._actionQueue = ActionModel(self, self._nao)
        self._LEDTime = QtCore.QTime.currentTime()

        Study.setup()

        #=======================================================================
        # Create Menus
        #=======================================================================
        menubar = self.menuBar()

        actConnect = QtGui.QAction(QtGui.QIcon(), '&Connect', self)
        actConnect.setShortcut('Ctrl+Alt+C')
        actConnect.triggered.connect(self.on_actConnect_triggered)

        actDisconnect = QtGui.QAction(QtGui.QIcon(), '&Disconnect', self)
        actDisconnect.setShortcut('Ctrl+Alt+D')
        actDisconnect.triggered.connect(self.on_actDisconnect_triggered)

        actExit = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        actExit.setShortcut('Ctrl+Alt+X')
        actExit.setStatusTip('Exit application')
        actExit.triggered.connect(self.close)

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(actConnect)
        fileMenu.addAction(actDisconnect)
        fileMenu.addAction(actExit)

        loadMenu = menubar.addMenu('Load')
        self._loadActions = []

        for i in range(len(Study.TASKS)):
            actLoad = QtGui.QAction(QtGui.QIcon(), "Load " + Study.TASKS[i][Study.TASK_NAME], self)
            actLoad.setShortcut("Ctrl+Alt+" + str(i + 1))
            actLoad.triggered.connect(self.on_actLoad_specific)
            loadMenu.addAction(actLoad)
            self._loadActions.append(actLoad)
        # END for

        actAboutBox = QtGui.QAction(QtGui.QIcon(), '&About', self)
        actAboutBox.triggered.connect(self.on_actAbout_triggered)
        actAboutBox.setShortcut("Ctrl+Alt+H")

        aboutMenu = menubar.addMenu('Help')
        aboutMenu.addAction(actAboutBox)

        #=======================================================================
        # Create Widgets
        #=======================================================================
        self._wgtMain = QtGui.QWidget(self)
        splitter = QtGui.QSplitter(self._wgtMain)
        splitter.setOrientation(QtCore.Qt.Horizontal)

        wgtLeft = QtGui.QWidget(splitter)
        wgtLeft.setMinimumWidth(350)

        splitterLeft = QtGui.QSplitter(wgtLeft)
        splitterLeft.setOrientation(QtCore.Qt.Vertical)

        self._wgtTimer = TimerWidget(splitterLeft)

        self._wgtCamera = CameraWidget(splitterLeft, self._nao.getCamera())
        self._wgtCamera.setMinimumHeight(385)
        self._wgtCamera.cameraChanged.connect(self._nao.getCamera().setCameraSource)
        self._wgtCamera.moveHead.connect(self.on__wgtCamera_moveHead)

        self._wgtActionList = ActionListWidget(splitterLeft, self._actionQueue)
        self._wgtActionList.setMinimumHeight(120)
        self._wgtActionList.editClicked.connect(self.on__wgtActionList_editClicked)

        layoutLeft = QtGui.QHBoxLayout(wgtLeft)
        layoutLeft.setMargin(0)
        layoutLeft.addWidget(splitterLeft)

        wgtRight = QtGui.QWidget(splitter)
        wgtRight.setMinimumWidth(380)

        splitterRight = QtGui.QSplitter(wgtRight)
        splitterRight.setOrientation(QtCore.Qt.Vertical)

        self._wgtTaskPanel = QtGui.QWidget(splitterRight)
        self._wgtTaskPanel.setMinimumHeight(400)

        self._layoutTaskPanel = QtGui.QStackedLayout(self._wgtTaskPanel)
        self._layoutTaskPanel.setMargin(0)
        for i in range(len(Study.TASKS)):
            Study.TASKS[i][Study.TASK_WIDGET].setParent(self._wgtTaskPanel)
            Study.TASKS[i][Study.TASK_WIDGET].setActionQueue(self._actionQueue)
            Study.TASKS[i][Study.TASK_WIDGET].setNao(self._nao)
            self._layoutTaskPanel.addWidget(Study.TASKS[i][Study.TASK_WIDGET])
        # END for

        widgetTextStiff = QtGui.QWidget(splitterRight)
        widgetTextStiff.setMinimumHeight(160)

        self._wgtSpeech = SpeechWidget(splitterRight)
        self._wgtSpeech.setInputFocus()
        self._wgtSpeech.inputCancelled.connect(self.setFocus)
        self._wgtSpeech.textSubmitted.connect(self.on__wgtSpeech_playSpeech)
        self._wgtSpeech.volumeChanged.connect(self._nao.setVolume)

        self._wgtMovement = MovementWidget(splitterRight)
        self._wgtMovement.setActionQueue(self._actionQueue)
        self._wgtMovement.setNao(self._nao)

        layoutTextStiff = QtGui.QHBoxLayout(widgetTextStiff)
        layoutTextStiff.setMargin(0)
        layoutTextStiff.addWidget(self._wgtSpeech)
        layoutTextStiff.addWidget(self._wgtMovement)

        layoutRight = QtGui.QHBoxLayout(wgtRight)
        layoutRight.setMargin(0)
        layoutRight.addWidget(splitterRight)

        layoutMain = QtGui.QHBoxLayout(self._wgtMain)
        layoutMain.addWidget(splitter)

        ##################################################
        # MainWindow
        ##################################################
        self.installEventFilter(self)
        self.setCentralWidget(self._wgtMain)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.setWindowTitle('NAO Robotic Controller')
        self.resize(1024, 768)
        self.show()
    # END __init__()

    def on_actConnect_triggered(self):
        if not self._nao.isConnected():
            self._dlgConnect = ConnectDialog(self)
            self._dlgConnect.accepted.connect(self.on__dlgConnect_accepted)
            self._dlgConnect.show()
        # END if
    # END on_actConnect_triggered()

    def on_actDisconnect_triggered(self):
        if self._nao.isConnected():
            self.killTimer(self._timerID)
            print "==================================="
            print "Disconnecting from Nao"
            self._nao.disconnect()
            print "==================================="
            self._wgtCamera.setDefaultImage()
        # END if
    # END on_actDisconnect_triggered()

    # noinspection PyUnusedLocal
    def on_actLoad_specific(self, studyShortName):
        for i in range(len(self._loadActions)):
            if self._loadActions[i] == self.sender():
                self._layoutTaskPanel.setCurrentIndex(i)
                return
            # END if
        # END for
    # END on_actLoad_specific

    def on_actAbout_triggered(self):
        dlgAbout = AboutWindow(self)
        dlgAbout.show()
    # END on_actAbout_triggered()

    def on__dlgConnect_accepted(self):
        if not self._nao.isConnected():
            ipAddress = str(self._dlgConnect.ipAddress)
            port = str(self._dlgConnect.port)
            print "==================================="
            print "Connecting to Nao (" + ipAddress + ":" + port + ")"
            if self._nao.connect(ipAddress, int(port)):
                self._timerID = self.startTimer(50)
            else:
                print "FAILED"
            # END if
            print "==================================="
            self._dlgConnect = None
        # END if
    # END on__dlgConnect_accepted()

    def on__wgtActionList_editClicked(self):
        QtGui.QMessageBox.information(self, "Information", "Not implemented", QtGui.QMessageBox.Ok, QtGui.QMessageBox.NoButton)
    # END on__wgtActionList_editClicked()

    def on__wgtCamera_moveHead(self, direction):
        if self._nao.isConnected():
            if direction == Direction.Up:
                self._nao.tiltHeadUp()
            elif direction == Direction.Down:
                self._nao.tiltHeadDown()
            elif direction == Direction.Left:
                self._nao.turnHeadLeft()
            elif direction == Direction.Right:
                self._nao.turnHeadRight()
            #END if
        #END if
    # END on__wgtCamera_moveHead()

    def on__wgtSpeech_playSpeech(self, value):
        speech = Speech(value, speed = self._wgtSpeech.getSpeed(), shaping = self._wgtSpeech.getShaping(), blocking = False)
        self._actionQueue.addActions(speech)
    # END on__wgtSpeech_playSpeech()

    # noinspection PyUnusedLocal
    def closeEvent(self, event):
        self._actionQueue.dispose()
        self.on_actDisconnect_triggered()
    # END closeEvent()

    # noinspection PyUnusedLocal
    def timerEvent(self, event):
        if self._LEDTime < QtCore.QTime.currentTime():
            if self._wgtSpeech.getText() == "" and (self._actionQueue.rowCount(None) <= 0 or self._actionQueue.isRunning()):
                Study.TASKS[self._layoutTaskPanel.currentIndex()][Study.TASK_WIDGET].LEDNormal()
            else:
                Study.TASKS[self._layoutTaskPanel.currentIndex()][Study.TASK_WIDGET].LEDActive()
            # END if
            self._LEDTime = QtCore.QTime.currentTime().addSecs(1.5)
        # END if
    # END timerEvent()
# END MainWindow
