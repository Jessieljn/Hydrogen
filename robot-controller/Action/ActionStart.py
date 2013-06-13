from BaseAction import BaseAction


class ActionStart(BaseAction):
    def __init__(self):
        super(ActionStart, self).__init__()
    #END __init__()

    def execute(self, nao):
        pass
    #END execute()

    def actionToString(self):
        return "ActionStart"
    #END actionToString()

    def paramToString(self):
        return "Start current action queue immediately"
    #END paramToString()
#END class
