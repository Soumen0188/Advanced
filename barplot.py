import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
categories = ['A', 'B', 'C', 'D', 'E']
x = np.arange(len(categories))
y = np.random.rand(len(categories))
z = np.zeros(len(categories))

# Create the 3D bar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar(x, y, z, zdir='y', align='center', alpha=0.8)

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Bar Plot')

ax.set_xticks(x)
ax.set_xticklabels(categories)

plt.show()

