# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=214

from math import ceil

def getResult(piece, n, m):
    if piece == 'r':
        return min(n, m)
    elif piece == 'k':
        return int(ceil(float(n * m) / 2))
    elif piece == 'Q':
        return min(n, m)
    elif piece == 'K':
        return int(ceil(float(n) /2)) * int(ceil (float(m) / 2))
        
# cases = int(raw_input())
cases = int(input())
for case in range(cases):
    # line = raw_input()
    line = input()
    strippedLine = line.strip()
    if line.strip():
        splittedLine = strippedLine.split()
        piece = str(splittedLine[0])
        n = int(splittedLine[1])
        m = int(splittedLine[2])
        print(getResult(piece, n, m))
    else:
        cases += 1
