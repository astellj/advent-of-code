import re

file = open("2023/01/input.txt", "r")

result = 0
for line in file:
    number_value = re.sub("\D", "", line)
    result += int(number_value[0] + number_value[-1])

file.close()
print(result)  # Correct answer: 54632
