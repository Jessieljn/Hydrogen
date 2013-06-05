from PyQt4 import QtCore, QtGui
from Action.Action import Action


class ActionPushButton(QtGui.QPushButton):
    def __init__(self, parent, title, actions = None):
        super(ActionPushButton, self).__init__(title, parent)
        self._actions = []
        self.appendActions(actions)
        self.clicked.connect(self.on_click)
    #END __init__()

    execute = QtCore.pyqtSignal(Action)

    def appendActions(self, actions):
        if actions is None:
            pass
        elif isinstance(actions, Action):
            self._actions.append(actions)
        else:
            for act in actions:
                self._actions.append(act)
            #END for
        #END if
    #END appendActions()

    def on_click(self):
        for act in self._actions:
            self.execute.emit(act)
        #END for
    #END on_click()
#END class
