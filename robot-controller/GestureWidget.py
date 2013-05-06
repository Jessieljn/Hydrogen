from PyQt4 import QtGui, QtNetwork, QtCore
import MainWindow


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
            self.setTitle("Gestures")

            self.stand = QtGui.QPushButton("Stand Up")
            self.stand.clicked.connect(self.nao.standUp)

            self.sit = QtGui.QPushButton("Sit Down")
            self.sit.clicked.connect(self.nao.sitDown)

            self.taiChi = QtGui.QPushButton("Tai Chi")
            self.taiChi.clicked.connect(self.nao.taiChi)

            #GestB(self, <<Button Name>>, <<What command to send>>)
            #self.b1 = GestB(self, 'Gesture 1', 'g1')
            #self.b2 = GestB(self, 'Gesture 2', 'g2')
            self.b3 = GestB(self, 'Gesture 3', 'g3')
            self.b4 = GestB(self, 'Gesture 4', 'g4')
            self.b5 = GestB(self, 'Gesture 5', 'g5')

            #Events for buttons.
            #self.b1.clicked.connect(self.sendMessage)
            #self.b2.clicked.connect(self.sendMessage)
            #self.b3.clicked.connect(self.sendMessage)
            #self.b4.clicked.connect(self.sendMessage)
            #self.b5.clicked.connect(self.sendMessage)

            #Set layout.
            vbox = QtGui.QHBoxLayout()

            vbox.addSpacing(10)
            vbox.addWidget(self.stand, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.sit, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.taiChi, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.b3, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.b4, 0, QtCore.Qt.AlignCenter)
            vbox.addWidget(self.b5, 0, QtCore.Qt.AlignCenter)
            vbox.addStretch(1)
            
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
