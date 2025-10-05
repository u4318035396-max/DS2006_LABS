import random

wins1 = 0
wins2 = 0
draws = 0

for i in range(10):
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)

    if p1 > p2:
        wins1 += 1
    elif p2 > p1:
        wins2 += 1
    else:
        draws += 1

print("Results after 10 games:")
print("Player 1 wins:", wins1)
print("Player 2 wins:", wins2)
print("Draws:", draws)