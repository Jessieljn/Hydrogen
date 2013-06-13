from PyQt4 import QtCore
from ActionQueue import ActionQueue
from ThreadTimer import ThreadTimer


class ActionModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, nao):
        super(ActionModel, self).__init__(parent)
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
        self._list.enqueue(actions)
    #END addActions()

    def clearActions(self):
        self._list.clear()
    #END clearActions()

    def isRunning(self):
        return self._list.isRunning()
    #END isRunning()

    def removeAction(self, index):
        self._list.remove(index)
    #END removeAction()

    def setAutorun(self, value):
        self._list.setAutorun(value)
    #END setAutorun()

    def setRunning(self, value):
        self._list.setRunning(value)
    #END setRunning()

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

    def rowCount(self, parent):
        return self._list.length()
    #END rowCount()

    def on__list_cleared(self, length):
        parent = QtCore.QModelIndex()
        self.beginRemoveRows(parent, 0, length - 1)
        self.endRemoveRows()
    #END on__list_cleared()

    def on__list_dequeued(self, index):
        parent = QtCore.QModelIndex()
        self.beginRemoveRows(parent, index, index)
        self.endRemoveRows()
    #END on__list_dequeued()

    def on__list_enqueued(self, index):
        parent = QtCore.QModelIndex()
        self.beginInsertRows(parent, index, index)
        self.endInsertRows()
    #END on__list_enqueued()
#END class
