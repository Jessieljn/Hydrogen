from PyQt4 import QtCore
from PyQt4 import QtGui
from SubmittableLineEdit import SubmittableLineEdit
from SudokuSolver import SudokuSolver


class SudokuBoard(QtGui.QWidget):

    valueChanged = QtCore.pyqtSignal(int, int, int)

    def __init__(self, parent = None):
        super(SudokuBoard, self).__init__(parent)
        self._boxes = []
        self._subgrids = []

        for i in range(9):
            self._boxes.append([])
            for j in range(9):
                self._boxes[i].append(SubmittableLineEdit())
                self._boxes[i][j].setAlignment(QtCore.Qt.AlignCenter)
                self._boxes[i][j].setFixedSize(30, 30)
                self._boxes[i][j].setInputMask("0")
                self._boxes[i][j].setMaxLength(1)
                self._boxes[i][j].inputCancelled.connect(self._on_box_inputCancelled)
                self._boxes[i][j].textSubmitted.connect(self._on_box_textSubmitted)
            #END for
        #END for

        layout = QtGui.QGridLayout(self)
        layout.setMargin(0)
        layout.setHorizontalSpacing(5)
        layout.setVerticalSpacing(5)

        for i in range(3):
            widgetLabel = QtGui.QWidget()
            widgetLabel.setMaximumHeight(20)
            layoutLabel = QtGui.QGridLayout(widgetLabel)
            layoutLabel.setMargin(1)
            layoutLabel.setHorizontalSpacing(1)
            layoutLabel.setVerticalSpacing(1)
            layoutLabel.addWidget(QtGui.QLabel(chr(ord('A') + i * 3 + 0)), 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
            layoutLabel.addWidget(QtGui.QLabel(chr(ord('A') + i * 3 + 1)), 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
            layoutLabel.addWidget(QtGui.QLabel(chr(ord('A') + i * 3 + 2)), 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
            layout.addWidget(widgetLabel, 0, i + 1, 1, 1)

            widgetLabel = QtGui.QWidget()
            widgetLabel.setMaximumWidth(20)
            layoutLabel = QtGui.QGridLayout(widgetLabel)
            layoutLabel.setMargin(1)
            layoutLabel.setHorizontalSpacing(1)
            layoutLabel.setVerticalSpacing(1)
            layoutLabel.addWidget(QtGui.QLabel(str(i * 3 + 1)), 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
            layoutLabel.addWidget(QtGui.QLabel(str(i * 3 + 2)), 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
            layoutLabel.addWidget(QtGui.QLabel(str(i * 3 + 3)), 2, 0, 1, 1, QtCore.Qt.AlignVCenter)
            layout.addWidget(widgetLabel, i + 1, 0, 1, 1)

            self._subgrids.append([])
            for j in range(3):
                self._subgrids[i].append(QtGui.QFrame(self))
                self._subgrids[i][j].setAutoFillBackground(True)
                self._subgrids[i][j].setLineWidth(4)
                self.highlightSubgrid(i, j)
                layoutGrid = QtGui.QGridLayout(self._subgrids[i][j])
                layoutGrid.setMargin(1)
                layoutGrid.setHorizontalSpacing(1)
                layoutGrid.setVerticalSpacing(1)
                for k in range(i * 3, (i + 1) * 3):
                    for l in range(j * 3, (j + 1) * 3):
                        layoutGrid.addWidget(self._boxes[k][l], k % 3, l % 3, 1, 1)
                    #END for
                #END for
                layout.addWidget(self._subgrids[i][j], i + 1, j + 1, 1, 1)
            #END for
        #END for
    #END __init__()

    def focus(self, i, j):
        self._boxes[i][j].setFocus()
    #END focus()

    def get(self, i, j):
        if self._boxes[i][j].text() == "":
            return 0
        return int(self._boxes[i][j].text())
    #END get()

    def highlightBox(self, i, j, color = QtGui.QColor(255, 255, 255)):
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Base, color)
        self._boxes[i][j].setPalette(palette)
    #END highlightSubgrid()

    def highlightSubgrid(self, i, j, color = QtGui.QColor(255, 255, 255)):
        palette = QtGui.QPalette(self.palette())
        palette.setColor(QtGui.QPalette.Window, color)
        self._subgrids[i][j].setPalette(palette)
    #END highlightSubgrid()

    def solveOne(self):
        solver = SudokuSolver()
        for i in range(9):
            for j in range(9):
                txt = self._boxes[i][j].text()
                value = 0
                if txt != "":
                    value = int(txt)
                #END if
                solver.set(j + 1, i + 1, value)
            #END for
        #END for
        j, i, value = solver.solveOne()
        if value == 0:
            self.valueChanged.emit(0, 0, 0)
        else:
            self._boxes[i - 1][j - 1].setText(str(value))
            self.valueChanged.emit(i - 1, j - 1, value)
        #END if
    #END solveOne()

    def set(self, i, j, value):
        value %= 10
        if value == 0:
            self._boxes[i][j].setText("")
        else:
            self._boxes[i][j].setText(str(value))
        #END if
    #END set()

    def _on_box_inputCancelled(self):
        self.setFocus()
    #END _on_box_inputCancelled()

    def _on_box_textSubmitted(self):
        for i in range(9):
            for j in range(9):
                if self.sender() == self._boxes[i][j]:
                    txt = self._boxes[i][j].text()
                    if txt == "":
                        self.valueChanged.emit(i, j, 0)
                    else:
                        self.valueChanged.emit(i, j, int(txt))
                    #END if
                    self.setFocus()
                    return
                #END if
            #END for
        #END for
    #END _on_box_textSubmitted()
#END SudokuBoard.py