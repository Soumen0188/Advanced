import numpy as np
import matplotlib.pyplot as plt

# Parameters
hbar = 1.0  # Reduced Planck's constant
v_fermi = 1.0  # Fermi velocity
k_vals = np.linspace(-np.pi, np.pi, 400)  # Wavevector values

# Dispersion relation of Tomonaga model
epsilon_k = hbar * v_fermi * np.abs(k_vals)

# Plot the dispersion relation
plt.figure(figsize=(8, 6))
plt.plot(k_vals, epsilon_k, color='b', label=r'$\epsilon_k = \hbar v_F |k|$')
plt.xlabel('Wavevector $k$')
plt.ylabel('Energy $\epsilon_k$')
plt.title('Dispersion Relation of Tomonaga Model')
plt.legend()
plt.grid()
plt.show()

