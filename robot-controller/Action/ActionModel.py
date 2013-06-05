from PyQt4 import QtCore
from Action import Action


class ActionModel(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        super(ActionModel, self).__init__(parent)
        self._list = []
        self._timerID = self.startTimer(250)
    #END __init__()

    def __del__(self):
        self.killTimer(self._timerID)
    #END __del()

    execute = QtCore.pyqtSignal(Action)

    def enqueue(self, action):
        parentIndex = QtCore.QModelIndex()
        self.beginInsertRows(parentIndex, len(self._list), len(self._list))
        self._list.append(action)
        self.endInsertRows()
    #END enqueue()

    def dequeue(self):
        parentIndex = QtCore.QModelIndex()
        self.beginRemoveRows(parentIndex, 0, 0)
        item = None
        if len(self._list) > 0:
            item = self._list.pop(0)
        #END if
        self.endRemoveRows()
        return item
    #END dequeue()

    def rowCount(self, parent):
        return len(self._list)
    #END rowCount()

    def columnCount(self, parent):
        return 2
    #END columnCount()

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if index.row() < len(self._list):
                if index.column() == 0:
                    return self._list[index.row()].actionToString()
                else:
                    return self._list[index.row()].paramToString()
                #END if
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

    def timerEvent(self, event):
        item = self.dequeue()
        if item is not None:
            self.execute.emit(item)
    #END timerEvent
#END class
