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

    def _init(self, names, times, keys):
        for v in names:
            self._names.append(v)
        for v in times:
            self._times.append(v)
        for v in keys:
            self._keys.append(v)
    #END _init()
#END class
