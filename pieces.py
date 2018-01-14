import helper
import lists
import moves


def checkTarget(target):
    # moves = knight.knightMoves(self.position)
    if target.upper() in moves:
        return True
    else:

        return False


class Piece:
    def __init__(self, color, position):
        self.position = position.upper()
        if color == "w":
            self.color = "w"
        elif color == "b":
            self.color = "b"
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        # place on board
        boardfile = board.files.index(self.position[0])
        boardrank = self.position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short

    def pos(self):
        print(self.position)

    def updateBoard(self, position=None):
        # remove old
        oldfile = board.files.index(((self.position[0]).upper()))
        oldrank = self.position[1:]
        board.matrix[int(oldfile) - 1][int(oldrank) - 1] = "  "
        # place new
        position = position or self.position
        file = board.files.index(((position[0]).upper()))
        rank = position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short
        # update position
        self.position = position.upper()

    def move(self, target):
        if checkTarget(target):
            if board.isEmpty(target):
                start = self.position.upper()
                self.updateBoard(target)
                print(f"{self.name} moves: {start} > {target.upper()}")
            else:
                self.capture(target)
        else:
            print("Cant go there")

    def capture(self, target):
        file = helper.let2num((target[0]).upper())
        rank = int(target[1:])
        if board.puzzlemode:
            print("Capture in puzzlemode")
            start = self.position.upper()
            self.updateBoard(target)
            print(f"{self.name} captures: {start} > {target.upper()}")
        else:
            opponent = board.matrix[file - 1][rank - 1]
            if self.color != opponent[:1]:
                start = self.position.upper()
                self.updateBoard(target)
                print(f"{self.name} captures: {start} > {target.upper()}")
            else:
                print(f"Can't capture piece of same color")


class Pawn(Piece):
    def __init__(self, color, position):
        self.value = "p"
        self.short = color + "P"
        super().__init__(color, self.value, position)


class Knight(Piece):
    def __init__(self, color, position):
        self.short = color + "N"
        super().__init__(color, value, position)


class Bishop(Piece):
    def __init__(self, color, value, position):
        self.short = color + "B"
        super().__init__(color, value, position)


class Rook(Piece):
    def __init__(self, color, value, position):
        self.short = color + "R"
        super().__init__(color, value, position)
        self.canCastle = True


class Queen(Piece):
    def __init__(self, color, value, position):
        self.short = color + "Q"
        super().__init__(color, value, position)


class King(Piece):
    def __init__(self, color, value, position):
        self.short = color + "K"
        super().__init__(color, value, position)
        self.canCastle = True


def listchange(manipulation, input, target=0):
    # manipulation "del" or "move"
    for k, v in pieces.copy().items():
        if k == input or v.position == input.upper():
            if manipulation == "del":
                if target != 0:
                    print("Unneccessary target!")
                del pieces[k]
            if manipulation == "move":
                if target == 0:
                    print("No target for move!")
                else:
                    v.position = target.upper()


pieces = {}
pdict = {name: Pawn(color, value, position)
         for name, color, value, position in lists.pawns}
ndict = {name: Knight(color, value, position)
         for name, color, value, position in lists.knights}
bdict = {name: Bishop(color, value, position)
         for name, color, value, position in lists.bishops}
rdict = {name: Rook(color, value, position)
         for name, color, value, position in lists.rooks}
qdict = {name: Queen(color, value, position)
         for name, color, value, position in lists.queens}
kdict = {name: King(color, value, position)
         for name, color, value, position in lists.kings}
pieces.update(pdict)
pieces.update(ndict)
pieces.update(bdict)
pieces.update(rdict)
pieces.update(qdict)
pieces.update(kdict)


def pieceList(modus):
    stats = {"Pawns": 0, "Knights": 0, "Bishops": 0, "Rooks": 0,
             "Queens": 0, "Kings": 0, "White": 0, "Black": 0}
    pieceList = []
    for k, v in pieces.copy().items():
        if v.short[0] == "w":
            stats["White"] += 1
            name = "White "
        elif v.short[0] == "b":
            stats["Black"] += 1
            name = "Black "
        if v.short[1] == "P":
            stats["Pawns"] += 1
            name += "Pawn"
        elif v.short[1] == "N":
            stats["Knights"] += 1
            name += "Knight"
        elif v.short[1] == "B":
            stats["Bishops"] += 1
            name += "Bishop"
        elif v.short[1] == "R":
            stats["Rooks"] += 1
            name += "Rook"
        elif v.short[1] == "Q":
            stats["Queens"] += 1
            name += "Queen"
        elif v.short[1] == "K":
            stats["Kings"] += 1
            name += "King"
        pieceList.append(v.position + " " + name)
    if modus == 0:
        return pieceList
    if modus == 1:
        return stats


def printColumns(xlist, columns, padding, seperator):
    # make it rectangualar by filling empty list entries
    missingentries = (columns - len(xlist) % columns) % columns
    for i in range(missingentries):
        xlist.append("")

    # make entries equally long
    columnwidth = max(len(row) for row in xlist) + padding
    for i in range(len(xlist)):
        difference = columnwidth - len(xlist[i])
        for j in range(difference):
            xlist[i] += seperator

    columnlength = len(xlist) // columns
    for i in range(columnlength):
        for j in range(columns):
            print(xlist[i + (j * columnlength)], end="")
        print("")


def printStats(xdict):
    for k, v in xdict.items():
        print(k, end=": ")
        print(v, end="")
        if k != list(xdict.keys())[-1]:
            print(", ", end="")
    print("")


def printPieces():
    printColumns(pieceList(0), 4, 5, " ")
    printStats(pieceList(1))


printPieces()
# draw.drawMatrix()
