import re


def game_structure(line):
    match = re.match(r"Game (\d+):", line)
    if match:
        game_number = int(match.group(1))

        all_cubes = line.split(":")[1].strip()
        cube_list = [i.strip() for i in re.split(r"[;,]", all_cubes)]

        return {game_number: cube_list}

    return None


file = open("2023/02/input.txt", "r")

my_dict = {}
colour_dict = {}
fewest_cubes_dict = {}
red_max = 0
green_max = 0
blue_max = 0
result = 0

for line in file:
    game_data = game_structure(line)
    if game_data:
        my_dict.update(game_data)

for game_number, cube_list in my_dict.items():
    for i in cube_list:
        value, colour = i.split()
        if colour == "red" and int(value) > int(red_max):
            red_max = value
        if colour == "green" and int(value) > int(green_max):
            green_max = value
        if colour == "blue" and int(value) > int(blue_max):
            blue_max = value

    fewest_cubes_dict[game_number] = {
        "Red max": red_max,
        "Green max": green_max,
        "Blue max": blue_max,
    }

    red_max = 0
    green_max = 0
    blue_max = 0


for game_number, min_values in fewest_cubes_dict.items():
    power = 1
    for i in min_values.values():
        power = power * int(i)
    result += power

print(result)  # Correct answer: 72227
