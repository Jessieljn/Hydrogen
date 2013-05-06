import sys
from PyQt4 import QtGui, QtNetwork, QtCore

class ServerWindow (QtGui.QWidget):

    def __init__(self):
        super(ServerWindow, self).__init__()
        self.init()
    #def __init__

    def init(self):
        self.setWindowTitle('Server')
        self.setFixedSize(300, 600)
        
        self.server = QtNetwork.QTcpServer(self)
        
        self.lbl1 = QtGui.QLabel('Status: ', self)
        self.stateb = QtGui.QPushButton('closed', self)
        self.lbl3 = QtGui.QLabel('Received:', self)
        self.lbl4 = QtGui.QTextEdit(self)
        self.lbl4.resize(200, 500)

        #set to wait for access
        self.stateb.clicked.connect(self.listen)
    
        self.server.connect(self.server, QtCore.SIGNAL("newConnection()"), self.newCon)

        #move
        self.lbl1.move(10, 10)
        self.stateb.move(80, 10)
        self.lbl3.move(10, 40)
        self.lbl4.move(80, 40)

        self.show()
    #end def init

    def listen(self):
        src = self.sender()

        if src.text() == 'closed':
            #set to wait for access
            self.server.listen(QtNetwork.QHostAddress('127.0.0.1'), int(5555))

            if not self.server.isListening():
                print('Error: failed to listen to the specified address')
            else:
                self.stateb.setText('open')
        elif src.text() == 'open':
            self.server.close()
            self.stateb.setText('closed')
            
    #end listen

    def changeInput(self):
        print('input has come')
        self.txt = self.socket.readAll()
        self.lbl4.append(self.toStr(self.txt))
    #end def readRequest

    def newCon(self):
        print('connected')
        self.socket = self.server.nextPendingConnection()
        self.connect(self.socket, QtCore.SIGNAL("readyRead()"), self.changeInput)
    #def changeConnection

    def toStr(self, ba):
        toReturn = '';
        
        for x in range(0, int(ba.size())):
            toReturn += ba[x]
        #end for

        return toReturn
    #end def toStr
#end class ServerWindow

def main():
    app = QtGui.QApplication(sys.argv)
    window = ServerWindow()
    sys.exit(app.exec_())
#end def main

if __name__ == '__main__':
    main()
#end if

    

        
