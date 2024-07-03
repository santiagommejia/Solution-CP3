n = int(input())
for n in range(n):
    s, d = map(int, input().split())
    b = (s - d) / 2
    if b != int(b):
        print('impossible')
    else:
        a = s - b
        difference = a - b
        if a + b == s and (difference == d or difference * -1 == d) and a >= 0 and b >= 0:
            print(str(int(max(a,b))) + ' ' + str(int(min(a,b))))   
        else:
            print('impossible')