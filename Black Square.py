total_calories = 0
calorie_values = list(map(int, input().split()))
sequence = input()
for char in sequence:
    total_calories += calorie_values[int(char) - 1]
print(total_calories)
