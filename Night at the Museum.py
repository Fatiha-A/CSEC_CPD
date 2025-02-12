alphabet = "abcdefghijklmnopqrstuvwxyz"
input_string = input()
current_position = 'a'
total_time = 0

for letter in input_string:
    distance = abs(alphabet.index(letter) - alphabet.index(current_position))
    if distance < 13:
        total_time += distance
    else:
        total_time += 26 - distance
    current_position = letter

print(total_time)
