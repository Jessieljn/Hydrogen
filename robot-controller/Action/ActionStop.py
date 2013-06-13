from BaseAction import BaseAction


class ActionStop(BaseAction):
    def __init__(self):
        super(ActionStop, self).__init__()
    #END __init__()

    def execute(self, nao):
        pass
    #END execute()

    def actionToString(self):
        return "ActionStop"
    #END actionToString()

    def paramToString(self):
        return "Stop action queue now"
    #END paramToString()
#END class
