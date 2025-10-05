import random

score1 = 0
score2 = 0

for i in range(3):
    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)
    print("Round", i+1, ":", p1, "vs", p2)

    if p1 > p2:
        score1 += 1
    elif p2 > p1:
        score2 += 1

print("Final score:", score1, "-", score2)

if score1 > score2:
    print("Player 1 wins the game!")
elif score2 > score1:
    print("Player 2 wins the game!")
else:
    print("The game is a draw!")