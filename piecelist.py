import board
import draw


class piece(object):
    def __init__(self, color, value, position):
        self.color = color
        self.value = value.upper()
        self.short = self.color + self.value
        # position and place
        self.position = position.upper()
        file = board.files.index(((self.position[0]).upper()))
        rank = self.position[1:]
        board.matrix[int(file) - 1][int(rank) - 1] = self.short


startlist = [
    # [name, color, piece, position]
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

piecelist = []

for i in range(32):
    pieceName = startlist[i][0]
    pieceName = piecelist.append(
        piece(startlist[i][1], startlist[i][2], startlist[i][3]))

draw.drawMatrix()
