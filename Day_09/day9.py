#AOC 2021 - Day 9 : Smoke Basin

#https://adventofcode.com/2021/day/9

#Part 1 Answer : 489

import os

def part1():
    risk_level = 0
    total_sum = 0

    for i in range(rows):
        for j in range(columns):
            current_value = grid[i][j]

            left_value = grid[i][j-1] if j > 0 else current_value + 1
            up_value = grid[i-1][j] if i > 0 else current_value + 1
            right_value = grid[i][j+1] if j < columns-1 else current_value + 1
            down_value = grid[i+1][j] if i < rows-1 else current_value + 1

            if current_value < right_value and current_value < left_value and \
                    current_value < down_value and current_value < up_value:

                risk_level = current_value + 1
                total_sum += risk_level

    return total_sum 

file_path = os.path.join(os.path.dirname('__file__'), "day9.in")

with open(file_path) as file:
    grid = [list(map(int, line.strip())) for line in file]

rows = len(grid)
columns = len(grid[0])

print("Part 1 : ", part1())
