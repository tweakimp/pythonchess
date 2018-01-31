import importlib
import time
from copy import deepcopy
from random import choice, sample
from string import ascii_uppercase

from ressources import pieces
from ressources.standard import start


class Chessboard():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.files = ascii_uppercase[:self.width]
        self.ranks = range(1, self.height + 1)
        self.piecedict = {}
        self.capturedlist = []
        self.matrix = [["  " for h in range(0, self.height)]
                       for w in range(0, self.width)]
        self.pieceMoves = []
        self.listOfSquares = [
            x + str(y) for x in self.files for y in self.ranks
        ]

    def resetMatrix(self):
        self.matrix = [["  " for h in range(0, self.height)]
                       for w in range(0, self.width)]

    def updateMatrix(self):
        self.resetMatrix()
        for key in self.piecedict:
            position = self.piecedict[key].position
            short = self.piecedict[key].short
            boardfile = int(self.files.index(position[0].upper()))
            boardrank = self.ranks.index(int(position[1:]))
            self.matrix[boardfile][boardrank] = short

    def checkSquare(self, position):
        boardfile = int(self.files.index(position[0].upper()))
        boardrank = self.ranks.index(int(position[1:]))
        if self.matrix[int(boardfile)][int(boardrank)] == "  ":
            return None
        else:
            return self.matrix[int(boardfile)][int(boardrank)][0]

    def movePiece(self, string, newposition):
        newposition = newposition.upper()
        for name, obj in self.piecedict.copy().items():
            if name == string or obj.position == string.upper():
                if newposition in obj.move(self):
                    # delete old piece at that position
                    self.deletePiece(newposition)
                    # change position of moving piece
                    obj.position = newposition
                    self.updateMatrix()
                    # self.printMatrix()
                    # self.inCheck(self.othercolor(obj.color))
                else:
                    print(f"\033[91m{chr(9888)} {obj.name} on ", end="")
                    print(f"{obj.position} can't go to {newposition}!\033[0m")

    def FORCEmovePiece(self, string, newposition):
        newposition = newposition.upper()
        for name, obj in self.piecedict.copy().items():
            if name == string or obj.position == string.upper():
                    # delete old piece at that position
                    self.deletePiece(newposition)
                    # change position of moving piece
                    obj.position = newposition
                    self.updateMatrix()

    def deletePiece(self, string):
        for key, obj in self.piecedict.copy().items():
            if key == string or obj.position == string.upper():
                del self.piecedict[key]

    def showPieceMoves(self, string):
        self.pieceMoves = []
        for key, obj in self.piecedict.items():
            if key == string or obj.position == string.upper():
                for move in obj.move(self):
                    self.pieceMoves.append(move)
        self.updateMatrix()
        self.drawBoard()

    def getPieceObject(self, string):
        for key, obj in self.piecedict.items():
            if key == string or obj.name == string or obj.position == string:
                piece = obj
        return piece

    def othercolor(self, color):
        return "w" if color == "b" else "b"

    def inCheck(self, color, notification=False):
        if color == "w":
            king = self.getPieceObject("White King")
        else:
            king = self.getPieceObject("Black King")
        for obj in self.piecedict.values():
            if obj.color == self.othercolor(color):
                if king.position in obj.move(self):
                    if notification is True:
                        print("--CHECK--")
                        print(f"{obj.name} checks {king.name}.")
                    return True
        if notification is True:
            print("-NO CHECK-")
        return False

    def getAllMoves(self, color):
        allMoves = []
        for obj in self.piecedict.values():
            if obj.color == color and obj.move(self) != []:
                allMoves.append([obj.position, obj.move(self)])
        return allMoves

    def showAllMoves(self, color):
        self.pieceMoves = []
        for obj in self.piecedict.values():
            if obj.color == color and obj.move(self) != []:
                for move in obj.move(self):
                    self.pieceMoves.append(move)
        self.updateMatrix()
        self.drawBoard()

    def inCheckmate(self, color):
        if self.inCheck(color) is False:
            return False
        allMoves = self.getAllMoves(color)
        for i in allMoves:
            for j in i[1]:
                testboard = deepcopy(self.createTestBoard(i[0], j))
                if testboard.inCheck(color) is False:
                    return False
                del testboard
        return True

    def createTestBoard(self, position, target):
        v = Chessboard(self.width, self.height)
        v.piecedict = deepcopy(self.piecedict)
        v.FORCEmovePiece(position, target)
        v.updateMatrix()
        return v

    def initPieces(self):
        # initiate pieces and update piecedict
        self.piecedict.update({
            name: pieces.Pawn(color, position)
            for name, color, position in start.pawns
        })
        self.piecedict.update({
            name: pieces.Knight(color, position)
            for name, color, position in start.knights
        })
        self.piecedict.update({
            name: pieces.Bishop(color, position)
            for name, color, position in start.bishops
        })
        self.piecedict.update({
            name: pieces.Rook(color, position)
            for name, color, position in start.rooks
        })
        self.piecedict.update({
            name: pieces.Queen(color, position)
            for name, color, position in start.queens
        })
        self.piecedict.update({
            name: pieces.King(color, position)
            for name, color, position in start.kings
        })
        # update matrix
        self.updateMatrix()

    def initTest(self):
        def squaresToRemove(firstKing):
            boardfile = int(self.files.index(firstKing[0].upper()))
            boardrank = int(self.ranks.index(int(firstKing[1:])))
            f, r = boardfile, boardrank
            directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),
                          (1, 0), (1, 1))
            squares = []
            for direction in directions:
                newf = f + direction[0]
                newr = r + direction[1]
                if newf in range(0, self.width):
                    if newr in range(0, self.height):
                        squares.append(f"{self.files[newf]}{self.ranks[newr]}")
            return squares

        # firstKing = choice(self.listOfSquares)
        firstKing, pos1, pos2, pos3 = sample(self.listOfSquares, 4)
        secondKing = choice([
            x for x in self.listOfSquares
            if x not in squaresToRemove(firstKing)
            and x not in [pos1, pos2, pos3]
        ])
        # col1 = choice(["w", "b"])
        # secondKing = sample(self.listOfSquares,1)
        self.piecedict.update({
            name: pieces.King(color, position)
            for name, color, position in [["firstKing", "w", f"{firstKing}"]]
        })
        self.piecedict.update({
            name: pieces.King(color, position)
            for name, color, position in [["secondKing", "b", f"{secondKing}"]]
        })
        self.piecedict.update({
            name: pieces.Bishop(color, position)
            for name, color, position in [["test1", "b", f"{pos1}"]]
        })
        self.piecedict.update({
            name: pieces.Rook(color, position)
            for name, color, position in [["test2", "b", f"{pos2}"]]
        })
        self.piecedict.update({
            name: pieces.Knight(color, position)
            for name, color, position in [["test3", "b", f"{pos3}"]]
        })
        # update matrix
        self.updateMatrix()

    def drawBoard(self):
        color = ["\033[0m", "\033[91m", "\033[31m", "\033[97m", "\033[92m"]

        #         no color   lightred      red         white       gree

        def printPiece(x):
            # codedict = {"K": "K", "Q": "N", "P": "P"}
            codedict = {
                "K": "♔",
                "Q": "♕",
                "R": "♜",
                "B": "♝",
                "N": "♞",
                "P": "♟"
            }
            if x[0] == "w":
                print(f"{color[3]}{codedict[x[1]]}{color[0]}", end="")
            elif x[0] == "b":
                print(f"{color[0]}{codedict[x[1]]}{color[0]}", end="")
            else:
                print(f"{chr(4447)}", end="")  # chr(4447) [ᅟ]

        def drawInLoops(i, j):
            if i == self.height:
                if j == 0:
                    # bottom left corner
                    print("", end=f"{chr(4447)*2}")  # 2*chr(4447) [ᅟ]
                else:
                    # bottom letter row
                    print(
                        f"{color[1]}{self.files[j-1]}{color[0]}",
                        end=f" {chr(4447)}")  # space + # chr(4447) [ᅟ]
            else:
                if j == 0:
                    # left number column
                    print(f"{color[1]}{self.ranks[-i-1]}{color[0]}", end=" ")
                else:
                    # squares
                    # drawn matrix is 1 higher and wider than self.matrix
                    current = str(self.files[j - 1]) + \
                        str(self.ranks[self.height - i - 1])
                    if current in self.pieceMoves:
                        squarecolor = color[4]
                    else:
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
        print("")  # new line after board for better looks

    def printInfo(self):
        print("width: ", self.width)
        print("height: ", self.height)
        print("files: ", self.files)
        print("ranks: ", self.ranks)
        self.printPiecelist()
        self.printMatrix()
        self.drawBoard()

    def printPiecelist(self):
        print("piecedict: ")
        if self.piecedict == {}:
            print("(empty)")
        else:
            printthis = []
            columns = 3
            padding = 2
            for key in self.piecedict:
                printthis.append(self.piecedict[key].position + " " +
                                 self.piecedict[key].name)
            # make it rectangualar by filling empty list entries
            missingentries = columns - len(printthis) % columns
            for i in range(missingentries):
                printthis.append("")
            # get widths for each column
            columnwidths = [0 for _ in range(columns)]
            columnlength = len(printthis) // columns
            for i in range(len(printthis)):
                currentwidth = len(printthis[i]) + padding
                if columnwidths[i // columnlength] < currentwidth:
                    columnwidths[i // columnlength] = currentwidth
            for i in range(len(printthis)):
                totalwidth = columnwidths[i // columnlength]
                printthis[i] = f"{printthis[i]: <{totalwidth}}"
            columnlength = len(printthis) // columns
            for i in range(columnlength):
                for j in range(columns):
                    print(printthis[i + (j * columnlength)], end="")
                print("")

    def printMatrix(self):
        print("matrix: ")
        for line in self.matrix:
            print(line)


if __name__ == '__main__':
    start_time = time.time()
    importlib.reload(pieces)
    board = Chessboard(8, 8)
    board.initPieces()
    board.printInfo()
    # board.drawBoard()
    print(f"{round(time.time() - start_time,5)} seconds")
