from Action import Action


class Behavior(Action):
    def __init__(self, param):
        super(Behavior, self).__init__()
        self.parameter = str(param)
    #END __init__()

    def execute(self, nao):
        nao.behavior(self.parameter)
    #END execute()

    def actionToString(self):
        return "Behavior"
    #END actionToString()

    def paramToString(self):
        return self.parameter
    #END paramToString()
#END class
