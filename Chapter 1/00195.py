from itertools import permutations
# hacer a mano?

allResults = []

def generateSortedPermutations(word):
    print('gsp enter:', word)
    wordLength = len(word)
    if wordLength == 1:
        return word[0]
    for i in range(wordLength):
        char = word[i]
        slicedWord = word[:i] + word[i + 1:]
        print('slicedWord', slicedWord)
        perms = [''.join(p) for p in permutations(slicedWord)]
        uniquePerms = set(perms)
        for perm in uniquePerms:
            allResults.append(char + perm)
    
    # firstPart = word[0]
    # perms = [''.join(p) for p in permutations(word[1:])]
    # uniquePerms = set(perms)
    # for perm in uniquePerms:
    #     allResults.append(word[0] + perm)
    # secondPart = generateSortedPermutations(word[1:])
    # print('firstPart', firstPart)
    # print('secondPart', secondPart)
    # newWord = firstPart + secondPart
    # allResults.append(newWord)

iteration = 0
def compare(word1, word2):
    global iteration, results
    iteration += 1
    print('current order', results)
    print("comparing words:", word1, word2, iteration)
    for i in range(len(word1)):
        char1 = word1[i]
        char2 = word2[i]
        char1lower = char1.lower()
        char2lower = char2.lower()
        char1Ascii = ord(char1)
        char2Ascii = ord(char2)
        if char1lower == char2lower:
            if char1 == char1lower and char2 == char2lower:
                pass
            else:
                result = -1 if char1Ascii < char2Ascii else 1
                print('returning', result) 
                return result
        else:
            result = -1 if char1lower < char2lower else 1
            print('returning', result) 
            return result
    return 0

cases = int(raw_input())
results = []

for case in range(cases):
    word = str(raw_input())
    word = sorted(word, key=lambda c: c.upper())
    # word = sorted(word)
    print("original word", word)
    # print("original permutations", uniquePerms)
    # allResults.append(word)
    # generateSortedPermutations(word)
    # results = [perm for perm in uniquePerms]
    # results.sort(key=compare)
    # results = sorted(results, cmp=compare)
    # results = sorted(resultslst, key=lambda L: (L.lower(), L))
    # results = sorted(results, key=lambda c: c.upper())

for result in results:
    # allResults.append(result)
    print(result)
    
# with open('test.txt', 'w') as writer:
#     for result in results:
#         writer.write(result + '\n')