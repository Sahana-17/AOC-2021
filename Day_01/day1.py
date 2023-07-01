#AOC 2021 - Day 1 : Sonar Sweep

#https://adventofcode.com/2021/day/1

#Part 1 Answer : 1532
#Part 2 Answer : 1571


import os

file_path = os.path.join(os.path.dirname('__file__'), "day1.in")

value = 0
count = -1
window_count = 0
random_list = []

with open(file_path) as file: 

    for line in file:
        line = line.strip()

        current_val = int(line)
        random_list.append(int(line))

        if current_val > value:
            count += 1

        value = current_val
        

for i in range(len(random_list)-3):

    one = random_list[i] + random_list[i+1] + random_list[i+2]
    two = random_list[i+1] + random_list[i+2] + random_list[i+3]

    if two > one:
        window_count += 1

print("Total Measurements Part 1 : ", count)
print("Total Measurements Part 2 : ", window_count)