import time

input_board = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 4, 0, 0, 7, 0, 0, 3, 0,
    1, 0, 8, 5, 0, 0, 6, 0, 4,
    0, 0, 6, 0, 0, 0, 0, 0, 3,
    0, 1, 0, 0, 8, 0, 0, 4, 0,
    5, 0, 0, 0, 0, 0, 1, 0, 0,
    6, 0, 7, 0, 0, 2, 9, 0, 5,
    0, 8, 0, 0, 1, 0, 0, 2, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

board_size = 9
subsquare_width = 3
subsquare_height = 3

start_time = time.time()


def pretty_print(board, board_size):
    print
    for i in range(board_size):
        print board[i * board_size:i * board_size + board_size]


col_labels = [i % board_size for i in range(len(input_board))]
row_labels = [i / board_size for i in range(len(input_board))]
sqr_labels = [(board_size / subsquare_width) * (row_labels[i] / subsquare_height) + col_labels[i] / subsquare_width for
              i in range(len(input_board))]


def solve(board):
    # noinspection PyBroadException
    try:
        i = board.index(0)
    except:
        pretty_print(board, board_size)
        return
    bag = [board[j] for j in filter(lambda x: (col_labels[i] == col_labels[x]) or (row_labels[i] == row_labels[x]) or (
        sqr_labels[i] == sqr_labels[x]), range(len(board)))]
    for j in filter(lambda x: x not in bag, range(1, board_size + 1)):
        board[i] = j
        solve(board)
        board[i] = 0
solve(input_board)

end_time = time.time()

print
print "Time it took: "
print (end_time - start_time)