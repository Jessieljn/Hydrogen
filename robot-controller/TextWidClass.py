from PyQt4 import QtGui, QtNetwork, QtCore
import MainWindow

class FocusTextEdit(QtGui.QTextEdit):
    def __init__(self, parent):
        super(FocusTextEdit, self).__init__()
        self.parent = parent

    def mousePressEvent(self, event):
        super(FocusTextEdit, self).mousePressEvent(event)
        self.grabKeyboard()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            print "enter key"
            self.parent.sendMessage()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.releaseKeyboard()
            self.parent.msg_sent.emit()

        else:
            QtGui.QTextEdit.keyPressEvent(self, event)

class TextWid (QtGui.QGroupBox):

    msg_sent = QtCore.pyqtSignal()

    def __init__(self, nao, parent):
        super(TextWid, self).__init__()
        self.nao = nao
        self.setTitle("Text To Speech")
        self.setParent(parent)

        self.message = FocusTextEdit(self)
        self.message.setMaximumHeight(65)
        self.message.textChanged.connect(self.changeLEDs)
        self.ledsProcessing = False

        self.button = QtGui.QPushButton('Say')
        self.button.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.button.setFixedWidth(100)
        self.button.setMaximumHeight(65)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.message)
        hbox.addWidget(self.button)

        #self.volumeLabel = QtGui.QLabel("Volume:")
        self.volumeSlider = QtGui.QSlider(QtCore.Qt.Vertical)
        self.volumeSlider.setMaximumHeight(55)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(85)
        self.volumeSlider.valueChanged.connect(self.setVolume)

        vbox = QtGui.QVBoxLayout()
        #vbox.addWidget(self.volumeLabel)
        vbox.addWidget(self.volumeSlider)

        hbox.addLayout(vbox)
        self.setLayout(hbox)

        self.button.clicked.connect(self.sendMessage)

        self.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)

    def sendMessage(self):
        print "send"
        if self.nao.isConnected():
            self.nao.say(str(self.message.toPlainText()))
            if self.ledsProcessing == True:
                self.ledsProcessing = False
                self.nao.setLEDsNormal()
        self.message.releaseKeyboard()
        self.msg_sent.emit()

    def setVolume(self, volume):
        self.nao.setVolume(float(volume) / 100)

    def changeLEDs(self):
        if str(self.message.toPlainText()) == "":
            if self.ledsProcessing == True:
                self.ledsProcessing = False
                self.nao.setLEDsNormal()
        else:
            if self.ledsProcessing == False:
                self.ledsProcessing = True
                self.nao.setLEDsProcessing()
