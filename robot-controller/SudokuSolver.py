
class SudokuSolver(object):
    def __init__(self, board = None):
        self._board = list()
        self._cans = list()
        for i in range(9):
            self._board.append(list())
            self._cans.append(list())
            for j in range(9):
                self._board[i].append(0)
                self._cans[i].append(dict())
                for k in range(1, 10):
                    self._cans[i][j][k] = True
                #END for
            #END for
        #END for

        if board is not None:
            for i in range(9):
                for j in range(9):
                    self.set(j + 1, i + 1, board[i][j])
                #END for
            #END for
        #END if
    #END __init__()

    def clear(self):
        for i in range(9):
            for j in range(9):
                self._board[i][j] = 0
                for k in range(1, 10):
                    self._cans[i][j][k] = True
                #END for
            #END for
        #END for
    #END clear()

    def get(self, x, y):
        return self._board[y - 1][x - 1]
    #END get()

    def set(self, x, y, value):
        if self._board[y - 1][x - 1] != 0:
            # we need to rebuild the map
            self._board[y - 1][x - 1] = 0
            self._rebuildCandidates()
        #END if
        self._board[y - 1][x - 1] = value
        self._removeCandidates(y - 1, x - 1, value)
    #END set()

    def solveOne(self):
        for i in range(9):
            for j in range(9):
                count = 0
                value = 0
                for k in range(1, 10):
                    if self._cans[i][j][k]:
                        count = count + 1
                        value = k
                    #END if
                #END for
                if count == 1:
                    self.set(j + 1, i + 1, value)
                    return j + 1, i + 1, value
                #END if
            #END for
        #END for

        # TODO Add complex methods to solve

        return 0, 0, 0
    #END solveOne()

    def printBoard(self):
        for i in range(9):
            txt = ""
            for j in range(9):
                txt = txt + str(self._board[i][j]) + " "
            #END for
            print txt
        #END for
    #END printBoard()

    def _rebuildCandidates(self):
        self._board = list()
        for i in range(9):
            self._board.append(list())
            for j in range(9):
                for k in range(1, 10):
                    self._cans[i][j][k] = True
                #END for
            #END for
        #END for
        for i in range(9):
            for j in range(9):
                self._removeCandidates(i, j, self._board[i][j])
            #END for
        #END for
    #END _rebuildCandidates()

    def _removeCandidates(self, y, x, value):
        if 1 <= value and value <= 9:
            for i in range(1, 10):
                self._cans[y][x][i] = False
            #END for
            for i in range(9):
                self._cans[y][i][value] = False
            #END for
            for i in range(9):
                self._cans[i][x][value] = False
            #END for
            for i in range((y / 3) * 3, (y / 3 + 1) * 3):
                for j in range((x / 3) * 3, (x / 3 + 1) * 3):
                    self._cans[i][j][value] = False
                #END for
            #END for
        #END if
    #END _removeCandidates()
#END class
