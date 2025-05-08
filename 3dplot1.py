'''
3D plot using python
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#----------------- Create a meshgrid of x and y values---------------
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

#------------ Calculate the z values using the sin function-------------------
z = np.sin(np.sqrt(x**2 + y**2))

#------------------- Create a 3D plot------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#---------------------- Plot the surface------------------------
surf = ax.plot_surface(x, y, z, cmap='viridis')

#-------------------- Add labels and title-------------------
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Plot of sin function')

#---------------------- Add a colorbar-------------------------
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

#-------------------- Show the plot-------------------------------------
plt.show()

