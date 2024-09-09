'''Throw fair coin, if head +1 else -1. Game ends if reach target or go bankrupt
    Starting from starting_money, chance of reaching target?'''

# Parameters
starting_money = 10
target_money = 100
# approx 0.1046

import random

def coin_flip():
    # Simulate a coin flip: 1 for heads (win), 0 for tails (lose)
    return random.choice([0, 1])

def simulate_game(starting_money, target_money):
    money = starting_money
    while money > 0 and money < target_money:
        bet = 1
        if coin_flip():
            money += bet  # Win: gain $1
        else:
            money -= bet  # Lose: lose $1
    return money == target_money  # Returns True if we reached the target, False if bankrupt

def run_simulation(starting_money, target_money, num_simulations):
    wins = 0
    for _ in range(num_simulations):
        if simulate_game(starting_money, target_money):
            wins += 1
    probability = wins / num_simulations
    return probability

num_simulations = 10000  # Number of simulations to run

# Run the simulation and calculate the probability of success
probability_of_winning = run_simulation(starting_money, target_money, num_simulations)
print(f"The probability of leaving with ${target_money} is approximately {probability_of_winning:.4f}")
