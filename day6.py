with open('day6input.txt') as f:
    f = str(f.read()).strip().split(',')
    timers = [int(i) for i in f]
    timers = {k: timers.count(k) for k in range(9)}

for n in range(256):
    timers = {(k-1)%9: v for k, v in timers.items()}
    timers[6] += timers[8]
    print(n)
print(sum(timers.values()))
