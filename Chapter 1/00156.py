keepReading = True
wordsList = []
while keepReading:
    # inputLine = str(raw_input())
    inputLine = str(input())
    if inputLine == '#':
        keepReading = False
    else:
        words = inputLine.split(' ')
        for word in words:
            if word.strip() != '':
                wordsList.append(word)

results = []
sortedLowerCaseWords = []
for word in wordsList:
    sortedLowerCaseWords.append(sorted(word.lower()))
sortedLowerCaseWordsCount = len(sortedLowerCaseWords)
for i in range(sortedLowerCaseWordsCount):
    word = sortedLowerCaseWords[i]
    count = sortedLowerCaseWords.count(word)
    if count == 1:
        results.append(wordsList[i])

results = sorted(results)
for result in results:
    print(result)

