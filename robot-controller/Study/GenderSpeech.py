from Action import Speech


class GenderSpeech(Speech):
    NAME_MARKER = "\\NAME\\"
    ParticipantName = ""

    def __init__(self, text, speed = 90, shaping = 100, blocking = True):
        super(GenderSpeech, self).__init__(text, speed, shaping, blocking)
    #END __init__()

    def execute(self, nao):
        txt = self.paramToString()
        txt = txt.replace(GenderSpeech.NAME_MARKER, GenderSpeech.ParticipantName)
        nao.say(txt, not self._blocking)
    #END execute()
#END class
