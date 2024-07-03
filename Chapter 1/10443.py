# This program returns the correct answer, is algorithmicly efficient but UVA return Time Limit Exceeded
# The same algorithm written in c++ runs just fine, I don't know if the TLE is due to Read/Write times in Python

# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1384

def isValidSquare(x,y,r,c):
    return x >= 0 and x < r and y >=0 and y < c

def printMatrix(matrix, r, c):
    for i in range(r):
        row = ''
        for j in range(c):
            row += matrix.get((i,j))
        print(row)

def getWinner(a, b):
    if a == b:
        return a
    elif a == 'R':
        return 'P' if b == 'P' else 'R'
    elif a == 'P':
        return 'S' if b == 'S' else 'P'
    elif a == 'S':
        return 'R' if b == 'R' else 'S'    

def getTomorrowMatrix(todayMatrix, r, c):
    tomorrowMatrix = {}
    for x in range(r):
        for y in range(c):
            if tomorrowMatrix.get((x, y)) is None:
                positions = [(x, y) ,(x, y-1), (x-1, y), (x, y+1), (x+1,y)]
                for position in positions:
                    xNeighbour = position[0]
                    yNeighbour = position[1]
                    if isValidSquare(xNeighbour, yNeighbour, r, c):
                        currentSquare = todayMatrix[(x, y)]
                        neighbour = todayMatrix[(xNeighbour, yNeighbour)]
                        winner = getWinner(currentSquare, neighbour)
                        tomorrowMatrix[x, y] = winner
                        if winner != neighbour:
                            tomorrowMatrix[xNeighbour, yNeighbour] = winner
                        if winner != currentSquare:
                            break                
    return tomorrowMatrix

# t = int(raw_input())
t = int(input())
isFirstTime = True
caseCounter = 0
keepReading = True

while keepReading:
    # inputLine = raw_input()
    inputLine = input()
    if inputLine.strip() != '':
        caseCounter += 1
    else:
        continue
    r, c, n = map(int, inputLine.split())
    todayMatrix = {}
    for i in range(r):
        # line = str(raw_input())
        line = str(input())
        for j in range(len(line)):
            todayMatrix[i, j] = line[j]
    for i in range(n):
        todayMatrix = getTomorrowMatrix(todayMatrix, r , c)
    
    if not isFirstTime:
        print('')
    isFirstTime = False

    printMatrix(todayMatrix, r, c)

    if caseCounter == t:
        keepReading = False