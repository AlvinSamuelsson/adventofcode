import re

def checkFirstLast(d: int, n: int): 
    if n > last_pos:
        last = d
        last_pos = n
    return first, last

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

def part1(rows):
    sum = 0
    for line in rows:
        first = re.search(r"\d", line)
        last = re.search(r"\d", line[::-1])
        if first and last:
            s = "{}{}".format(line[first.start()],line[::-1][last.start()])
            sum += int(s)

    print(sum)

def part2(rows: str):
    num_map = {  
    'one': '1',  
    'two': '2',  
    'three': '3',  
    'four': '4',  
    'five' : '5',  
    'six': '6',  
    'seven': '7',  
    'eight': '8',  
    'nine': '9'  
    }  
    nums = num_map.keys()  
    max_len = 5  
    to_sumup = [] 
    for line in rows:  
        found_nums = []  
        line = line.strip()  
        for idx, char in enumerate(line):   
            try:  
                found = int(char)  
                found_nums.append(char)  
                continue  
            except ValueError:   
                for i in range(1, max_len+1):  
                    if line[idx:idx+i] in nums:  
                        found_nums.append(num_map[line[idx:idx+i]])  
                        break  
        to_sumup.append(int(found_nums[0]+found_nums[-1]))
    print(sum(to_sumup))

# part1(lines)
part2(lines)