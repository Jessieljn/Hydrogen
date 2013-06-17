from BaseAction import BaseAction


class WaitSpeech(BaseAction):
    def __init__(self):
        super(WaitSpeech, self).__init__()
    #END __init__()

    def execute(self, nao):
        nao.wait(moving = False, saying = True)
    #END execute()

    def actionToString(self):
        return "WaitSpeech"
    #END actionToString()

    def paramToString(self):
        return ""
    #END paramToString()
#END class
