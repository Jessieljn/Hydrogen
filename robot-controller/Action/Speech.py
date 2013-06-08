from Action import Action


class Speech(Action):
    def __init__(self, text, speed = 100, shaping = 100, blocking = True):
        super(Speech, self).__init__()
        self._text = str(text)
        speed = int(speed)
        if speed <= 50:
            self._speed = 50
        elif speed >= 200:
            self._speed = 200
        else:
            self._speed = speed
        #END if
        shaping = int(shaping)
        if shaping <= 50:
            self._shaping = 50
        elif shaping >= 150:
            self._shaping = 150
        else:
            self._shaping = shaping
        #END if
        self._blocking = blocking
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
        return "\\RSPD=" + str(self._speed) + "\\ \\VCT=" + str(self._shaping) + "\\ " + self._text + " \\RST\\"
    #END paramToString()
#END class
