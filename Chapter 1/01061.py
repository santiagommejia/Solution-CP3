# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=0&problem=3502

bloodTypeMatrix = [
    ['O','O', ['O']],
    ['AB','AB', ['A','AB','B']],
    ['AB', 'B', ['AB','B','A']],
    ['AB', 'O', ['A','B']],
    ['B','B', ['B', 'O']],
    ['B','O', ['B', 'O']],
    ['A', 'A', ['A', 'O']],
    ['A', 'AB', ['A', 'AB', 'B']],
    ['A', 'B', ['A', 'AB', 'B', 'O']],
    ['A', 'O', ['A', 'O']]
]

def getSign(bloodType):
    return bloodType[len(bloodType) -1]

def getBloodType(bloodType):
    return bloodType[0: len(bloodType) -1 ]

def getChildBloodSet(p1, p2):
    signP1 = getSign(p1)
    signP2 = getSign(p2)
    bloodType1 = getBloodType(p1)
    bloodType2 = getBloodType(p2)
    possibleBloodTypes = []
    for i in bloodTypeMatrix:
        if (bloodType1 == i[0] and bloodType2 == i[1]) or (bloodType1 == i[1] and bloodType2 == i[0]):
            possibleBloodTypes = i[2]
    rh = []
    if signP1 == '+' and signP2 == '+':
        rh = ['+', '-']
    elif signP1 == '+' and signP2 == '-' or signP1 == '-' and signP2 == '+':
        rh = ['+', '-']
    else:
        rh = ['-']
    results = []
    for i in possibleBloodTypes:
        for j in rh:
            results.append(i + j)
    return results

def getParentBloodSet(p, ch):
    signP = getSign(p)
    signCH = getSign(ch)
    bloodTypeP = getBloodType(p)
    bloodTypeCH = getBloodType(ch)
    bloodTypes = []
    for i in bloodTypeMatrix:
        for j in i[2]:
            if j == bloodTypeCH:
                if bloodTypeP == i[0]:
                    bloodTypes.append(i[1])
                    break
                elif bloodTypeP == i[1]:
                    bloodTypes.append(i[0])
                    break
    possibleBloodTypes = set(bloodTypes)
    rh = []
    if signP == '+' and signCH == '+':
        rh = ['+','-']
    elif signP == '+' and signCH == '-':
        rh = ['+', '-']
    elif signP == '-' and signCH == '+':
        rh = ['+']
    elif signP == '-' and signCH == '-':
        rh = ['+', '-']
    results = []
    for i in possibleBloodTypes:
        for j in rh:
            results.append(i + j)
    return results
    
def formatBloodSet(bloodSet):
    if len(bloodSet) == 0:
        return 'IMPOSSIBLE'
    if len(bloodSet) == 1:
        return str(bloodSet[0])
    result = '{'
    totalOptions = len(bloodSet)
    for i in range(totalOptions):
        result += bloodSet[i]
        if i != totalOptions - 1:
            result += ', '
    result += '}'
    return result


keepReading = True
case = 1
while keepReading:
    inputLine = input().split(' ')
    data = [str(x) for x in inputLine if x != '']
    p1 = data[0]
    p2 = data[1]
    ch = data[2]
    if p1 == 'E' and p2 == 'N' and ch == 'D':
        keepReading = False
        break
    if p1 == '?' or p2 == '?':
        parentBlood = p1 if p2 == '?' else p2
        bloodSet = getParentBloodSet(parentBlood, ch)
    else:
        bloodSet = getChildBloodSet(p1, p2)
    result = 'Case ' + str(case) + ': '
    
    if p1 == '?':
        result += formatBloodSet(bloodSet) + ' ' + p2 + ' ' + ch
    elif p2 == '?':
        result += p1 + ' ' + formatBloodSet(bloodSet) + ' ' + ch
    else:
        result += p1 + ' ' + p2 + ' ' + formatBloodSet(bloodSet)
    print(result)
    case += 1


    