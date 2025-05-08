import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Define the dimensions (x, y, z, color)
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
color_dimension = np.sqrt(x**2 + y**2)
color_dimension = color_dimension / color_dimension.max()

# Create a 3D figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface with color mapping
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(color_dimension), alpha=0.7, cmap=cm.jet, linewidth=0, antialiased=False)

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('4D Surface Plot')

# Add a color bar
cbar = fig.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_label('Color')

# Show the plot
plt.show()

