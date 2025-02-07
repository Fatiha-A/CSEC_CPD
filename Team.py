number = int(input())
count = 0
for i in range(number):
    team = input().split()
    if team.count('1') > 1:
        count += 1
print(count)
