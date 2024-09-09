import random

# Function to simulate one game of dealing cards until two aces are seen
def simulate_game():
    deck = ['A'] * 4 + ['Other'] * 48  # 4 aces and 48 non-aces
    random.shuffle(deck)
    
    ace_count = 0
    cards_dealt = 0
    
    for card in deck:
        cards_dealt += 1
        if card == 'A':
            ace_count += 1
        if ace_count == 2:
            break
            
    return cards_dealt

# Simulate the game 1000 times and collect results
num_simulations = 100000
results = [simulate_game() for _ in range(num_simulations)]

# Calculate average result
average_cards_dealt = sum(results) / num_simulations

print(f"Average number of cards needed to deal: {average_cards_dealt}")
