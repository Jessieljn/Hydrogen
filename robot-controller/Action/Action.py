from abc import abstractmethod
from PyQt4 import QtCore


class Action(QtCore.QObject):
    def __init__(self):
        super(Action, self).__init__()
        self.parameter = None
    #END __init__()

    @abstractmethod
    def execute(self, nao):
        pass
    #END execute()

    @abstractmethod
    def actionToString(self):
        return ""
    #END actionToString()

    @abstractmethod
    def paramToString(self):
        return ""
    #END paramToString()
#END class
