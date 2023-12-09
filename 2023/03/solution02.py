import sys
import math


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
            yield (grid[neighbour_x][neightbour_y], neighbour_x, neightbour_y)


def find_stars(stars, i, j):
    for n, i2, j2 in get_neighbours(i, j):
        if n == "*":
            stars.add((i2, j2))
    return stars


file_path = "2023/03/input.txt"
with open(file_path, "r") as file:
    grid = [line.strip() for line in file]


valid = False

stars = set()
result = {}

current = 0
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if valid:
            if char.isnumeric():
                current = current * 10 + int(char)
                stars = find_stars(stars, i, j)
            else:
                for x, y in stars:
                    if x not in result:
                        result[x] = {}
                    if y not in result[x]:
                        result[x][y] = []
                    result[x][y].append(current)
                valid = False
                stars = set()
        else:
            if char.isnumeric():
                valid = True
                current = int(char)
                stars = find_stars(stars, i, j)
result = 0
for i in result:
    for j in result[i]:
        values_list = result[i][j]
        size = len(values_list)
        if size == 2:
            result = result + math.prod(values_list)

print(result)  # Correct answer : 72553319
