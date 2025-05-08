'''
3D plot using python
'''
import numpy as np
import matplotlib.pyplot as plt

# Create a meshgrid of x and y values
x = np.linspace(0.1, 5, 100)  # Avoiding x = 0 for log function
y = np.linspace(0.1, 5, 100)
x, y = np.meshgrid(x, y)

# Define the function to plot (logarithm)
z = np.log(x)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Logarithm Plot')

# Add a colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()

