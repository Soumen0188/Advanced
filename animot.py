import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)

# Create a line object for the plot
line, = ax.plot([], [], lw=2)

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(frame):
    theta = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(theta) + np.sin(9 * theta / 2) ** 3
    line.set_data(theta, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, animate, frames=200, init_func=init, blit=True)

plt.show()

