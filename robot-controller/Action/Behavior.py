from Action import Action


class Behavior(Action):
    def __init__(self, param, blocking = True):
        super(Behavior, self).__init__()
        self.parameter = str(param)
        self.blocking = blocking
    #END __init__()

    def execute(self, nao):
        if self.blocking:
            nao.behavior(self.parameter)
        else:
            nao.postBehavior(self.parameter)
    #END execute()

    def actionToString(self):
        return "Behavior"
    #END actionToString()

    def paramToString(self):
        return self.parameter
    #END paramToString()
#END class
