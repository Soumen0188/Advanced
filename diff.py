import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function representing the second-order differential equation
def model(y, x):
    y0, y1 = y
    dy0 = y1
    dy1 = -2 * y1 - 2 * y0
    return [dy0, dy1]

# Initial conditions
y0_initial = 1
y1_initial = 0
initial_conditions = [y0_initial, y1_initial]

# Time points for the solution
x = np.linspace(0, 10, 100)

# Solve the differential equation using odeint
solution = odeint(model, initial_conditions, x)

# Extract the y values from the solution
y_values = solution[:, 0]

# Plot the solution
plt.plot(x, y_values)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution of Second-Order Differential Equation')
plt.grid(True)
plt.show()

