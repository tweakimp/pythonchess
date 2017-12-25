import board
import help


def queenMoves(position):
    # calculate all queen moves from position
    print(
        f"On {help.aORan} {board.width}*{board.height} board a Queen on {position.upper()} can go to:"
    )
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    moves = []  # moves are absolute coordinates

    # left
    if(f != 1):
        for i in range(1, f):
            moves.append((f - i, r))

    # up and left
    if(f != 1 or r != board.height):
        for j in range(1, min(f, board.height + 1 - r)):
            moves.append((f - j, r + j))

    # up
    if(r != board.height):
        for j in range(1, board.height + 1 - r):
            moves.append((f, r + j))

    # up and right
    if(f != board.width or r != board.height):
        for k in range(1, min(board.width + 1 - f, board.height + 1 - r)):
            moves.append((f + k, r + k))

    # right
    if(f != board.width):
        for k in range(1, board.width + 1 - f):
            moves.append((f + k, r))

    # down and right
    if(f != board.width or r != 1):
        for l in range(1, min(board.width + 1 - f, r)):
            moves.append((f + l, r - l))

    # down
    if(r != 1):
        for l in range(1, r):
            moves.append((f, r - l))

    # down and left
    if(f != 1 or r != 1):
        for i in range(1, min(f, r)):
            moves.append((f - i, r - i))

    for move in moves:
        print(f"{help.numberToLetter(move[0])}{move[1]}", end=' ')


# TEST
# queenMoves("e3")
