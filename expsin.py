import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def func(theta):
    return np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) * np.sin(1000 * theta)**4

# Generate theta values
theta = np.linspace(0, 2 * np.pi, 300)
theta_3d = np.linspace(0, 2 * np.pi, 300)
theta_3d, theta_2d = np.meshgrid(theta_3d, theta)

# Compute the function values
z = func(theta_2d)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
ax.plot_surface(theta_3d, theta_2d, z, cmap='viridis')

# Set labels for the axes
ax.set_xlabel('Theta 3D')
ax.set_ylabel('Theta 2D')
ax.set_zlabel('Function Value')

# Set the title of the plot
plt.title('3D Plot of Exp[Cos(theta)] - 2 * Cos(4 * theta) * Sin^4(1000 * theta)')

# Show the plot
plt.show()

