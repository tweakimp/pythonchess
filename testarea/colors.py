# 0 zurücksetzen
# 1 fett
# 3,4 unterstrichen
# 8 alles weg?!
# 9 durchgestrichen
# textfarbe 30-37,39
# hintergrundfarbe 40-47,49
# textfarbe 90-97
# hintergrundfarbe 100-107

# for i in range(0, 50):
#  print(f"\x1b[{i}mAt {i} THIS happens! \x1b[0m", end="")
#  print(f"\x1b[{i+60}mAt {i+60} THIS happens! \x1b[0m")


import sys

txtfile = "unicode_table.txt"
print("creating file: " + txtfile)
F = open(txtfile, "w", encoding="utf-8", errors='ignore')
percolumn = 2000
for i in range(1, percolumn + 1):
    print("Nr.", i, chr(i),
          "\t", "Nr.", i + percolumn, chr(i + percolumn),
          "\t", "Nr.", i + percolumn * 2, chr(i + percolumn * 2),
          "\t", "Nr.", i + percolumn * 3, chr(i + percolumn * 3),
          "\t", "Nr.", i + percolumn * 4, chr(i + percolumn * 4),
          "\t", "Nr.", i + percolumn * 5, chr(i + percolumn * 5), )#file=F)
# except UnicodeEncodeError:
#     print("Nr. ", i, "UnicodeEncodeError",file=F)

# characters = [12,33-126,161-887, 890-895,900-906,908,910-1366,
# 1369-1375, 1377-2042, 2137-2139, 2208-2228,2275-
# ]

# import sys
# txtfile = "unicode_table.txt"
# print("creating file: " + txtfile)
# F = open(txtfile, "w", encoding="utf-8", errors='ignore')
# for uc in range(sys.maxunicode):
#     line = "%s  %s %s" % (uc, hex(uc), chr(uc))
#     print(line, file=F)
# F.close()
