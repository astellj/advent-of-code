file = open("2023/01/input.txt", "r")

my_dict = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_digits(line):
    digits_dict = {}
    for key, value in my_dict.items():
        index = 0
        while index < len(line):
            index = line.find(key, index)
            if index == -1:
                break
            digits_dict[index] = value
            index += 1

    return digits_dict


result = 0
for line in file:
    digits = extract_digits(line)
    result += int(str(digits[min(digits)]) + str(digits[max(digits)]))

file.close()
print(result)  # Correct answer: 54019
