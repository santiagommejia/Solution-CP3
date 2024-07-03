# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2162

import math 

def getCleanLine(inputLine):
    line = ''
    for char in inputLine:
        if char.isalpha():
            line += char.lower()
    return line

def getSquareDimensions(lineLength):
    sqr = int(math.sqrt(lineLength))
    if sqr * sqr == lineLength:
        return sqr
    elif sqr * sqr < lineLength:
        if (sqr + 1) * (sqr + 1) == lineLength:
            return int(sqr + 1)
    return None

def isMagicSquare(line, k):
    rows = []
    columnCounter = 0
    rowChars = ''
    columnMap = { i: '' for i in range(k) }
    for i in range(len(line)):
        char = line[i]
        if columnCounter < k:
            rowChars += char
        else:
            rows.append(rowChars)
            rowChars = char
            columnCounter = 0
        currentColumn = columnMap.get(columnCounter)
        currentColumn += char
        columnMap[columnCounter] = currentColumn
        columnCounter += 1
    rows.append(rowChars) # append last row
    
    # checks:

    # condition 1 and 3:
    condition1Line = ''
    condition3Line = ''
    rowsLength = len(rows)
    for i in range(rowsLength):
        firstRow = rows[i]
        lastRow = rows[rowsLength - 1 - i]
        condition1Line += firstRow
        condition3Line += lastRow[::-1]
    condition1 = True if condition1Line == line else False
    condition3 = True if condition3Line == line else False

    # condition 2 and 4:
    condition2Line = ''
    condition4Line = ''
    for i in range(k):
        firstColumn = columnMap.get(i)
        lastColumn = columnMap.get(k - 1 - i)
        condition2Line += firstColumn
        condition4Line += lastColumn[::-1]
    condition2 = True if condition2Line == line else False
    condition4 = True if condition4Line == line else False

    return condition1 and condition2 and condition3 and condition4

# cases = int(raw_input())
cases = int(input())
for case in range(1, cases +1):
    # inputLine = str(raw_input())
    inputLine = str(input())
    cleanLine = getCleanLine(inputLine)
    k = getSquareDimensions(len(cleanLine))
    print('Case #' + str(case) + ':')
    if k is None:
        print('No magic :(')
        pass
    else:
        magicSquare = isMagicSquare(cleanLine, k)
        if magicSquare:
            print(k)
        else:
            print('No magic :(')
    