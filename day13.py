with open('day13input.txt') as f:
    f = f.read().splitlines()
points = {(int(i.split(',')[0]), int(i.split(',')[1])) for i in f[:f.index('')]}
folds = [(i[11], int(i[13:])) for i in f[f.index('') + 1:]]

def foldX(lineX):
    global points
    new = set()
    for x, y in points:
        if x > lineX:
            new.add((-(x-lineX)+lineX, y))
        else:
            new.add((x, y))
    points = new

def foldY(lineY):
    global points
    new = set()
    for x, y in points:
        if y > lineY:
            new.add((x, -(y-lineY)+lineY))
        else:
            new.add((x, y))
    points = new

for axis, num in folds:
    if axis == 'x':
        foldX(num)
    elif axis == 'y':
        foldY(num)
    else:
        raise Exception(f'There is no axis called: {axis}')

for y in range(max([i[1] for i in points]) + 1):
    for x in range(max([i[0] for i in points]) + 1):
        if (x, y) in points:
            print('#', end='')
        else:
            print('.', end='')
    print()

