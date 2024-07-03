# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2899

t = int(input())
for i in range(1, t+1):
    maximum = -1
    arr = [int(x) for x in input().split()]
    for j in arr:
        maximum = j if j > maximum else maximum
    print('Case '+ str(i) +': ' + str(maximum))
