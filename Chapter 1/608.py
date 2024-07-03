POSSIBLE_RESULTS = [
    [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
]

def computeResult(possibleResult, a, b, isHeavy):
    isOnLeftSide = None
    for char in a:
        position = ord(char) - 65
        coin = possibleResult[position]
        if coin == -1:
            isOnLeftSide = True
    sumRight = 0
    for char in b:
        position = ord(char) - 65
        coin = possibleResult[position]
        if coin == -1:
            isOnLeftSide = False
    
    if isOnLeftSide is None:
        return 'even'
    if isHeavy:
        return 'up' if isOnLeftSide else 'down'
    if not isHeavy:
        return 'up' if not isOnLeftSide else 'down'
    

cases = int(input())
for case in range(cases):
    a, b, c = map(str, input().split())
    d, e, f = map(str, input().split())
    g, h, i = map(str, input().split())
    foundResult = False
    for possibleResult in POSSIBLE_RESULTS: #heavy
        myResult1 = computeResult(possibleResult, a, b, True)
        myResult2 = computeResult(possibleResult, d, e, True)
        myResult3 = computeResult(possibleResult, g, h, True)
        if myResult1 == c and myResult2 == f and myResult3 == i:
            index = possibleResult.index(-1)
            letter = chr(index + 65)
            foundResult = True
            print(letter + ' is the counterfeit coin and it is heavy.')
    
    if not foundResult: # (0.18 sec optimization on UVa)
        for possibleResult in POSSIBLE_RESULTS: #light
            myResult1 = computeResult(possibleResult, a, b, False)
            myResult2 = computeResult(possibleResult, d, e, False)
            myResult3 = computeResult(possibleResult, g, h, False)
            if myResult1 == c and myResult2 == f and myResult3 == i:
                index = possibleResult.index(-1)
                letter = chr(index + 65)
                print(letter + ' is the counterfeit coin and it is light.')
