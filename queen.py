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
    directions = []  # directions are absolute coordinates

    for i in range(1, board.width + 1):
        if i != f:
            directions.append((i, r))
    for j in range(1, board.height + 1):
        if j != r:
            directions.append((f, j))
    for k in range(1, board.width):
        if (f - k in range(1, board.width + 1)
                and r - k in range(1, board.height + 1)):
            directions.append((f - k, r - k))
        if (f + k in range(1, board.width + 1)
                and r + k in range(1, board.height + 1)):
            directions.append((f + k, r + k))
        if (f - k in range(1, board.width + 1)
                and r + k in range(1, board.height + 1)):
            directions.append((f - k, r + k))
        if (f + k in range(1, board.width + 1)
                and r - k in range(1, board.height + 1)):
            directions.append((f + k, r - k))

    for direction in directions:
        print(f"{help.numberToLetter(direction[0])}{direction[1]}", end=' ')


# TEST
# queenMoves("a1")
