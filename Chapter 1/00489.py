# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=430

while True:
    # roundNumber = int(raw_input())
    roundNumber = int(input())
    if roundNumber is -1:
        break
    else:
        correctGuessedLetters = set()
        failedGuessedLetters = set()
        solutionLetters = set()

        failedAttemptsCount = 0
        finished = False
        # solution = str(raw_input())
        solution = str(input())
        for char in solution:
            solutionLetters.add(char)

        # guesses = str(raw_input())
        guesses = str(input())
        for char in guesses:
            if char in solutionLetters:
                correctGuessedLetters.add(char)
            else:
                if char not in failedGuessedLetters: 
                    failedGuessedLetters.add(char)
                    failedAttemptsCount += 1
            
            if len(correctGuessedLetters) == len(solutionLetters):
                finished = True
                print('Round ' + str(roundNumber))
                print('You win.')
                break
            if failedAttemptsCount is 7:
                finished = True
                print('Round ' + str(roundNumber))
                print('You lose.')
                break
        if not finished:
            print('Round ' + str(roundNumber))
            print('You chickened out.')



