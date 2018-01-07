import board
import helper


def knightMoves(position):
    # calculate all knight moves from position
    # print(f"On {helper.aORan} {board.width} * {board.height} ", end="")
    # print(f"board a Knight on {position.upper()} can go to:")
    file = helper.let2num((position[0]).upper())
    rank = position[1:]
    f, r = int(file), int(rank)
    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),
                  (2, -1), (2, 1))
    moves = []
    for direction in directions:
        newf = f + direction[0]
        newr = r + direction[1]
        if newf in range(1, board.width + 1):
            if newr in range(1, board.height + 1):
                moves.append(f"{helper.num2let(newf)}{newr}")
    return moves


# TEST
# print(knightMoves("e4"))
