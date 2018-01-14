class Piece():
    def __init__(self, color, position):
        self.position = position.upper()
        if color == "w" or "b":
            self.color = color
        else:
            raise Exception("Wrong color (\"w\" or \"b\")")
        # place on board
        self.position = position.upper()


class Pawn(Piece):
    def __init__(self, color, position):
        self.value = "p"
        self.short = color + "P"
        super().__init__(color, position)


class Knight(Piece):
    def __init__(self, color, position):
        self.short = color + "N"
        super().__init__(color,  position)


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
