import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points in the x and y dimensions
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

# Define the initialization function
def init():
    ax.plot_surface(X, Y, np.zeros_like(X), cmap='viridis')
    return fig,

# Define the update function for animation
def update(frame):
    Z = np.sin(np.sqrt(X**2 + Y**2 + frame * 0.1))
    ax.clear()  # Clear the previous frame
    ax.plot_surface(X, Y, Z, cmap='viridis')
    return fig,

# Create the animation
animation = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Show the plot
plt.show()

