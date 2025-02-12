num_wires = int(input())
birds_on_wire = list(map(int, input().split()))

for _ in range(int(input())):
    wire_index, bird_position = map(int, input().split())
    wire_index -= 1  # Adjust to zero-based index

    if wire_index > 0:
        birds_on_wire[wire_index - 1] += bird_position - 1
    if wire_index < num_wires - 1:
        birds_on_wire[wire_index + 1] += birds_on_wire[wire_index] - bird_position

    birds_on_wire[wire_index] = 0

for birds in birds_on_wire:
    print(birds)
