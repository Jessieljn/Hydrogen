from PyQt4 import QtCore
from PyQt4 import QtGui


class ActionListWidget(QtGui.QWidget):
    def __init__(self, parent, model):
        super(ActionListWidget, self).__init__(parent)

        self._table = QtGui.QTableView(self)
        self._table.setModel(model)
        self._table.setColumnWidth(0, 100)
        self._table.setColumnWidth(1, 180)

        self._btnClear = QtGui.QPushButton("Clear", self)
        self._btnClear.clicked.connect(self.clearClicked)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._table)
        layoutMain.addWidget(self._btnClear)
    #END __init__()

    clearClicked = QtCore.pyqtSignal()
#END class
