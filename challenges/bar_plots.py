#!/usr/bin/env python
# Ans: http://www.labri.fr/perso/nrougier/teaching/matplotlib/scripts/bar_ex.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import cnames

n = 12. 
x = np.arange(n)
y1 = (1 - x/n) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x/n) * np.random.uniform(0.5, 1.0, n)

fig, ax = plt.subplots(nrows = 1, ncols = 1)
ax.bar(x, y1, facecolor = cnames['skyblue'], edgecolor = 'white')
ax.bar(x, -y2, facecolor = cnames['lime'], edgecolor = 'white')

for a, b in zip(x, y1):
    ax.text(a + 0.4, b + 0.05, '%.2f' % b, ha = 'center', va = 'bottom') 
    # ha for horizontal alignment, va for vertical alignment.

for a, b in zip(x, y2):
    ax.text(a + 0.4, -b - 0.05, '%.2f' % b, ha = 'center', va = 'top')

ax.set_ylim(-1.25, 1.25)
ax.axis('off')
plt.show()

fig.savefig("bar_plots.jpg")