#AOC 2021 - Day 7 : The Treachery of Whales

#https://adventofcode.com/2021/day/7

#Part 1 Answer : 355764


import os

def find_fuel(positions, alignment):

    total_fuel_cost = 0
    for position in positions:
        fuel_cost = abs(position - alignment)
        total_fuel_cost += fuel_cost

    return total_fuel_cost
    

file_path = os.path.join(os.path.dirname('__lines__'), "day7.in")

with open(file_path) as file:
    positions = [int(position) for position in file.readline().strip().split(",")]

min_fuel_cost = float('inf')
optimal_alignment = None


for alignment in positions:
    fuel_cost = find_fuel(positions, alignment)
    if fuel_cost < min_fuel_cost:
        min_fuel_cost = fuel_cost
        optimal_alignment = alignment

print("Part 1:", min_fuel_cost)

