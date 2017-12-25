import board
import help

boardmatrix = boardmatrix = [[" " for x in range(1, board.height + 1)]
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


def drawMatrix():

    for i in range(0, board.height + 1):
        for j in range(0, board.width + 1):
            if i == board.height:
                if j == 0:
                    # bottom left corner
                    print("", end="   ")
                else:
                    # bottom letter row
                    print(
                        f"\033[1;91m{help.numberToLetter(j)}\033[0m", end="  ")
            else:
                if j == 0:
                    # left number column
                    print(f"\033[1;91m{board.height-i}\033[0m", end=" ")
                else:
                    # squares
                    printSquare(j, i)

        print("")


def printSquare(j, i):
    if((j + board.height - i) % 2 == 0):
        print(f"\033[1;31m[\033[0m", end="")
        # drawn matrix is 1 higher and wider then boardmatrix
        black = boardmatrix[j - 1][board.height - i - 1]
        printPiece(black)
        print(f"\033[1;31m]\033[0m", end="")
    else:
        print(f"\033[1;91m[\033[0m", end="")
        # drawn matrix is 1 higher and wider then boardmatrix
        white = boardmatrix[j - 1][board.height - i - 1]
        printPiece(white)
        print(f"\033[1;91m]\033[0m", end="")


def printPiece(x):
    if x[0] == "w":
        print("\033[0;97m", end="")
        print(f"{x[1:]}", end="")
        print("\033[0m", end="")
    elif x[0] == "b":
        print("\033[0m", end="")
        print(f"{x[1:]}", end="")
        print("\033[0m", end="")
    else:
        print(f"{x}", end="")


reset("start")
drawMatrix()
