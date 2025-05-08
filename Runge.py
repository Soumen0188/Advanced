import numpy as np
import matplotlib.pyplot as plt

# Define the ODE dy/dx = f(x, y)
def f(x, y):
    return x - y

# Fourth-order Runge-Kutta method
def runge_kutta_4th_order(x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]
    
    for _ in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        
        y0 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        
        x_values.append(x0)
        y_values.append(y0)
    
    return x_values, y_values

# Initial conditions and parameters
x0 = 0
y0 = 1
h = 0.1  # Step size
n = 50   # Number of steps

# Solve the ODE using RK4
x_values, y_values = runge_kutta_4th_order(x0, y0, h, n)

# Plot the results
plt.figure()
plt.plot(x_values, y_values, label='Numerical Solution (RK4)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Numerical Solution of dy/dx = x - y using RK4')
plt.legend()
plt.grid(True)
plt.show()

