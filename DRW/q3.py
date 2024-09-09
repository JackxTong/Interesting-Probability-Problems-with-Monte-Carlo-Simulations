'''Answer is 1.382, or 6/sqrt(6 pi)'''

import numpy as np
import matplotlib.pyplot as plt

# Function Q(x) based on the value of c
def Q(x, c):
    return np.where(x > 0, c, -c)

# Function to calculate the mean squared error (MSE)
def calculate_mse(c, n_samples=1000000):
    # Generate standard normal samples
    x = np.random.normal(0, np.sqrt(3), n_samples)
    
    # Calculate Q(x) for given c
    Q_x = Q(x, c)
    
    # Calculate the mean squared error (MSE)
    mse = np.mean((Q_x - x) ** 2)
    
    return mse

# Generate values of c between 0.001 and 2 with 2000 steps
c_values = np.linspace(1, 2, 1000)
mse_values = [calculate_mse(c) for c in c_values]

# Find the value of c that minimizes the MSE
min_mse_index = np.argmin(mse_values)
min_c = c_values[min_mse_index]
min_mse = mse_values[min_mse_index]

# Print the minimum c and the corresponding MSE
print(f"Minimum MSE is {min_mse:.6f} at c = {min_c:.6f}")

# Plot the MSE as a function of c
plt.plot(c_values, mse_values, label='MSE for different values of c')
plt.scatter(min_c, min_mse, color='red', label=f'Minimum at c = {min_c:.4f}', zorder=5)
plt.xlabel('c value')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE of Q(x) vs c')
plt.legend()
plt.grid(True)
plt.show()
