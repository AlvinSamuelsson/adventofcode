import re
from functools import reduce

ans = {"green": 13, "red": 12, "blue": 14}
sum_1 = 0
sum_2 = 0
with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    opt = []

    for line in lines:
        ans2 = {"green": 0, "red": 0, "blue": 0}
        valid = True
        game = line.split(":")
        sets = game[1].split(";")
        for set in sets:
            for cubes in set.split(","): 
                amount = cubes.strip().split(" ")
                if ans[amount[1]] < int(amount[0]):
                    valid = False 
                if ans2[amount[1]] < int(amount[0]):
                    ans2[amount[1]] = int(amount[0])
        if valid is True:
            score = game[0].strip().split(" ")
            sum_1 += int(score[1])

        sum_2 += reduce(lambda x, key: x*ans2[key], ans2, 1)
        
print("answer 1 is {}".format(sum_1))
print("answer 2 is {}".format(sum_2))