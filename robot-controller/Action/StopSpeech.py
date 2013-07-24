from BaseAction import BaseAction


class StopSpeech(BaseAction):
    def __init__(self):
        super(StopSpeech, self).__init__()
    #END __init__()

    def execute(self, nao):
        nao.stopSaying()
    #END execute()

    def actionToString(self):
        return "Stop Speech"
    #END actionToString()

    def paramToString(self):
        return ""
    #END paramToString()
#END StopSpeech.py