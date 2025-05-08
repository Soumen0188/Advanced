import numpy as np
import matplotlib.pyplot as plt

# Define the range of theta values
theta = np.linspace(0, 2*np.pi, 1000)

# Define the functions
function1 = 2 * np.cos(theta) + np.cos(60 * theta)
function2 = np.sin(2 * theta) + np.sin(60 * theta)

# Create a figure and axis
plt.figure(figsize=(10, 6))
plt.title("Plot of Functions")
plt.xlabel("Theta")
plt.ylabel("Function Values")

# Plot the functions
plt.plot(theta, function1, label="2Cos(theta) + Sin(2theta) Cos(60theta)")
plt.plot(theta, function2, label="Sin(2theta) + Sin(60theta)")

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

