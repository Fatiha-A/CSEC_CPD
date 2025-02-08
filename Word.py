text = input()
count = 0
for i in range(len(text)):
    if text[i] == text[i].upper():
        count += 1
if count > len(text) / 2:
    print(text.upper())
else:
    print(text.lower())
