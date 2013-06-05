from Action import Action


class Speech(Action):
    def __init__(self, param):
        super(Speech, self).__init__()
        self.parameter = str(param)
    #END __init__()

    def execute(self, nao):
        nao.post.say(self.parameter)
    #END execute()

    def actionToString(self):
        return "Speech"
    #END actionToString()

    def paramToString(self):
        return self.parameter
    #END paramToString()
#END class