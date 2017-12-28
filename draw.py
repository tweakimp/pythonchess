import board
import help


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
        # drawn matrix is 1 higher and wider then board.matrix
        black = board.matrix[j - 1][board.height - i - 1]
        printPiece(black)
        print(f"\033[1;31m]\033[0m", end="")
    else:
        print(f"\033[1;91m[\033[0m", end="")
        # drawn matrix is 1 higher and wider then board.matrix
        white = board.matrix[j - 1][board.height - i - 1]
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
        print(f" ", end="")


board.reset("start")
drawMatrix()
