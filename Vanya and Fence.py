list = input().split(" ")
list2 = input().split(" ")
total = 0
for i in range(int(list[0])):
    if int(list2[i]) > int(list[1]):
        total += 2
    else:
        total += 1
print(total)
