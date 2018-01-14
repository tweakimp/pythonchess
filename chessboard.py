from string import ascii_uppercase


class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.files = ascii_uppercase[:self.width]
        self.ranks = str([x for x in range(1, self.height + 1)])
        self.piecelist = []
        self.boardmatrix = [["  " for h in range(0, self.height)]
                            for w in range(0, self.width)]

    def printInfo(self):
        print("width: ", self.width)
        print("height: ", self.height)
        print("files: ", self.files)
        print("ranks: ", self.ranks)
        print("piecelist: ", self.piecelist)
        print("boardmatrix: ")
        self.printMatrix()

    def resetBoard(self):
        self.boardmatrix = [["  " for h in range(0, self.height)]
                            for w in range(0, self.width)]

    def printMatrix(self):
        for line in self.boardmatrix:
            print(line)

    def drawBoard(self):
        # TODO create this
        pass

    def printPiecelist(self):
        # TODO create this
        pass

    def checkSquare(self, position):
        boardfile = self.files.index((position[0]).upper())
        boardrank = position[1:]
        if self.boardmatrix[int(boardfile) - 1][int(boardrank) - 1] == "  ":
            return None
        else:
            return str(self.boardmatrix[int(boardfile) - 1][int(boardrank) - 1])

    def underAttack(self, color):
        # TODO create this
        pass


if __name__ == '__main__':
    testboard = Board(8, 8)
    testboard.printInfo()

# def isEmpty(position):
#     readPos(position)
#     if matrix[int(file) - 1][int(rank) - 1] == "  ":
#         return True
#     else:
#         return False
#
#
# def squareColor(position):
#     readPos(position)
#     if (file + int(rank)) % 2 == 0:
#         return "black"
#     else:
#         return "white"
#
#
# def readPos(position):
#     global file, rank
#
#     return file, rank
