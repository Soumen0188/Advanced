import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the complex function (example: f(z) = 1/(z-pole1) + 1/(z-pole2))
def complex_function(z, poles):
    result = np.zeros_like(z, dtype=np.complex128)
    for pole in poles:
        result += 1 / (z - pole)
    return result

# Create a grid of complex numbers (in this example, you can adjust the range)
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Define the poles (adjust as needed)
poles = [1 + 1j, -2 - 2j]

# Calculate the complex function values at each point in the grid
W = complex_function(Z, poles)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract the real and imaginary parts of the complex function values
W_real = np.real(W)
W_imag = np.imag(W)

# Plot the real and imaginary parts as surfaces
ax.plot_surface(X, Y, W_real, cmap='viridis', rstride=1, cstride=1, alpha=0.8)
ax.plot_surface(X, Y, W_imag, cmap='plasma', rstride=1, cstride=1, alpha=0.8)

# Add labels
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_zlabel('Function Value')

# Show the plot
plt.show()

