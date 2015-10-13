#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
t = np.arctan2(y, x)

fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.scatter(x, y, s = 75, c = t, alpha = .5) # s for size, c for color
ax.set_xlim(-1.5, 1.5)
ax.xaxis.set_ticks([])
ax.set_ylim(-1.5, 1.5)
ax.yaxis.set_ticks([])

plt.show()
fig.savefig("scatter_plot.jpg")
