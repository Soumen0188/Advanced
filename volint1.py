import scipy.integrate as spi

# Define the function to be integrated as a Python function
def f(x, y, z):
    return x**2 + y**2 + z**2

# Define the integration limits
x_min, x_max = 0, 1
y_min, y_max = 0, 1
z_min, z_max = 0, 1

# Perform the numerical volume integral
result, _ = spi.nquad(f, [(x_min, x_max), (y_min, y_max), (z_min, z_max)])

# Print the result
print("Numerical Result:", result)

