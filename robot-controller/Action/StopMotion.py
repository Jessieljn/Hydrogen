from BaseAction import BaseAction


class StopMotion(BaseAction):
    def __init__(self):
        super(StopMotion, self).__init__()
    #END __init__()

    def execute(self, nao):
        nao.stopMoving()
    #END execute()

    def actionToString(self):
        return "Stop Motion"
    #END actionToString()

    def paramToString(self):
        return ""
    #END paramToString()
#END class