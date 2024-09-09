'''Return yes if 4 dices sum to even'''
# 0.5


import random
def roll():
    # Simulate a coin flip: 1 for heads (win), 0 for tails (lose)
    dices = []
    for i in range(4):
        dices.append(random.choice(list(range(1,7))))

    if sum(dices) % 2 == 0:
        return 1
    return 0

wins = 0
for i in range(10000):
    wins += roll()

print(wins)