from PyQt4 import QtCore
from PyQt4 import QtGui


###
# ActionListWidget.py
#
# Creates the list of current actions being pushed to the NAO.
###
class ActionListWidget(QtGui.QWidget):
    def __init__(self, parent, model):
        super(ActionListWidget, self).__init__(parent)

        self._table = QtGui.QTableView(self)
        self._table.setModel(model)
        self._table.setColumnWidth(0, 100)
        self._table.setColumnWidth(1, 180)
        self._table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self._table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self._table.verticalHeader().setVisible(False)

        self._cbAuto = QtGui.QCheckBox("Auto Run (Ctrl+T)", self)
        self._cbAuto.setShortcut("Ctrl+T")
        self._cbAuto.clicked.connect(lambda: model.setAutorun(self._cbAuto.isChecked()))

        self._btnRun = QtGui.QPushButton("Run (Ctrl+R)", self)
        self._btnRun.setShortcut("Ctrl+R")
        self._btnRun.clicked.connect(lambda: model.setRunning(True))

        self._btnStop = QtGui.QPushButton("Stop (Ctrl+S)", self)
        self._btnStop.setShortcut("Ctrl+S")
        self._btnStop.clicked.connect(lambda: model.setRunning(False))

        layoutControls = QtGui.QHBoxLayout()
        layoutControls.addWidget(self._cbAuto)
        layoutControls.addWidget(self._btnRun)
        layoutControls.addWidget(self._btnStop)

        self._btnClear = QtGui.QPushButton("Clear (Ctrl+Space)", self)
        self._btnClear.setShortcut("Ctrl+Space")
        self._btnClear.clicked.connect(model.clearActions)

        self._btnDelete = QtGui.QPushButton("Delete (Ctrl+D)", self)
        self._btnDelete.setShortcut("Ctrl+D")
        self._btnDelete.clicked.connect(lambda: model.removeAction(self._table.currentIndex().row()))

        self._btnEdit = QtGui.QPushButton("Edit (Ctrl+E)", self)
        self._btnEdit.setShortcut("Ctrl+E")
        self._btnEdit.clicked.connect(self.editClicked)

        layoutModifiers = QtGui.QHBoxLayout()
        layoutModifiers.addWidget(self._btnClear)
        layoutModifiers.addWidget(self._btnDelete)
        layoutModifiers.addWidget(self._btnEdit)

        layoutMain = QtGui.QVBoxLayout(self)
        layoutMain.setMargin(0)
        layoutMain.addWidget(self._table)
        layoutMain.addLayout(layoutControls)
        layoutMain.addLayout(layoutModifiers)
    #END __init__()

    editClicked = QtCore.pyqtSignal()

    # noinspection PyUnusedLocal
    def resizeEvent(self, event):
        self._table.setColumnWidth(1, self._table.width() - self._table.columnWidth(0) - 24)
    #END resizeEvent()
#END ActionListWidget.py