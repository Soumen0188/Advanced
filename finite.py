import numpy as np
from scipy.linalg import eigh

# Define parameters
omega_r = 1.0
l = 1
N = 100
r_min = 0.01  # Start from a small positive value to avoid division by zero
r_max = 10.0

# Define the grid
r = np.linspace(r_min, r_max, N)
dr = r[1] - r[0]

# Define the potential
V = omega_r**2 * r**2 / 2 + 1/(2*r) + l*(l+1)/(2*r**2)

# Construct the matrix
A = np.zeros((N, N))
np.fill_diagonal(A, -2/dr**2 + V)
A += np.diag(1/dr**2 * np.ones(N-1), k=-1)
A += np.diag(1/dr**2 * np.ones(N-1), k=1)

# Solve the eigenvalue problem
eigvals, eigvecs = eigh(A)

# Extract the ground state eigenvector (corresponding to the lowest eigenvalue)
u = eigvecs[:, 0]

# Normalize the wave function
u /= np.sqrt(np.sum(u**2) * dr)

# Now u contains the normalized wave function at the grid points
print(u)
