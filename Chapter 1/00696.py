# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=637

from math import ceil

def getResult(n,m):
    smallMatrix = [[1,2,3],[2,4,4],[3,4,5]]
    minValue = min(n,m)
    maxValue = max(n,m)
    result = 0
    if minValue is 0 or maxValue is 0:
        result = 0
    elif minValue is 1:
        result = maxValue
    elif minValue is 2:
        if maxValue % 4 is 0:
            result = maxValue
        elif (maxValue + 1) % 4 is 0:
            result = maxValue + 1
        elif (maxValue + 2) % 4 is 0:
            result = maxValue + 2
        elif (maxValue + 3) % 4 is 0:
            result = maxValue + 1
    elif minValue <= 3 and maxValue <= 3:
        result = smallMatrix[n-1][m-1]
    else:
        result = int(ceil(float(n*m)/2))
    return str(result) + ' knights may be placed on a ' + str(n) + ' row ' + str(m) + ' column board.'


# results = []
while True:
    # n, m = map(int, raw_input().split())
    n, m = map(int, input().split())
    if n is 0 and m is 0:
        break
    else:
        result = getResult(n, m)
        # results.append(result)
        print(result)

# for result in results:
#     print(result)