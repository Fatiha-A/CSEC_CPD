items = input().split()
limak = int(items[0])
bob = int(items[1])
count = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    count += 1
print(count)
