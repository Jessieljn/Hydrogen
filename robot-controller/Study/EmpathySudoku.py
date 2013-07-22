SudokuBoards = \
    [
        [
            # Training board
            [0, 7, 8, 4, 9, 0, 1, 3, 5],
            [9, 1, 5, 8, 0, 6, 7, 0, 4],
            [3, 2, 4, 7, 1, 5, 0, 9, 8],
            [5, 0, 6, 3, 7, 4, 9, 1, 2],
            [1, 0, 7, 6, 2, 8, 0, 5, 0],
            [4, 0, 2, 9, 5, 1, 8, 6, 7],
            [0, 4, 9, 0, 6, 3, 5, 0, 1],
            [8, 5, 3, 1, 4, 9, 2, 7, 6],
            [2, 0, 1, 5, 8, 0, 3, 0, 9],
        ], [ # Game 1
            [0, 3, 0, 8, 0, 0, 0, 0, 0],
            [9, 0, 5, 6, 0, 0, 7, 0, 0],
            [0, 0, 1, 0, 9, 3, 2, 0, 0],
            [8, 0, 6, 5, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 7, 2, 3, 0, 6, 9, 5, 0],
            [0, 1, 9, 4, 8, 7, 0, 6, 0],
            [3, 6, 8, 2, 5, 9, 0, 1, 0],
        ], [ # Game 2
            [1, 5, 0, 0, 0, 0, 9, 2, 4],
            [0, 0, 4, 0, 0, 0, 7, 0, 6],
            [0, 0, 0, 0, 0, 0, 3, 8, 5],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 2, 0, 3, 0, 0, 0, 6, 0],
            [0, 0, 6, 7, 0, 0, 4, 0, 3],
            [0, 0, 2, 4, 0, 0, 5, 3, 1],
            [0, 0, 7, 2, 0, 3, 6, 9, 8],
            [0, 8, 3, 0, 0, 1, 2, 4, 0],
        ], [ # Game 3
            [8, 0, 0, 0, 0, 2, 4, 3, 6],
            [3, 0, 0, 0, 7, 0, 9, 0, 2],
            [0, 0, 0, 1, 0, 0, 7, 8, 5],
            [0, 0, 0, 0, 8, 3, 0, 5, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 0, 3, 7, 9],
            [0, 2, 0, 0, 9, 0, 6, 4, 7],
            [0, 4, 0, 8, 0, 0, 1, 9, 0],
            [1, 0, 0, 4, 0, 0, 5, 2, 8],
        ], [ # Game 4
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [9, 0, 0, 1, 3, 7, 0, 0, 6],
            [0, 0, 7, 0, 0, 9, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 6, 4, 0, 2, 0, 0, 0],
            [1, 2, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 2, 3, 8, 4, 0],
            [2, 9, 8, 7, 4, 1, 3, 6, 0],
            [7, 0, 0, 6, 8, 5, 2, 9, 0],
        ], [ # Game 5
            [0, 7, 0, 4, 0, 0, 6, 0, 3],
            [0, 0, 0, 0, 0, 0, 8, 0, 0],
            [4, 6, 5, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 7, 3, 0, 0, 0, 0],
            [5, 0, 4, 0, 0, 0, 0, 0, 0],
            [8, 4, 3, 6, 5, 1, 9, 0, 2],
            [9, 0, 6, 3, 2, 7, 0, 0, 4],
            [2, 1, 7, 0, 4, 8, 3, 0, 6],
        ], [ # Game 6
            [0, 0, 0, 9, 3, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 4, 6, 0, 2, 7, 0, 0, 0],
            [6, 3, 0, 8, 9, 1, 2, 0, 5],
            [0, 0, 1, 0, 4, 5, 0, 0, 7],
            [2, 0, 0, 0, 0, 3, 0, 0, 8],
            [9, 0, 0, 0, 7, 2, 3, 0, 0],
            [4, 0, 2, 3, 5, 6, 1, 0, 0],
            [0, 0, 0, 4, 8, 9, 0, 0, 0],
        ], [ # Game 7
            [0, 3, 0, 9, 7, 5, 6, 0, 0],
            [0, 0, 0, 1, 8, 0, 9, 0, 0],
            [8, 0, 1, 4, 6, 3, 0, 0, 0],
            [0, 0, 0, 2, 3, 7, 0, 6, 0],
            [0, 0, 9, 5, 1, 6, 0, 4, 0],
            [0, 7, 0, 0, 9, 4, 2, 1, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 2, 1, 0, 0, 0],
            [1, 0, 6, 7, 5, 0, 0, 0, 0],
        ], [ # Game 8
            [6, 0, 5, 0, 2, 1, 0, 0, 8],
            [9, 0, 7, 5, 3, 8, 4, 0, 2],
            [2, 8, 3, 6, 4, 7, 9, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 6, 2, 0, 0, 0],
            [3, 0, 8, 0, 9, 0, 0, 0, 0],
            [0, 0, 6, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 2, 1, 0, 8, 0, 0],
            [0, 5, 0, 4, 0, 9, 2, 0, 0],
        ], [ # Game 9
            [0, 5, 0, 0, 0, 0, 9, 0, 0],
            [8, 6, 4, 9, 0, 0, 0, 0, 5],
            [3, 9, 1, 2, 7, 0, 6, 0, 8],
            [7, 0, 8, 0, 5, 0, 0, 0, 0],
            [5, 2, 3, 4, 0, 1, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 0, 0, 0],
            [9, 8, 2, 0, 0, 0, 0, 0, 0],
            [4, 3, 5, 6, 8, 0, 0, 0, 0],
            [1, 7, 0, 0, 0, 4, 8, 0, 0],
        ], [ # Game 10
            [0, 6, 0, 3, 7, 0, 9, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 8, 9, 0, 0, 7],
            [9, 0, 0, 6, 3, 4, 7, 0, 0],
            [4, 0, 0, 8, 0, 1, 0, 0, 0],
            [1, 0, 8, 7, 9, 5, 2, 0, 0],
            [0, 0, 0, 1, 5, 0, 0, 7, 8],
            [0, 0, 0, 9, 4, 7, 5, 0, 2],
            [0, 0, 0, 2, 6, 8, 0, 0, 4],
        ]
    ]
# END EmpathySudoku.py