from itertools import product

with open('day11input.txt') as f:
    f = f.read().splitlines()
o = {(x, y): int(f[y][x]) for x, y in product(range(10), range(10))}
flashes = 0


def adjacent(fx, fy):
    return [(x, y) for x, y in product(range(fx-1, fx+2), range(fy-1, fy+2))
            if 0 <= x < 10 and 0 <= y < 10 and (x != fx or y != fy)]


def flash(x, y):
    global flashes
    if not flashed[x, y]:
        flashed[x, y] = True
        flashes += 1
        for i in adjacent(x, y):
            o[i] += 1
            if o[i] > 9:
                flash(*i)


for s in range(1000):
    flashed = {(x, y): False for x, y in product(range(10), range(10))}

    for i in o:
        o[i] += 1
        if o[i] > 9:
            flash(*i)

    for i in o:
        if flashed[i]:
            o[i] = 0

#    for y in range(10):
#        for x in range(10):
#            print(o[x, y], end='')
#        print()
#    print()

    if False not in flashed.values():
        print(s+1)
        break
