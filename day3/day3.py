import re

def getTrimmedLine(num, line):
    start = numPos if numPos == 0 else numPos-1
    end = numPos+len(num)+1
    numRound = line[start : end]
    trimmed = numRound.replace(num,"")
    trimmed = trimmed.replace(".","")
    return trimmed

sum = 0
sumStar = 0
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    for idx, line in enumerate(lines):
        numbers = re.findall("\d+", line)
        stars = re.findall("\*", line)
        posSum = 0
        posStar = 0
        for num in numbers:
            found = False
            numPos = line.find(num, posSum)
            posSum = numPos + len(num)
            trimmed = getTrimmedLine(num, line)
            if len(trimmed) != 0:
                found = True
            if idx +1 < len(lines) and found == False:
                trimmed2 = getTrimmedLine(num, lines[idx+1])
                if len(trimmed2) != 0:
                    found = True
            if idx -1 > 0 and found == False:
                trimmed3  = getTrimmedLine(num, lines[idx-1])
                if len(trimmed3) != 0:
                    found = True
            if found == True:
                sum += int(num)
    print(sum)
    print(sumStar)