# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=525

def getScore(score):
    if score == 'X':
        return 10
    elif score == '/':
        return 10
    else:
        return score

def getPositionsScore(positions, rolls):
    score = 0
    totalRolls = len(rolls)
    positionsLength = len(positions)
    if positionsLength == 1: # previous roll was '/'
        if positions[0] < totalRolls:
            roll = rolls[positions[0]] # can only be number or 'X'
            score = 10 if roll is 'X' else int(roll)
    elif positionsLength == 2:
        if positions[0] < totalRolls and positions[1] < totalRolls:
            roll1 = rolls[positions[0]]
            roll2 = rolls[positions[1]]
            if roll1.isdigit() and roll2.isdigit():
                score = int(roll1) + int(roll2)
            elif roll1.isdigit() and roll2 is '/':
                score = 10
            elif roll1 is 'X':
                score = 10
                score += 10 if roll2 is 'X' else int(roll2)
        elif positions[0] < totalRolls:
            roll = rolls[positions[0]] # can only be number or 'X'
            score = 10 if roll is 'X' else int(roll)
    return score
            
while True:
    # inputLine = str(raw_input())
    inputLine = str(input())
    if inputLine == 'Game Over':
        break
    rolls = inputLine.split(' ')
    
    totalRolls = len(rolls)
    totalScore = 0
    
    frameScore = 0
    attemptCounter = 0
    lastDigitAdded = 0
    frameCounter = 0

    for i in range(totalRolls):
        roll = rolls[i]
        if roll.isdigit():
            digit = int(roll)
            lastDigitAdded = digit
            frameScore += digit
            attemptCounter += 1
        elif roll == '/':
            frameScore += 10 - lastDigitAdded
            frameScore += getPositionsScore([i + 1], rolls)
            attemptCounter += 1
        elif roll == 'X':
            attemptCounter = 2
            frameScore = 10
            frameScore += getPositionsScore([i + 1, i + 2], rolls)
        
        if attemptCounter == 2 and frameCounter < 10:
            frameCounter += 1
            totalScore += frameScore
            frameScore = 0
            attemptCounter = 0
    print(totalScore)

