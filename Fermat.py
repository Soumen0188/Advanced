import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the source, mirror, and observation point
source = np.array([0, 2])
mirror = np.array([1, 0])
observation = np.array([3, 2])

# Define the mirror equation: y = ax + b
a = (mirror[1] - source[1]) / (mirror[0] - source[0])
b = source[1] - a * source[0]

# Generate x-coordinates along the path of the light ray
x_ray = np.linspace(source[0], observation[0], num=100)

# Calculate corresponding y-coordinates using the mirror equation
y_ray = a * x_ray + b

# Calculate the distance traveled by the light ray at each point
distances = np.sqrt((x_ray - source[0])**2 + (y_ray - source[1])**2) + np.sqrt((x_ray - observation[0])**2 + (y_ray - observation[1])**2)

# Find the index where the total distance is minimized
min_distance_index = np.argmin(distances)

# Plot the mirror and light ray path
plt.plot([source[0], observation[0]], [source[1], observation[1]], 'bo-')
plt.plot(x_ray, y_ray, 'r-')
plt.plot(mirror[0], mirror[1], 'go')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Light Ray Path According to Fermat's Principle")
plt.legend(['Source to Observation', 'Light Ray Path', 'Mirror'])
plt.grid()
plt.show()

