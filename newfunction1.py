import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of theta values
theta = np.linspace(-2*np.pi, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Calculate the x, y, and z values based on the function
x = (1 + np.sin(theta)) * np.sin(phi)
y = (1 + np.sin(theta)**5 + np.cos(theta)**3) * np.cos(phi)
z = (1 + np.sin(theta)) * np.cos(phi)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot title
ax.set_title('3D Plot of sin(theta) + sin(theta)**5 + cos(theta)**3')

plt.show()

