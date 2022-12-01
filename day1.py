with open('day1input.txt') as f:
    f = [int(i.strip()) for i in f]
    count = 0
    for i in range(3, len(f)):
        if f[i] > f[i-3]:
            count += 1
    print(count)
