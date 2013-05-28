from PyQt4 import QtGui, QtNetwork, QtCore
from TaskTabs import TaskTabs
from TextWidClass import TextWid
from GestureWidget import GestureWidget
from CameraWidget import CameraWidget
from GeneralWidget import GeneralWidget
from StiffnessWidget import StiffnessWidget
from PopupWindow import Popup
import Nao
from About import AboutWindow
##
# MainWindow.py
#
# Puts all the widgets together in one windows.
##

KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowIcon(QtGui.QIcon("images/icon.png"))
        self.init()
    #END __init__()

    def init(self):

        self.keys = dict()
        self.keys[KEY_UP] = False
        self.keys[KEY_DOWN] = False
        self.keys[KEY_LEFT] = False
        self.keys[KEY_RIGHT] = False

        self.setWindowTitle('NAO Robotic Controller')

        # Creates a socket.
        self.socket = QtNetwork.QTcpSocket(self)
        mainWidget = QtGui.QWidget(self)

        # Creates a camera widget.
        self.cameraWidget = CameraWidget(mainWidget)
        self.nao = Nao.Nao(self.cameraWidget)
        self.generalWidget = GeneralWidget(self.nao, mainWidget)
        self.stiffnessWidget = StiffnessWidget(self.nao, mainWidget)
        self.cameraWidget.setNao(self.nao)

        # Create the text widget.
        self.textWid = TextWid(self.nao, mainWidget)
        self.textWid.msg_sent.connect(self.grab_keyboard)

        # Creates the gesture widget.
        self.gestureWidget = GestureWidget(self.nao, mainWidget)

        # Create a tabbed task bar.
        self.taskTabs = TaskTabs(self.nao, mainWidget)

        # Create a popup window
        self.popup = Popup()

        # Create the about popup window
        self.about = AboutWindow()

        # Create the connect button.
        self.connectButton = QtGui.QPushButton('Connect', self)
        self.naoIP = QtGui.QLineEdit(Nao.DEFAULT_IP)
        self.naoIP.setMaximumWidth(100)
        self.naoPort = QtGui.QLineEdit(str(Nao.DEFAULT_PORT))
        self.naoPort.setMaximumWidth(60)

        # ActionEvent for button.
        self.connectButton.clicked.connect(self.connectToNao)

        # Widget layout.
        self.resize(1000, 700)

        # Create layouts.
        mainLayout = QtGui.QHBoxLayout()
        hbox = QtGui.QHBoxLayout()   # Main Box for layout
        hbox3 = QtGui.QHBoxLayout()  # Text and Stiffness Widgets

        vbox = QtGui.QVBoxLayout()
        vbox1 = QtGui.QVBoxLayout()  # General and Gesture Widgets
        vbox2 = QtGui.QVBoxLayout()  # Task Tabs

        # Add camera widget to the main layout.
        mainLayout.addWidget(self.cameraWidget)
        mainLayout.addLayout(vbox)
        mainWidget.setLayout(mainLayout)

        # Add general and gesture widgets to horizontal box 2.
        vbox1.addWidget(self.generalWidget)
        vbox1.addWidget(self.gestureWidget)

        # Add text and stiffness widgets to horizontal box 3.
        hbox3.addWidget(self.textWid, 5)
        hbox3.addWidget(self.stiffnessWidget, 1)

        # Add elements to layout.
        vbox.addLayout(hbox3)
        vbox.addLayout(vbox1)
        vbox2.addWidget(self.taskTabs)
        hbox.addLayout(vbox2)

        # Set layout.
        vbox.addLayout(hbox)  # Right side of the UI

        # Add connection widget to the layout.
        naoConnectionLayout = QtGui.QHBoxLayout()
        naoConnectionLayout.addWidget(self.connectButton, 0, QtCore.Qt.AlignLeft)
        naoConnectionLayout.addWidget(self.naoIP, 0, QtCore.Qt.AlignLeft)
        naoConnectionLayout.addWidget(self.naoPort, 0, QtCore.Qt.AlignLeft)
        vbox.addLayout(naoConnectionLayout)

        ###################################################
        # TODO: Add on click connect for connection window.
        ###################################################
        menubar = self.menuBar()

        """
        File Menubar
        """
        connect = QtGui.QAction(QtGui.QIcon(), '&Connect', self)
        connect.setShortcut('Ctrl+C')
        connect.triggered.connect(self.popup.doit)

        disconnect = QtGui.QAction(QtGui.QIcon(), '&Disconnect', self)
        disconnect.setShortcut('Ctrl+D')
        disconnect.triggered.connect(self.nao.disconnect)

        exitAction = QtGui.QAction(QtGui.QIcon('images/exit.png'), '&Exit', self)
        exitAction.setShortcut('Esc')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        """
        Load Menubar
        """

        loadGeneral = QtGui.QAction(QtGui.QIcon(), '&Load General', self)
        loadGeneral.setShortcut('Ctrl+1')
        loadGeneral.triggered.connect(lambda: self.taskTabs.remove('General'))

        loadTedium = QtGui.QAction(QtGui.QIcon(), '&Load Tedium', self)
        loadTedium.setShortcut('Ctrl+2')
        loadTedium.triggered.connect(lambda: self.taskTabs.remove("Tedium"))

        loadChallenge = QtGui.QAction(QtGui.QIcon(), '&Load Mental Challenge', self)
        loadChallenge.setShortcut('Ctrl+3')
        loadChallenge.triggered.connect(lambda: self.taskTabs.remove("Challenge"))

        loadEmpathy = QtGui.QAction(QtGui.QIcon(), '&Load Empathy', self)
        loadEmpathy.setShortcut('Ctrl+4')
        loadEmpathy.triggered.connect(lambda: self.taskTabs.remove("Empathy"))

        """
        About
        """

        aboutBox = QtGui.QAction(QtGui.QIcon(), '&About', self)
        aboutBox.triggered.connect(self.about.doit)

        ##########
        # Toolbar instead of menubar
        ##########
        #self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(exitAction)
        #  self.setWindowTitle('Toolbar')
        ##########

        fileMenu = menubar.addMenu('File')
        loadMenu = menubar.addMenu('Load')
        aboutMenu = menubar.addMenu('Help')
        fileMenu.addAction(connect)
        fileMenu.addAction(disconnect)
        loadMenu.addAction(loadGeneral)
        loadMenu.addAction(loadTedium)
        loadMenu.addAction(loadChallenge)
        loadMenu.addAction(loadEmpathy)
        aboutMenu.addAction(aboutBox)
        fileMenu.addAction(exitAction)
        ##################################################

        self.setCentralWidget(mainWidget)
        self.show()
        self.grabKeyboard()
    #END init()

    def connectToNao(self):
        if self.connectButton.text() == 'Connect':
            print "==================================="
            print "Connecting to Nao (" + str(self.naoIP.text()) + ":" + str(self.naoPort.text()) + ")"
            if self.nao.connect(str(self.naoIP.text()), int(str(self.naoPort.text()))):
                self.nao.startCamera()
                self.connectButton.setText('Disconnect')
            #END if
            else:
                print "FAILED"
            #END else
            print "==================================="
        #END if
        elif self.connectButton.text() == 'Disconnect':
            self.nao.disconnect()
            self.connectButton.setText('Connect')
        #END elif
    #END connectToNao()

    def closeEvent(self, event):
        if self.nao.isConnected():
            self.nao.disconnect()
        #END if
    #END closeEvent()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.keys[KEY_UP] = True
        #END if
        if event.key() == QtCore.Qt.Key_Down:
            self.keys[KEY_DOWN] = True
        #END if
        if event.key() == QtCore.Qt.Key_Left:
            self.keys[KEY_LEFT] = True
        #END if
        if event.key() == QtCore.Qt.Key_Right:
            self.keys[KEY_RIGHT] = True
        #END if

        print "key"
        if event.key() == QtCore.Qt.Key_Escape:
            print "tab"
            self.releaseKeyboard()
            self.textWid.message.setFocus(QtCore.Qt.OtherFocusReason)
            self.textWid.message.grabKeyboard()
        #END if
    #END keyPressEvent()

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.keys[KEY_UP] = False
        #END if
        if event.key() == QtCore.Qt.Key_Down:
            self.keys[KEY_DOWN] = False
        #END if
        if event.key() == QtCore.Qt.Key_Left:
            self.keys[KEY_LEFT] = False
        #END if
        if event.key() == QtCore.Qt.Key_Right:
            self.keys[KEY_RIGHT] = False
        #END if
    #END keyReleaseEvent()

    def timerEvent(self, event):
        if self.nao.isConnected():
            if self.keys[KEY_UP]:
                self.nao.tiltHeadUp()
            #END if
            if self.keys[KEY_DOWN]:
                self.nao.tiltHeadDown()
            #END if
            if self.keys[KEY_LEFT]:
                self.nao.turnHeadLeft()
            #END if
            if self.keys[KEY_RIGHT]:
                self.nao.turnHeadRight()
            #END if
        #END if
    #END timerEvent()

    def grab_keyboard(self):
        self.setFocus(QtCore.Qt.OtherFocusReason)
    #END grab_keyboard()

    def focusInEvent(self, event):
        self.grabKeyboard()
    #END focusInEvent
#END MainWindow