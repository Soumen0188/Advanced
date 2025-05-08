'''
4D plot using python
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate random 4D data
np.random.seed(0)
num_points = 100
x = np.random.rand(num_points)  # First dimension
y = np.random.rand(num_points)  # Second dimension
z = np.random.rand(num_points)  # Third dimension
fourth_dimension = np.random.rand(num_points)  # Fourth dimension (represented by color and size)

# Create a scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with color and size representing the fourth dimension
scatter = ax.scatter(x, y, z, c=fourth_dimension, cmap='viridis', s=100*fourth_dimension)

# Add colorbar to the plot
cbar = plt.colorbar(scatter)
cbar.set_label('Fourth Dimension')

# Set labels for the three spatial dimensions
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('4D Scatter Plot')
plt.show()

