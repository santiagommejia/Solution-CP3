# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1754

def printResult(number):
    print('BINGO after ' + str(number) +' numbers announced')

# cases = int(raw_input())
cases = int(input())
for case in range(cases):
    bingoMap = {} # number -> (row,column) #free space on 2,2
    for i in range(5):
        # row = [int(number) for number in raw_input().split()]
        row = [int(number) for number in input().split()]
        for j in range(len(row)):
            number = row[j]
            jPosition = j+1 if i == 2 and j >= 2 else j
            bingoMap[number] = (i, jPosition)
    keepReading = True
    bingoOrder = []
    while keepReading:
        # line = raw_input()
        line = input()
        if line.strip() == '':
            continue
        else:
            numbers = [int(number) for number in line.split()]
            bingoOrder = bingoOrder + numbers
        if len(bingoOrder) == 75:
            keepReading = False
    rowMap = {} # rowNumber -> markedCount
    columnMap = {} # columnNumber -> markedCount
    diagonal1Count = 0
    diagonal2Count = 0

    for i in range(len(bingoOrder)):
        number = bingoOrder[i]
        position = bingoMap.get(number)
        if position is not None:
            row = position[0]
            column = position[1]
            rowCount = rowMap.get(row)
            columnCount = columnMap.get(column)
            rowCount = 1 if rowCount is None else rowCount + 1
            columnCount = 1 if columnCount is None else columnCount + 1
            rowMap[row] = rowCount
            columnMap[column] = columnCount
            if row == column:
                diagonal1Count += 1
            if row + column == 4:
                diagonal2Count += 1
            
            if diagonal1Count == 4 or diagonal2Count is 4:
                printResult(i + 1)
                break     
            if row is 2 and rowCount is 4:
                printResult(i + 1)
                break
            elif row is not 2 and rowCount is 5:
                printResult(i + 1)
                break
            elif column is 2 and columnCount is 4:
                printResult(i + 1)
                break
            elif column is not 2 and columnCount is 5:
                printResult(i + 1)
                break
            