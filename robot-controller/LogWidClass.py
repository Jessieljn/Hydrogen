from PyQt4 import QtGui, QtNetwork, QtCore

class LogWid (QtGui.QWidget):
    def __init__ (self, parent):
        super(LogWid, self).__init__()
        self.init()
        self.setParent(parent)
    #end def __init__

    def init(self):
        self.lbl = QtGui.QLabel('Messages sent:')
        self.te = QtGui.QTextEdit(self)

        self.te.setReadOnly(True)
        
        #Layout
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.te)
        self.setLayout(vbox)
    #end def init

    def appendActivity(self, newActivity):
        self.te.append(newActivity)
    #class def update
#end class LogWid
