import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameter range (theta values)
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(theta) + np.sin(9*theta/2)**3

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.linspace(0, 1, len(theta))  # Z values for each point

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label=r'$\sin(\theta) + \sin^3\left(\frac{9\theta}{2}\right)$')
ax.set_title('3D Plot of Function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

