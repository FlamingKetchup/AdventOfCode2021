from itertools import product
from queue import PriorityQueue

with open('day15input.txt') as f:
    f = f.read().splitlines()
    fw = len(f[0])
    fh = len(f)
    w = fw * 5
    h = fh * 5
    risk = {(x, y): (int(f[y % fh][x % fw]) + x//fw + y//fh - 1) % 9 + 1 for x, y in product(range(w), range(h))}

def adjacent(point):
    x, y = point
    result = []
    if x > 0: result.append((x-1, y))
    if x < w-1: result.append((x+1, y))
    if y > 0: result.append((x, y-1))
    if y < h-1: result.append((x, y+1))
    return result

cost = {}
frontier = PriorityQueue()
frontier.put((0,0), 0)
cost[0, 0] = 0
while True:
    current = frontier.get()

    if current == (w-1, h-1):
        break

    for i in adjacent(current):
        newCost = cost[current] + risk[i]
        if i not in cost or newCost < cost[i]:
            cost[i] = newCost
            frontier.put(i, newCost + abs(w-1 - i[0]) + abs(h-1 - i[1]))

print(cost[w-1, h-1])
