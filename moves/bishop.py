import board
import helper


def bishopMoves(position):

    # calculate all bishop moves from position
    print(f"On {helper.aORan} {board.width}*{board.height}  ", end="")
    print(f"board a Bishop on {position.upper()} can go to:")
    file = helper.let2num((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    moves = []  # moves are absolute coordinates

    # down and left
    if f != 1 or r != 1:
        for i in range(1, min(f, r)):
            moves.append((f - i, r - i))

    # up and left
    if f != 1 or r != board.height:
        for j in range(1, min(f, board.height + 1 - r)):
            moves.append((f - j, r + j))

    # up and right
    if f != board.width or r != board.height:
        for k in range(1, min(board.width + 1 - f, board.height + 1 - r)):
            moves.append((f + k, r + k))

    # down and right
    if f != board.width or r != 1:
        for l in range(1, min(board.width + 1 - f, r)):
            moves.append((f + l, r - l))

    for move in moves:
        print(f"{helper.num2let(move[0])}{move[1]}", end=' ')


# TEST
# bishopMoves("d4")
