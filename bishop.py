import board
import help


def bishopMoves(position):
    # calculate all bishop moves from position
    print(
        f"On {help.aORan} {board.width}*{board.height} board a Bishop on {position.upper()} can go to:"
    )
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    directions = []  # directions are absolute coordinates

    for i in range(1, board.width):
        if (f - i in range(1, board.width + 1)
                and r - i in range(1, board.height + 1)):
            directions.append((f - i, r - i))
        if (f + i in range(1, board.width + 1)
                and r + i in range(1, board.height + 1)):
            directions.append((f + i, r + i))
        if (f - i in range(1, board.width + 1)
                and r + i in range(1, board.height + 1)):
            directions.append((f - i, r + i))
        if (f + i in range(1, board.width + 1)
                and r - i in range(1, board.height + 1)):
            directions.append((f + i, r - i))
    for direction in directions:
        print(f"{help.numberToLetter(direction[0])}{direction[1]}", end=' ')


# TEST
# bishopMoves("a3")
