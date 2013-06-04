from PyQt4 import QtCore, QtGui


class BehaviorPushButton(QtGui.QPushButton):
    def __init__(self, parent, title, motion):
        super(BehaviorPushButton, self).__init__(title, parent)
        self.clicked.connect(self.onClick)
        self._motion = motion
    #END __init__()

    execute = QtCore.pyqtSignal(str)

    def onClick(self):
        self.execute.emit(self._motion)
    #END onClick()
#END class
