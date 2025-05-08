import numpy as np
import matplotlib.pyplot as plt

# Define the parameter range (theta values)
theta = np.linspace(0, 2*np.pi, 1000)

# Define the function
def parametric_function(theta):
    return np.exp(np.cos(theta) - 2 * np.cos(4 * theta)) * np.sin(700 * theta)**4

# Calculate the x and y coordinates using the parametric function
x = parametric_function(theta) * np.cos(theta)
y = parametric_function(theta) * np.sin(theta)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Parametric Plot')
plt.title('Parametric Plot of Exp[Cos(theta) - 2Cos(4*theta)] * Sin^4(700*theta)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()

