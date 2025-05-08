import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Define the Legendre polynomial order (n)
n = 3

# Create a grid of x and y values
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Legendre polynomial values for the grid
Z = legendre(n)(X)

# Create a 3D plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Legendre P%d(X)' % n)

# Show the plot
plt.title('Legendre Polynomial P%d(X)' % n)
plt.show()

