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
            nao.LEDfadeRGB(self._ledname, int(self._value), self._seconds, not self._blocking)
        elif self._action == LED.ACTION_FADE_INTENSITY:
            nao.LEDfadeIntensity(self._ledname, float(self._value), self._seconds, not self._blocking)
        elif self._action == LED.ACTION_SET_INTENSITY:
            nao.LEDsetIntensity(self._ledname, float(self._value), not self._blocking)
        elif self._action == LED.ACTION_RANDOM_EYES:
            nao.LEDrandomEyes(self._seconds, not self._blocking)
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
