def areAnagrams(word1, word2):
    word1CharMap = {}
    word2CharMap = {}
    for char in word1:
        if char != ' ':
            currentCharCount = word1CharMap.get(char, 0)
            word1CharMap[char] = currentCharCount + 1
    for char in word2:
        if char != ' ':
            currentCharCount = word2CharMap.get(char, 0)
            word2CharMap[char] = currentCharCount + 1
    for key in word1CharMap:
        char1Count = word1CharMap.get(key, None)
        char2Count = word2CharMap.get(key, None)
        if char1Count is None or char2Count is None or char1Count != char2Count:
            return False
    for key in word2CharMap:
        char1Count = word1CharMap.get(key, None)
        char2Count = word2CharMap.get(key, None)
        if char1Count is None or char2Count is None or char2Count != char1Count:
            return False
    return True

cases = int(input())
allResults = []
blank_line = str(input())
for case in range(cases):
    results = []
    anagramHashMap = {}
    anagramHashMap.clear()
    keepReading = True
    currentHashList = []
    while 1:
        try:
            phrase = input()
            if phrase:
                phraseHash = 0
                for char in phrase:
                    if char != ' ':
                        phraseHash += ord(char)
                currentHashList = anagramHashMap.get(phraseHash, [])
                currentHashList.append(phrase)
                newList = currentHashList
                anagramHashMap[phraseHash] = newList
            else:
                break
        except (EOFError):
            break

    for key in anagramHashMap:
        probableAnagramsList = anagramHashMap.get(key, [])
        probableAnagramsList.sort()
        wordsCount = len(probableAnagramsList)
        if wordsCount > 1:
            for i in range(wordsCount - 1):
                word1 = probableAnagramsList[i]
                for j in range(i + 1, wordsCount): 
                    word2 = probableAnagramsList[j]
                    wordsAreAnagrams = areAnagrams(word1, word2)
                    if wordsAreAnagrams:
                        results.append(word1 + ' = ' + word2)
    results.sort()
    for result in results:
        allResults.append(result)
    if case < cases -1:
        allResults.append('')

for result in allResults:
    print(result)

        
