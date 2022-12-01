class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if p1.y == p2.y:
            Xs = range(p1.x, p2.x + 1) if p2.x > p1.x else range(p2.x, p1.x + 1)
            self.points = {Point(x, p1.y) for x in Xs}
        elif p1.x == p2.x:
            Ys = range(p1.y, p2.y + 1) if p2.y > p1.y else range(p2.y, p1.y + 1)
            self.points = {Point(p1.x, y) for y in Ys}
        else:
            Xs = range(p1.x, p2.x + 1) if p2.x > p1.x else range(p2.x, p1.x + 1)
            slope = (p2.y - p1.y)//(p2.x - p1.x)
            yInt = p1.y - p1.x*slope
            self.points = {Point(x, slope*x + yInt) for x in Xs}

with open('day5input.txt') as f:
    f = [i.strip() for i in f]

f = [i.split(' -> ') for i in f]
f = [(i.split(','), j.split(',')) for i, j in f]
lines = [Line(Point(int(i[0]), int(i[1])), Point(int(j[0]), int(j[1]))) for i, j in f]
overlaps = set()

for i in lines:
    for j in lines:
        if i != j:
            overlaps |= i.points & j.points

print(len(overlaps))
