import sympy as sp

# Define the variables and the function to be integrated
x, y, z = sp.symbols('x y z')
f = x**2 + y**2 + z**2

# Define the integration limits
x_min, x_max = 0, 1
y_min, y_max = 0, 1
z_min, z_max = 0, 1

# Perform the symbolic volume integral
result = sp.integrate(f, (x, x_min, x_max), (y, y_min, y_max), (z, z_min, z_max))

# Print the result
print("Symbolic Result:", result)

