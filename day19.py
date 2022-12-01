from operator import sub, add
from itertools import combinations
    

with open('day19input.txt') as f:
    f = f.read().splitlines()


class Rot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Rot('{self.x}', '{self.y}', '{self.z}')"

    def apply(self, point):
        result = []
        x, y, z = point
        for i in (self.x, self.y, self.z):
            if i == 'x': result.append(x)
            elif i == 'y': result.append(y)
            elif i == 'z': result.append(z)
            elif i == '-x': result.append(-x)
            elif i == '-y': result.append(-y)
            elif i == '-z': result.append(-z)
        return tuple(result)

    def composite(self, rotation):
        result = []
        x = rotation.x
        y = rotation.y
        z = rotation.z
        for i in (self.x, self.y, self.z):
            if i == 'x': result.append(x)
            elif i == 'y': result.append(y)
            elif i == 'z': result.append(z)
            elif i == '-x':
                if x[0] == '-': result.append(x[1])
                else: result.append('-' + x)
            elif i == '-y':
                if y[0] == '-': result.append(y[1])
                else: result.append('-' + y)
            elif i == '-z':
                if z[0] == '-': result.append(z[1])
                else: result.append('-' + z)
        return Rot(*result)

    def inverse(self):
        result = {}
        if self.x == 'x': result[0] = 'x'
        elif self.x == 'y': result[1] = 'x'
        elif self.x == 'z': result[2] = 'x'
        elif self.x == '-x': result[0] = '-x'
        elif self.x == '-y': result[1] = '-x'
        elif self.x == '-z': result[2] = '-x'
        if self.y == 'x': result[0] = 'y'
        elif self.y == 'y': result[1] = 'y'
        elif self.y == 'z': result[2] = 'y'
        elif self.y == '-x': result[0] = '-y'
        elif self.y == '-y': result[1] = '-y'
        elif self.y == '-z': result[2] = '-y'
        if self.z == 'x': result[0] = 'z'
        elif self.z == 'y': result[1] = 'z'
        elif self.z == 'z': result[2] = 'z'
        elif self.z == '-x': result[0] = '-z'
        elif self.z == '-y': result[1] = '-z'
        elif self.z == '-z': result[2] = '-z'
        return Rot(*(result[i] for i in sorted(result)))
        

scanners = []
for l in f:
    if l == '':
        pass
    elif l[0:3] == '---': 
        scanners.append([])
    else:
        scanners[-1].append(tuple([int(i) for i in l.split(',')]))

positions = {0: (0, 0, 0)}
rotations = {0: Rot('x', 'y', 'z')}

distances = [{frozenset(map(abs, map(sub, a, b))): frozenset((a, b))
                     for a, b in combinations(s, 2)} for s in scanners]

n0 = 0
while n0 < len(distances):
    d0 = distances[n0]
    for n, d in {i: distances[i] for i in range(len(distances))
                 if i not in positions}.items():
        congruent = set(d) & set(d0)
        for e in congruent:
            pointSharers = {i for i in congruent
                            if not d0[e].isdisjoint(d0[i])
                            and i != e}
            edge1 = pointSharers.pop()
            # Ensure that edge2 doesn't share a point with both e and edge1
            edge2 = {i for i in pointSharers if d[i] & d[e] & d[edge1] == set()}.pop()
            point1 = (*[i for i in d0[e] & d0[edge1]],
                      *[i for i in d[e] & d[edge1]])
            point2 = (*[i for i in d0[e] & d0[edge2]],
                      *[i for i in d[e] & d[edge2]])
            # Directed distance
            a = tuple(map(sub, point1[0], point2[0]))
            b = tuple(map(sub, point1[1], point2[1]))
            if len(set(map(abs, a))) == 3:
                orientation = []
                for i in a:
                    if i == b[0]: orientation.append('x')
                    elif i == b[1]: orientation.append('y')
                    elif i == b[2]: orientation.append('z')
                    elif i == -b[0]: orientation.append('-x')
                    elif i == -b[1]: orientation.append('-y')
                    elif i == -b[2]: orientation.append('-z')
                relativeRot = Rot(*orientation)
                rotations[n] = rotations[n0].composite(relativeRot)

            relativePos = tuple(map(sub,
                                    point1[0],
                                    relativeRot.apply(point1[1])))

            positions[n] = tuple(map(add,
                                     positions[n0],
                                     rotations[n0].apply(relativePos)))

            break

    n0 += 1
    while n0 not in rotations:
        n0 += 1
        if n0 >= len(distances):
            break


beacons = set()
for s in range(len(scanners)):
    for b in scanners[s]:
        a = rotations[s].apply(map(add,
                                   b,
                                   positions[s]))
        beacons.add(a)


print({k: str(rotations[k]) for k in sorted(rotations)})
print({k: positions[k] for k in sorted(positions)})
print(len(beacons))
