from BaseAction import BaseAction
from PyQt4 import QtCore


class Wait(BaseAction):
    def __init__(self, msecs):
        super(Wait, self).__init__()
        self._msecs = int(msecs)
    #END __init__()

    def execute(self, nao):
        QtCore.QThread.msleep(self._msecs)
    #END execute()

    def actionToString(self):
        return "Wait"
    #END actionToString()

    def paramToString(self):
        return str(self._msecs)
    #END paramToString()
#END class