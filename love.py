import numpy as np
import matplotlib.pyplot as plt

# Define the function
def func(x, y, z):
    term1 = (2 * (4/3 * x)**2 + 2 * y**2 + z**2 - 1)**3
    term2 = ((4/3 * x)**2 * z**3) / 10
    term3 = y**2 * z**3
    return term1 - term2 - term3

# Define the fixed values for x and y
x_val = 1.0
y_val = 2.0

# Create an array of z values
z_vals = np.linspace(-2, 2, 100)

# Calculate the function values for each z value
F = func(x_val, y_val, z_vals)

# Create a 2D plot
plt.figure()
plt.plot(z_vals, F)
plt.xlabel('Z')
plt.ylabel('Function Value')
plt.title('2D Plot of the Given Function for x=1.0, y=2.0')
plt.grid()

# Show the plot
plt.show()

