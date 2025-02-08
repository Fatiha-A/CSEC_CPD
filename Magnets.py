number = int(input())
magnets = []
count = 1
for i in range(number):
    magnets.append(input())
for j in range(len(magnets) - 1):
    if magnets[j] != magnets[j + 1]:
        count += 1
print(count)
