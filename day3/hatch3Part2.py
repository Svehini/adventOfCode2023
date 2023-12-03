
def gridChecker(grid, numStart, numEnd, lineNum):
    j = lineNum 
    for i in range(numStart, numEnd+1):
        for m in range(-1,2):
            for n in range(-1,2):
                try:
                    dot = grid[j+m][i+n]; x=j+m; y=i+n
                except:
                    try: 
                        dot = grid[j+m-1][i+n]; x=j+m-1; y=i+n
                    except:
                        try:
                            dot = grid[j+m][i+n-1]; x=j+m; y=i+n-1
                        except: 
                            dot = grid[j+m-1][i+n-1]; x=j+m-1; y=i+n-1
                if dot == "*":
                    return True, (str(x)+str(y))
                
    return False, ["NotValid"]


def task1(content):
    total = 0
    grid = []
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    starDict = {}
    for line in content:
        line = line.replace("\n", "")
        grid.append(line)
    for j in range(len(grid)):
        line = grid[j]
        numStart = -1
        numEnd = -1
        num = []
        for i in range(len(line)):
            hasStar = False
            if (i == len(line)-1) and ((numStart != -1) or (grid[j][i].isnumeric())):
                if line[i].isnumeric():
                    num.append(line[i])
                hasStar, starCoord = gridChecker(grid, numStart, i, j)
                if hasStar == True:
                    if starCoord not in list(starDict.keys()):
                        starDict[starCoord] = [int("".join(num))]
                    else:
                        starList = starDict[starCoord]
                        starList.append(int("".join(num)))
                        starDict[starCoord] = starList
                num = []
                numStart = -1
                numEnd = -1

            elif (line[i] in nums) and (numStart == -1):
                numStart = i; numEnd = i
                num.append((line[i]))

            elif line[i] in nums:
                numEnd = i
                num.append((line[i]))

            elif (line[i] not in nums) and (numStart != -1):
                hasStar, starCoord = gridChecker(grid, numStart, numEnd, j)
                if hasStar == True:
                    if starCoord not in list(starDict.keys()):
                        starDict[starCoord] = [int("".join(num))]
                    else:
                        starList = starDict[starCoord]
                        starList.append(int("".join(num)))
                        starDict[starCoord] = starList
                num = []
                numStart = -1
                numEnd = -1

    for star, nums in starDict.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total




# print(task1(open("test2.txt", "r")))
print(task1(open("inputDay3.txt", "r")))