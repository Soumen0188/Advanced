import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the complex function
def complex_function(z):
    return z**2 + np.conj(z)

# Generate a grid of complex numbers
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Evaluate the complex function at each point in the grid
W = complex_function(Z)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the real and imaginary parts of the result
ax.plot_surface(X, Y, np.real(W), cmap='viridis', rstride=1, cstride=1, alpha=0.8)
ax.plot_surface(X, Y, np.imag(W), cmap='plasma', rstride=1, cstride=1, alpha=0.8)

# Set labels and title
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_zlabel('Value')
ax.set_title('3D Plot of Complex Function')

# Add colorbars
cbar_real = fig.colorbar(ax.plot_surface(X, Y, np.real(W), cmap='viridis', rstride=1, cstride=1, alpha=0.8), ax=ax, pad=0.1)
cbar_real.set_label('Real Part')
cbar_imag = fig.colorbar(ax.plot_surface(X, Y, np.imag(W), cmap='plasma', rstride=1, cstride=1, alpha=0.8), ax=ax, pad=0.1)
cbar_imag.set_label('Imaginary Part')

# Show the plot
plt.show()


