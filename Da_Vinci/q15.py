import numpy as np

# Number of simulations
n_simulations = 1000000

# Generate X and Y from uniform distribution between -1 and 1
X = np.random.uniform(-1, 1, n_simulations)
Y = np.random.uniform(-1, 1, n_simulations)

# Condition 1: X + Y < 1
condition1 = (X + Y) < 1

# Condition 2: X^2 + Y^2 > 1
condition2 = (X**2 + Y**2) > 1

# Both conditions must be satisfied
successes = condition1 & condition2

# Estimate probability
p = np.mean(successes)

print(f"Estimated probability p: {p}")
