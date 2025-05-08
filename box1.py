import numpy as np
import matplotlib.pyplot as plt

def parametric_function(t, j):
    x = t
    y = np.sin(j * t)
    return x, y

# Define the parameter values
j_value = 2  # You can adjust this value to see how the plot changes

# Generate values for the parameter t
t_values = np.linspace(0, 10 * np.pi, 1000)  # Adjust the range as needed

# Compute the corresponding x and y values using the parametric function
x_values, y_values = parametric_function(t_values, j_value)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=f'j = {j_value}')
plt.title(f'Parametric Plot: {{t, Sin({j_value}*t)}}')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

