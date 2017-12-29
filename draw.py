import board
import helper

col = ["\033[0m", "\033[1;91m", "\033[1;31m", "\033[1;97m"]


def printMatrix():
    for line in board.matrix:
        print(line)


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
                        f"{col[1]}{helper.num2let(j)}{col[0]}", end="  ")
            else:
                if j == 0:
                    # left number column
                    print(f"{col[1]}{board.height-i}{col[0]}", end=" ")
                else:
                    # squares
                    printSquare(j, i)
        print("")


def printSquare(j, i):
    # drawn matrix is 1 higher and wider then board.matrix
    if((j + board.height - i) % 2 == 1):
        print(f"{col[1]}[{col[0]}", end="")
        white = board.matrix[j - 1][board.height - i - 1]
        printPiece(white)
        print(f"{col[1]}]{col[0]}", end="")
    else:
        print(f"{col[2]}[{col[0]}", end="")
        black = board.matrix[j - 1][board.height - i - 1]
        printPiece(black)
        print(f"{col[2]}]{col[0]}", end="")


def printPiece(x):
    if x[0] == "w":
        print(f"{col[3]}", end="")
        print(f"{x[1:]}", end="")
        print(f"{col[0]}", end="")
    elif x[0] == "b":
        print(f"{col[0]}", end="")
        print(f"{x[1:]}", end="")
        print(f"{col[0]}", end="")
    else:
        print(f" ", end="")


# board.reset("start")
# drawMatrix()
