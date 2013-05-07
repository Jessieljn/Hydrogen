import sys
from PyQt4 import QtGui, QtNetwork, QtCore
from TaskTabs import TaskTabs
from TextWidClass import TextWid
from GestureWidget import GestureWidget
from CameraWidget import CameraWidget
from GeneralWidget import GeneralWidget
from StiffnessWidget import StiffnessWidget
import Nao

##
# MainWindow.py
#
# Puts all the widgets together in one windows.
##

KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3


class MainWindow (QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
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

        # Creates a camera widget.
        self.cameraWidget = CameraWidget(self)

        self.nao = Nao.Nao(self.cameraWidget)

        self.generalWidget = GeneralWidget(self.nao, self)

        self.stiffnessWidget = StiffnessWidget(self.nao, self)

        self.cameraWidget.setNao(self.nao)

        # Create the text widget.
        self.textWid = TextWid(self.nao, self)
        self.textWid.msg_sent.connect(self.grab_keyboard)

        # Creates the gesture widget.
        self.gestureWidget = GestureWidget(self.nao, self)

        # Create a tabbed task bar.
        self.taskTabs = TaskTabs(self.nao, self)

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

        mainLayout = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()
        vbox2 = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        
        mainLayout.addWidget(self.cameraWidget)
        mainLayout.addLayout(vbox)
        self.setLayout(mainLayout)

        hbox2 = QtGui.QVBoxLayout()
        hbox2.addWidget(self.generalWidget)
        hbox2.addWidget(self.gestureWidget)

        hbox3 = QtGui.QHBoxLayout()
        hbox3.addWidget(self.textWid, 5)
        hbox3.addWidget(self.stiffnessWidget, 1)
        hbox2.addLayout(hbox3)
        vbox.addLayout(hbox2)
        vbox2.addWidget(self.taskTabs)
        hbox.addLayout(vbox2)

        #Uncomment for smaller camera, and gestures on their own half of screen.
        #hbox.addWidget(self.gestureWidget)
        vbox.addLayout(hbox)

        naoConnectionLayout = QtGui.QHBoxLayout()
        naoConnectionLayout.addWidget(self.connectButton, 0, QtCore.Qt.AlignLeft)
        naoConnectionLayout.addWidget(self.naoIP, 0, QtCore.Qt.AlignLeft)
        naoConnectionLayout.addWidget(self.naoPort, 0, QtCore.Qt.AlignLeft)

        vbox.addLayout(naoConnectionLayout)

        self.show()
        self.grabKeyboard()
        timerID = self.startTimer(1000/100)
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

    def updateImageTop(self, image):
        self.cameraWidget.setImage(1, image)
    #END updateImageTop()

    def updateImageBottom(self, image):
        self.cameraWidget.setImage(2, image)
    #END updateImageBottom()

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