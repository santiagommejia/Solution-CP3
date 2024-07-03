# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=403

def getResult(cards):
    points = 0
    suiteCount = [0, 0, 0, 0] # S, H, D, C
    stoppedSuite = [False, False, False, False] # S, H, D, C
    # count number of cards per suite
    for card in cards:
        suite = card[1]
        if suite == 'S':
            suiteCount[0] = suiteCount[0] + 1
        if suite == 'H':
            suiteCount[1] = suiteCount[1] + 1
        if suite == 'D':
            suiteCount[2] = suiteCount[2] + 1
        if suite == 'C':
            suiteCount[3] = suiteCount[3] + 1
    # count points
    for card in cards:
        rank = card[0]
        suite = card[1]
        if rank == 'A':
            points += 4 
            stoppedSuite[getSuitePosition(suite)] = True
        elif rank == 'K':
            points += 3 
            suiteAmount = suiteCount[getSuitePosition(suite)]
            if suiteAmount == 1:
                points -= 1
            elif suiteAmount > 1:
                stoppedSuite[getSuitePosition(suite)] = True
        elif rank == 'Q':
            points += 2 
            suiteAmount = suiteCount[getSuitePosition(suite)]
            if suiteAmount == 1 or suiteAmount == 2:
                points -= 1
            elif suiteAmount > 2:
                stoppedSuite[getSuitePosition(suite)] = True
        elif rank == 'J':
            points += 1 
            suiteAmount = suiteCount[getSuitePosition(suite)]
            if suiteAmount == 1 or suiteAmount == 2 or suiteAmount == 3:
                points -= 1

    pointsNoTrump = points
    # rule 5
    S = suiteCount[getSuitePosition('S')]
    H = suiteCount[getSuitePosition('H')]
    D = suiteCount[getSuitePosition('D')]
    C = suiteCount[getSuitePosition('C')]
    pointsNoTrump += 1 if S == 2 else 0
    pointsNoTrump += 1 if H == 2 else 0
    pointsNoTrump += 1 if D == 2 else 0
    pointsNoTrump += 1 if C == 2 else 0
    # rule 6
    pointsNoTrump += 2 if S == 1 else 0
    pointsNoTrump += 2 if H == 1 else 0
    pointsNoTrump += 2 if D == 1 else 0
    pointsNoTrump += 2 if C == 1 else 0
    # rule 7
    pointsNoTrump += 2 if S == 0 else 0
    pointsNoTrump += 2 if H == 0 else 0
    pointsNoTrump += 2 if D == 0 else 0
    pointsNoTrump += 2 if C == 0 else 0

    allSuitesStopped = stoppedSuite[0] and stoppedSuite[1] and stoppedSuite[2] and stoppedSuite[3]
    if points >= 16 and allSuitesStopped:
        return 'BID NO-TRUMP'
    elif pointsNoTrump >= 14:
        suitePosition = suiteCount.index(max(suiteCount))
        return 'BID ' + getSuiteFromPosition(suitePosition)
    elif pointsNoTrump < 14:
        return 'PASS'

def getSuitePosition(suite):
    if suite == 'S':
        return 0
    if suite == 'H':
        return 1
    if suite == 'D':
        return 2
    if suite == 'C':
        return 3

def getSuiteFromPosition(position):
    if position == 0:
        return 'S'
    if position == 1:
        return 'H'
    if position == 2:
        return 'D'
    if position == 3:
        return 'C'

while True:
    try:
        # cards = [str(x) for x in raw_input().split()]
        cards = [str(x) for x in input().split()]
        result = getResult(cards)        
        print(result)
    except EOFError:
        break
