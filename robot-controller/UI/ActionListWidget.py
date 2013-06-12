from PyQt4 import QtCore
from PyQt4 import QtGui


class ActionListWidget(QtGui.QWidget):
    def __init__(self, parent, model):
        super(ActionListWidget, self).__init__(parent)

        self._table = QtGui.QTableView(self)
        self._table.setModel(model)
        self._table.setColumnWidth(0, 100)
        self._table.setColumnWidth(1, 180)

        self._cbAuto = QtGui.QCheckBox("Auto Run (Ctrl+T)", self)
        self._cbAuto.setShortcut("Ctrl+T")

        self._btnRun = QtGui.QPushButton("Run (Ctrl+R)", self)
        self._btnRun.setShortcut("Ctrl+R")
        self._btnRun.clicked.connect(self.runClicked)

        layoutRunButtons = QtGui.QHBoxLayout()
        layoutRunButtons.addWidget(self._cbAuto)
        layoutRunButtons.addWidget(self._btnRun)

        self._btnClear = QtGui.QPushButton("Clear (Ctrl+Space)", self)
        self._btnClear.setShortcut("Ctrl+Space")
        self._btnClear.clicked.connect(self.clearClicked)

        self._btnDelete = QtGui.QPushButton("Delete (Ctrl+D)", self)
        self._btnDelete.setShortcut("Ctrl+D")
        self._btnDelete.clicked.connect(self.clearClicked)

        self._btnEdit = QtGui.QPushButton("Edit (Ctrl+E)", self)
        self._btnEdit.setShortcut("Ctrl+E")
        self._btnEdit.clicked.connect(self.clearClicked)

        layoutModifyButtons = QtGui.QHBoxLayout()
        layoutModifyButtons.addWidget(self._btnClear)
        layoutModifyButtons.addWidget(self._btnDelete)
        layoutModifyButtons.addWidget(self._btnEdit)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._table)
        layoutMain.addLayout(layoutRunButtons)
        layoutMain.addLayout(layoutModifyButtons)
    #END __init__()

    clearClicked = QtCore.pyqtSignal()

    runClicked = QtCore.pyqtSignal()

    def resizeEvent(self, event):
        self._table.setColumnWidth(1, self._table.width() - self._table.columnWidth(0) - 44)
    #END resizeEvent()
#END class
