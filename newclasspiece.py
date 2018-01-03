import board
import helper
import knight


class Piece:
    # Summons a piece of given color and position
    def __init__(self, color, value, position):
        # position
        self.position = position.upper()
        # color
        if color == "w":
            self.color = "w"
        elif color == "b":
            self.color = "b"
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        self.value = value.upper()
        self.short = self.color + self.value
        # place on board
        file = board.files.index(self.position[0])
        rank = self.position[1:]
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
        if(self.checkTarget(target)):
            if(board.isEmpty(target)):
                start = (self.position).upper()
                self.updateBoard(target)
                print(f"{self.name} moves: {start} > {target.upper()}")
            else:
                self.capture(target)
        else:
            print("Cant go there")

    def capture(self, target):
        file = helper.let2num((target[0]).upper())
        rank = int(target[1:])
        if(board.puzzlemode):
            print("Capture in puzzlemode")
            start = (self.position).upper()
            self.updateBoard(target)
            print(f"{self.name} captures: {start} > {target.upper()}")
        else:
            opponent = board.matrix[file - 1][rank - 1]
            if(self.color != opponent[:1]):
                start = (self.position).upper()
                self.updateBoard(target)
                print(f"{self.name} captures: {start} > {target.upper()}")
            else:
                print(f"Can't capture piece of same color")

    def checkTarget(self, target):
        moves = knight.knightMoves(self.position)
        if target.upper() in moves:
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, color, position):
        self.name = "Knight"
        self.short = color + "N"
        super().__init__(color, position)

startlist = [
    # [name, color, value, position]
    ["wApawn", "w", "p", "a2"],
    ["wBpawn", "w", "p", "b2"],
    ["wCpawn", "w", "p", "c2"],
    ["wDpawn", "w", "p", "d2"],
    ["wEpawn", "w", "p", "e2"],
    ["wFpawn", "w", "p", "f2"],
    ["wGpawn", "w", "p", "g2"],
    ["wHpawn", "w", "p", "h2"],
    ["bApawn", "b", "p", "a7"],
    ["bBpawn", "b", "p", "b7"],
    ["bCpawn", "b", "p", "c7"],
    ["bDpawn", "b", "p", "d7"],
    ["bEpawn", "b", "p", "e7"],
    ["bFpawn", "b", "p", "f7"],
    ["bGpawn", "b", "p", "g7"],
    ["bHpawn", "b", "p", "h7"],
    ["wQrook", "w", "r", "a1"],
    ["wQknight", "w", "n", "b1"],
    ["wBbishop", "w", "b", "c1"],
    ["wQueen", "w", "q", "d1"],
    ["wKing", "w", "k", "e1"],
    ["wWbishop", "w", "b", "f1"],
    ["wKknight", "w", "n", "g1"],
    ["wKrook", "w", "r", "h1"],
    ["bQrook", "b", "r", "a8"],
    ["bQknight", "b", "n", "b8"],
    ["bBbishop", "b", "b", "c8"],
    ["bQueen", "b", "q", "d8"],
    ["bWbishop", "b", "b", "f8"],
    ["bKing", "b", "k", "e8"],
    ["bKknight", "b", "n", "g8"],
    ["bKrook", "b", "r", "h8"]
]
