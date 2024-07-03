# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2827

t = int(input())
for i in range(1, t+1):
    salaries = [int(n) for n in input().split()]
    # salaries = [int(n) for n in raw_input().split()]
    salaries.sort()
    print('Case ' + str(i) + ': ' + str(salaries[1]))
