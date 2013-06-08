from BaseAction import BaseAction


class LED(BaseAction):
    ACTION_FADE_RGB = "fadeRGB"
    ACTION_FADE_INTENSITY = "fadeIntensity"
    ACTION_SET_INTENSITY = "setIntensity"
    ACTION_RANDOM_EYES = "randomEyes"

    def __init__(self, action, ledname, value, seconds = 0.5, blocking = False):
        super(LED, self).__init__()
        self._action = str(action)
        self._ledname = str(ledname)
        self._value = value
        self._seconds = float(seconds)
        self._blocking = blocking
    #END __init__()

    def execute(self, nao):
        if self._action == LED.ACTION_FADE_RGB:
            if self._blocking:
                nao.LEDfadeRGB(self._ledname, int(self._value), self._seconds)
            else:
                nao.postLEDfadeRGB(self._ledname, int(self._value), self._seconds)
            #END if
        elif self._action == LED.ACTION_FADE_INTENSITY:
            if self._blocking:
                nao.LEDfadeIntensity(self._ledname, float(self._value), self._seconds)
            else:
                nao.postLEDfadeIntensity(self._ledname, float(self._value), self._seconds)
            #END if
        elif self._action == LED.ACTION_SET_INTENSITY:
            if self._blocking:
                nao.LEDsetIntensity(self._ledname, float(self._value))
            else:
                nao.postLEDsetIntensity(self._ledname, float(self._value))
            #END if
        elif self._action == LED.ACTION_RANDOM_EYES:
            if self._blocking:
                nao.LEDrandomEyes(self._seconds)
            else:
                nao.postLEDrandomEyes(self._seconds)
            #END if
        #END if
    #END execute()

    def actionToString(self):
        return "LED"
    #END actionToString()

    def paramToString(self):
        ret = self._action + ": ";
        if self._action == LED.ACTION_FADE_RGB:
            return ret + self._ledname + " with RGB " + str(self._value) + " and duration " + str(self._seconds)
        elif self._action == LED.ACTION_FADE_INTENSITY:
            return ret + self._ledname + " with intensity " + str(self._value) + " and duration " + str(self._seconds)
        elif self._action == LED.ACTION_SET_INTENSITY:
            return ret + self._ledname + " with intensity " + str(self._value)
        elif self._action == LED.ACTION_RANDOM_EYES:
            return ret + " with duration " + str(self._seconds)
        return "INVALID PARAMETER(S)"
    #END paramToString()
#END class
