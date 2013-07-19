from Action import BaseAction
from PyQt4 import QtGui


class ActionPushButton(QtGui.QPushButton):
    def __init__(self, parent, title, actions = None):
        super(ActionPushButton, self).__init__(title, parent)
        self._actions = []
        self.addRobotActions(actions)
    #END __init__()

    def addRobotActions(self, actions):
        if actions is None:
            pass
        elif isinstance(actions, BaseAction):
            self._actions.append(actions)
        else:
            for act in actions:
                self._actions.append(act)
            #END for
        #END if
    #END addRobotActions()

    def getRobotActions(self):
        return self._actions
    #END getRobotActions()

    def setRobotActions(self, actions):
        self._actions = []
        self.addRobotActions(actions)
    #END setRobotActions()
#END ActionPushButton.py