import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of position and momentum values
x = np.linspace(-5, 5, 100)
p = np.linspace(-5, 5, 100)
x, p = np.meshgrid(x, p)

# Example: Probability distribution of a squeezed state
# Replace this with your own data or mathematical expressions
sigma_x = 0.5  # Uncertainty in position
sigma_p = 2.0  # Uncertainty in momentum
prob_density = np.exp(-(x**2 / (2 * sigma_x**2)) - (p**2 / (2 * sigma_p**2)))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, p, prob_density, cmap='viridis')

# Add labels and title
ax.set_xlabel('Position')
ax.set_ylabel('Momentum')
ax.set_zlabel('Probability Density')
ax.set_title('Squeezed State Probability Distribution')

# Add a colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()

