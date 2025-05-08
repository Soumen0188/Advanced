import sympy as sp

# Define the symbolic variables
x = sp.symbols('x')

# Define the function you want to integrate
f = x**2 + 2*x + 1

# Compute the integral symbolically
integral = sp.integrate(f, x)

# Display the result
print("Symbolic Integral:", integral)

