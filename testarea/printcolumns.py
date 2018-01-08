testlist = ['A2 White Pawn', 'B2 White Pawn', 'C2 White Pawn', 'D2 White Pawn',
            'E2 White Pawn', 'F2 White Pawn', 'G2 White Pawn', 'H2 White Pawn',
            'A7 Black Pawn', 'B7 Black Pawn', 'C7 Black Pawn', 'D7 Black Pawn',
            'E7 Black Pawn', 'F7 Black Pawn', 'G7 Black Pawn', 'H7 Black Pawn',
            'B1 White Knight', 'G1 White Knight', 'B8 Black Knight',
            'G8 Black Knight', 'C1 White Bishop', 'F1 White Bishop',
            'C8 Black Bishop', 'F8 Black Bishop', 'A1 White Rook',
            'H1 White Rook', 'A8 Black Rook', 'H8 Black Rook',
            'D1 White Queen', 'D8 Black Queen', 'E1 White King',
            'E8 Black King']


def printColumns(xlist, columns, padding, seperator):

    # make it rectangualar by filling empty list entries
    missingentries = (columns - len(xlist) % columns) % columns
    for i in range(missingentries):
        xlist.append("")

    # make entries equally long
    columnwidth = max(len(row) for row in xlist) + padding
    for i in range(len(xlist)):
        difference = columnwidth - len(xlist[i])
        for j in range(difference):
            xlist[i] += seperator
    
    columnlength = len(xlist) // columns
    for i in range(columnlength):
        for j in range(columns):
            print(xlist[i + (j * columnlength)], end="")
        print("")


printColumns(testlist, 4, 10, " ")
