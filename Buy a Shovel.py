price, coin = map(int, input().split())
shovels = 1
while True:
    total_cost = price * shovels
    if total_cost % 10 == 0 or total_cost % 10 == coin:
        print(shovels)
        break
    shovels += 1
