# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2113

t = int(input())
for i in range(t):
    n, m = map(int, input().split()) #python 3
    # n, m = map(int, raw_input().split()) #python 2
    if n < m: 
        print('<')
    elif n > m: 
        print('>')
    else:
        print('=')