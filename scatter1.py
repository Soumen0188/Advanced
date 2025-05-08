import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create some random data for demonstration
np.random.seed(42)
num_points = 50
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the scatter plot
scatter = ax.scatter(x, y, z, c=z, cmap='viridis')

# Define the update function for animation
def update(frame):
    # Generate new random data for each frame
    new_z = np.random.rand(num_points)
    
    # Update the data for the scatter plot
    scatter._offsets3d = (x, y, new_z)
    scatter.set_array(new_z)
    
    # Set the title for each frame
    ax.set_title(f'Frame {frame}')

# Create the animation
animation = FuncAnimation(fig, update, frames=10, interval=500, repeat=True)

# Show the plot
plt.show()

