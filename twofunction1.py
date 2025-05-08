import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of theta values
theta = np.linspace(0, 2*np.pi, 100)
theta_3d, theta_2d = np.meshgrid(theta, theta)

# Define the functions
function1 = 2 * np.cos(theta_3d) + np.sin(2 * theta_3d) * np.cos(60 * theta_3d)
function2 = np.sin(2 * theta_3d) + np.sin(60 * theta_3d)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D Plot of Functions")

# Plot the functions in 3D
ax.plot_surface(theta_3d, theta_2d, function1, cmap='viridis', label="2Cos(theta) + Sin(2theta) Cos(60theta)")
ax.plot_surface(theta_3d, theta_2d, function2, cmap='plasma', label="Sin(2theta) + Sin(60theta)")

# Set labels for the axes
ax.set_xlabel("Theta")
ax.set_ylabel("Theta")
ax.set_zlabel("Function Values")

# Add a legend
#ax.legend()

# Display the 3D plot
plt.show()

