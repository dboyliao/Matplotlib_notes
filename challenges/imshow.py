#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

f = lambda x, y: (1 - x/2 + x**5 + y**3)*np.exp(-x**2 - y**2)

n = 10
x = np.linspace(-3, 3, 4*n)
y = np.linspace(-3, 3, 3*n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(1, 1)
im = ax.imshow(Z, cmap = plt.cm.bone, interpolation = 'nearest', origin = 'lower')
cbar = plt.colorbar(im, ax = ax, shrink = 0.75)

ax.axis('off')
plt.show()
fig.savefig('../figs/imshow.jpg')