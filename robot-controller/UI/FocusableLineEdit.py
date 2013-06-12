from PyQt4 import QtGui


class FocusableLineEdit(QtGui.QLineEdit):
    def __init__(self, parent):
        super(FocusableLineEdit, self).__init__(parent)
    #END __init__()

    def mousePressEvent(self, event):
        super(FocusableLineEdit, self).mousePressEvent(event)
        self.grabKeyboard()
    #END mousePressEvent()
#END FocusableLineEdit
