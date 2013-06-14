from PyQt4 import QtCore
from PyQt4 import QtGui


class SudokuBoard(QtGui.QWidget):
    def __init__(self, parent = None):
        super(SudokuBoard, self).__init__(parent)
        self._boxes = []
        self._subgrids = []

        for i in range(9):
            self._boxes.append([])
            for j in range(9):
                self._boxes[i].append(QtGui.QLineEdit())
                self._boxes[i][j].setAlignment(QtCore.Qt.AlignCenter)
                self._boxes[i][j].setFixedSize(30, 30)
                self._boxes[i][j].setInputMask("0")
                self._boxes[i][j].setMaxLength(1)
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

    def set(self, i, j, value):
        value = value % 10
        if value == 0:
            self._boxes[i][j].setText("")
        else:
            self._boxes[i][j].setText(str(value))
        #END if
    #END set()
#END class
