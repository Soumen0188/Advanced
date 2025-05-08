import numpy as np
import matplotlib.pyplot as plt

# Define the function
def func(x, y):
    return np.sin(x + np.cos(y**2))

# Generate x and y values
x_vals = np.linspace(-10, 10, 400)  # Adjust range and number of points as needed
y_vals = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = func(X, Y)

# Create the plot
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label='Function Value')
plt.title(r'$\sin(x + \cos(y^2))$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

