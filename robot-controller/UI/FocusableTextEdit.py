from PyQt4 import QtCore, QtGui


class FocusableTextEdit(QtGui.QTextEdit):
    def __init__(self, parent):
        super(FocusableTextEdit, self).__init__(parent)
    #END __init__()

    textSubmitted = QtCore.pyqtSignal()
    inputCancelled = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super(FocusableTextEdit, self).mousePressEvent(event)
        self.grabKeyboard()
    #END mousePressEvent()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.textSubmitted.emit()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.releaseKeyboard()
            self.inputCancelled.emit()
        else:
            super(FocusableTextEdit, self).keyPressEvent(event)
        #END if
    #END keyPressEvent()
#END class
