class piece(object):
    def __init__(self, value, color, position):
        self.value = value
        self.color = color
        self.position = position


def deletePiece(square):
    for i in range(len(piecelist) - 1):
        if piecelist[i].position == square:
            print(f"Delete obj on position {piecelist[i].position}.")
            del piecelist[i]


piecelist = []  # dictionary mit mehreren variablen

for i in range(1, 33):
    if 1 <= i <= 8:
        piecelist.append(piece("p", "w", f"{i} 2"))
        if(i == 1):
            n1 = piece("k", "w", "4 9")
            piecelist.append(n1)
    elif 9 <= i <= 16:
        piecelist.append(piece("p", "b", f"{i-8} 7"))

for obj in piecelist:
    print(f"{obj.color} {obj.value} {obj.position}")

print("===============")
deletePiece("1 7")
deletePiece("6 2")
print("===============")

for obj in piecelist:
    print(f"{obj.color} {obj.value} {obj.position}")
