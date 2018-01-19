class Piece():
    def __init__(self, color, position):
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

    def move(self, board):
        # calculate all rook moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        moves = []
        if(self.color == "w"):
            directions = ((-1, 1), (0, 1), (1, 1))
            if(boardrank == 1):
                directions = directions + ((0, 2),)
        else:
            directions = ((-1, -1), (0, -1), (1, -1))
            if(boardrank == 6):
                directions = directions + ((0, -2),)
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    moves.append(f"{board.files[newf]}{board.ranks[newr]}")
        return moves


class Knight(Piece):
    def __init__(self, color, position):
        self.short = color + "N"
        self.name = "White Knight" if color == "w" else "Black Knight"
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
        self.name = "White Bishop" if color == "w" else "Black Bishop"
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

    def move(self, board):
        # calculate all rook moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        moves = []
        # left
        if f != 0:
            for i in range(1, f + 1):
                moves.append(f"{board.files[f - i]}{board.ranks[r]}")
        # up
        if r != board.height - 1:
            for j in range(1, board.height - r):
                moves.append((f"{board.files[f]}{board.ranks[r + j]}"))
        # right
        if f != board.width - 1:
            for k in range(1, board.width - f):
                moves.append((f"{board.files[f +k]}{board.ranks[r]}"))
        # down
        if r != 0:
            for l in range(1, r + 1):
                moves.append((f"{board.files[f]}{board.ranks[r - l]}"))
        return moves


class Queen(Piece):
    def __init__(self, color, position):
        self.short = color + "Q"
        super().__init__(color, position)

    def move(self, board):
        # calculate all queen moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        moves = []
        # down and left
        if f != 0 and r != 0:
            for i in range(1,  1 + min(f, r)):
                moves.append(f"{board.files[f - i]}{board.ranks[r - i]}")
        # left
        if f != 0:
            for i in range(1, f + 1):
                moves.append(f"{board.files[f - i]}{board.ranks[r]}")
        # up and left
        if f != 0 and r != board.height - 1:
            for j in range(1, 1 + min(f, board.height - 1 - r)):
                moves.append(f"{board.files[f - j]}{board.ranks[r + j]}")
        # up
        if r != board.height - 1:
            for j in range(1, board.height - r):
                moves.append((f"{board.files[f]}{board.ranks[r + j]}"))
        # up and right
        if f != board.width - 1 and r != board.height - 1:
            for k in range(1, min(board.width - f, board.height - r)):
                moves.append(f"{board.files[f + k]}{board.ranks[r + k]}")
        # right
        if f != board.width - 1:
            for k in range(1, board.width - f):
                moves.append((f"{board.files[f +k]}{board.ranks[r]}"))
        # down and right
        if f != board.width - 1 and r != 0:
            for l in range(1, 1 + min(board.width - 1 - f, r)):
                moves.append(f"{board.files[f + l]}{board.ranks[r - l]}")
        # down
        if r != 0:
            for l in range(1, r + 1):
                moves.append((f"{board.files[f]}{board.ranks[r - l]}"))
        return moves


class King(Piece):
    def __init__(self, color, position):
        self.short = color + "K"
        super().__init__(color, position)

    def move(self, board):
        # calculate all king moves from position
        boardfile = int(board.files.index(self.position[0].upper()))
        boardrank = board.ranks.index(int(self.position[1:]))
        f, r = int(boardfile), int(boardrank)
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1))
        moves = []
        for direction in directions:
            newf = f + direction[0]
            newr = r + direction[1]
            if newf in range(0, board.width):
                if newr in range(0, board.height):
                    moves.append(f"{board.files[newf]}{board.ranks[newr]}")
        return moves
