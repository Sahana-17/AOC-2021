#AOC 2021 - Day 3 : Binary Diagnostic

#https://adventofcode.com/2021/day/3

#Part 1 Answer : 2583164

import os

def power_consumption(lines):

    val_lists = [[] for _ in range(12)]
    power_consumption = 0
    gamma_rate = ''
    epsilon_rate = ''

    for line in lines:
        line = line.strip()
        for i, val_list in enumerate(val_lists):
            val_list.append(line[i])

    for val_list in val_lists:
        one = val_list.count('1')
        zero = val_list.count('0')
        if one > zero:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption



lines_path = os.path.join(os.path.dirname('__lines__'), "day3.in")

with open(lines_path) as file:
    lines = file.readlines()

print("Part 1 :", power_consumption(lines))
