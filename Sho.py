import numpy as np
import scipy.sparse.linalg as linalg
from scipy import integrate
import matplotlib.pyplot as plt
from scipy import sparse
from types import SimpleNamespace

N = 3000
x = np.linspace(-15, 15, N, dtype = float)
dx = x[1] - x[0]

w = 1

def potential(x):
    return (0.5*w**2*x**2)

V = potential(x)
D2 = sparse.diags([1,-2,1],[-1,0,1],shape=(N,N))/(dx**2)
T = -0.5 * D2
U = sparse.diags(V.reshape(N),(0))
H = T + U 
eigv, eigvec = linalg.eigs(H, k=10, sigma = 0)

vec = eigvec.T

print(eigv)  # printing eigen value

n = 1 #no of excited state, for ground state n = 0

plt.plot(x,vec.real[1],'-')
plt.show()
