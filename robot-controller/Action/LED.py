from Action import Action


class LED(Action):
    ACTION_FADE_RGB = "fadeRGB"
    ACTION_FADE_INTENSITY = "fadeIntensity"
    ACTION_SET_INTENSITY = "setIntensity"
    ACTION_RANDOM_EYES = "randomEyes"

    def __init__(self, action, ledname, value, seconds = 0.5, blocking = False):
        super(LED, self).__init__()
        self.action = str(action)
        self.ledname = str(ledname)
        self.value = value
        self.seconds = float(seconds)
        self.blocking = blocking
    #END __init__()

    def execute(self, nao):
        if self.action == LED.ACTION_FADE_RGB:
            if self.blocking:
                nao.LEDfadeRGB(self.ledname, int(self.value), self.seconds)
            else:
                nao.postLEDfadeRGB(self.ledname, int(self.value), self.seconds)
            #END if
        elif self.action == LED.ACTION_FADE_INTENSITY:
            if self.blocking:
                nao.LEDfadeIntensity(self.ledname, float(self.value), self.seconds)
            else:
                nao.postLEDfadeIntensity(self.ledname, float(self.value), self.seconds)
            #END if
        elif self.action == LED.ACTION_SET_INTENSITY:
            if self.blocking:
                nao.LEDsetIntensity(self.ledname, float(self.value))
            else:
                nao.postLEDsetIntensity(self.ledname, float(self.value))
            #END if
        elif self.action == LED.ACTION_RANDOM_EYES:
            if self.blocking:
                nao.LEDrandomEyes(self.seconds)
            else:
                nao.postLEDrandomEyes(self.seconds)
            #END if
        #END if
    #END execute()

    def actionToString(self):
        return "LED"
    #END actionToString()

    def paramToString(self):
        ret = self.action + ": ";
        if self.action == LED.ACTION_FADE_RGB:
            return ret + self.ledname + " with RGB " + str(self.value) + " and duration " + str(self.seconds)
        elif self.action == LED.ACTION_FADE_INTENSITY:
            return ret + self.ledname + " with intensity " + str(self.value) + " and duration " + str(self.seconds)
        elif self.action == LED.ACTION_SET_INTENSITY:
            return ret + self.ledname + " with intensity " + str(self.value)
        elif self.action == LED.ACTION_RANDOM_EYES:
            return ret + " with duration " + str(self.seconds)
        return "INVALID PARAMETER(S)"
    #END paramToString()
#END class
