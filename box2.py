import numpy as np
import matplotlib.pyplot as plt

# Define the parameter range (theta values)
theta = np.linspace(0, 2*np.pi, 1000)

# Define the parametric equations
x = np.sin(theta)
y = np.sin(9*theta/2)**3

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, label=r'$\sin(\theta) + \sin^3\left(\frac{9\theta}{2}\right)$')
plt.title('Parametric Plot of Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

