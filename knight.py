import board
import help


def knightMoves(position):
    # calculate all knight moves from position
    print(
        f"On {help.aORan} {board.width}*{board.height} board a Knight on {position.upper()} can go to:"
    )
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),
                  (2, -1), (2, 1))
    moves = []
    for direction in directions:
        if (f + direction[0]) in range(1, board.width + 1) and (r + direction[1]) in board.ranks:
            moves.append((f + direction[0], r + direction[1]))
            print(
                f"{help.numberToLetter(f + direction[0])}{r + direction[1]}", end=' ')


# TEST
# knightMoves("e7")
