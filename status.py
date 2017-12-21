import board
import help

boardmatrix = boardmatrix = [[" " for x in range(board.height + 1)]
                             for x in range(board.width + 1)]


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
    boardmatrix[1][1], boardmatrix[8][1] = "wR", "wR"
    boardmatrix[2][1], boardmatrix[7][1] = "wN", "wN"
    boardmatrix[3][1], boardmatrix[6][1] = "wB", "wB"
    boardmatrix[4][1], boardmatrix[5][1] = "wQ", "wK"

    for i in range(board.width + 1):
        boardmatrix[i][2] = "wP"

    # black
    boardmatrix[1][8], boardmatrix[8][8] = "bR", "bR"
    boardmatrix[2][8], boardmatrix[7][8] = "bN", "bN"
    boardmatrix[3][8], boardmatrix[6][8] = "bB", "bB"
    boardmatrix[4][8], boardmatrix[5][8] = "bQ", "bK"
    for i in range(board.width + 1):
        boardmatrix[i][7] = "bP"


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
        black = boardmatrix[j][board.height - i]
        printPiece(black)
        print(f"\033[1;31m]\033[0m", end="")
    else:
        print(f"\033[1;91m[\033[0m", end="")
        white = boardmatrix[j][board.height - i]
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
