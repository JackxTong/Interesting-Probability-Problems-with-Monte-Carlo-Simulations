import random
import numpy as np

def simulate_coin_games(num_simulations):
    valid_games = []
    
    for _ in range(num_simulations):
        # Simulate rolling the coin 6 times
        rolls = [random.choice(['H', 'T']) for _ in range(5)]
        
        # Check if 1st, 3rd, and 5th rolls are the same
        if rolls[0] == rolls[2] == rolls[4]:
            # Count the number of heads
            num_heads = rolls.count('H')
            
            # Check if the number of heads is greater than 1
            if num_heads > 1:
                valid_games.append(num_heads)
    
    # Calculate the expected number of heads for valid games
    if valid_games:
        return np.mean(valid_games)
    else:
        return None

# Simulate the game for a large number of simulations
num_simulations = 100000
expected_heads = simulate_coin_games(num_simulations)
print(expected_heads)
