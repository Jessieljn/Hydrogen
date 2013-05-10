import sys
from PyQt4 import QtGui, QtNetwork, QtCore


##
# server.py
##
class ServerWindow (QtGui.QWidget):

    def __init__(self):
        super(ServerWindow, self).__init__()
        self.init()
    #END __init__()

    def init(self):
        self.setWindowTitle('Server')
        self.setFixedSize(300, 600)
        
        self.server = QtNetwork.QTcpServer(self)
        
        self.lbl1 = QtGui.QLabel('Status: ', self)
        self.stateb = QtGui.QPushButton('Closed', self)
        self.lbl3 = QtGui.QLabel('Received:', self)
        self.lbl4 = QtGui.QTextEdit(self)
        self.lbl4.resize(200, 500)

        # Set to wait for access
        self.stateb.clicked.connect(self.listen)
    
        self.server.connect(self.server, QtCore.SIGNAL("newConnection()"), self.newCon)

        # Move
        self.lbl1.move(10, 10)
        self.stateb.move(80, 10)
        self.lbl3.move(10, 40)
        self.lbl4.move(80, 40)

        self.show()
    #END init()

    def listen(self):
        src = self.sender()

        if src.text() == 'Closed':
            # Set to wait for access
            self.server.listen(QtNetwork.QHostAddress('130.179.30.44'), int(9559))

            if not self.server.isListening():
                print('Error: failed to listen to the specified address')
            #END if not
            else:
                self.stateb.setText('Open')
            #END else
        #END if
        elif src.text() == 'open':
            self.server.close()
            self.stateb.setText('Closed')
        #END elif
    #END listen()

    def changeInput(self):
        print('Input has come')
        self.txt = self.socket.readAll()
        self.lbl4.append(self.toStr(self.txt))
    #END readRequest

    def newCon(self):
        print('Connected')
        self.socket = self.server.nextPendingConnection()
        self.connect(self.socket, QtCore.SIGNAL("readyRead()"), self.changeInput)
    #END newCon()

    def toStr(self, ba):
        toReturn = '';
        
        for x in range(0, int(ba.size())):
            toReturn += ba[x]
        #END for

        return toReturn
    #END toStr
#END ServerWindow


def main():
    app = QtGui.QApplication(sys.argv)
    window = ServerWindow()
    sys.exit(app.exec_())
#END main()

if __name__ == '__main__':
    main()
#END if