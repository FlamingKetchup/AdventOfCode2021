with open('day14input.txt') as f:
    f = f.read().splitlines()
template = f[0]
folds = dict([i.split(' -> ') for i in f[2:]])
pairs = {pair: template.count(pair) for pair in folds}

for step in range(40):
    temp = {k: v for k, v in pairs.items()}
    for pair, insertion in folds.items():
        temp[pair[0] + insertion] += pairs[pair]
        temp[insertion + pair[1]] += pairs[pair]
        temp[pair] -= pairs[pair]
    pairs = {k: v for k, v in temp.items()}

monomers = {i: 0.0 for i in set(''.join(pairs))}
for k, v in pairs.items():
    for i in k:
        monomers[i] += v/2
monomers[template[0]] += 0.5
monomers[template[-1]] += 0.5

print(monomers)

print(max(monomers.values()) - min(monomers.values()))
