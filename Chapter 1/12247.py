# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3399

while True:
    # A, B, C, X, Y = map(int, raw_input().split())
    A, B, C, X, Y = map(int, input().split())
    her = sorted([A, B, C])
    his = sorted([X, Y])
    card = -1
    available = [True for i in range(0, 53)]
    possibleResults = []
    if A is 0 and B is 0 and C is 0 and X is 0 and Y is 0:
        break
    for i in range(3):
        available[her[i]] = False
        if i < 2:
            available[his[i]] = False
    # Both are higher
    if his[0] > her[2]:
        for i in range(1, 53):
            if available[i]:
                possibleResults.append(i)

                break
        
    # One is higher than all
    if his[1] > her[2]:
        for i in range(her[2] , 53):
            if available[i]:
                possibleResults.append(i)
                break

    if his[0] > her[1]:
        for i in range(her[1] , 53):
            if available[i]:
                possibleResults.append(i)
                break

    if len(possibleResults) == 0:
        possibleResults.append(-1)

    result = sorted(possibleResults)[0]
    print(result)
