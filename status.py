import board
import help

boardmatrix = [["  " for x in range(1, board.height + 1)]
               for y in range(1, board.width + 1)]


def reset(setting):
    global boardmatrix
    if setting == "empty":
        boardmatrix = [["  " for x in range(1, board.height + 1)]
                       for x in range(1, board.width + 1)]
    elif setting == "start":
        boardmatrix = [["  " for x in range(1, board.height + 1)]
                       for x in range(1, board.width + 1)]
        startPosition()
    else:
        print("Something failed.")
