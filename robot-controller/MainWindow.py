from Definitions import Direction
from PyQt4 import QtCore, QtGui
from Nao import Nao
from Action.ActionModel import ActionModel
from Action.Behavior import Behavior
from Action.HeadMotion import HeadMotion
from Action.Speech import Speech
from Study.General import General
from Study.Tedium import Tedium
from Study.MentalChallenge import MentalChallenge
from Study.Empathy import Empathy
from UI.AboutWindow import AboutWindow
from UI.ActionListWidget import ActionListWidget
from UI.CameraWidget import CameraWidget
from UI.ConnectDialog import ConnectDialog
from UI.GeneralWidget import GeneralWidget
from UI.SpeechWidget import SpeechWidget
from UI.StiffnessWidget import StiffnessWidget


##
# MainWindow.py
#
# Puts all the widgets together in one windows.
##
class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        ##################################################
        # Create Widgets
        ##################################################
        self._wgtMain = QtGui.QWidget(self)

        self._wgtCamera = CameraWidget(self._wgtMain)
        self._wgtCamera.setFixedHeight(385)
        self._wgtCamera.cameraChanged.connect(self.on_cameraChanged)
        self._wgtCamera.moveHead.connect(self.on_moveHead)

        self._actionQueue = ActionModel(self)
        self._actionQueue.dequeue.connect(self.on__actionQueue_execute)
        self._actionQueue.startProcessing()
        self._wgtActionList = ActionListWidget(self._wgtMain, self._actionQueue)
        self._wgtActionList.setFixedWidth(328)

        self._wgtSpeech = SpeechWidget(self._wgtMain)
        self._wgtSpeech.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        self._wgtSpeech.textEditing.connect(self.on_chagingLEDs)
        self._wgtSpeech.textInputCancelled.connect(self.grab_keyboard)
        self._wgtSpeech.textSubmitted.connect(self.on_playSpeech)
        self._wgtSpeech.volumeChanged.connect(self.on_chagingVolume)

        self._wgtStiffness = StiffnessWidget(self._wgtMain)
        self._wgtStiffness.stiffnessChanged.connect(self.on_changingStiffness)

        self._wgtGeneral = GeneralWidget(self._wgtMain)
        self._wgtGeneral.playBehavior.connect(self.on_playBehaviour)
        self._wgtGeneral.speechSynthesis.connect(self.on_playSpeech)

        self._wgtTaskPanel = QtGui.QFrame(self._wgtMain)
        self._wgtTaskPanel.setFrameShape(QtGui.QFrame.Panel)
        self._wgtTaskPanel.setFrameShadow(QtGui.QFrame.Plain)
        self._wgtTaskPanel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        layoutTaskPanel = QtGui.QHBoxLayout(self._wgtTaskPanel)

        layoutLeft = QtGui.QVBoxLayout()
        layoutLeft.addWidget(self._wgtCamera, 2)
        layoutLeft.addWidget(self._wgtActionList, 1)

        layoutTextStiff = QtGui.QHBoxLayout()
        layoutTextStiff.addWidget(self._wgtSpeech, 5)
        layoutTextStiff.addWidget(self._wgtStiffness, 1)

        layoutRight = QtGui.QVBoxLayout()
        layoutRight.addLayout(layoutTextStiff)
        layoutRight.addWidget(self._wgtGeneral)
        layoutRight.addWidget(self._wgtTaskPanel)

        layoutMain = QtGui.QHBoxLayout(self._wgtMain)
        layoutMain.addLayout(layoutLeft)
        layoutMain.addLayout(layoutRight)

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

        actExit = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        actExit.setShortcut('Ctrl+X')
        actExit.setStatusTip('Exit application')
        actExit.triggered.connect(QtGui.qApp.quit)

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(actConnect)
        fileMenu.addAction(actDisconnect)
        fileMenu.addAction(actExit)

        actLoadGeneral = QtGui.QAction(QtGui.QIcon(), 'Load General', self)
        actLoadGeneral.setShortcut('Ctrl+1')
        actLoadGeneral.triggered.connect(lambda: self.on_actLoad_specific("General"))
        self._taskGeneral = General(self._wgtTaskPanel, self._actionQueue)
        self._task = self._taskGeneral
        layoutRight.addWidget(self._taskGeneral)

        actLoadTedium = QtGui.QAction(QtGui.QIcon(), 'Load Tedium', self)
        actLoadTedium.setShortcut('Ctrl+2')
        actLoadTedium.triggered.connect(lambda: self.on_actLoad_specific("Tedium"))
        self._taskTedium = Tedium(self._wgtTaskPanel, self._actionQueue)
        self._taskTedium.hide()
        layoutRight.addWidget(self._taskTedium)

        actLoadChallenge = QtGui.QAction(QtGui.QIcon(), 'Load Mental Challenge', self)
        actLoadChallenge.setShortcut('Ctrl+3')
        actLoadChallenge.triggered.connect(lambda: self.on_actLoad_specific("Challenge"))
        self._taskChallenge = MentalChallenge(self._wgtTaskPanel, self._actionQueue)
        self._taskChallenge.hide()
        layoutRight.addWidget(self._taskChallenge)

        actLoadEmpathy = QtGui.QAction(QtGui.QIcon(), 'Load Empathy', self)
        actLoadEmpathy.setShortcut('Ctrl+4')
        actLoadEmpathy.triggered.connect(lambda: self.on_actLoad_specific("Empathy"))
        self._taskEmpathy = Empathy(self._wgtTaskPanel, self._actionQueue)
        self._taskEmpathy.hide()
        layoutRight.addWidget(self._taskEmpathy)

        loadMenu = menubar.addMenu('Load')
        loadMenu.addAction(actLoadGeneral)
        loadMenu.addAction(actLoadTedium)
        loadMenu.addAction(actLoadChallenge)
        loadMenu.addAction(actLoadEmpathy)

        actAboutBox = QtGui.QAction(QtGui.QIcon(), '&About', self)
        actAboutBox.triggered.connect(self.on_actAbout_triggered)

        aboutMenu = menubar.addMenu('Help')
        aboutMenu.addAction(actAboutBox)

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

        self._keys = dict()
        self._keys[Direction.Up] = False
        self._keys[Direction.Down] = False
        self._keys[Direction.Left] = False
        self._keys[Direction.Right] = False
        self._nao = Nao()
        self._nao.frameAvailable.connect(self._wgtCamera.setImage)
    #END __init__()


    def on__actionQueue_execute(self, action):
        if self._nao.isConnected():
            action.execute(self._nao)
        #END if
    #END on__actionQueue_execute()


    def on_cameraChanged(self, which):
        self._nao.cameraSource = which
    #END on_cameraChanged()


    def on_chagingLEDs(self):
        if self._wgtSpeech.isSpeechTextEmpty():
            self._nao.setLEDsNormal()
        else:
            self._nao.setLEDsProcessing()
        #END if
    #END on_chagingLEDs()


    def on_changingStiffness(self, value):
        self._nao.setStiffness(value)
    #END on_changingStiffness()


    def on_chagingVolume(self, value):
        self._nao.setVolume(value)
    #END on_chagingVolume()


    def on_moveHead(self, direction):
        self._actionQueue.enqueue(HeadMotion(direction))
    #END on_moveHead()


    def on_playBehaviour(self, value):
        self._actionQueue.enqueue(Behavior(value))
    #END on_playSpeech()


    def on_playSpeech(self, value):
        self._actionQueue.enqueue(Speech(value))
    #END on_playSpeech()


    def on_actConnect_triggered(self):
        if not self._nao.isConnected():
            self._dlgConnect = ConnectDialog(self)
            self._dlgConnect.accepted.connect(self.on_dlgConnect_accepted)
            self._dlgConnect.show()
        #END if
    #END on_actConnect_triggered()


    def on_actDisconnect_triggered(self):
        if self._nao.isConnected():
            self.killTimer(self._timerID)
            print "==================================="
            print "Disconnecting from Nao"
            self._nao.disconnect()
            print "==================================="
        #END if
    #END on_actDisconnect_triggered()


    def on_actLoad_specific(self, study):
        self._task.hide()
        if study == "General":
            self._task = self._taskGeneral
        elif study == "Tedium":
            self._task = self._taskTedium
        elif study == "Challenge":
            self._task = self._taskChallenge
        elif study == "Empathy":
            self._task = self._taskEmpathy
        #END if
        self._task.show()
    #END on_actLoad_specific


    def on_actAbout_triggered(self):
        dlgAbout = AboutWindow(self)
        dlgAbout.show()
    #END on_actAbout_triggered()


    def on_dlgConnect_accepted(self):
        if not self._nao.isConnected():
            ipAddress = str(self._dlgConnect.ipAddress)
            port = str(self._dlgConnect.port)
            print "==================================="
            print "Connecting to Nao (" + ipAddress + ":" + port + ")"
            if self._nao.connect(ipAddress, int(port)):
                self._nao.startCamera()
                self._timerID = self.startTimer(1000 / 100)
            else:
                print "FAILED"
            #END if
            print "==================================="
        #END if
    #END on_dlgConnect_accepted()


    def closeEvent(self, event):
        self._actionQueue.stopProcessing()
        self.on_actDisconnect_triggered()
    #END closeEvent()


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self._keys[Direction.Up] = True;
        elif event.key() == QtCore.Qt.Key_Down:
            self._keys[Direction.Down] = True;
        elif event.key() == QtCore.Qt.Key_Left:
            self._keys[Direction.Left] = True;
        elif event.key() == QtCore.Qt.Key_Right:
            self._keys[Direction.Right] = True;
        elif event.key() == QtCore.Qt.Key_Escape:
            self.releaseKeyboard()
            self._wgtSpeech.setTextEditFocus()
        else:
            super(MainWindow, self).keyPressEvent(event)
        #END if
    #END keyPressEvent()


    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self._keys[Direction.Up] = False;
        elif event.key() == QtCore.Qt.Key_Down:
            self._keys[Direction.Down] = False;
        elif event.key() == QtCore.Qt.Key_Left:
            self._keys[Direction.Left] = False;
        elif event.key() == QtCore.Qt.Key_Right:
            self._keys[Direction.Right] = False;
        else:
            super(MainWindow, self).keyReleaseEvent(event)
        #END if
    #END keyReleaseEvent()


    def timerEvent(self, event):
        if self._keys[Direction.Up]:
            self._actionQueue.enqueue(HeadMotion(Direction.Up))
        #END if
        if self._keys[Direction.Down]:
            self._actionQueue.enqueue(HeadMotion(Direction.Down))
        #END if
        if self._keys[Direction.Left]:
            self._actionQueue.enqueue(HeadMotion(Direction.Left))
        #END if
        if self._keys[Direction.Right]:
            self._actionQueue.enqueue(HeadMotion(Direction.Right))
        #END if
    #END timerEvent()


    def focusInEvent(self, event):
        self.grabKeyboard()
    #END focusInEvent()


    def grab_keyboard(self):
        self.setFocus(QtCore.Qt.OtherFocusReason)
    #END grab_keyboard()


#END MainWindow
