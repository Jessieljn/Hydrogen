from PyQt4 import QtGui, QtNetwork, QtCore


class ConnectionWin (QtGui.QWidget):
    def __init__(self, mainwindow):
        super(ConnectionWin, self).__init__()
        self.parent = mainwindow
        self.init()
    #END __init__()

    def init(self):
        self.setWindowTitle('Connection Setting')
        self.setFixedSize(250, 100)
        self.iPLb = QtGui.QLabel('IP address:', self)
        self.portLb = QtGui.QLabel('Port number:', self)
        self.ip = QtGui.QLineEdit('nao.local', self)
        self.port = QtGui.QLineEdit('9559', self)
        self.conB = QtGui.QPushButton('Connect', self)

        self.conB.clicked.connect(self.passToMain)

        self.iPLb.move(15, 10); self.ip.move(105, 10)
        self.portLb.move(15, 30); self.port.move(105, 30)
        self.conB.move(80, 70)
        
        self.show()
    #END init()

    #passToMain(): Passes the IP and Port to the main
    def passToMain(self):
        li = []
        li.append(self.ip.displayText())#li[0]
        li.append(self.port.displayText())#li[1]

        self.parent.tryConnect(li)
        self.close()
    #END passToMain()
#END ConnectionWin