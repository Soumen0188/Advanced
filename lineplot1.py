import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the number of points in the line
num_points = 50

# Create an initial empty line plot
line, = ax.plot([], [], [], lw=2)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Define the initialization function
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Define the update function for animation
def update(frame):
    t = np.linspace(0, 2 * np.pi, num_points)
    x = np.cos(t + frame * 0.1)
    y = np.sin(t + frame * 0.1)
    z = t
    
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Show the plot
plt.show()

