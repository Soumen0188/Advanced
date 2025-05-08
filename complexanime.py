import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define the complex function
def complex_function(x, y):
    z = x + 1j * y
    return np.sin(z)  # Example function: sin(z)

# Create a meshgrid of x and y values
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = complex_function(X, Y)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the plot with the initial frame
plot = [ax.plot_surface(X, Y, Z, cmap='viridis')]

# Animation update function
def update(frame):
    ax.clear()
    new_z = complex_function(X, Y) * np.exp(1j * frame * 0.1)  # Animation phase shift
    plot[0] = ax.plot_surface(X, Y, np.real(new_z), cmap='viridis')

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=100)

# Show the animation
plt.show()

