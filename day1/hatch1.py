numDict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

text = open("input.txt", "r")
total = 0
for line in text:
    lineNum = ""
    line = str(line)
    for key, value in numDict.items():
        line = line.replace(key, key+value+key)
    for i in line:
        if i.isdigit():
            lineNum += i
    total += int(lineNum[0] + lineNum[-1])
print(total)