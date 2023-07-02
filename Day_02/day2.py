#AOC 2021 - Day 2 : Dive!

#https://adventofcode.com/2021/day/2

#Part 1 Answer : 1947824
#Part 2 Answer : 1813062561

import os

def depth_part1(lines):

    horizontal = 0
    vertical = 0
    depth = 0

    for line in lines:
        line = line.strip()

        for i in range(len(line)):
            if line[i].isdigit():
                value = int(line[i])
    
                if line[0] == 'f':
                    horizontal += value
                elif line[0] == 'u':
                    vertical -= value
                else:
                    vertical += value

    depth = horizontal * vertical
    return depth


def depth_part2(lines):

    horizontal = 0
    depth = 0
    aim = 0
    final_value = 0

    for line in lines:
        line = line.strip()
        
        for i in range(len(line)):
            if line[i].isdigit():
                value = int(line[i])
    
                if line[0] == 'f':
                    horizontal += value
                    depth += aim * value
                elif line[0] == 'u':
                    aim -= value
                else:
                    aim += value


    final_value = horizontal * depth

    return final_value


lines_path = os.path.join(os.path.dirname('__lines__'), "day2.in")

with open(lines_path) as file:
    lines = file.readlines()

print("Part 1 :", depth_part1(lines))
print("Part 2 :", depth_part2(lines))