# 0 zurücksetzen
# 1 fett
# 3,4 unterstrichen
# 8 alles weg?!
# 9 durchgestrichen
# textfarbe 30-37,39
# hintergrundfarbe 40-47,49
# textfarbe 90-97
# hintergrundfarbe 100-107

for i in range(0, 50):
    print(f"\033[{i}mAt {i} THIS happens! \033[0m", end="")
    print(f"\033[{i+60}mAt {i+60} THIS happens! \033[0m")