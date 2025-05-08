import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

wL = 3.0
m = 0.0
E = 10.0
l = 1.0
wz = 3.0
k = 0.0

def f(y, r):
    y,z=y
    dydr = [z, (2(wL*m + E) - l*(l+1)/r**2 - wz**2 * r**2 -2*k/r )*y]
    return dydr # Example function, replace with your own


r = np.linspace(0,1,101)  # Time points for evaluation

sol = odeint(f,[-5,5],r)

plt.plot(r, sol[:,0])
plt.show()
