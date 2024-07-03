# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=7&page=show_problem&problem=497

def turnLeft(lookingAt):
    if lookingAt == 'E':
        return 'N'
    elif lookingAt == 'N':
        return 'W'
    elif lookingAt == 'W':
        return 'S'
    else:
        return 'E'

def turnRight(lookingAt):
    if lookingAt == 'E':
        return 'S'
    elif lookingAt == 'N':
        return 'E'
    elif lookingAt == 'W':
        return 'N'
    else:
        return 'W'

def initEmptyCountMaze(b, w):
    maze = {x: [] for x in range(b)}
    for i in range(0, b):
        currentLine = maze[i]
        for j in range(0,w):
            currentLine.append(0)
        maze[i] = currentLine
    return maze

# def printMaze(b,w, maze):
#     print()
#     print('Printing Maze...', maze)
#     for i in range(0,b):
#         mazeLine = ''
#         for j in range(0,w):
#             mazeLine += str(maze[i][j])
#         print(mazeLine)

def format(num):
    l = len(str(num))
    if l == 1:
        return '  ' + str(num)
    if l == 2:
        return ' ' + str(num)
    return str(num)


def simulation(b, w, maze):
    mazeCount = initEmptyCountMaze(b, w)
    currentX = b - 1
    currentY = 0
    lookingAt = 'E' # 'E', 'N', 'W', 'S'
    
    startingSquare = [currentX, currentY] # [X, Y]
    previousSquare = None # [X, Y]
    currentSquare = [currentX, currentY] # [X, Y]

    continueSimulation = True
    while continueSimulation:
        currentSquare = [currentX, currentY]
        if currentSquare != previousSquare:
            if previousSquare != None and currentSquare == startingSquare:
                continueSimulation = False
            else:
                currentSquareCount = mazeCount[currentSquare[0]][currentSquare[1]]
                mazeCount[currentSquare[0]][currentSquare[1]] = currentSquareCount + 1
            
            
        
        previousSquare = [currentX, currentY]
        if lookingAt == 'E': # try to go east
            canGoRight = currentX + 1 < b and maze[currentX + 1][currentY] != '1'
            canGoStraight = currentY + 1 < w and maze[currentX][currentY + 1] != '1'
            if canGoRight:
                currentX = currentX + 1
                lookingAt = turnRight(lookingAt)
            elif canGoStraight:
                currentY = currentY + 1 
            else:
                lookingAt = turnLeft(lookingAt)
        elif lookingAt == 'N': # try to go north
            canGoRight = currentY + 1 < w and maze[currentX][currentY + 1] != '1'
            canGoStraight = currentX - 1 >= 0 and maze[currentX - 1][currentY] != '1'
            if canGoRight:
                currentY = currentY + 1
                lookingAt = turnRight(lookingAt)
            elif canGoStraight:
                currentX = currentX - 1
            else:
                lookingAt = turnLeft(lookingAt)
        elif lookingAt == 'W': # try to go west
            canGoRight = currentX - 1 >= 0 and maze[currentX - 1][currentY] != '1'
            canGoStraight = currentY - 1 >= 0 and maze[currentX][currentY - 1] != '1'
            if canGoRight:
                currentX = currentX - 1
                lookingAt = turnRight(lookingAt)
            elif canGoStraight:
                currentY = currentY - 1
            else:
                lookingAt = turnLeft(lookingAt)
        elif lookingAt == 'S': # try to go south
            canGoRight = currentY - 1 >= 0 and maze[currentX][currentY - 1] != '1'
            canGoStraight = currentX + 1 < b and maze[currentX + 1][currentY] != '1'
            if canGoRight:
                currentY = currentY - 1
                lookingAt = turnRight(lookingAt)
            elif canGoStraight:
                currentX = currentX + 1
            else:
                lookingAt = turnLeft(lookingAt)
    
    return mazeCount

maze = {}
b, w = map(int, input().split())
while b!= 0 and w!=0:
    for i in range(0, b):
        mazeLine = input()
        maze[i] =  str(mazeLine).strip()
    mazeCount = simulation(b, w, maze)
    r = [0, 0, 0, 0, 0]
    for i in range(0, b):
        for j in range(0, w):
            n = mazeCount[i][j] 
            if maze[i][j] != '1' and (n == 0 or n == 1 or n == 2 or n == 3 or n == 4):
                r[n] = r[n] + 1
    strResult = format(r[0]) + format(r[1]) + format(r[2]) + format(r[3]) + format(r[4])
    print(strResult)
    b, w = map(int, input().split())