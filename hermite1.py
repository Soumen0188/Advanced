import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from mpl_toolkits.mplot3d import Axes3D

# Define the Hermite polynomial order (n)
n = 4

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Hermite polynomial values for the grid
Z = hermite(n)(X) * np.exp(-X**2)

# Create a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Hermite H%d(X) * exp(-X^2)' % n)

# Show the plot
plt.title('Hermite Polynomial H%d(X) * exp(-X^2)' % n)
plt.show()

