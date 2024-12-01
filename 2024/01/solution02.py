file = open("2024/01/input.txt", "r")

list1 = []
list2 = []

for line in file:
    x = line.split()
    list1.append(x[0])
    list2.append(x[1])

i = 0
sum = 0

while i < len(list1):
    x = int(list1[i])

    j = 0
    for num in list2:
        if int(num) == x:
            j += 1

    sum += j * x
    i = i + 1

print(sum)
