balicek = []
barvy = ['♠', '♥', '♦', '♣']
hodnoty = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for barva in barvy:
    for hodnota in hodnoty:
        balicek.append(hodnota + " " + barva)

print(balicek)
# print(len(balicek))

import random
random.shuffle(balicek)
print(balicek)