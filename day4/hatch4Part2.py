

def toIntList(winningNums, yourNums):
    for i in range(len(winningNums)):
        if winningNums[i] != '':
            num = winningNums.pop(i)
            winningNums.insert(i, int(num))
    for i in range(len(yourNums)):
        if yourNums[i] != '':
            num = yourNums.pop(i)
            yourNums.insert(i, int(num))
    return yourNums, winningNums

def lineCounter(winNums, yourNums):
    total = 0
    winNums, yourNums = toIntList(winNums, yourNums)
    for num in winNums:
        if (num in yourNums) and (num != ''):
            total += 1
    return total


def gameNumGetter(game):
    num = []
    for i in game:
        if i.isnumeric():
            num.append(i)
    return "".join(num)



def part2(content):
    cardDict = {}
    for line in content:
        line.replace("\n", "")
        game, scores = line.split(":")
        winningNums, yourNums = scores.split("|")
        winningNums = winningNums.split(" ")
        yourNums = yourNums.split(" ")
        gameNum = int(gameNumGetter(game))

        if gameNum not in cardDict.keys():
            cardDict[gameNum] = 1
        else:
            cardDict[gameNum] += 1
        times = cardDict[gameNum]
        noOfExtraCards = lineCounter(winningNums, yourNums)
        for i in range(gameNum+1, gameNum+noOfExtraCards+1):
            if i not in cardDict.keys():
                cardDict[i] = times
            else:
                cardDict[i] += times
    totalCards = sum(cardDict.values())
    return totalCards

print(part2(open("test.txt", "r")))
print(part2(open("inputDay4.txt", "r")))
