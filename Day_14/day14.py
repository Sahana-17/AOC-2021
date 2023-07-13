import os
from collections import Counter

rules = {}
value = ''

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day14.in")

with open(file_path) as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if (' -> ') in line:
        lhs, rhs = line.split(' -> ')
        rules[lhs] = rhs

    elif line:
        value = line

step = 0

while step < 10:
    template = ''
    prev = value[0]

    for i in range(1, len(value)):
        template += prev
        pair = value[i - 1] + value[i]
        if pair in rules:
            template += rules[pair]
        prev = value[i]
    template = template + prev
    value = template

    step += 1


letter_counts = Counter(value)
letter_list = list(letter_counts.values())
letter_list.sort(reverse=True)

quantity = letter_list[0] - letter_list[-1]
print("Part 1 : ", quantity)

