from PyQt4 import QtCore, QtGui
from Action.Action import Action


class ActionPushButton(QtGui.QPushButton):
    def __init__(self, parent, title, actions = None):
        super(ActionPushButton, self).__init__(title, parent)
        self.clicked.connect(self.onClick)
        self._actions = []
        if actions is None:
            pass
        elif isinstance(actions, Action):
            self._actions.append(actions)
        else:
            for act in actions:
                self._actions.append(act)
            #END for
        #END if
    #END __init__()

    execute = QtCore.pyqtSignal(Action)

    def onClick(self):
        for act in self._actions:
            self.execute.emit(act)
        #END for
    #END onClick()
#END class
