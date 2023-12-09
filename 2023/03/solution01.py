import sys


def get_neighbours(x, y):
    for i in [-1, 0, 1]:
        neighbour_x = x + i
        if neighbour_x < 0 or neighbour_x >= len(grid):
            continue
        for j in [-1, 0, 1]:
            neightbour_y = y + j
            if neightbour_y < 0 or neightbour_y >= len(grid[neighbour_x]):
                continue
            if i == 0 and j == 0:
                continue
            yield grid[neighbour_x][neightbour_y]


def is_valid_char(char):
    return char != "." and not ("0" <= char <= "9")


def is_valid_position(old, i, j):
    if old:
        return old
    return any([is_valid_char(char) for char in get_neighbours(i, j)])


file_path = "2023/03/input.txt"
with open(file_path, "r") as file:
    grid = [line.strip() for line in file]

num = 0
valid = False

numbers = []
symbols = []

current = 0
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if num:
            if char.isnumeric():
                current = current * 10 + int(char)
                valid = is_valid_position(valid, i, j)
            else:
                if valid:
                    numbers.append(current)
                else:
                    symbols.append(current)
                num = False
                valid = False
        else:
            if char.isnumeric():
                num = True
                current = int(char)
                valid = is_valid_position(valid, i, j)

print(sum(numbers))  # Correct answer: 507214
