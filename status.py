import board
import help

'''
def createMatrix():
'''

boardmatrix = [[" " for x in range(board.height + 1)]
               for x in range(board.width + 1)]
# print(boardmatrix)


def startPosition():

    # white
    boardmatrix[1][1], boardmatrix[8][1] = "R", "R"
    boardmatrix[2][1], boardmatrix[7][1] = "N", "N"
    boardmatrix[3][1], boardmatrix[6][1] = "B", "B"
    boardmatrix[4][1], boardmatrix[5][1] = "Q", "K"
    for i in range(board.width + 1):
        boardmatrix[i][2] = "P"

    # black
    boardmatrix[1][8], boardmatrix[8][8] = "r", "r"
    boardmatrix[2][8], boardmatrix[7][8] = "n", "n"
    boardmatrix[3][8], boardmatrix[6][8] = "b", "b"
    boardmatrix[4][8], boardmatrix[5][8] = "q", "k"
    for i in range(board.width + 1):
        boardmatrix[i][7] = "p"


startPosition()

for i in range(0, board.height + 1):
    for j in range(0, board.width + 1):
        if i == board.height:
            if j == 0:
                print(" # ", end=" ")
            else:
                print(f" {help.numberToLetter(j)} ", end=" ")
        else:
            if j == 0:
                print(f" {board.height-i} ", end=" ")
            else:
                print(f"[{boardmatrix[j][board.height-i]}]", end=" ")
    print("")
