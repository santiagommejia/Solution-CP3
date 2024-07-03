# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=242&page=show_problem&problem=3212

from fractions import Fraction

keepReading = True
case = 1
while keepReading:
    inputLine = str(input()).split(' ')
    if inputLine == ['0']:
        keepReading = False
        break
    
    divisor = int(inputLine[0])
    total = 0
    for i in range(1, len(inputLine)):
        total += int(inputLine[i])
    isNegative = True if total < 0 else False
    sign = '-' if isNegative else ''
    if isNegative:
        total *= -1

    print('Case ' + str(case) + ':')
    remainder = total % divisor
    if remainder == 0: # is integer
        result = int(total/divisor)
        strResult = sign + ' ' + str(result) if isNegative else str(result)
        print(strResult)
    
    elif remainder != 0: # is fraction
        integer = int((total - remainder) / divisor)
        q = Fraction(remainder, divisor)
        a = q.numerator
        b = q.denominator
        
        topPositionCount = 2 if isNegative else 0
        bottomPositionCount = 2 if isNegative else 0
        middle = '- ' if isNegative else ''
        if integer != 0:
            topPositionCount += len(str(integer))
            bottomPositionCount += len(str(integer))
            middle += str(integer)
        topPositionCount += len(str(b)) - len(str(a))
        top = ''.join([' ' for i in range(topPositionCount)]) + str(a)
        bottom = ''.join([' ' for i in range(bottomPositionCount)]) + str(b)
        middle += ''.join(['-' for i in range(len(str(b)))])
        print(top)
        print(middle)
        print(bottom)
    case += 1

