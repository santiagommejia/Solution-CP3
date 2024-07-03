# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=0&problem=520

keepReading = True
while keepReading:
    inputLine = str(input())
    split = inputLine.split(':')
    H = int(split[0])
    M = int(split[1])
    if H == 0 and M == 0:
        keepReading = False
        break
    hour = (H*30 + M*0.5) % 360 
    minute = M*6 % 360
    bigger = max(hour, minute)
    lower = min(hour, minute)
    res1 = (bigger - lower)
    res2 = (360 + lower - bigger)
    res1 = res1 if res1 >=0 else -1*res1 
    res2 = res2 if res2 >=0 else -1*res2 
    result = min(res1, res2)
    print("{:.3f}".format(result))