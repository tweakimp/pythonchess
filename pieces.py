class Piece():
    def __init__(self, color, position):
        self.position = position.upper()
        if color == "w" or "b":
            self.color = color
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        # place on board
        self.position = position.upper()
        self.unmoved = True


class Pawn(Piece):
    def __init__(self, color, position):
        self.value = "p"
        self.short = color + "P"
        super().__init__(color, position)


class Knight(Piece):
    def __init__(self, color, position):
        self.short = color + "N"
        super().__init__(color,  position)

    def move(self, board):
        # calculate all knight moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),
                      (2, -1), (2, 1))
        moves = []
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    moves.append(f"{board.files[newf]}{board.ranks[newr]}")
        return moves


class Bishop(Piece):
    def __init__(self, color, position):
        self.short = color + "B"
        super().__init__(color, position)

    def move(self, board):
        # calculate all bishop moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        moves = []
        # down and left
        if f != 0 and r != 0:
            for i in range(1,  1 + min(f, r)):
                moves.append(f"{board.files[f - i]}{board.ranks[r - i]}")
        # up and left
        if f != 0 and r != board.height - 1:
            for j in range(1, 1 + min(f, board.height - 1 - r)):
                moves.append(f"{board.files[f - j]}{board.ranks[r + j]}")
        # up and right
        if f != board.width - 1 and r != board.height - 1:
            for k in range(1, min(board.width - f, board.height - r)):
                moves.append(f"{board.files[f + k]}{board.ranks[r + k]}")
        # down and right
        if f != board.width - 1 and r != 0:
            for l in range(1, 1 + min(board.width - 1 - f, r)):
                moves.append(f"{board.files[f + l]}{board.ranks[r - l]}")
        return moves


class Rook(Piece):
    def __init__(self, color, position):
        self.short = color + "R"
        super().__init__(color, position)
        self.unmoved = True


class Queen(Piece):
    def __init__(self, color, position):
        self.short = color + "Q"
        super().__init__(color, position)


class King(Piece):
    def __init__(self, color, position):
        self.short = color + "K"
        super().__init__(color, position)
        self.canCastle = True
