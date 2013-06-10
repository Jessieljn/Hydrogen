from BaseAction import BaseAction


class AutoRunAction(BaseAction):
    def __init__(self):
        super(AutoRunAction, self).__init__()
    #END __init__()

    def execute(self, nao):
        pass
    #END execute()

    def actionToString(self):
        return "AutoRunAction"
    #END actionToString()

    def paramToString(self):
        return "Run current action queue automatically"
    #END paramToString()
#END class