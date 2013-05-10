from PyQt4 import QtGui, QtNetwork, QtCore
import MainWindow


##
# GestureWidget.py
#
# Creates the Gesture Widget in the GUI, used for motions.
##
class GestB (QtGui.QPushButton):
        def __init__ (self, parent, title, command):
                super(GestB, self).__init__(title)
                self.setParent(parent)
                self.command = command
        #end def __init__()

        def getCommand(self):
                return self.command
        #END getCommand()
#END GestB


class GestureWidget (QtGui.QGroupBox):
        def __init__(self, nao, parent):
            super(GestureWidget, self).__init__()
            self.nao = nao
            self.init()
            self.setParent(parent)
        #END __init__()

        def init(self):
            self.setTitle("General Motions")

            # Buttons for motions.
            self.stand = QtGui.QPushButton("Stand Up")
            self.stand.clicked.connect(self.nao.standUp)

            self.sit = QtGui.QPushButton("Sit Down")
            self.sit.clicked.connect(self.nao.sitDown)

            self.taiChi = QtGui.QPushButton("Tai Chi")
            self.taiChi.clicked.connect(self.nao.taiChi)

            self.handShake = QtGui.QPushButton("Hand Shake")
            self.handShake.clicked.connect(self.nao.shakeHand)

            self.thriller = QtGui.QPushButton("Thriller")
            self.thriller.clicked.connect(self.nao.thriller)

            self.wave  = QtGui.QPushButton("Wave")
            self.wave.clicked.connect(self.nao.wave)

            vbox = QtGui.QHBoxLayout()

            # Add buttons to vertical box.
            vbox.addSpacing(10)
            vbox.addWidget(self.stand, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.sit, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.taiChi, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.handShake, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.thriller, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.wave, 0, QtCore.Qt.AlignCenter)
            vbox.addStretch(1)

            # Set layout.
            self.setLayout(vbox)
        #END init()

        def sendMessage(self):
                src = self.sender()
                wid = self

                while not(isinstance(wid, MainWindow.MainWindow)):
                        wid = wid.parent()
                #END while

                if isinstance(wid, MainWindow.MainWindow)   :
                        wid.sendMessage('Gest:'+src.getCommand())
                #END if
                else:
                        print("Error: sendMessage in GestureWid")
                #END else
        #END sendMessage()
#END GestureWidget