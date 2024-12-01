file = open("2024/01/input.txt", "r")

list1 = []
list2 = []

for line in file:
    x = line.split()
    list1.append(x[0])
    list2.append(x[1])

list1.sort()
list2.sort()

i = 0
sum = 0

while i < len(list1):
    sum += abs(int(list1[i]) - int(list2[i]))
    i = i + 1

print(sum)
