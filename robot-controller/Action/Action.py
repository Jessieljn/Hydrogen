from abc import ABCMeta, abstractmethod


class Action(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.parameter = None
    #END __init__()

    @abstractmethod
    def execute(self, nao):
        pass
    #END execute()

    @abstractmethod
    def actionToString(self):
        pass
    #END actionToString()

    @abstractmethod
    def paramToString(self):
        pass
    #END paramToString()
#END class
