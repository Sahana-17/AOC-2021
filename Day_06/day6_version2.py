#AOC 2021 - Day 6 : Lanternfish (using Counter built-in function)

#https://adventofcode.com/2021/day/6

#Part 2 Answer : 1592918715629

import os
from collections import Counter

def lanternfish(content):
    fish = Counter(map(int, content.split(',')))

    for i in range(256):
        new_fish = Counter() #assigns keys and values as number and count of it
        
        for j, z in fish.items():
            if j != 0:
                new_fish[j - 1] += z
        
        new_fish[6] += fish[0]
        new_fish[8] += fish[0]
        
        fish = new_fish
    
    total_fish = sum(fish.values())
    return total_fish


file_path = os.path.join(os.path.dirname('__lines__'), "day6.in")

with open(file_path) as file:
    content = file.read()

print("Part 1:", lanternfish(content))
