while True:
    try:
        data = [int(x) for x in input().split()]
        n = data[0]
        jollySet = set()
        for i in range(2, n + 1):
            difference = abs(data[i] - data[i-1])
            jollySet.add(difference)
        isJollyJumper = True
        for i in range(n - 1):
            if not (i + 1) in jollySet:
                isJollyJumper = False
                break
        if isJollyJumper:
            print('Jolly')
        else:
            print('Not jolly')
    except EOFError:
        break