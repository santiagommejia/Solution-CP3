# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2454

# cases = int(raw_input())
cases = int(input())
for case in range(cases):
    # players, b, c = map(int, raw_input().split())
    players, b, c = map(int, input().split())
    snakes = {}
    ladders = {}
    positions = []
    for i in range(players):
        positions.append(1)
    for i in range(b):
        # start, end = map(int, raw_input().split())
        start, end = map(int, input().split())
        if start < end: # ladder
            ladders[start] = end
        else: # snake
            snakes[start] = end
    gameOver = False
    dices = []
    for dummy in range(c):
        dice = int(input())
        # dice = int(raw_input())
        dices.append(dice)
    if players > 0:
        for counter in range(len(dices)):
            dice = dices[counter]
            currentPlayer = counter % players
            currentPosition = positions[currentPlayer]
            newPosition = currentPosition + dice
            if newPosition > 100:
                newPosition = 100
                positions[currentPlayer] = newPosition
                gameOver = True
            if not gameOver:
                if ladders.get(newPosition) is not None:
                    newPosition = ladders.get(newPosition)
                elif snakes.get(newPosition) is not None:
                    newPosition = snakes.get(newPosition)
                newPosition = 100 if newPosition >= 100 else newPosition
                positions[currentPlayer] = newPosition
                gameOver = gameOver or newPosition >= 100
            else:
                break
    for player in range(players):
        print('Position of player ' + str(player + 1) + ' is ' + str(positions[player]) + '.')
    

        

