a, b = map(int, input().split())
highest = max(a, b)
favorable_outcomes = 6 - highest + 1
total_outcomes = 6
for i in [2, 3]:
    while favorable_outcomes % i == 0 and total_outcomes % i == 0:
        favorable_outcomes //= i
        total_outcomes //= i

print(f"{favorable_outcomes}/{total_outcomes}")
