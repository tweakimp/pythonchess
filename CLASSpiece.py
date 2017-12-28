import board


class piece:
    # Summons piece of given color and position
    def __init__(self, color, piece, position):

        # color
        if color == "w":
            self.color = "white"
        elif color == "b":
            self.color = "black"
        else:
            self.color = "none"

        # piece
        if piece == "p":
            self.piece = "pawn"
            self.short = color + "P"
        elif piece == "n":
            self.piece = "knight"
            self.short = color + "N"
        elif piece == "b":
            self.piece = "bishop"
            self.short = color + "B"
        elif piece == "r":
            self.piece = "rook"
            self.short = color + "R"
            self.canCastle = True
        elif piece == "q":
            self.piece = "queen"
            self.short = color + "Q"
        elif piece == "k":
            self.piece = "king"
            self.short = color + "K"
            self.canCastle = True

        # position and place
        self.position = position.upper()
        file = board.files.index(((self.position[0]).upper()))
        rank = self.position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short

    def place(self, position=None):
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
        self.position = position


wApawn = piece("w", "p", "a2")
wBpawn = piece("w", "p", "b2")
wCpawn = piece("w", "p", "c2")
wDpawn = piece("w", "p", "d2")
wEpawn = piece("w", "p", "e2")
wFpawn = piece("w", "p", "f2")
wGpawn = piece("w", "p", "g2")
wHpawn = piece("w", "p", "h2")

bApawn = piece("b", "p", "a7")
bBpawn = piece("b", "p", "b7")
bCpawn = piece("b", "p", "c7")
bDpawn = piece("b", "p", "d7")
bEpawn = piece("b", "p", "e7")
bFpawn = piece("b", "p", "f7")
bGpawn = piece("b", "p", "g7")
bHpawn = piece("b", "p", "h7")

wQrook = piece("w", "r", "a1")
wQknight = piece("w", "n", "b1")
wBbishop = piece("w", "b", "c1")
wQueen = piece("w", "q", "d1")
wKing = piece("w", "k", "e1")
wWbishop = piece("w", "b", "f1")
wKknight = piece("w", "n", "g1")
wKrook = piece("w", "r", "h1")

bQrook = piece("b", "r", "a8")
bQknight = piece("b", "n", "b8")
bBbishop = piece("b", "b", "c8")
bQueen = piece("b", "q", "d8")
bKing = piece("b", "k", "e8")
bWbishop = piece("b", "b", "f8")
bKknight = piece("b", "n", "g8")
bKrook = piece("b", "r", "h8")

# draw.drawMatrix()
for line in board.matrix:
    print(line)
print(bKrook.position)
print(bKrook.color)
print(bKrook.canCastle)
