num_stones = int(input())
stone_colors = input()
removal_count = 0
for index in range(num_stones - 1):
    if stone_colors[index] == stone_colors[index + 1]:
        removal_count += 1
print(removal_count)
