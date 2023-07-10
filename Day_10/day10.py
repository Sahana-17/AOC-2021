import os

def calculate_score(closing_char):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return scores.get(closing_char, 0)

def corrupted(line):
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        elif char in ')]}>':
            if not stack or (stack.pop(), char) not in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                return True
    return bool(stack)

def find_corrupted_lines(navigation):
    return [line for line in navigation if corrupted(line)]

def calculate_syntax_error_score(line):
    stack = []
    score = 0
    for char in line:
        if char in '([{<':
            stack.append(char)
        elif char in ')]}>':
            if not stack:
                break
            opening_char = stack.pop()
            if (opening_char, char) not in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                score += calculate_score(char)
    return score

def calculate_total_syntax_error_score(navigation):
    corrupted_lines = find_corrupted_lines(navigation)
    return sum(calculate_syntax_error_score(line) for line in corrupted_lines)

file_path = os.path.join(os.path.dirname('__file__'), "day10.in")

with open(file_path) as file:
    lines = file.readlines()

total_score = calculate_total_syntax_error_score(lines)
print("Total Syntax Error Score:", total_score)
