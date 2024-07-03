# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1587

def getCardValue(card):
    rank = card[0]
    tenValue = ['A', 'T', 'J', 'Q', 'K']
    if rank in tenValue:
        return 10
    else:
        return int(rank)

# cases = int(raw_input())
cases = int(input())
for case in range(1, 1 + cases):
    # cards = [str(x) for x in raw_input().split()]
    cards = [str(x) for x in input().split()]
    cards = cards[::-1]
    y = 0
    hand = cards[0:25]
    pile = cards[25:52]
    for z in range(3):
        card = pile[0]
        x = getCardValue(card)
        y += x
        toRemove = 10 - x + 1
        pile = pile[toRemove:]
    newDeck = hand + pile
    print('Case ' + str(case) + ': ' + newDeck[len(newDeck) - y])
