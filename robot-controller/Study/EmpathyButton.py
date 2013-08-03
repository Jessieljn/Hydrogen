from PyQt4 import QtGui


class EmpathyButton(QtGui.QPushButton):
    def __init__(self, actionCollection):
        super(EmpathyButton, self).__init__(actionCollection.getName())
        self._actions = actionCollection
    #END __init__()

    def getActionCollection(self):
        return self._actions
    #END getActionCollection()

    def getRobotActions(self, level):
        return self._actions.get(level)
    #END getRobotActions()
#END class
