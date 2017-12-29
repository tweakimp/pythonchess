import board
import helper


def kingMoves(position):
    print(f"On {helper.aORan} {board.width}*{board.height}", end="")
    print(f"board a King on {position.upper()} can go to:")
    file = helper.let2num((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1))

    moves = []
    for direction in directions:
        if (f + direction[0]) in range(1, board.width + 1) and (r + direction[1]) in range(1, board.height + 1):
            moves.append((f + direction[0], r + direction[1]))
            print(
                f"{helper.num2let(f + direction[0])}{r + direction[1]}", end=" ")


# TEST
# kingMoves("e5")
