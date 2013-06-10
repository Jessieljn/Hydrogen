from BaseAction import BaseAction


class Behavior(BaseAction):
    def __init__(self, bhvName, blocking = True):
        super(Behavior, self).__init__()
        self._bhvName = str(bhvName)
        self._blocking = blocking
    #END __init__()

    def execute(self, nao):
        nao.behavior(self._bhvName, not self._blocking)
    #END execute()

    def actionToString(self):
        return "Behavior"
    #END actionToString()

    def paramToString(self):
        return self._bhvName
    #END paramToString()
#END class
