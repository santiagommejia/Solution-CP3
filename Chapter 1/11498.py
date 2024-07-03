# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2493

read = True
while read:
    cases = int(input())
    if cases is 0:
        read = False
        break
    n, m = map(int, input().split())
    # n, m = map(int, raw_input().split()) #python 2
    for i in range(cases):
        x, y = map(int, input().split())
        # x, y = map(int, raw_input().split())
        if x > n and y >m:
            print('NE')
        elif x > n and y < m:
            print('SE')
        elif x < n and y > m:
            print('NO')
        elif x < n and y < m:
            print('SO')
        else:
            print('divisa')
