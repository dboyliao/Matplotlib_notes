#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import numpy as np

x = np.arange(200)
y = 20*np.sin(np.pi*x/44.0) + 25*np.random.random((len(x),)) + 50

fig, (ax1, ax2)= plt.subplots(2, 1, figsize = (12, 9))
ax1.step(x, y)
ax1.set_ylabel("y")
ax1.set_xlabel('x')
step2, = ax2.step([], [])
ax1.axis("image")
ax2.axis("image")

def onselect(xmin, xmax):
    ind_min, ind_max = np.searchsorted(x, (xmin, xmax))
    ind_max = min(len(x) - 1, ind_max)

    x_segment = x[ind_min:ind_max]
    y_segment = y[ind_min:ind_max]
    step2.set_data(x_segment, y_segment)
    ax2.set_xlim(x_segment[0], x_segment[-1])
    ax2.set_ylim(y_segment.min(), y_segment.max())
    fig.canvas.draw_idle()

span = SpanSelector(ax1, onselect, 'horizontal', span_stays = True,
                    rectprops = dict(alpha = 0.5, facecolor = "cyan"))

plt.show()
