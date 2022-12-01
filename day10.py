with open('day10input.txt') as f:
    score = 0
    incomplete = []
    for l in f:
        o = []
        corrupt = False
        for i in l:
            if i in ('(', '[', '{', '<'):
                o.append(i)
            else:
                if i == ')' and o[-1] != '(':
                    score += 3
                    corrupt = True
                    o.pop()
                elif i == ']' and o[-1] != '[':
                    score += 57
                    corrupt = True
                    o.pop()
                elif i == '}' and o[-1] != '{':
                    score += 1197
                    corrupt = True
                    o.pop()
                elif i == '>' and o[-1] != '<':
                    score += 25137
                    corrupt = True
                    o.pop()
                else:
                    o.pop()
        if not corrupt:
            incomplete.append(l)
    
    linePoints = []
    for l in incomplete:
        o = []
        points = 0
        l = l.strip()
        for i in l:
            if i in ('(', '[', '{', '<'):
                o.append(i)
            else:
                o.pop()
        o.reverse()
        print(o)
        for i in o:
            points *= 5
            if i == '(':
                points += 1
            elif i == '[':
                points += 2
            elif i == '{':
                points += 3
            else:
                points += 4
        linePoints.append(points)

    linePoints.sort()

    print(linePoints)
    print(linePoints[len(linePoints)//2])
