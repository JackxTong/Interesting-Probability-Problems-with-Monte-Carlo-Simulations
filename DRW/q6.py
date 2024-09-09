'''Answer given by p4 = 11/16, p10 = 683/1024
    1000*(p4 + p10) = 1354.492'''
import random

# Number of steps in each simulation and number of trials
N = 1000  # Number of steps in each simulation
M = 100000  # Number of trials

def simulate():
    step = 0
    hit_4 = False
    hit_10 = False
    for _ in range(N):
        if random.random() < 0.5:  # Heads -> move 1 step
            step += 1
        else:  # Tails -> move 2 steps
            step += 2
        
        # Check if we hit exactly step 4 or step 10
        if step == 4:
            hit_4 = True
        if step == 10:
            hit_10 = True
        
        # If we go beyond step 10, we can stop early
        if step > 10:
            break
            
    return hit_4, hit_10

# Arrays to store the results of each trial
p4_results = []
p10_results = []

# Run M trials
for _ in range(M):
    hits_4 = 0
    hits_10 = 0
    
    # Run N simulations within each trial
    for _ in range(N):
        hit_4, hit_10 = simulate()
        if hit_4:
            hits_4 += 1
        if hit_10:
            hits_10 += 1
    
    # Store the ratio for this trial
    p4_results.append(hits_4 / N)
    p10_results.append(hits_10 / N)

# Calculate the average ratios
average_p4 = sum(p4_results) / M
average_p10 = sum(p10_results) / M

# Calculate the final result: 1000 * (average_p4 + average_p10)
result = 1000 * (average_p4 + average_p10)

# Output the result rounded to 3 decimal places
print(f"The result is: {result:.3f}")
