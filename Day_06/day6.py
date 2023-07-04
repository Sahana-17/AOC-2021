#AOC 2021 - Day 6 : Lanternfish

#https://adventofcode.com/2021/day/6

#Part 1 Answer : 350917

import os

def lanternfish(content):

    fish = str(content)
    fish_list = []

    fish_list = [int(num.strip()) for num in fish.split(",")]

    for i in range(80):
        
        for j in range(len(fish_list)):
            if fish_list[j] != 0:
                fish_list[j] -= 1
            else:
                fish_list[j] = 6
                fish_list.append(8)

    return len(fish_list)
        
file_path = os.path.join(os.path.dirname('__lines__'), "day6.in")

with open(file_path) as file:
    content = file.read()

print("Part 1 :", lanternfish(content))
