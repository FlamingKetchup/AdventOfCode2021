from itertools import product

Xs = {k: set() for k in range(1000)}
for i in Xs:
    velX = i
    x = 0
    steps = 0
    while x <= 129 and velX >= 0:
        steps += 1
        x += velX
        if 81 <= x <= 129:
            if velX > 0:
                Xs[i].add(steps)
            else:
                Xs[i] |= set(range(steps, 1000))
        velX -= 1 

print()

Ys = {k: set() for k in range(-200, 1000)}
for i in Ys:
    velY = i
    y = 0
    steps = 0
    while y >= -150:
        steps += 1
        y += velY
        if -150 <= y <= -108:
            Ys[i].add(steps)
        velY -= 1

print(len([(x, y) for x, y in product(Xs, Ys) if Xs[x] & Ys[y] != set()]))
