import numpy as np

# Number of simulations
n_simulations = 10000000

# Simulate the problem
count_success = 0

for _ in range(n_simulations):
    # Toss the coin twice (1 for heads, 0 for tails)
    heads = np.random.binomial(1, 0.5, 2).sum()
    
    # If no heads, the product will always be 0 (less than 10)
    if heads == 0:
        count_success += 1
        continue
    
    # Roll the dice 10 times
    dice_sum = np.random.randint(1, 7, 10).sum()
    
    # Calculate the product of heads and dice_sum
    product = heads * dice_sum
    
    # Check if the product is less than or equal to 10
    if product <= 10:
        count_success += 1

# Estimate the probability
p = count_success / n_simulations

print(f"Estimated probability p: {p}")
