file = open("../02/input.txt", "r")

direction = []
turns = []
dial = 50
sum = 0

for line in file:
    direction.append(line[0])
    turns.append(int(line[1::]))

i = 0

while i < len(direction):
    if direction[i] == "L":
        for j in range(turns[i]):
            dial = dial - 1
            if dial < 0:
                dial = 99
            if dial == 0:
                sum = sum + 1
    elif direction[i] == "R":
        for j in range(turns[i]):
            dial = dial + 1
            if dial > 99:
                dial = 0
            if dial == 0:
                sum = sum + 1

    i = i + 1

print("sum: " + str(sum))
