from PyQt4 import QtCore
from Action import Action


class ActionModel(QtCore.QAbstractTableModel):
    def __init__(self, parent):
        super(ActionModel, self).__init__(parent)
        self._list = []
    #END __init__()

    def enqueue(self, action):
        self._list.append(action)
    #END enqueue()

    dequeue = QtCore.pyqtSignal(Action)

    def startProcessing(self):
        self._timerID = self.startTimer(1000 / 100)
    #END startProcessing

    def stopProcessing(self):
        self.killTimer(self._timerID)
    #END stopProcessing

    def rowCount(self, parent):
        return len(self._list)
    #END rowCount()

    def columnCount(self, parent):
        return 2
    #END columnCount()

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return self._list[index.row()].actionToString()
            else:
                return self._list[index.row()].paramToString()
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
        if len(self._list) > 0:
            self.dequeue.emit(self._list.pop(0))
    #END timerEvent
#END class