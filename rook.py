import board
import help


def rookMoves(position):
    # calculate all rook moves from position
    print(
        f"On {help.aORan} {board.width}*{board.height} board a Rook on {position.upper()} can go to:"
    )
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    moves = []  # directions are absolute coordinates

    for i in range(1, board.width + 1):
        if i != f:
            moves.append((i, r))
    for j in range(1, board.height + 1):
        if j != r:
            moves.append((f, j))
    for move in moves:
        print(f"{help.numberToLetter(move[0])}{move[1]}", end=' ')


# TEST
# rookMoves("e7")
