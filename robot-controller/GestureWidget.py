from PyQt4 import QtGui, QtCore
import MainWindow


##
# GestureWidget.py
#
# Creates the Gesture Widget in the GUI, used for motions.
##
class GestB (QtGui.QPushButton):
        def __init__(self, parent, title, command):
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

            self.wave = QtGui.QPushButton("Wave")
            self.wave.clicked.connect(self.nao.wave)

            self.introduce = QtGui.QPushButton("Introduce")
            self.introduce.clicked.connect(self.nao.introduce)

            layout = QtGui.QVBoxLayout()

            hbox = QtGui.QHBoxLayout()
            hbox2 = QtGui.QHBoxLayout()

            hbox.addSpacing(10)
            hbox.addWidget(self.stand, 0, QtCore.Qt.AlignCenter)
            hbox.addWidget(self.sit, 0, QtCore.Qt.AlignCenter)
            hbox.addWidget(self.taiChi, 0, QtCore.Qt.AlignCenter)
            hbox.addWidget(self.handShake, 0, QtCore.Qt.AlignCenter)
            hbox.addWidget(self.thriller, 0, QtCore.Qt.AlignCenter)

            hbox2.addWidget(self.wave, 0, QtCore.Qt.AlignCenter)
            hbox2.addWidget(self.introduce, 0, QtCore.Qt.AlignCenter)

            layout.addLayout(hbox)
            layout.addLayout(hbox2)

            self.setLayout(layout)
        #END init()

        def sendMessage(self):
                src = self.sender()
                wid = self

                while not(isinstance(wid, MainWindow.MainWindow)):
                        wid = wid.parent()
                #END while

                if isinstance(wid, MainWindow.MainWindow):
                        wid.sendMessage('Gest:' + src.getCommand())
                #END if
                else:
                        print("Error: sendMessage in GestureWid")
                #END else
        #END sendMessage()
#END GestureWidget