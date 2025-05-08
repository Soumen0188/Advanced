import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the symbolic variables
x = sp.symbols('x')

# Define the function you want to integrate
f = x**3 + 3*x**2 + 3*x + 1

# Compute the integral symbolically
integral = sp.integrate(f, x)

# Convert the symbolic integral to a Python function
integral_function = sp.lambdify(x, integral, 'numpy')

# Create a range of x values for plotting
x_values = np.linspace(0, 5, 100)  # Adjust the range and number of points as needed

# Compute the corresponding y values for the integral
y_values_integral = [integral_function(x_val) for x_val in x_values]

# Plot the integral
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values_integral, label='Integral')
plt.xlabel('x')
plt.ylabel('Integral Value')
plt.title('Plot of Integral')
plt.legend()
plt.grid(True)
plt.show()

