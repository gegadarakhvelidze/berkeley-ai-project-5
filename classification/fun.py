x = 1
y = 1

def inBounds(pos):
    x, y = pos
    return x in range(2) and y in range(2)

from itertools import product
prod = set(product([x - 1, x, x + 1], [y - 1, y, y + 1]))
prod.remove((x, y))
neighbours = filter(inBounds, prod)
print type(neighbours)