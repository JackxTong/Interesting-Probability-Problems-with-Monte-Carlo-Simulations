'''32 teams, ranked from strongest (1st) to 32nd. what is probability of 2nd team meeting
3rd team in the semi final?'''

# equivalent to team1, team2 and team3 not in same 8-team group.
# which is 1 * 3/4 * 2/4 = 3/8
# then could be (2 vs 3) or (2 vs 1) or (2 vs X), so 3/8 * 1/3 = 1/8

import random
import numpy as np

def simulate_tournament(N=32, num_simulations=100000):
    teams = list(range(1, N + 1))
    count = 0

    for _ in range(num_simulations):
        random.shuffle(teams)
        round_of_16 = [min(teams[i], teams[i+1]) for i in range(0, N, 2)]
        quarter_finals = [min(round_of_16[i], round_of_16[i+1]) for i in range(0, len(round_of_16), 2)]
        semi_finals = [min(quarter_finals[i], quarter_finals[i+1]) for i in range(0, len(quarter_finals), 2)]
        # print(teams, round_of_16, quarter_finals, semi_finals)
        # Check if teams 2 and 3 meet in the semifinals
        semi_pairs = [(semi_finals[0], semi_finals[1]), (semi_finals[2], semi_finals[3])]
        if (2, 3) in semi_pairs or (3, 2) in semi_pairs:
            count += 1

    return count, num_simulations

# Simulate the tournament and count how many times team 2 and 3 meet in the semifinals
count, total_simulations = simulate_tournament(num_simulations=100000)
probability = count / total_simulations
print(count, probability)
