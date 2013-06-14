from PyQt4 import QtCore
from PyQt4 import QtGui
from SubmittableLineEdit import SubmittableLineEdit


class SudokuBoard(QtGui.QWidget):
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
                layout.addWidget(self._subgrids[i][j], i, j, 1, 1)
            #END for
        #END for
    #END __init__()

    valueChanged = QtCore.pyqtSignal(int, int, int)

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
        # TODO
        self.valueChanged.emit(0, 0, 0)
    #END solveOne()

    def set(self, i, j, value):
        value = value % 10
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
#END class
