
def gridChecker(grid, numStart, numEnd, lineNum):
    j = lineNum 
    nums = ["0","1","2","3","4","5","6","7","8","9", "."]
    for i in range(numStart, numEnd+1):
        for m in range(-1,2):
            for n in range(-1,2):
                try:
                    dot = grid[j+m][i+n]
                except:
                    try: 
                        dot = grid[j+m-1][i+n]
                    except:
                        try:
                            dot = grid[j+m][i+n-1]
                        except: 
                            dot = grid[j+m-1][i+n-1]
                if (dot not in nums):
                    return True
    return False


def task1(content):
    total = 0
    grid = []
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    for line in content:
        line = line.replace("\n", "")
        grid.append(line)
    for j in range(len(grid)):
        line = grid[j]
        numStart = -1
        numEnd = -1
        num = []
        for i in range(len(line)):
            if (i == len(line)-1) and ((numStart != -1) or (grid[j][i].isnumeric())):
                if line[i].isnumeric():
                    num.append(line[i])
                if gridChecker(grid, numStart, i, j):
                    total += int("".join(num))
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
                if gridChecker(grid, numStart, numEnd, j):
                    total += int("".join(num))
                num = []
                numStart = -1
                numEnd = -1
    return total




print(task1(open("test2.txt", "r")))
# print(task1(open("inputDay3.txt", "r")))