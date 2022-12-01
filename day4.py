from bidict import bidict

with open('day4input.txt') as f:
    f = [i.strip() for i in f]
    numbers = [int(i) for i in f[0].split(',')]
    boards = []
    temp = bidict()
    line = 0
    for i in f[2:]:
        if i != '':
            for j in enumerate(i.split()):
                temp[line, j[0]] = (int(j[1]), False)
            line += 1
        else:
            boards.append(temp)
            temp = bidict()
            line = 0
    boards.append(temp)

    def printBoard(board):
        for i in range(5):
            for j in range(5):
                if board[i, j][1] is True:
                    print(str(board[i, j][0]).rjust(3) + 'X ', end='')
                else:
                    print(str(board[i, j][0]).rjust(3) + 'O ', end='')
            print()

    def callNumbers():
        notWinning = [i for i in boards]
        for i in numbers:
            for b in boards:
                print(i, end=' ')
                for k, v in b.items():
                    if v[0] == i:
                        b[k] = (v[0], True)
                        for j in range(5):
                            row = [b[l][1] for l in b if l[0] == j]
                            column = [b[l][1] for l in b if l[1] == j]
                            if (False not in row or False not in column) and b in notWinning:
                                if len(notWinning) > 1:
                                    notWinning.remove(b)
                                else:
                                    print('\n')
                                    printBoard(b)
                                    return i, b

    lastCall, winningBoard = callNumbers()
    unmarked = 0
    for i in winningBoard.inv:
        if i[1] is False:
            unmarked += i[0]

    print(lastCall, unmarked)
    print(lastCall * unmarked)
