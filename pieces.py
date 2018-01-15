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
        print(moves)
        # return moves


class Bishop(Piece):
    def __init__(self, color, position):
        self.short = color + "B"
        super().__init__(color, position)


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
