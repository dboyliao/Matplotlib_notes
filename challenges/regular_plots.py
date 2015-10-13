#!/usr/bin/env python
## Ans: http://www.labri.fr/perso/nrougier/teaching/matplotlib/scripts/plot_ex.py

import matplotlib.pyplot as plt
import numpy as np
import time

n = 256
x = np.linspace(-np.pi, np.pi, n, endpoint = True)
y = np.sin(2*x)

fig, axs = plt.subplots(nrows = 2, ncols = 1)
ax1 = axs[0]
ax2 = axs[1]

ax1.plot(x, y, c = 'b', alpha = 0.5)
ax1.fill_between(x, 0, y, color = 'b', alpha = 0.25)
ax1.axis('off')

ax2.plot(x, y, c = 'b', alpha = 1)
ax2.fill_between(x, 0, y, y > 0, color = 'b', alpha = 0.25)
ax2.fill_between(x, 0, y, y < 0, color = 'r', alpha = 0.25)
ax2.axis('off')

plt.show()
fig.savefig('regular_plot.jpg')
# Do not use fig.show() since fig.show() is in interative mode
# which means you can not see the figure since the process terminate immediately.
