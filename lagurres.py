import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre
from mpl_toolkits.mplot3d import Axes3D

# Define the Laguerre polynomial order (n)
n = 3

# Create a grid of x and y values
x = np.linspace(0, 10, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Laguerre polynomial values for the grid
Z = genlaguerre(n, 0)(X) * np.exp(-X/2)

# Create a 3D plot
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Laguerre L%d(X) * exp(-X/2)' % n)

# Show the plot
plt.title('Laguerre Polynomial L%d(X) * exp(-X/2)' % n)
plt.show()

