import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))  # Shift the sine wave over time
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()

