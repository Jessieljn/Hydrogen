from Action import Action
from PyQt4 import QtCore


class Wait(Action):
    def __init__(self, param):
        super(Wait, self).__init__()
        self.parameter = int(param)
    #END __init__()

    def execute(self, nao):
        QtCore.QThread.msleep(self.parameter)
    #END execute()

    def actionToString(self):
        return "Wait"
    #END actionToString()

    def paramToString(self):
        return str(self.parameter)
    #END paramToString()
#END class
