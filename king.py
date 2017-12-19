import board
import help


def kingMoves(position):
    """Calculate all king moves from position."""
    print(
        f"On {help.aORan} {board.width} * {board.height} board a King on {position.upper()} can go to: "
    )
    file = help.letterToNumber((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                  (1, 1))

    for direction in directions:
        testfile = f + direction[0]
        testrank = r + direction[1]
        if testfile in range(1, board.width + 1) and testrank in board.ranks:
            print(f"{help.numberToLetter(testfile)}{testrank}", end=' ')


# TEST
# kingMoves("a1")
