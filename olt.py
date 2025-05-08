import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.cos(x ** 2 + y ** 2)

# Create a figure and a 3D Axes
fig = plt.figure()
ax = plt.axes(projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
