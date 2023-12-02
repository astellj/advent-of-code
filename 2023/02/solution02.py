import re


def game_structure(line):
    match = re.match(r"Game (\d+):", line)
    if match:
        game_number = int(match.group(1))

        all_cubes = line.split(":")[1].strip()
        cube_list = [i.strip() for i in re.split(r"[;,]", all_cubes)]

        return {game_number: cube_list}

    return None


def process_file(file_path):
    game_data_dict = {}

    with open(file_path, "r") as file:
        for line in file:
            game_data = game_structure(line)
            if game_data:
                game_data_dict.update(game_data)

    file.close()
    return game_data_dict


def main():
    game_dict = process_file("2023/02/input.txt")

    fewest_cubes_dict = {}
    result = 0

    for game_number, cube_list in game_dict.items():
        red_max, green_max, blue_max = 0, 0, 0

        for cube in cube_list:
            value, colour = cube.split()
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


if __name__ == "__main__":
    main()
