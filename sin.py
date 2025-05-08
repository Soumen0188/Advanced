import numpy as np
import matplotlib.pyplot as plt

# Generate data for the sine plot
x = np.linspace(0, 2 * np.pi, 100)  # 100 data points between 0 and 2*pi
y = np.sin(x)  # Calculate the sine of each data point

# Create the plot
plt.plot(x, y)

# Customize the plot (optional)
plt.title('Sine Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Display the plot
plt.show()

