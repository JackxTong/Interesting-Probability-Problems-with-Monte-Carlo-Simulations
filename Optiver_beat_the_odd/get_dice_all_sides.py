'''Expectation of how many times needed to get all sides of a dice at least once'''

# this is 1+6/5+6/4+6/3+6/2+6=14.7
import numpy as np
count_list = []
N = 100000
for _ in range(N):
    rolled = set()
    count=0
    while len(rolled) < 6:
        rolled.add(np.random.randint(1, 7))
        count += 1

    count_list.append(count)

print(sum(count_list)/N)
