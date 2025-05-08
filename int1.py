import scipy.integrate as spi
import numpy as np

# Define the function you want to integrate
def f(x):
    return x**2 + 2*x + 1

# Define the integration limits
a = 0  # Lower limit
b = 2  # Upper limit

# Compute the numerical integral using quad from SciPy
result, error = spi.quad(f, a, b)

# Display the result
print("Numerical Integral:", result)

