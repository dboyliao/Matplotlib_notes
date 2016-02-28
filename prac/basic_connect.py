#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 1000)
y = np.sinc(10*x)

fig, ax = plt.subplots(1, 1)
fig.suptitle("sinc(10x)")
ax.plot(x, y, c = 'b', ls = '--')

def key_callback(event):
    print dir(event)
    print "Key:", event.key

def button_callback(event):
    print dir(event)
    print "Button:", event.x, event.y, event.xdata, event.ydata, event.button

fig.canvas.mpl_connect('key_press_event', key_callback)
fig.canvas.mpl_connect('button_release_event', button_callback)
fig.canvas.mpl_connect('button_press_event', button_callback)

plt.show()
