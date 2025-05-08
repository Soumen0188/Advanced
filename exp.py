import numpy as np
import matplotlib.pyplot as plt

# Create a meshgrid of x and y values
x = np.linspace(-1, 1, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define the function to plot (exponential)
a = 0.1  # Adjust this value to control the rate of exponential growth
z = np.exp(a * (x**2 + y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Exponential Function Plot')

# Add a colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()

