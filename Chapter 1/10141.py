# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1082

keepReading = True
caseCounter = 1
while keepReading:
    # n, p = map(int, raw_input().split())
    n, p = map(int, input().split())
    if n is 0 and p is 0:
        keepReading = False
        break
    for i in range(n):
        # dummy_requirement = raw_input()
        dummy_requirement = input()
    bestProposalName = ''
    mostRequirementsMetYet = 0
    bestPriceYet = 0
    for i in range(1, p+1):
        # proposalName = raw_input()
        proposalName = str(input())
        # input_line = raw_input().split()
        input_line = input().split()
        price = float(input_line[0])
        metRequirements = int(input_line[1])
        for j in range(metRequirements):
            # dummy_requirement = raw_input()
            dummy_requirement = input()
        if i is 1:
            bestProposalName = proposalName
            mostRequirementsMetYet = metRequirements
            bestPriceYet = price
        elif metRequirements > mostRequirementsMetYet:
            bestProposalName = proposalName
            mostRequirementsMetYet = metRequirements
            bestPriceYet = price
        elif metRequirements == mostRequirementsMetYet:
            if price < bestPriceYet:
                bestProposalName = proposalName
                mostRequirementsMetYet = metRequirements
                bestPriceYet = price
    if caseCounter is not 1:
        print('')
    print('RFP #' + str(caseCounter))
    print(str(bestProposalName))
    caseCounter += 1 