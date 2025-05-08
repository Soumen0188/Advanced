import numpy as np
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function to be integrated
def f(x, y):
    return x**2 + y**2

# Define the limits of integration
x_lower_limit = 0
x_upper_limit = 1
y_lower_limit = 0
y_upper_limit = 1

# Perform the double integral
result, _ = dblquad(f, x_lower_limit, x_upper_limit, y_lower_limit, y_upper_limit)

# Create a 3D plot of the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a mesh grid for x and y values
x = np.linspace(x_lower_limit, x_upper_limit, 50)
y = np.linspace(y_lower_limit, y_upper_limit, 50)
X, Y = np.meshgrid(x, y)

# Calculate the function values for the mesh grid
Z = f(X, Y)

# Plot the surface
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add a color bar to the plot
fig.colorbar(surface)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title
plt.title(f'Surface Integration Result = {result:.2f}')

# Show the plot
plt.show()

