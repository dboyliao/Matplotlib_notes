#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

n = 20
Z = np.ones(n)
Z[-1] *= 2

fig, ax = plt.subplots(1, 1)

colors = ['%0.3f' % ((i+0.03)/(n+0.03)) for i in range(n)]
explode = [0.05*Z[i] for i in range(n)]
ax.pie(Z, 
       colors = colors, 
       labels = [str(z) for z in Z.flat],
       explode = explode,
       autopct = '%0.5f')
plt.show()

fig.savefig("../figs/pie_plot.jpg", transparent = True, dpi = 100)
