# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1130

def isValidPosition(row, column, n, m):
    return row >= 0 and row < n and column >=0 and column < m

def getPopulatedField(field, n ,m):
    solution = {}
    for i in range(n):
        for j in range(m):
            if field[(i, j)] == '*':
                solution[i, j] = '*'
            else:
                adjacentMines = 0
                positions = [ (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                for position in positions:
                    row = position[0]
                    column = position[1]
                    if isValidPosition(row, column, n, m):
                        adjacentMines += 1 if field[(row, column)] == '*' else 0
                solution[i, j] = str(adjacentMines)
    return solution


keepReading = True
case = 1
isFirstCase = True
while keepReading:
    field = []
    # n, m = map(int, raw_input().split())
    n, m = map(int, input().split())
    if n is 0 and m is 0:
        keepReading = False
        break
    if isFirstCase:
        isFirstCase = False
    else:
        print('')
    field = {}
    for i in range(n):
        # fieldLine = raw_input()
        fieldLine = input()
        for j in range(m):
            field[i, j] = fieldLine[j]
    solution = getPopulatedField(field, n, m)
    print('Field #' + str(case) +':')
    case += 1
    for i in range(0, n):
        line = ''
        for j in range(0, m):
            line += solution[(i, j)]
        print(line)
    