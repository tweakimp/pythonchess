import board
import helper


def rookMoves(position):
    # calculate all rook moves from position
    print(f"On {helper.aORan} {board.width}*{board.height}", end="")
    print(f"board a Rook on {position.upper()} can go to:")
    file = helper.let2num((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    moves = []  # moves are absolute coordinates

    # left
    if(f != 1):
        for i in range(1, f):
            moves.append((f - i, r))
    # up
    if(r != board.height):
        for j in range(1, board.height + 1 - r):
            moves.append((f, r + j))
    # right
    if(f != board.width):
        for k in range(1, board.width + 1 - f):
            moves.append((f + k, r))
    # down
    if(r != 1):
        for l in range(1, r):
            moves.append((f, r - l))

    for move in moves:
        print(f"{helper.num2let(move[0])}{move[1]}", end=' ')


# TEST
# rookMoves("e7")
