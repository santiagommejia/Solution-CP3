# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=342

mirroredMap = { 
        'A': 'A', 
        'E': '3', 
        'H': 'H', 
        'I': 'I', 
        'J': 'L', 
        'L': 'J', 
        'M': 'M', 
        'O': 'O', 
        'S': '2', 
        'T': 'T', 
        'U': 'U', 
        'V': 'V', 
        'W': 'W', 
        'X': 'X', 
        'Y': 'Y', 
        'Z': '5', 
        '1': '1', 
        '2': 'S', 
        '3': 'E', 
        '5': 'Z', 
        '8': '8', 
}

def getClasification(palindrome, mirrored):
    if not palindrome and not mirrored:
        return ' -- is not a palindrome.'
    elif palindrome and not mirrored:
        return ' -- is a regular palindrome.'
    elif not palindrome and mirrored:
        return ' -- is a mirrored string.'
    elif palindrome and mirrored:
        return ' -- is a mirrored palindrome.'

while True:
    try:
        # inputLine = str(raw_input())
        inputLine = str(input())
        if inputLine.strip() != '':
            strLength = len(inputLine)
            hi = strLength + 1 if strLength % 2 == 1 else strLength
            hi = int(hi/2)
            isPalindrome = True
            isMirrored = True
            for i in range(hi):
                if isPalindrome:
                    if inputLine[i] != inputLine[strLength - 1 - i]:
                        isPalindrome = False
                if isMirrored:
                    mirrored = mirroredMap.get(inputLine[i])
                    if mirrored is None:
                        isMirrored = False
                    elif mirrored != inputLine[strLength - 1 - i]:
                        isMirrored = False
            clasification = getClasification(isPalindrome, isMirrored)
            print(inputLine + clasification)
            print('')
        else:
            continue
    except:
        break