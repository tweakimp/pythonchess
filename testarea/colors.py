# 0 zurücksetzen
# 1 fett
# 3,4 unterstrichen
# 8 alles weg?!
# 9 durchgestrichen
# textfarbe 30-37,39
# hintergrundfarbe 40-47,49
# textfarbe 90-97
# hintergrundfarbe 100-107
import itertools

for i in itertools.chain(range(30, 38), range(40, 48)):
    print(f"\x1b[{i}mAt {i} THIS happens! \x1b[0m", end="")
    print(f"\x1b[{i+60}mAt {i+60} THIS hhappens! \x1b[0m")
