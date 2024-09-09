import numpy as np

jar_A = np.array([1, 2, 3, 4, 5, 6, 7])
jar_B = np.array([8, 9, 10, 11, 12, 13, 14])

# Function to simulate swapping balls
def swap_balls(jar_A, jar_B):
    # Randomly pick a ball from each jar
    ball_A = np.random.choice(jar_A)
    ball_B = np.random.choice(jar_B)
    
    # Perform the swap
    jar_A = np.where(jar_A == ball_A, ball_B, jar_A)
    jar_B = np.where(jar_B == ball_B, ball_A, jar_B)
    
    return jar_A, jar_B

# Simulate the product of the two balls picked after the swap
def simulate_product(trials=100000):
    total_product = 0
    
    for _ in range(trials):
        # Swap the balls
        jar_A_swapped, jar_B_swapped = swap_balls(jar_A, jar_B)
        
        # Pick a ball from each jar
        pick_A = np.random.choice(jar_A_swapped)
        pick_B = np.random.choice(jar_B_swapped)
        
        # Calculate the product and accumulate
        total_product += pick_A * pick_B
        
    # Return the expected product
    return total_product / trials

# Perform the simulation
expected_product = simulate_product()

print(expected_product)
