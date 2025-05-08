import numpy as np

# Parameters and discretization setup
N = 1000  # Number of grid points
R_max = 100.0  # Maximum radius
dr = R_max / N  # Step size
r = np.linspace(dr, R_max, N)  # Radial grid

# Construct the matrix A
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = -2 / dr**2 - 2 / r[i] + l * (l + 1) / r[i]**2
    if i > 0:
        A[i, i-1] = 1 / dr**2 - 1 / (2 * r[i] * dr)
    if i < N-1:
        A[i, i+1] = 1 / dr**2 + 1 / (2 * r[i] * dr)

# Adjust constants to match units and hydrogen atom potential specifics
# Note: This example omits these adjustments for simplicity

# Solve the eigenvalue problem
eigenvalues, eigenvectors = np.linalg.eigh(A)

# The eigenvalues correspond to the energy levels, and the eigenvectors are the radial wave functions
