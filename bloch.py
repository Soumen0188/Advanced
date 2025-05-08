import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# Create a Bloch sphere
b = Bloch()

# Define a state vector (e.g., a superposition state)
psi = (basis(2, 0) + basis(2, 1)).unit()

# Add the state vector to the Bloch sphere
b.add_states(psi)

# Set the view parameters
b.view = [90, 0]

# Render the Bloch sphere
b.show()

# To save the plot as an image file, you can use:
# mlab.savefig("bloch_sphere.png")

# Show the Bloch sphere plot
plt.show()

