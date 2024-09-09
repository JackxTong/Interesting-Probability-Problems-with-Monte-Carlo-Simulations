'''Stock worth 100, roll dice and flip a coin.
    If head, stock + dice number, else - dice number
    Chance of > 150 after 10 days?'''

# Note this is random walk, each step Xi can be (-6,-5..-1,1,2,..,6)
# each with 1/2*1/6=1/12
# so E(Xi)=0, var(Xi)=E(Xi^2)=91/12
# Variance of total change in 10 days has var 10*91/12=75.833
# so standard deviation=8.708
# question asks P(U>50) for U~N(0, 8.708), or 4e-09

from scipy.stats import norm

print(1 - norm.cdf(50/8.708))

import numpy as np
S0 = 100
days = 10
N = 100000

def simulate_stock_price():
    stock_price = S0
    for _ in range(days):
        dice_roll = np.random.randint(1, 7)  # Roll a six-sided dice
        coin_flip = np.random.choice(['heads', 'tails'])  # Flip a coin
        
        if coin_flip == 'heads':
            stock_price += dice_roll
        else:
            stock_price -= dice_roll
            
    return stock_price

count_above_150 = 0
for _ in range(N):
    final_price = simulate_stock_price()
    if final_price > 150:
        count_above_150 += 1

Pr = count_above_150 / N
print(Pr)
print(count_above_150)


