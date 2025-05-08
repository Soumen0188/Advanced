import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import jn  # Import Bessel function from SciPy

# Create a meshgrid of x and y values
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Calculate the Bessel function values for various orders and input values
order = 2  # Bessel function order
Z = jn(order, np.sqrt(X**2 + Y**2))  # Calculate Bessel function values

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Bessel Function')
ax.set_title(f'Bessel Function of Order {order}')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()

