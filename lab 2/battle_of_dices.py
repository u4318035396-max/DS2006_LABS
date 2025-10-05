import random

p1 = random.randint(1, 6)
p2 = random.randint(1, 6)

print("Player 1 rolled:", p1)
print("Player 2 rolled:", p2)

if p1 > p2:
    print("Player 1 wins!")
elif p2 > p1:
    print("Player 2 wins!")
else:
    print("It's a tie!")