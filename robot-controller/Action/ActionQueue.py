from PyQt4 import QtCore


class ActionQueue(QtCore.QObject):
    def __init__(self, nao = None):
        super(ActionQueue, self).__init__()
        self._list = []
        self._mutex = QtCore.QMutex()
        self._nao = nao
    #END __init__()

    cleared = QtCore.pyqtSignal(int)

    dequeued = QtCore.pyqtSignal(int)

    enqueued = QtCore.pyqtSignal(int)

    def clear(self):
        self._mutex.lock()
        length = len(self._list)
        self._list = []
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

    def enqueue(self, action):
        self._mutex.lock()
        index = len(self._list)
        self._list.append(action)
        self._mutex.unlock()
        self.enqueued.emit(index)
    #END enqueue()

    def execute(self):
        item = self.dequeue()
        if item is not None and self._nao is not None and self._nao.isConnected():
            item.execute(self._nao)
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

    def length(self):
        self._mutex.lock()
        length = len(self._list)
        self._mutex.unlock()
        return length
    #END length()

    def peek(self):
        return self.get(0)
    #END peek()

    def setNao(self, nao):
        self._nao = nao
    #END setNao()
#END class
