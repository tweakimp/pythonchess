import importlib
from random import choice
from string import ascii_uppercase

import lists
import pieces


class Chessboard():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.files = ascii_uppercase[:self.width]
        self.ranks = range(1, self.height + 1)
        self.piecelist = {}
        self.capturedlist = []
        self.matrix = [["  " for h in range(0, self.height)]
                       for w in range(0, self.width)]

    def printInfo(self):
        print("width: ", self.width)
        print("height: ", self.height)
        print("files: ", self.files)
        print("ranks: ", self.ranks)
        print("piecelistRAW: ", self.piecelist)
        self.printPiecelist()
        self.printMatrix()
        self.drawBoard()

    def movePiece(self, string, newposition):
        newposition = newposition.upper()
        for name, obj in self.piecelist.copy().items():
            if name == string or obj.position == string.upper():
                if newposition in obj.move(self):
                    obj.position = newposition
                else:
                    print(f"\033[91m{chr(9888)} {obj.name} on ", end="")
                    print(f"{obj.position} can't go to {newposition}!\033[0m")

    def deletePiece(self, string):
        for k, v in self.piecelist.copy().items():
            if k == string or v.position == string.upper():
                del self.piecelist[k]

    def resetMatrix(self):
        self.matrix = [["  " for h in range(0, self.height)]
                       for w in range(0, self.width)]

    def updateMatrix(self):
        self.resetMatrix()
        for key in self.piecelist:
            position = self.piecelist[key].position
            short = self.piecelist[key].short
            boardfile = int(self.files.index(position[0].upper()))
            boardrank = self.ranks.index(int(position[1:]))
            self.matrix[boardfile][boardrank] = short

    def printMatrix(self):
        print("matrix: ")
        for line in self.matrix:
            print(line)

    def printPiecelist(self):
        print("piecelist: ")
        if self.piecelist == {}:
            print("(empty)")
        else:
            printthis = []
            for key in self.piecelist:
                if self.piecelist[key].short[0] == "w":
                    name = "White "
                elif self.piecelist[key].short[0] == "b":
                    name = "Black "
                if self.piecelist[key].short[1] == "P":
                    name += "Pawn"
                elif self.piecelist[key].short[1] == "N":
                    name += "Knight"
                elif self.piecelist[key].short[1] == "B":
                    name += "Bishop"
                elif self.piecelist[key].short[1] == "R":
                    name += "Rook"
                elif self.piecelist[key].short[1] == "Q":
                    name += "Queen"
                elif self.piecelist[key].short[1] == "K":
                    name += "King"
                printthis.append(
                    self.piecelist[key].position.upper() + " " + name)
            # make it rectangualar by filling empty list entries
            missingentries = (3 - len(printthis) % 3) % 3
            for i in range(missingentries):
                printthis.append("")
            # make entries equally long
            columnwidth = max(len(row) for row in printthis) + 2
            for i in range(len(printthis)):
                difference = columnwidth - len(printthis[i])
                for j in range(difference):
                    printthis[i] += " "
            columnlength = len(printthis) // 3
            for i in range(columnlength):
                for j in range(3):
                    print(printthis[i + (j * columnlength)], end="")
                print("")

    def checkSquare(self, position):
        boardfile = int(self.files.index(position[0].upper()))
        boardrank = self.ranks.index(int(position[1:]))
        if self.matrix[int(boardfile) - 1][int(boardrank) - 1] == "  ":
            return None
        else:
            return str(self.matrix[int(boardfile) - 1][int(boardrank) - 1])

    def pieceShowMoves(self, string):
        for name, obj in self.piecelist.copy().items():
            if name == string or obj.position == string.upper():
                for move in obj.move(self):
                    boardfile = int(self.files.index(move[0].upper()))
                    boardrank = self.ranks.index(int(move[1:]))
                    self.matrix[boardfile][boardrank] = f"xX"

    def initiatePieces(self):
        # initiate pieces and update piecelist
        self.piecelist.update({name: pieces.Pawn(color, position)
                               for name, color, position in lists.pawns})
        self.piecelist.update({name: pieces.Knight(color, position)
                               for name, color, position in lists.knights})
        self.piecelist.update({name: pieces.Bishop(color, position)
                               for name, color, position in lists.bishops})
        self.piecelist.update({name: pieces.Rook(color, position)
                               for name, color, position in lists.rooks})
        self.piecelist.update({name: pieces.Queen(color, position)
                               for name, color, position in lists.queens})
        self.piecelist.update({name: pieces.King(color, position)
                               for name, color, position in lists.kings})
        # update matrix
        self.updateMatrix()

    def initTest(self):
        randomPos = str(choice(self.files)) + str(choice(self.ranks))
        self.piecelist.update({name: pieces.Knight(color, position)
                               for name, color, position in [
                               ["test", "w", f"{randomPos}"]]})
        # update matrix
        self.updateMatrix()

    def drawBoard(self):

        color = ["\033[0m", "\033[91m", "\033[31m", "\033[97m"]

        def printPiece(x):
            codedict = {"K": "♔", "Q": "♕", "R": "♜",
                        "B": "♝", "N": "♞", "P": "♟"}
            if x[0] == "w":
                print(f"{color[3]}{codedict[x[1]]}{color[0]}", end="")
            elif x[0] == "b":
                print(f"{color[0]}{codedict[x[1]]}{color[0]}", end="")
            elif x[0] == "x":
                print(f"{color[3]}ᆞ{color[0]}", end="")  # chr(4510) [ᆞ]
            else:
                print("ᅟ", end="")  # chr(4447) [ᅟ]

        def drawInLoops(i, j):
            if i == self.height:
                if j == 0:
                    # bottom left corner
                    print("", end=f"{chr(12288)}{chr(12288)}")
                else:
                    # bottom letter row
                    print(f"{color[1]}{self.files[j-1]}{color[0]}",
                          end=f" {chr(12288)}")
            else:
                if j == 0:
                    # left number column
                    print(
                        f"{color[1]}{self.ranks[-i-1]}{color[0]}", end=" ")
                else:
                    # squares
                    # drawn matrix is 1 higher
                    # and wider than self.matrix
                    if (j + self.height - i) % 2 == 1:
                        squarecolor = color[1]
                    else:
                        squarecolor = color[2]
                    print(f"{squarecolor}[{color[0]}", end="")
                    piece = self.matrix[j - 1][self.height - i - 1]
                    printPiece(piece)
                    print(f"{squarecolor}]{color[0]}", end="")

        for i in range(0, self.height + 1):
            for j in range(0, self.width + 1):
                drawInLoops(i, j)
            print("")


if __name__ == '__main__':
    importlib.reload(pieces)
    board = Chessboard(8, 8)
    board.initiatePieces()
    board.printInfo()
    board.movePiece("c1", "e4")
    board.updateMatrix()
    board.printInfo()
    print(board.piecelist["wBbishop"].move(board))
