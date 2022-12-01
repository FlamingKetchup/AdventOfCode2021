with open('day2input.txt') as f:
    f = [(i.split(' ')[0], int(i.split(' ')[1])) for i in f]
    aim = 0
    horizontal = 0
    depth = 0
    for i in f:
        if i[0] == 'forward':
            horizontal += i[1]
            depth += aim * i[1]
        elif i[0] == 'down':
            aim += i[1]
        elif i[0] == 'up':
            aim -= i[1]
        else:
            raise Exception(f'Got {i[0]}, expected forward, down, or up')
    print(horizontal * depth)
