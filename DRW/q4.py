'''Answer for the 7-side game should be 85.05
Given by (1+7/6+7/5+7/4+7/3+7/2+1)*7'''

import random

def simulate_game():
    """Simulate the game and return the number of rolls needed to see all 7 sides."""
    sides_seen = set()
    rolls = 0
    
    while True:
        rolls += 1
        roll = random.randint(1, 7)  # Simulate rolling a 7-sided die
        sides_seen.add(roll)
        
        if len(sides_seen) == 6:  # If 6 unique sides have been seen
            next_roll = random.randint(1, 7)  # Roll again
            rolls += 1
            if next_roll in sides_seen:
                # Reset the process if the next roll is a side already seen
                sides_seen = set()
            else:
                sides_seen.add(next_roll)
        
        # If all 7 sides have been seen, break the loop
        if len(sides_seen) == 7:
            break
    
    return rolls

def simulate_n_games(n):
    """Simulate the game n times and return the average number of rolls."""
    total_rolls = 0
    for _ in range(n):
        total_rolls += simulate_game()
    
    return total_rolls / n

# Run the simulation for 1,000,000 trials
n_trials = 1000000
average_rolls = simulate_n_games(n_trials)

# Output the result rounded to 3 decimal places
print(f"Expected number of rolls: {average_rolls:.3f}")
