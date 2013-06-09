from PyQt4 import QtCore


class NaoMotion(QtCore.QObject):
    METHOD_BEZIER = "Bezier"
    METHOD_SIMPLIFIED = "Simplified"

    def __init__(self, name):
        super(NaoMotion, self).__init__()
        self._name = name # motion name
        self._names = list() # joint names
        self._times = list() # time in seconds
        self._keys = list() # angles of joint
        self._method = NaoMotion.METHOD_SIMPLIFIED
    #END __init__()

    def name(self):
        return self._name
    #END name()

    def getMethod(self):
        return self._method
    #END getMethod()

    def getNames(self):
        return self._names
    #END getNames()

    def getKeys(self):
        return self._keys
    #END getKeys()

    def getTimes(self):
        return self._times
    #END getTimes()

    def applyRepeat(self, beginIndex, endIndex, repeats, repeatTimeModifier = 1.0):
        names = list()
        times = list()
        keys = list()

        endLength = False
        if beginIndex < 0:
            beginIndex = 0
        #END if
        if endIndex < 0:
            endLength = True
        #END if

        i = 0
        while i < len(self._names):
            names.append(self._names[i])
            times.append(list())
            keys.append(list())

            if endLength:
                endIndex = len(self._keys[i]) - 1
            #END if
            j = 0
            while j < len(self._keys[i]) and j < beginIndex:
                times[i].append(self._times[i][j])
                keys[i].append(self._keys[i][j])
                j = j + 1
            #END while

            timeCurrent = self._times[i][j]
            timePrevious = 0
            k = 0
            while k < repeats:
                j = beginIndex
                if j <= 0:
                    timePrevious = 0
                else:
                    timePrevious = self._times[i][j - 1]
                #END if
                while j < len(self._keys[i]) and j <= endIndex:
                    timeCurrent = timeCurrent + (self._times[i][j] - timePrevious) * repeatTimeModifier
                    timePrevious = self._times[i][j]
                    times[i].append(timeCurrent)
                    keys[i].append(self._keys[i][j])
                    j = j + 1
                #END while
                k = k + 1
            #END while

            while j < len(self._keys[i]):
                timeCurrent = timeCurrent + (self._times[i][j] - timePrevious)
                timePrevious = self._times[i][j]
                times[i].append(timeCurrent)
                keys[i].append(self._keys[i][j])
                j = j + 1
            #END while

            i = i + 1
        #END while

        motion = NaoMotion(self._name)
        motion.init(names, times, keys, self._method)
        return motion
    #END applyRepeat()

    def applySpeed(self, timeModifier):
        names = list()
        times = list()
        keys = list()

        i = 0
        while i < len(self._names):
            names.append(self._names[i])
            time = list()
            for v in self._times[i]:
                time.append(v * timeModifier)
            #END for
            times.append(time)
            keys.append(self._keys[i])
            i = i + 1
        #END while

        motion = NaoMotion(self._name)
        motion.init(names, times, keys, self._method)
        return motion
    #END applySpeed()

    def init(self, names, times, keys, method):
        for value in names:
            self._names.append(value)
        #END for
        for value in times:
            self._times.append(value)
        #END for
        for value in keys:
            self._keys.append(value)
        #END for
        self._method = method
    #END _init()
#END class
