from BaseAction import BaseAction


class WaitMotion(BaseAction):
    def __init__(self):
        super(WaitMotion, self).__init__()
    #END __init__()

    def execute(self, nao):
        nao.wait(moving = True, saying = False)
    #END execute()

    def actionToString(self):
        return "WaitMotion"
    #END actionToString()

    def paramToString(self):
        return ""
    #END paramToString()
#END class
