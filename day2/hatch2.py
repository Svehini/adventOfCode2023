def counter(score):
    res = []
    for i in score:
        if i.isnumeric():
            res.append(i)
    num = int("".join(res))
    return num

def gameOne(content1):
    possibleGames = []
    for line in content1:
        game, scores = line.split(":")
        scores = scores.replace("\n", "")
        rounds = scores.split(";")
        for i in range(len(rounds)):
            roundScore = rounds[i]
            red = True; blue = True; green = True; gamePossible = True
            roundScore = roundScore.split(",")
            for score in roundScore:
                if "red" in score:
                    if counter(score) > 12:
                        red = False
                        break
                if "blue" in score:
                    if counter(score) > 14:
                        blue = False
                        break
                if "green" in score:
                    if counter(score) > 13:
                        green = False
                        break
            if (red == False) or ( blue == False) or (green == False):
                gamePossible = False
                break
        if gamePossible == True:
            if i == len(rounds)-1:
                possibleGames.append(counter(game))
    return sum(possibleGames)

def gameTwo(content2):
    totalPowerCubes = 0
    for line in content2:
        game, scores = line.split(":")
        scores = scores.replace("\n", "")
        rounds = scores.split(";")
        reds = []; blues = []; greens = []
        for i in range(len(rounds)):
            roundScore = rounds[i]
            roundScore = roundScore.split(",")
            for score in roundScore:
                if "red" in score:
                    reds.append(counter(score))
                if "blue" in score:
                    blues.append(counter(score))
                if "green" in score:
                    greens.append(counter(score))        
        totalPowerCubes += max(greens) * max(reds) * max(blues)
    return totalPowerCubes


print(gameOne(open("day2.txt", "r")))
print(gameTwo(open("day2.txt", "r")))
