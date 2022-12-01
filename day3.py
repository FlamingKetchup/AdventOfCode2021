with open('day3input.txt') as f:
    f = [i.strip() for i in f]
    bitcount = [0 for i in range(12)]
    for i in f:
        for j in enumerate(i):
            if j[1] == '1':
                bitcount[j[0]] += 1
    gamma = ''
    epsilon = ''
    for i in bitcount:
        if i > len(f)/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    # Part 2
    oxy = f
    for i in range(12):
        count = 0
        for j in oxy:
            if j[i] == '1':
                count += 1
        print(f'1s: {count}, half length: {len(oxy)/2}')
        if count >= len(oxy)/2:
            bit = '1'
        else:
            bit = '0'
        oxy = [j for j in oxy if j[i] == bit]

    co2 = f
    for i in range(12):
        count = 0
        if len(co2) == 1:
            break
        else:
            for j in co2:
                if j[i] == '1':
                    count += 1
            if count < len(co2)/2:
                bit = '1'
            else:
                bit = '0'
        co2 = [j for j in co2 if j[i] == bit]

    oxy = int(oxy[0], 2)
    co2 = int(co2[0], 2)

    print(oxy * co2)
