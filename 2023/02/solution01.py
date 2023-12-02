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
invalid_games = {}
sum_of_game_numbers = 0
inverse_result = 0
result = 0

for line in file:
    game_data = game_structure(line)
    if game_data:
        my_dict.update(game_data)

file.close()

for game_number, cube_list in my_dict.items():
    for i in cube_list:
        value, colour = i.split()
        if (
            (colour == "red" and int(value) > 12)
            or (colour == "green" and int(value) > 13)
            or (colour == "blue" and int(value) > 14)
        ):
            invalid_games[game_number] = True

for game_number in invalid_games.keys():
    inverse_result += game_number

for game_number in my_dict.keys():
    sum_of_game_numbers += game_number

result = sum_of_game_numbers - inverse_result
print(result)  # Correct answer: 2716
