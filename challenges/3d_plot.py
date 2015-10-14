#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

f = lambda X, Y: np.sin(np.sqrt(X**2 + Y**2))
fig = plt.figure()
ax3D = Axes3D(fig)
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)
Z = f(X, Y) + 1

surf = ax3D.plot_surface(X, Y, Z, 
                         rstride = 1, 
                         cstride = 1, 
                         cmap = plt.cm.hot,
                         linewidth = 0)
ct = ax3D.contourf(X, Y, Z, cmap = plt.cm.hot, zdir = 'z', offset = -0.5)
ax3D.set_zlim(-0.5, Z.max())
cbar = plt.colorbar(surf, ax = ax3D, shrink = 0.5, aspect = 5)
ax3D.axis('off')
plt.show()

fig.savefig("../figs/3d_plot.jpg")