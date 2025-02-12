c = 0
a = []
b = []
for d in range(int(input())):
    e, f = map(int, input().split())
    a.append(e)
    b.append(f)
for g in range(len(a)):
    c += b.count(a[g])

print(c)
