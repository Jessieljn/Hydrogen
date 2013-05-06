import sys
from PyQt4 import QtGui, QtNetwork, QtCore
from TaskTabs import TaskTabs
from TextWidClass import TextWid
from GestureWidget import GestureWidget
from CameraWidget import CameraWidget
from GeneralWidget import GeneralWidget
from StiffnessWidget import StiffnessWidget
import Nao

KEY_UP = 0
KEY_DOWN = 1
KEY_LEFT = 2
KEY_RIGHT = 3

class MainWindow (QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.init()

    def init(self):

        self.keys = dict()
        self.keys[KEY_UP] = False
        self.keys[KEY_DOWN] = False
        self.keys[KEY_LEFT] = False
        self.keys[KEY_RIGHT] = False

        self.setWindowTitle('Robot Controller')

        #create a socket
        self.socket = QtNetwork.QTcpSocket(self)

        #create camera widget
        self.cameraWidget = CameraWidget(self)

        self.nao = Nao.Nao(self.cameraWidget)

        self.generalWidget = GeneralWidget(self.nao, self)

        self.stiffnessWidget = StiffnessWidget(self.nao, self)

        self.cameraWidget.setNao(self.nao)

        #create text widget
        self.textWid = TextWid(self.nao, self)
        self.textWid.msg_sent.connect(self.grab_keyboard)

        #create gesture widget
        self.gestureWidget = GestureWidget(self.nao, self)

        #create tabbed widget
        self.taskTabs = TaskTabs(self.nao, self)

        #create connection button
        self.connectButton = QtGui.QPushButton('Connect', self)
        self.naoIP = QtGui.QLineEdit(Nao.DEFAULT_IP)
        self.naoIP.setMaximumWidth(100)
        self.naoPort = QtGui.QLineEdit(str(Nao.DEFAULT_PORT))
        self.naoPort.setMaximumWidth(60)

        #event action for connection button
        self.connectButton.clicked.connect(self.connectToNao)

        #widget layout
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

    def connectToNao(self):
        if self.connectButton.text() == 'Connect':
            print "==================================="
            print "Connecting to Nao (" + str(self.naoIP.text()) + ":" + str(self.naoPort.text()) + ")"
            if self.nao.connect(str(self.naoIP.text()), int(str(self.naoPort.text()))):
                self.nao.startCamera()
                self.connectButton.setText('Disconnect')
            else:
                print "FAILED"
            print "==================================="
        elif self.connectButton.text() == 'Disconnect':
            self.nao.disconnect()
            self.connectButton.setText('Connect')

    def updateImageTop(self, image):
        self.cameraWidget.setImage(1, image)

    def updateImageBottom(self, image):
        self.cameraWidget.setImage(2, image)

    def closeEvent(self, event):
        if self.nao.isConnected():
            self.nao.disconnect()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.keys[KEY_UP] = True
        if event.key() == QtCore.Qt.Key_Down:
            self.keys[KEY_DOWN] = True
        if event.key() == QtCore.Qt.Key_Left:
            self.keys[KEY_LEFT] = True
        if event.key() == QtCore.Qt.Key_Right:
            self.keys[KEY_RIGHT] = True

        print "key"
        if event.key() == QtCore.Qt.Key_Escape:
            print "tab"
            self.releaseKeyboard()
            self.textWid.message.setFocus(QtCore.Qt.OtherFocusReason)
            self.textWid.message.grabKeyboard()

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.keys[KEY_UP] = False
        if event.key() == QtCore.Qt.Key_Down:
            self.keys[KEY_DOWN] = False
        if event.key() == QtCore.Qt.Key_Left:
            self.keys[KEY_LEFT] = False
        if event.key() == QtCore.Qt.Key_Right:
            self.keys[KEY_RIGHT] = False

    def timerEvent(self, event):
        if self.nao.isConnected():
            if self.keys[KEY_UP]:
                self.nao.tiltHeadUp()
            if self.keys[KEY_DOWN]:
                self.nao.tiltHeadDown()
            if self.keys[KEY_LEFT]:
                self.nao.turnHeadLeft()
            if self.keys[KEY_RIGHT]:
                self.nao.turnHeadRight()
    def grab_keyboard(self):
        self.setFocus(QtCore.Qt.OtherFocusReason)

    def focusInEvent(self, event):
        self.grabKeyboard()
