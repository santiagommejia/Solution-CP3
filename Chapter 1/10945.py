# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1886

def isPalindrome(str):
    copyStr = ''
    for char in str:
        if char.isalpha():
            copyStr += char.lower()
    copyStrLength = len(copyStr)
    halfLength = int(copyStrLength / 2)
    for i in range(halfLength):
        if copyStr[i] != copyStr[copyStrLength - 1 - i]:
            return False
    return True
        
while True:
    # inputLine = str(raw_input())
    inputLine = str(input())
    if inputLine == 'DONE':
        break
    elif inputLine.strip() == '':
        pass
    else:
        palindrome = isPalindrome(inputLine)
        result = "You won't be eaten!" if palindrome else 'Uh oh..'
        print(result)
