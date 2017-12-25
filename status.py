import board
import help

boardmatrix = [[" " for x in range(1, board.height + 1)]
               for x in range(1, board.width + 1)]


def reset(setting):
    if setting == "empty":
        boardmatrix = [[" " for x in range(board.height + 1)]
                       for x in range(board.width + 1)]
    if setting == "start":
        boardmatrix = [[" " for x in range(board.height + 1)]
                       for x in range(board.width + 1)]
        startPosition()


def startPosition():

    # white
    boardmatrix[0][0], boardmatrix[7][0] = "wR", "wR"
    boardmatrix[1][0], boardmatrix[6][0] = "wN", "wN"
    boardmatrix[2][0], boardmatrix[5][0] = "wB", "wB"
    boardmatrix[3][0], boardmatrix[4][0] = "wQ", "wK"

    for i in range(0, board.width):
        boardmatrix[i][1] = "wP"

    # black
    boardmatrix[0][7], boardmatrix[7][7] = "bR", "bR"
    boardmatrix[1][7], boardmatrix[6][7] = "bN", "bN"
    boardmatrix[2][7], boardmatrix[5][7] = "bB", "bB"
    boardmatrix[3][7], boardmatrix[4][7] = "bQ", "bK"

    for i in range(0, board.width):
        boardmatrix[i][6] = "bP"


#("start")
# drawMatrix()
