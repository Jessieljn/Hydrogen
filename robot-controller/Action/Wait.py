from PyQt4 import QtCore
from Action import Action


class Wait(Action):
    def __init__(self, param):
        super(Wait, self).__init__()
        self.parameter = int(param)
    #END __init__()

    def execute(self, nao):
        Wait.msleep(self.parameter)
    #END execute()

    def actionToString(self):
        return "Wait"
    #END actionToString()

    def paramToString(self):
        return str(self.parameter)
    #END paramToString()

    @staticmethod
    def msleep(msecs, mutex = QtCore.QMutex(), waitCond = QtCore.QWaitCondition()):
        mutex.lock()
        waitCond.wait(mutex, msecs)
        mutex.unlock()
    #END msleep
#END class
