from itertools import product

with open('day9input.txt') as f:
    f = f.read().splitlines()
h = {(x, y): int(f[y][x]) for x, y in product(range(len(f[0])), range(len(f)))}

risk = 0
for (x, y), i in h.items():
    if ((x == 0 or h[x-1, y] > i)
    and (x == len(f[0]) - 1 or h[x+1, y] > i)
    and (y == 0 or h[x, y-1] > i)
    and (y == len(f) - 1 or h[x, y+1] > i)):
        risk += i + 1

def pocketSizeTest(x, y, label):
    pocketSize = 0

    def floodfill(fx, fy):
        nonlocal pocketSize
        if h[fx, fy] < 9:
            h[fx, fy] = label
            pocketSize += 1
            if fx > 0: floodfill(fx - 1, fy)
            if fx < len(f[0]) - 1: floodfill(fx + 1, fy)
            if fy > 0: floodfill(fx, fy - 1)
            if fy < len(f) - 1: floodfill(fx, fy + 1)

    floodfill(x, y)
    return pocketSize

sizes = []
for x, y in h:
    if h[x, y] < 9:
        sizes.append(pocketSizeTest(x, y, 10))

from heapq import nlargest
print(nlargest(3, sizes))
