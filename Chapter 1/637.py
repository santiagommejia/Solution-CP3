keepReading = True
while keepReading:
    pages = int(input())
    if pages == 0:
        keepReading = False
    else:
        pagesOrder = []
        print('Printing order for ' + str(pages) + ' pages:')
        tempSheets = int(pages / 4)
        sheets = tempSheets if tempSheets * 4 >= pages else tempSheets + 1
        top = sheets * 4
        pageCounter = 1
        for sheet in range(sheets):
                pagesOrder.append(top - pageCounter + 1)
                pagesOrder.append(pageCounter)
                pageCounter += 1
                pagesOrder.append(pageCounter)
                pagesOrder.append(top - pageCounter + 1)
                pageCounter += 1

        pageCounter = 0
        for sheetCounter in range(1, sheets + 1):
            number1 = 'Blank' if  pagesOrder[pageCounter] > pages else str(pagesOrder[pageCounter])
            pageCounter += 1
            number2 = 'Blank' if  pagesOrder[pageCounter] > pages else str(pagesOrder[pageCounter])
            if not (number1 == 'Blank' and number2 == 'Blank'):
                print('Sheet ' + str(sheetCounter) + ', front: ' + number1 + ', ' + number2)
            pageCounter += 1
            number3 = 'Blank' if  pagesOrder[pageCounter] > pages else str(pagesOrder[pageCounter])
            pageCounter += 1
            number4 = 'Blank' if  pagesOrder[pageCounter] > pages else str(pagesOrder[pageCounter])
            if not (number3 == 'Blank' and number4 == 'Blank'):
                print('Sheet ' + str(sheetCounter) + ', back : ' + number3 + ', ' + number4)
            pageCounter += 1
        

