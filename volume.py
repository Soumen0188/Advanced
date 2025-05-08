import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import nquad

# Define the function to integrate
def f(x, y):
    return x**2 + y**2

# Define the integration limits for x and y
x_lower_limit = -1
x_upper_limit = 1
y_lower_limit = -1
y_upper_limit = 1

# Perform the volume integration
result, _ = nquad(f, [(x_lower_limit, x_upper_limit), (y_lower_limit, y_upper_limit)])

# Create a grid of points for the 3D plot
x = np.linspace(x_lower_limit, x_upper_limit, 50)
y = np.linspace(y_lower_limit, y_upper_limit, 50)
X, Y = np.meshgrid(x, y)
Z = x**2 + y**2

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and a title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Volume Integration Result = {result:.2f}')

# Show the plot
plt.show()

