#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np

delta = 0.025
x = y = np.arange(-3., 3.01, delta)
X, Y = np.meshgrid(x, y)
Z1 = plt.mlab.bivariate_normal(X, Y)
Z2 = plt.mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
Z = 10 * (Z1 - Z2)

nr, nc = Z.shape

Z[-nr//6:, -nc//6:] = np.nan
Z = np.ma.array(Z)
Z[:nr//6, :nc//6] = np.ma.masked

fig, axs = plt.subplots(2, 2)
ax1 = axs.flat[0]
ax2 = axs.flat[1]
ax3 = axs.flat[2]
ax4 = axs.flat[3]

## Contour plot with default settings.
ct1 = ax1.contourf(X, Y, Z, 10, alpha = 0.5, cmap = plt.cm.bone, origin = 'lower')
# contour using coordinates form X and Y with value in Z in 10 levels.
# `contourf` will fill the gap between levels with proper face color.
# 10 tells contourf to automatically generate 10 levels.

ct2 = ax1.contour(X, Y, Z, ct1.levels[::2], alpha = 0.75, colors = ['r', 'b', 'g', 'y'], origin = 'lower', hold = 'on')
# `contour` will plot the contour "line" only. In this contour `ct2`, it is the same contour as `ct1`
# except that it only take account for every two level in ct1.levels.

ax1.title.set_text("contourf and contour (horizontal cbar)")
ax1.title.set_y(1.1)
ax1.xaxis.set_label_text("x value (-3, 3.01)")
ax1.yaxis.set_label_text("y value (-3, 3.01)")
ax1.axis('image')

# colorbar
cbar = fig.colorbar(ct1, ax = ax1, shrink = 0.6, orientation = 'horizontal', pad = 0.25)
cbar.ax.tick_params(labelsize = 8)
cbar.add_lines(ct2)

levels = [-1.5, -1, -0.5, 0, 0.5, 1]
ct3 = ax2.contourf(X, Y, Z, levels, cmap = cm.bone, alpha = 0.75, extend = 'both') # extend the colormap.
ct3.cmap.set_under(colors.cnames["darkblue"])
ct3.cmap.set_over(colors.cnames["aqua"])
ax2.title.set_text("contour with extend color (both)")
ax2.title.set_y(1.1)
ax2.axis('image')

# listed colors
ct4 = ax3.contourf(X, Y, Z, levels, colors = ["r", "g", "b"], origin = 'lower', extend = 'both')
ct4.cmap.set_under('y')
ct4.cmap.set_over('cyan')
ax3.title.set_text("Listed Colors with white label words.")
ax3.title.set_y(1.1)
ct5 = ax3.contour(X, Y, Z, levels, colors = ['k'])
ax3.clabel(ct5, fmt = '%2.1f', colors = 'w', fontsize = 14)
ax3.xaxis.set_label_text("x")
ax3.yaxis.set_label_text("y")
ax3.axis('image')

# different label text color

ct6 = ax4.contourf(X, Y, Z, 10, cmap = cm.hot, alpha = 0.75)
ax4.title.set_text("Change x, y label colors")
ax4.title.set_y(1.1)
ax4.xaxis.set_label_text("x", color = 'y')
ax4.yaxis.set_label_text('y', color = 'b')
ax4.axis('image')

fig.subplots_adjust(hspace = 0.5, wspace = 0.5)

plt.tight_layout()
plt.show()
fig.savefig("../figs/contour_parc.jpg")

