#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

f = lambda x, y: (1 - x/2 + x**5 + y**3)*np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(1, 1)
ct1 = ax.contourf(X, Y, Z, 8, alpha = 0.75, cmap = 'hot')
ct2 = ax.contour(X, Y, Z, 8, colors = [u'k'], linewidth = 0.5)
ax.clabel(ct2, fmt = '%1.3f', colors = u'k', fontsize = 10)

ax.axis('off')

plt.show()

fig.savefig("../figs/contour_plot.jpg", transparent = True)

