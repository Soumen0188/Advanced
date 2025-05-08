import numpy as np
from scipy.integrate import dblquad

# Define the function to be integrated
def f(x, y):
    return x**2 + y**2

# Define the limits of integration
x_lower_limit = 0
x_upper_limit = 1
y_lower_limit = 0
y_upper_limit = 1

# Perform the double integral
result, error = dblquad(f, x_lower_limit, x_upper_limit, y_lower_limit, y_upper_limit)

print(f"Result of surface integration: {result}")
print(f"Error estimate: {error}")

