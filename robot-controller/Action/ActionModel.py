from PyQt4 import QtCore
from Action import Action
from ActionQueue import ActionQueue
from ThreadTimer import ThreadTimer


class ActionModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, nao):
        super(ActionModel, self).__init__(parent)
        self._list = ActionQueue(nao)
        self._list.dequeued.connect(self.on__list_dequeued)
        self._list.enqueued.connect(self.on__list_enqueued)
        self._timer = ThreadTimer()
        self._timer.start()
        self._timer.addToThread(self._list)
        self._timer.timeElapsed.connect(self._list.execute)
    #END __init__()

    def dispose(self):
        self._timer.stop()
    #END dispose()

    def addActions(self, actions):
        if actions is None:
            pass
        elif isinstance(actions, Action):
            self._timer.addToThread(actions)
            self._list.enqueue(actions)
        else:
            for act in actions:
                self._timer.addToThread(act)
                self._list.enqueue(act)
            #END for
        #END if
    #END addAction()

    def clearActions(self):
        parentIndex = QtCore.QModelIndex()
        self.beginRemoveRows(parentIndex, 0, self._list.length())
        self._list.clear()
        self.endRemoveRows()
    #END clearActions

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

    def on__list_dequeued(self, index):
        parentIndex = QtCore.QModelIndex()
        self.beginRemoveRows(parentIndex, 0, 0)
        self.endRemoveRows()
    #END on__list_dequeued()

    def on__list_enqueued(self, index):
        parentIndex = QtCore.QModelIndex()
        self.beginInsertRows(parentIndex, index, index)
        self.endInsertRows()
    #END on__list_enqueued()
#END class
