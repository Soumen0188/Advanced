import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)  # Generate values for theta

# Calculate the values of the function for each theta
y = np.sin(theta) + np.sin(theta)**5 + np.cos(theta)**3

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(theta, y, label=r'$\sin(\theta) + \sin^5(\theta) + \cos^3(\theta)$')
plt.xlabel(r'$\theta$')
plt.ylabel('Function Value')
plt.title('Plot of Function: Sin(theta) + Sin^5(theta) + Cos^3(theta)')
plt.legend()
plt.grid(True)
plt.show()

