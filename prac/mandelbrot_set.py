#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
import numpy as np

def iter_count(C, max_iter):
    X = C
    for n in range(max_iter):
        if abs(X) > 2:
            return n
        X = X**2 + C
    return max_iter

def make_label(v, p):
    return '%.2f' % v

N = 512
max_iter = 64
xmin, xmax, ymin, ymax = -2.2, 0.8, -1.5, 1.5

X = np.linspace(xmin, xmax, N)
Y = np.linspace(ymin, ymax, N)
Z = np.empty((N, N))

for i, y in enumerate(Y):
    for j, x in enumerate(X):
        Z[i, j] = iter_count(complex(x, y), max_iter)

fig, ax = plt.subplots(nrows = 1, ncols = 1)
#ax.xaxis.set_major_formatter(ticker.FuncFormatter(make_label))
ax.axis('off')
ax.imshow(Z, cmap = cm.pink)
plt.show()

fig.savefig("../figs/mandelbrot.jpg")
