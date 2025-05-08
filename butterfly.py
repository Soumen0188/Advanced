import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for the butterfly shape
t = np.linspace(0, 10*np.pi, 1000)
x = np.sin(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
z = np.sin(t/12)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the butterfly shape
ax.plot(x, y, z, lw=3)

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title for the plot
ax.set_title('3D Butterfly Plot')

# Show the plot
plt.show()

