from PyQt4 import QtCore
from ActionQueue import ActionQueue
from AutoRunAction import AutoRunAction
from BaseAction import BaseAction
from ThreadTimer import ThreadTimer


class ActionModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, nao):
        super(ActionModel, self).__init__(parent)
        self._autorun = False
        self._list = ActionQueue(nao)
        self._list.cleared.connect(self.on__list_cleared)
        self._list.dequeued.connect(self.on__list_dequeued)
        self._list.enqueued.connect(self.on__list_enqueued)
        self._list.removed.connect(self.on__list_dequeued)
        self._timer = ThreadTimer()
        self._timer.start()
        self._timer.addToThread(self._list)
        self._timer.timeElapsed.connect(self._list.execute)
    #END __init__()

    def dispose(self):
        self._timer.stop()
    #END dispose()

    def addActions(self, actions):
        run_queue = self._autorun
        if actions is None:
            pass
        elif isinstance(actions, AutoRunAction):
            run_queue = True
        elif isinstance(actions, BaseAction):
            self._timer.addToThread(actions)
            self._list.enqueue(actions)
        else:
            for act in actions:
                if isinstance(act, AutoRunAction):
                    run_queue = True
                else:
                    self._timer.addToThread(act)
                    self._list.enqueue(act)
                #END if
            #END for
        #END if
        if run_queue:
            self._list.setRunning(True)
        #END if
    #END addAction()

    def clearActions(self):
        self._list.setRunning(False)
        self._list.clear()
    #END clearActions()

    def isRunning(self):
        return self._list.isRunning()
    #END isRunning()

    def removeAction(self, index):
        self._list.remove(index)
    #END removeAction()

    def runActions(self):
        self._list.setRunning(True)
    #END runActions()

    def setAutoRun(self, enabled):
        self._autorun = enabled
    #END setAutoRun()

    def rowCount(self, parent):
        return self._list.length()
    #END rowCount()

    def columnCount(self, parent):
        return 2
    #END columnCount()

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            item = self._list.get(index.row())
            if index.column() == 0:
                return item.actionToString()
            else:
                return item.paramToString()
            #END if
        #END if
        return QtCore.QVariant()
    #END data()

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section == 0:
                    return "Action"
                else:
                    return "Parameter"
            else:
                return section
            #END if
        #END if
        return QtCore.QVariant()
    #END headerData()

    def on__list_cleared(self, length):
        parentIndex = QtCore.QModelIndex()
        self.beginRemoveRows(parentIndex, 0, length - 1)
        self.endRemoveRows()
    #END on__list_cleared()

    def on__list_dequeued(self, index):
        parentIndex = QtCore.QModelIndex()
        self.beginRemoveRows(parentIndex, index, index)
        self.endRemoveRows()
    #END on__list_dequeued()

    def on__list_enqueued(self, index):
        parentIndex = QtCore.QModelIndex()
        self.beginInsertRows(parentIndex, index, index)
        self.endInsertRows()
    #END on__list_enqueued()
#END class
