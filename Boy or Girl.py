text = input()
cart = []
for i in text:
    if i not in cart:
        cart.append(i)
if len(cart) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
