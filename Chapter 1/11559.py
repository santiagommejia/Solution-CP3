# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2595

while True:
    try:
        N, B, H, W = map(int, raw_input().split())
        minPrice = -1
        for i in range(H):
            p = int(raw_input())
            beds = [int(x) for x in raw_input().split()]
            beds.sort()
            for bed in beds:
                if bed >= N:
                    price = N*p
                    if price < B:
                        if minPrice is -1:
                            minPrice = price
                        else:
                            minPrice = price if price < minPrice else minPrice
        if minPrice is not -1:
            print(str(minPrice))
        else:
            print('stay home')
    except EOFError:
        break
