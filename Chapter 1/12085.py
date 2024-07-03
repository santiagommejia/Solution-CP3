# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=242&page=show_problem&problem=3237

def getBlockAbbrev(blockStart, blockEnd):
    for i in range(len(blockStart)):
        if blockStart[i] != blockEnd[i]:
            return blockStart + '-' + blockEnd[i::]
    return

keepReading = True
caseCounter = 1
while keepReading:
    n = int(input())
    if n == 0:
        keepReading = False
        break
    phones = []
    for i in range(n):
        phoneStr = input()
        phones.append(phoneStr)
    isCountingSame = False
    blockStartStr = None
    print('Case ' + str(caseCounter) + ':')
    for i in range(1, n):
        previousPhoneStr = phones[i-1]
        phoneStr = phones[i]
        previousPhone = int(previousPhoneStr)
        phone = int(phoneStr)
        if phone - previousPhone == 1:
            isCountingSame = True
            if blockStartStr is None:
                blockStartStr = phones[i-1]
        else:
            if isCountingSame: #chain is broken
                print(getBlockAbbrev(blockStartStr, previousPhoneStr))
                isCountingSame = False
                blockStartStr = None
            else:
                print(previousPhoneStr)
    if isCountingSame:
        print(getBlockAbbrev(blockStartStr, phones[n-1]))
        isCountingSame = False
        blockStartStr = None
    else:
        print(phones[n-1])
    print()
    caseCounter += 1