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
    print("direction: " + direction[i])
    print("turns: " + str(turns[i]))
    print("starting dial: " + str(dial))
    if direction[i] == "L":
        for j in range(turns[i]):
            print(dial)
            if dial == 0:
                dial = 99
            else:
                dial = dial - 1
    elif direction[i] == "R":
        for j in range(turns[i]):
            print(dial)
            if dial == 100:
                dial = 1
            else:
                dial = dial + 1

    if dial == 0 or dial == 100:
        print("adding to sum")
        sum = sum + 1
    i = i + 1

print("sum: " + str(sum))