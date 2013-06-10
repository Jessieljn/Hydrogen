from PyQt4 import QtCore


class ThreadTimer(QtCore.QObject):
    THREAD_SLEEP_INTERVAL = 7

    def __init__(self, parent = None, interval = 100):
        super(ThreadTimer, self).__init__(parent)
        self._thread = None
        self._interval = interval
        self._running = False
    #END __init__()

    timeElapsed = QtCore.pyqtSignal()

    def addToThread(self, obj):
        if self._thread is not None:
            obj.moveToThread(self._thread)
        #END if
    #END addToThread()

    def interval(self):
        return self._interval
    #END interval()

    def isRunning(self):
        return self._running
    #END isRunning()

    def setInterval(self, value):
        self._interval = value
    #END setInterval()

    def start(self):
        if self._thread is None:
            self._running = True
            self._thread = QtCore.QThread()
            self.moveToThread(self._thread)
            self.connect(self._thread, QtCore.SIGNAL("started()"), self._process)
            self._thread.start()
        #END if
    #END start()

    def stop(self):
        if self._thread is not None:
            self._running = False
            self._thread.quit()
            self._thread.wait()
            self._thread = None
        #END if
    #END stop()

    def _process(self):
        while self._running:
            end = QtCore.QTime.currentTime().addMSecs(self._interval)
            self.timeElapsed.emit()
            while self._running and QtCore.QTime.currentTime() < end:
                QtCore.QThread.msleep(ThreadTimer.THREAD_SLEEP_INTERVAL)
            #END while
        #END while
        self._running = False
    #END _process()
#END class