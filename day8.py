with open('day8input.txt') as f:
    f = [i.strip() for i in f]

f = [(i.split(' | ')[0].split(), i.split(' | ')[1].split()) for i in f]

count = 0
for i, j in f:
    u = i + j
    # t = top, m = middle, b = bottom, tl = top-left, etc.
    t, m, b, tl, tr, bl, br = (set('abcdefg') for k in range(7))
    # 1
    k = set('abcdefg').intersection(*(set(l) for l in u if len(l) == 2))
    tr &= k
    br &= k
    t -= k
    m -= k
    b -= k
    tl -= k
    bl -= k
    # 4
    k = set('abcdefg').intersection(*(set(l) for l in u if len(l) == 4))
    tr &= k
    br &= k
    tl &= k
    m &= k
    t -= k
    bl -= k
    b -= k
    # 7
    k = set('abcdefg').intersection(*(set(l) for l in u if len(l) == 3))
    tr &= k
    br &= k
    t &= k
    m -= k
    b -= k
    tl -= k
    bl -= k
    # 0, 6, 9
    k = set('abcdefg').intersection(*(set(l) for l in u if len(l) == 6))
    t &= k
    b &= k
    tl &= k
    br &= k
    # 2, 3, 5
    k = set('abcdefg').intersection(*(set(l) for l in u if len(l) == 5))
    t &= k
    m &= k
    b &= k

    for d in (t, m, b, tl, bl, tr, br):
        if len(d) > 1:
            d.difference_update(*(l for l in (t, m, b, tl, bl, tr, br) if len(l) == 1))

    output = ''
    for k in j:
        k = set(k)
        # 1
        if len(k) == 2:
            output += '1'
        # 4
        elif len(k) == 4:
            output += '4'
        # 7
        elif len(k) == 3:
            output += '7'
        # 8
        elif len(k) == 7:
            output += '8'
        # 0, 6, 9
        elif len(k) == 6:
            # 0
            if k <= t | tl | tr | bl | br | b:
                output += '0'
            # 6
            if k <= t | tl | m | bl | br | b:
                output += '6'
            # 9
            if k <= t | tl | m | tr | br | b:
                output += '9'
        # 2, 3, 5
        elif len(k) == 5:
            # 2
            if k <= t | m | b | tr | bl:
                output += '2'
            # 3
            if k <= t | m | b | tr | br:
                output += '3'
            # 5
            if k <= t | m | b | tl | br:
                output += '5'
    print(output, end=' ')
    count += int(output)

print(count)
