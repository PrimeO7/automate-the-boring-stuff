# CoinFlipStreak

import random 
from itertools import groupby



numberofStreaks = 0

possibleoutcomes = ['Head', 'Tail']

for experimentNumber in range(10000):  # loops 10000 times.
    outcomes = []
    for flip in range(100):
        outcomes.append(random.choice(possibleoutcomes))
          # chooses a randomly selected item from possibleoutcomes and appends to the list outcomes
    
    # Consecutive maximum occurrence in list.
    aux = [sum(1 for _ in b) for a, b in groupby(outcomes)]  # stolen from Stackoverflow
    consecutive = max(aux)

    # Add to count.
    if consecutive == 6:
        numberofStreaks += 1

print('Chance of Streak: %s%%' % (numberofStreaks / 100))