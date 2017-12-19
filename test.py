# für directions:
'''
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
'''
bwidth = 8
bheight = 8
f = 7
r = 2
'''directions = []
for i in range(1, bwidth + 1):
    if i != f:
        directions.append((i, r))
for j in range(1, bheight + 1):
    if j != r:
        directions.append((f, j))
print(directions)
print(len(directions))'''

for i in range(1, bwidth + 1):
    if i != f:
        directions.append((i, r))
for j in range(1, bheight + 1):
    if j != r:
        directions.append((f, j))
print(directions)
print(len(directions))


'''
What is it?
To most, it is how they see the world.
To many, it is most important.
To itself, it is about one fifth.
Telling you any more, I would just be giving you the answer.
'''
