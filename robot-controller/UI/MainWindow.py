from Definitions import Direction
from PyQt4 import QtCore
from PyQt4 import QtGui
from Nao import Nao
from Action import ActionModel
from Action import Speech
from Study import Study
from AboutWindow import AboutWindow
from ActionListWidget import ActionListWidget
from CameraWidget import CameraWidget
from ConnectDialog import ConnectDialog
from GeneralWidget import GeneralWidget
from SpeechWidget import SpeechWidget
from StiffnessWidget import StiffnessWidget


##
# MainWindow.py
#
# Puts all the widgets together in one windows.
##
class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._nao = Nao()
        self._actionQueue = ActionModel(self, self._nao)
        self._blinkLEDTime = QtCore.QTime.currentTime()
        self._keys = dict()
        self._keys[Direction.Up] = False
        self._keys[Direction.Down] = False
        self._keys[Direction.Left] = False
        self._keys[Direction.Right] = False

        Study.setup()

        ##################################################
        # Create Menus
        ##################################################
        menubar = self.menuBar()

        actConnect = QtGui.QAction(QtGui.QIcon(), '&Connect', self)
        actConnect.setShortcut('Ctrl+C')
        actConnect.triggered.connect(self.on_actConnect_triggered)

        actDisconnect = QtGui.QAction(QtGui.QIcon(), '&Disconnect', self)
        actDisconnect.setShortcut('Ctrl+D')
        actDisconnect.triggered.connect(self.on_actDisconnect_triggered)

        actExit = QtGui.QAction(QtGui.QIcon('images/exit.png'), 'E&xit', self)
        actExit.setShortcut('Ctrl+X')
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
            actLoad.setShortcut("Ctrl+" + str(i + 1))
            actLoad.triggered.connect(self.on_actLoad_specific)
            loadMenu.addAction(actLoad)
            self._loadActions.append(actLoad)
        # END for

        actAboutBox = QtGui.QAction(QtGui.QIcon(), '&About', self)
        actAboutBox.triggered.connect(self.on_actAbout_triggered)

        aboutMenu = menubar.addMenu('Help')
        aboutMenu.addAction(actAboutBox)

        ##################################################
        # Create Widgets
        ##################################################
        self._wgtMain = QtGui.QWidget(self)
        splitter = QtGui.QSplitter(self._wgtMain)
        splitter.setOrientation(QtCore.Qt.Horizontal);

        wgtLeft = QtGui.QWidget(splitter)
        wgtLeft.setMinimumWidth(350)
        splitterLeft = QtGui.QSplitter(wgtLeft)
        splitterLeft.setOrientation(QtCore.Qt.Vertical);
        layoutLeft = QtGui.QHBoxLayout(wgtLeft)
        layoutLeft.setMargin(0)
        layoutLeft.addWidget(splitterLeft)

        self._wgtCamera = CameraWidget(splitterLeft, self._nao.getCamera())
        self._wgtCamera.setMinimumHeight(385)
        self._wgtCamera.cameraChanged.connect(self._nao.setCameraSource)
        self._wgtCamera.moveHead.connect(self.on_moveHead)

        self._wgtActionList = ActionListWidget(splitterLeft, self._actionQueue)
        self._wgtActionList.setMinimumHeight(120)
        self._wgtActionList.clearClicked.connect(self._actionQueue.clearActions)

        wgtRight = QtGui.QWidget(splitter)
        wgtRight.setMinimumWidth(380)

        self._wgtSpeech = SpeechWidget(wgtRight)
        self._wgtSpeech.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        self._wgtSpeech.textEditing.connect(self.on_changingLEDs)
        self._wgtSpeech.textInputCancelled.connect(self.grab_keyboard)
        self._wgtSpeech.textSubmitted.connect(self.on_playSpeech)
        self._wgtSpeech.volumeChanged.connect(self._nao.setVolume)
        layoutSpeech = QtGui.QHBoxLayout()
        layoutSpeech.setMargin(0)
        layoutSpeech.addWidget(self._wgtSpeech)

        self._wgtStiffness = StiffnessWidget(wgtRight)
        self._wgtStiffness.stiffnessChanged.connect(self._nao.setStiffness)

        layoutTextStiff = QtGui.QHBoxLayout()
        layoutTextStiff.addLayout(layoutSpeech)
        layoutTextStiff.addWidget(self._wgtStiffness)

        self._wgtGeneral = GeneralWidget(wgtRight)
        self._wgtGeneral.playAction.connect(self._actionQueue.addActions)

        self._wgtTaskPanel = QtGui.QFrame(wgtRight)
        self._wgtTaskPanel.setFrameShape(QtGui.QFrame.Panel)
        self._wgtTaskPanel.setFrameShadow(QtGui.QFrame.Plain)
        self._wgtTaskPanel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self._layoutTaskPanel = QtGui.QStackedLayout(self._wgtTaskPanel)
        self._layoutTaskPanel.setMargin(0)

        for i in range(len(Study.TASKS)):
            Study.TASKS[i][Study.TASK_WIDGET].setParent(self._wgtTaskPanel)
            Study.TASKS[i][Study.TASK_WIDGET].setActionQueue(self._actionQueue)
            self._layoutTaskPanel.addWidget(Study.TASKS[i][Study.TASK_WIDGET])
        # END for

        self._layoutTaskPanel.setCurrentIndex(0)

        layoutRight = QtGui.QVBoxLayout(wgtRight)
        layoutRight.setMargin(0)
        layoutRight.addLayout(layoutTextStiff)
        layoutRight.addWidget(self._wgtGeneral)
        layoutRight.addWidget(self._wgtTaskPanel)

        layoutMain = QtGui.QHBoxLayout(self._wgtMain)
        layoutMain.addWidget(splitter)

        ##################################################
        # MainWindow
        ##################################################
        self.setCentralWidget(self._wgtMain)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.setWindowTitle('NAO Robotic Controller')
        self.resize(800, 600)
        self.show()
        self.grabKeyboard()
    # END __init__()

    def on_changingLEDs(self):
        if self._nao.isConnected():
            if self._wgtSpeech.isSpeechTextEmpty():
                self._nao.LEDNormal()
            else:
                if self._blinkLEDTime < QtCore.QTime.currentTime():
                    self._nao.postLEDrandomEyes(1)
                    self._blinkLEDTime = QtCore.QTime.currentTime().addSecs(1)
                # END if
            # END if
        # END if
    # END on_changingLEDs()

    def on_moveHead(self, direction):
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
    # END on_moveHead()

    def on_playSpeech(self, value):
        print Speech(value, blocking = False).paramToString()
        self._actionQueue.addActions(Speech(value, blocking = False))
    # END on_playSpeech()

    def on_actConnect_triggered(self):
        if not self._nao.isConnected():
            self._dlgConnect = ConnectDialog(self)
            self._dlgConnect.accepted.connect(self.on_dlgConnect_accepted)
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

    def on_dlgConnect_accepted(self):
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
        # END if
    # END on_dlgConnect_accepted()

    def closeEvent(self, event):
        self.on_actDisconnect_triggered()
        self._actionQueue.dispose()
    # END closeEvent()

    def focusInEvent(self, event):
        self.grabKeyboard()
    # END focusInEvent()

    def grab_keyboard(self):
        self.setFocus(QtCore.Qt.OtherFocusReason)
    # END grab_keyboard()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self._keys[Direction.Up] = True
        elif event.key() == QtCore.Qt.Key_Down:
            self._keys[Direction.Down] = True
        elif event.key() == QtCore.Qt.Key_Left:
            self._keys[Direction.Left] = True
        elif event.key() == QtCore.Qt.Key_Right:
            self._keys[Direction.Right] = True
        elif event.key() == QtCore.Qt.Key_Escape:
            self.releaseKeyboard()
            self._wgtSpeech.setTextEditFocus()
        else:
            super(MainWindow, self).keyPressEvent(event)
        # END if
    # END keyPressEvent()

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self._keys[Direction.Up] = False
        elif event.key() == QtCore.Qt.Key_Down:
            self._keys[Direction.Down] = False
        elif event.key() == QtCore.Qt.Key_Left:
            self._keys[Direction.Left] = False
        elif event.key() == QtCore.Qt.Key_Right:
            self._keys[Direction.Right] = False
        else:
            super(MainWindow, self).keyReleaseEvent(event)
        # END if
    # END keyReleaseEvent()

    def timerEvent(self, event):
        if self._keys[Direction.Up]:
            self._nao.tiltHeadUp()
        #END if
        if self._keys[Direction.Down]:
            self._nao.tiltHeadDown()
        #END if
        if self._keys[Direction.Left]:
            self._nao.turnHeadLeft()
        #END if
        if self._keys[Direction.Right]:
            self._nao.turnHeadRight()
        #END if
    # END timerEvent()
# END MainWindow
