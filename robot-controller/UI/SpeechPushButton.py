from PyQt4 import QtCore, QtGui


class SpeechPushButton(QtGui.QPushButton):
    def __init__(self, parent, title, speech):
        super(SpeechPushButton, self).__init__(title, parent)
        self.clicked.connect(self.onClick)
        self._speech = speech
    #END __init__()

    execute = QtCore.pyqtSignal(str)

    def onClick(self):
        self.execute.emit(self._speech)
    #END onClick()
#END class
