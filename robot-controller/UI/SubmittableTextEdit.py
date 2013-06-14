from PyQt4 import QtCore
from PyQt4 import QtGui


class SubmittableTextEdit(QtGui.QTextEdit):
    def __init__(self, parent = None):
        super(SubmittableTextEdit, self).__init__(parent)
    #END __init__()

    inputCancelled = QtCore.pyqtSignal()

    textSubmitted = QtCore.pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.textSubmitted.emit()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.inputCancelled.emit()
        else:
            super(SubmittableTextEdit, self).keyPressEvent(event)
        #END if
    #END keyPressEvent()
#END class
