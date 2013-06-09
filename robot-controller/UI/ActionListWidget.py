from PyQt4 import QtCore
from PyQt4 import QtGui


class ActionListWidget(QtGui.QWidget):
    def __init__(self, parent, model):
        super(ActionListWidget, self).__init__(parent)

        self._table = QtGui.QTableView(self)
        self._table.setModel(model)
        self._table.setColumnWidth(0, 100)
        self._table.setColumnWidth(1, 180)

        self._btnClear = QtGui.QPushButton("Clear (Ctrl+Space)", self)
        self._btnClear.setShortcut("Ctrl+Space")
        self._btnClear.clicked.connect(self.clearClicked)
        self._btnRun = QtGui.QPushButton("Run (Ctrl+R)", self)
        self._btnRun.setShortcut("Ctrl+R")
        self._btnRun.clicked.connect(self.runClicked)

        layoutButtons = QtGui.QHBoxLayout()
        layoutButtons.addWidget(self._btnClear)
        layoutButtons.addWidget(self._btnRun)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._table)
        layoutMain.addLayout(layoutButtons)
    #END __init__()

    clearClicked = QtCore.pyqtSignal()

    runClicked = QtCore.pyqtSignal()

    def resizeEvent(self, event):
        self._table.setColumnWidth(1, self._table.width() - self._table.columnWidth(0) - 44)
    #END resizeEvent()
#END class
