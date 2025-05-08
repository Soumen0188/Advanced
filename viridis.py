# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:30:06 2024

@author: Admin
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri

# Example 1: Triangulation plot
ang = 32
rad = 10
radm = 0.35
radii = np.linspace(radm, 0.95, rad)
angles = np.linspace(0, 1.4 * np.pi, ang)
angles = np.repeat(angles[..., np.newaxis], rad, axis=1)
angles[:, 1::2] += np.pi
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.sin(4 * radii) * np.cos(4 * angles)).flatten()
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1), y[triang.triangles].mean(axis=1)) < radm)
tpc = plt.tripcolor(triang, z, shading='flat', cmap='viridis')
plt.colorbar(tpc)
plt.title('matplotlib.pyplot.viridis() function Example', fontweight="bold")
plt.show()

# Example 2: Image plot
dx, dy = 0.015, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(6), range(6)) % 2
plt.imshow(Z1, cmap="binary_r", interpolation='nearest', extent=extent, alpha=1)

def geeks(x, y):
    return (1 - x / 2 + x**5 + y**6) * np.exp(-(x**2 + y**2))

Z2 = geeks(X, Y)
plt.imshow(Z2, alpha=0.7, interpolation='bilinear', extent=extent, cmap='viridis')
plt.title('matplotlib.pyplot.viridis() function Example', fontweight="bold")
plt.show()
