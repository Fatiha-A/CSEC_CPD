number = int(input())
col = input().split()
for i in range(number):
    col[i] = int(col[i])
col.sort()
for i in range(number):
    col[i] = str(col[i])
col = " ".join(col)
print(col)
