from abc import abstractmethod
from PyQt4 import QtCore


class BaseAction(QtCore.QObject):
    def __init__(self):
        super(BaseAction, self).__init__()
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