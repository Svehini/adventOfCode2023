import re

def part1(content):
    total = 0
    roundScore = 0
    for line in content:
        line.replace("\n", "")
        game, scores = line.split(":")
        winningNums, yourNums = scores.split("|")
        winningNums = winningNums.split(" ")
        yourNums = yourNums.split(" ")
        for i in range(len(winningNums)):
            if winningNums[i] != '':
                num = winningNums.pop(i)
                winningNums.insert(i, int(num))
        for i in range(len(yourNums)):
            if yourNums[i] != '':
                num = yourNums.pop(i)
                yourNums.insert(i, int(num))
        for n in winningNums:
            if (n in yourNums ) and (n != ''):
                if roundScore == 0:
                    roundScore += 1
                else:
                    roundScore = roundScore * 2
        total += roundScore
        roundScore = 0
            
    return total




# print(part1(open("test.txt", "r")))
print(part1(open("inputDay4.txt", "r")))