from curses.ascii import isdigit
import re
from turtle import pos


def sum_numeric_values(input_text):
    total_sum = 0
    current_number = ""

    for char in input_text:
        if char.isdigit():
            current_number += char
        elif current_number:
            total_sum += int(current_number)
            current_number = ""

    # Check for any remaining number at the end of the input
    if current_number:
        total_sum += int(current_number)

    return total_sum


file_path = "2023/03/sampleInput.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    sum_of_all_parts = sum_numeric_values("".join(lines))

# Define a regular expression pattern to match only digits
pattern = r"\d+"


# for i in range(len(lines)):
#     print("Line:", i)

#     # Previous line
#     if i > 0:
#         previous_line = lines[i - 1].strip()
#         # print("Previous line:", previous_line)

#     # Current line
#     current_line = lines[i].strip()
#     print("Current line:", current_line)
#     matches = re.findall(pattern, current_line)
#     print(matches)
#     for matches in current_line:
#         print(current_line)


#     # Next line
#     if i < len(lines) - 1:
#         next_line = lines[i + 1].strip()
#         # print("Next line:", next_line)


def is_symbol(char):
    if char != "." and not char.isdigit():
        return True


def extract_number(line, index, position):
    print("Line:", line)
    print("Index:", index)
    number = ""

    # while index < len(line):
    if line[index - 2].isdigit() and line[index - 1] != ".":
        number += line[index - 2]
        position_of_values.add(position)
    if line[index - 1].isdigit() and line[index - 1] != ".":
        number += line[index - 1]
        position_of_values.add(position)
    if line[index].isdigit() and line[index] != ".":
        number += line[index]
        position_of_values.add(position)
    if line[index + 1].isdigit() and line[index + 1] != ".":
        number += line[index + 1]
        position_of_values.add(position)
    if line[index + 2].isdigit() and line[index + 1] != ".":
        number += line[index + 2]
        position_of_values.add(position)

    print(number)
    return number


result = 0
position = 0
position_of_values = set()


for i in range(len(lines)):
    for j in range(len(lines[i])):
        position += 1
        # print(lines[i][j])
        if is_symbol(lines[i][j]):
            # Here we have found all the symbols, now we need to look either side of the symbol to see if it is a digit
            # print(lines[i][j])

            if i > 0 and lines[i - 1][j].isdigit():
                print("Digit above:", lines[i - 1][j])
                result += int(extract_number(lines[i - 1], j, position))

            if (
                i < len(lines) - 1
                and j < len(lines[i + 1])
                and lines[i + 1][j].isdigit()
            ):
                print("Digit below:", lines[i + 1][j])
                result += int(extract_number(lines[i + 1], j, position))

            if j > 0 and lines[i][j - 1].isdigit():
                print("Digit before:", lines[i][j - 1])
                result += int(extract_number(lines[i], j - 1, position))

            if j < len(lines[i]) - 1 and lines[i][j + 1].isdigit():
                print("Digit after:", lines[i][j + 1])
                result += int(extract_number(lines[i], j + 1, position))

            if i > 0 and j > 0 and lines[i - 1][j - 1].isdigit():
                print("Digit NW:", lines[i - 1][j - 1])
                result += int(extract_number(lines[i - 1], j - 1, position))

            if i > 0 and j < len(lines[i]) - 1 and lines[i - 1][j + 1].isdigit():
                print("Digit NE:", lines[i - 1][j + 1])
                result += int(extract_number(lines[i - 1], j + 1, position))

            if (
                i < len(lines) - 1
                and j < len(lines[i + 1])
                and j < len(lines[i]) - 1
                and lines[i + 1][j + 1].isdigit()
            ):
                print("Digit SE:", lines[i + 1][j + 1])
                result += int(extract_number(lines[i + 1], j + 1, position))

            if (
                i < len(lines) - 1
                and j < len(lines[i + 1])
                and lines[i + 1][j - 1].isdigit()
                and j > 0
            ):
                print("Digit SW:", lines[i + 1][j - 1])
                result += int(extract_number(lines[i + 1], j - 1, position))

            # Okay so we have found all the adjacent numbers to the symbols

print("Position of values:", position_of_values)
print("Sum of all parts:", sum_of_all_parts)
print("Result:", result)
