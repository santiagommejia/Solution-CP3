# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1055

keepReading = True
while keepReading:
    # months, downPayment, loanAmount, interestCount = map(float, raw_input().split())
    months, downPayment, loanAmount, interestCount = map(float, input().split())
    if months < 0:
        keepReading = False
        break
    interestList = []
    loanPayment = loanAmount / months
    for i in range(int(interestCount)):
        # month, interest = map(float, raw_input().split())
        month, interest = map(float, input().split())
        interestList.append((month, interest))
        interestListCounter = 0
        currentCarValue = downPayment + loanAmount
    for i in range(0, int(months) + 1):
        pluralMonths = 'months' if i != 1 else 'month'
        if interestListCounter < len(interestList):
            (month, interest) = interestList[interestListCounter]
        else:
            month = -1
            interest = 0
        if i == 0:
            currentCarValue = currentCarValue * (1 - interest) # depreciation
            currentInterest = interest
            interestListCounter += 1
            if loanAmount < currentCarValue:
                print(str(i) + ' ' + pluralMonths)
                break
            continue
        if i == month:
            currentInterest = interest
            interestListCounter += 1
        loanAmount -= loanPayment
        currentCarValue = currentCarValue * (1 - currentInterest) # depreciation
        if loanAmount < currentCarValue:
            print(str(i) + ' ' + pluralMonths)
            break
