import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function
def func(theta):
    return np.exp(np.cos(theta) - 2 * np.cos(4 * theta)) * np.sin(700 * theta)**4

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], lw=2)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation update function
def animate(i):
    theta = np.linspace(0, 2 * np.pi, 1000)
    y = func(theta - i * 0.1)
    line.set_data(theta, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

