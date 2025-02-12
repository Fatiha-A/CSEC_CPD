steps = list(input())
instructions = list(input())
current_position = 0
moves = 1
for instruction in instructions:
    if instruction == steps[current_position]:
        current_position += 1
        moves += 1
        if current_position == len(steps):
            break
print(moves)
