with open('day7input.txt') as f:
    f = f.read().strip().split(',')

crabs = [int(i) for i in f]

costs = []
for i in range(min(crabs), max(crabs) + 1):
    cost = 0
    for c in crabs:
        dist = abs(i - c)
        cost += dist * (dist + 1)/2
    costs.append(cost)

print(min(costs))
