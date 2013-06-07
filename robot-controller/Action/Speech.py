from Action import Action


class Speech(Action):
    def __init__(self, param, blocking = True):
        super(Speech, self).__init__()
        self.parameter = str(param)
        self.blocking = blocking
    #END __init__()

    def execute(self, nao):
        if self.blocking:
            nao.say(self.parameter)
        else:
            nao.postSay(self.parameter)
    #END execute()

    def actionToString(self):
        return "Speech"
    #END actionToString()

    def paramToString(self):
        return self.parameter
    #END paramToString()
#END class