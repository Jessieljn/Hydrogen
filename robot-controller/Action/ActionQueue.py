from PyQt4 import QtCore
from ActionStart import ActionStart
from ActionStop import ActionStop
from BaseAction import BaseAction
from StopMotion import StopMotion
from StopSpeech import StopSpeech


class ActionQueue(QtCore.QObject):
    def __init__(self, nao):
        super(ActionQueue, self).__init__()
        self._autorun = False
        self._list = []
        self._nao = nao
        self._mutex = QtCore.QMutex()
        self._running = False
    #END __init__()

    cleared = QtCore.pyqtSignal(int)

    dequeued = QtCore.pyqtSignal(int)

    enqueued = QtCore.pyqtSignal(int)

    removed = QtCore.pyqtSignal(int)

    def clear(self):
        self._mutex.lock()
        length = len(self._list)
        while len(self._list) > 0:
            self._list.pop(0)
        #END while
        self._mutex.unlock()
        self.cleared.emit(length)
    #END clear()

    def dequeue(self):
        self._mutex.lock()
        item = None
        if len(self._list) > 0:
            item = self._list.pop(0)
        #END if
        self._mutex.unlock()
        self.dequeued.emit(0)
        return item
    #END dequeue()

    def enprior(self, actions):
        self._enqueue(actions, True)
    #END enprior()

    def enqueue(self, actions):
        self._enqueue(actions, False)
    #END enqueue()

    def execute(self):
        if self._running:
            item = self.dequeue()
            if item is None or isinstance(item, ActionStop):
                self._running = False
            elif self._nao is not None and self._nao.isConnected():
                item.execute(self._nao)
            #END if
        #END if
    #END execute()

    def get(self, index):
        self._mutex.lock()
        item = None
        if index < len(self._list):
            item = self._list[index]
        self._mutex.unlock()
        return item
    #END get()

    def isRunning(self):
        return self._running
    #END isRunning()

    def length(self):
        self._mutex.lock()
        length = len(self._list)
        self._mutex.unlock()
        return length
    #END length()

    def peek(self):
        return self.get(0)
    #END peek()

    def remove(self, index):
        if 0 <= index:
            self._mutex.lock()
            if index < len(self._list):
                self._list.pop(index)
            #END if
            self._mutex.unlock()
            self.removed.emit(index)
        #END if
    #END remove()

    def setAutorun(self, value):
        self._autorun = value
    #END setAutorun()

    def setRunning(self, value):
        self._running = value
    #END setRunning()

    def _enqueue(self, actions, prior):
        run_queue = False
        self._mutex.lock()
        if actions is None:
            return
        elif isinstance(actions, ActionStart):
            run_queue = True
        elif isinstance(actions, BaseAction):
            if prior:
                self._list.insert(0, actions)
            else:
                self._list.append(actions)
            #END if
        else:
            for action in actions:
                if action is None:
                    return
                elif isinstance(action, ActionStart):
                    run_queue = True
                elif prior:
                    self._list.insert(0, action)
                else:
                    self._list.append(action)
                #END if
            #END for
        #END if
        self._mutex.unlock()
        self._running = self._autorun or self._running or run_queue
        self.enqueued.emit(0)
    #END _enqueue()
#END class
