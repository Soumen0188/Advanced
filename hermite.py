import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import hermite

def hermite_polynomial(x, n):
    return hermite(n)(x)

# Create a grid of x and y values
x_vals = np.linspace(-3, 3, 100)
y_vals = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x_vals, y_vals)

# Calculate the Hermite polynomial values for each point in the grid
n = 3  # Choose the order of the Hermite polynomial
z = hermite_polynomial(x, n) * hermite_polynomial(y, n)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Hermite polynomial surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Hermite Polynomial')

# Set title for the plot
ax.set_title(f'Hermite Polynomial (n={n})')

# Show the plot
plt.show()

