# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1225

def isValidPosition(row, column):
    return row >=0 and row <=7 and column >= 0 and column <= 7

def getAttackedPositions(char, row, column):
    attackedPositions = []
    rowAttack1 = []
    columnAttack1 = []
    rowAttack2 = []
    columnAttack2 = []

    rowCounter = row
    while rowCounter > 0:
        rowCounter -= 1
        columnAttack1.append((rowCounter, column))
    rowCounter = row
    while rowCounter < 8:
        rowCounter += 1
        columnAttack2.append((rowCounter, column))
    
    columnCounter = column
    while columnCounter > 0:
        columnCounter -= 1
        rowAttack1.append((row, columnCounter))
    columnCounter = column
    while columnCounter < 8:
        columnCounter += 1
        rowAttack2.append((row, columnCounter))

    diagonalAttack1 = []
    diagonalAttack2 = []
    diagonalAttack3 = []
    diagonalAttack4 = []

    rowCounter = row
    columnCounter = column
    while rowCounter > 0 and columnCounter > 0:
        rowCounter -= 1
        columnCounter -= 1
        diagonalAttack1.append((rowCounter, columnCounter))
    
    rowCounter = row
    columnCounter = column
    while rowCounter < 8 and columnCounter < 8:
        rowCounter += 1
        columnCounter += 1
        diagonalAttack2.append((rowCounter, columnCounter))
    
    rowCounter = row
    columnCounter = column
    while rowCounter > 0 and columnCounter < 8:
        rowCounter -= 1
        columnCounter += 1
        diagonalAttack3.append((rowCounter, columnCounter))
    
    rowCounter = row
    columnCounter = column
    while rowCounter < 8 and columnCounter > 0:
        rowCounter += 1
        columnCounter -= 1
        diagonalAttack4.append((rowCounter, columnCounter))

    if char == 'p':
        attackedPositions.append([ (row + 1, column - 1), (row + 1, column + 1) ])
    elif char == 'P':
        attackedPositions.append([ (row - 1, column - 1), (row - 1, column + 1) ])
    elif char == 'n' or char == 'N':
        attackedPositions.append([ (row - 2, column + 1), (row - 2, column - 1), (row + 2, column + 1), (row + 2, column - 1), (row - 1, column -2), (row + 1, column -2), (row - 1, column +2), (row + 1, column +2) ])
    elif char == 'b' or char == 'B':
        attackedPositions.append(diagonalAttack1)
        attackedPositions.append(diagonalAttack2)
        attackedPositions.append(diagonalAttack3)
        attackedPositions.append(diagonalAttack4)
    elif char == 'r' or char == 'R':
        attackedPositions.append(rowAttack1)
        attackedPositions.append(columnAttack1)
        attackedPositions.append(rowAttack2)
        attackedPositions.append(columnAttack2)
    elif char == 'q' or char == 'Q':
        attackedPositions.append(rowAttack1)
        attackedPositions.append(columnAttack1)
        attackedPositions.append(rowAttack2)
        attackedPositions.append(columnAttack2)
        attackedPositions.append(diagonalAttack1)
        attackedPositions.append(diagonalAttack2)
        attackedPositions.append(diagonalAttack3)
        attackedPositions.append(diagonalAttack4)
    elif char == 'k' or char == 'K':
        attackedPositions.append([ (row - 1, column - 1), (row - 1, column), (row - 1, column + 1), (row, column - 1), (row, column + 1), (row + 1, column - 1), (row + 1, column), (row + 1, column + 1) ])
    return attackedPositions

def setAttackedSquares(char, row, column, attackedBoard, originalBoard):
    attackedPositions = getAttackedPositions(char, row, column)
    attackCutOffPieces = ['Q','q','B','b','R','r']
    for attack in attackedPositions:
        for attackedPosition in attack:
            attackedRow = attackedPosition[0]
            attackedColumn = attackedPosition[1]
            if isValidPosition(attackedRow, attackedColumn):
                if char in attackCutOffPieces and not originalBoard[(attackedRow, attackedColumn)]:
                    break
                else:
                    attackedBoard[attackedRow, attackedColumn] = False
    return attackedBoard

while True:
    try:
        attackedBoard = { (i,j):True for i in range(8) for j in range(8) }
        originalBoard = { (i,j):True for i in range(8) for j in range(8) }
        # inputLine = str(raw_input())
        inputLine = str(input())
        boardLines = inputLine.split('/')
        rowCounter = 0
        for row in boardLines:
            columnCounter = 0
            for char in row:
                if char.isdigit():
                    digit = int(char)
                    columnCounter += digit
                else:
                    originalBoard[rowCounter, columnCounter] = False
                    columnCounter += 1
            rowCounter += 1
        rowCounter = 0                    
        for row in boardLines:
            columnCounter = 0
            for char in row:
                if char.isdigit():
                    digit = int(char)
                    columnCounter += digit
                else:
                    attackedBoard[rowCounter, columnCounter] = False
                    attackedBoard = setAttackedSquares(char, rowCounter, columnCounter, attackedBoard, originalBoard)
                    columnCounter += 1
            rowCounter += 1
        freeSquaresCounter = 0
        for i in attackedBoard.keys():
            freeSquaresCounter += 1 if attackedBoard[i] else 0
        print(freeSquaresCounter)
    except:
        break
