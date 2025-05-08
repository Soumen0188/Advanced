import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function to be integrated
def f(x, y, z):
    return x**2 + y**2 + z**2

# Define the integration limits
x_min, x_max = 0, 1
y_min, y_max = 0, 1
z_min, z_max = 0, 1

# Create a grid of points in the integration domain
x_vals = np.linspace(x_min, x_max, 50)
y_vals = np.linspace(y_min, y_max, 50)
z_vals = np.linspace(z_min, z_max, 50)

# Initialize an empty 3D array to store function values
values = np.zeros((len(x_vals), len(y_vals), len(z_vals)))

# Evaluate the function at each point in the grid
for i, x in enumerate(x_vals):
    for j, y in enumerate(y_vals):
        for k, z in enumerate(z_vals):
            values[i, j, k] = f(x, y, z)

# Calculate the volume integral
result = np.trapz(np.trapz(np.trapz(values, x_vals, axis=0), y_vals, axis=0), z_vals)

# Create a 3D plot of the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)

ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(values / values.max() ))

# Display the result in the title of the plot
plt.title(f'Volume Integral Result: {result:.2f}')

# Show the plot
plt.show()

