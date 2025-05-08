import numpy as np
import matplotlib.pyplot as plt


# Generate data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create the 3D contour plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(x, y, z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Contour Plot')

plt.show()

