#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pickle

with open("../data/tracks.pickle") as pf:
    tracks = pickle.load(pf)
    tracks = dict((tid, t) for tid, t in tracks.items() if tid != -9)

fig, ax = plt.subplots(1, 1)

def onpick_callback(event):
    if not isinstance(event.artist, LineCollection):
        return
    lws = event.artist.get_linewidths()
    print event.ind
    for i in event.ind:
        lws[i] = 4 if lws[i] != 4 else 1
    event.artist.set_linewidths(lws)
    fig.canvas.draw_idle()

lc = LineCollection(tracks.values(), color = 'b', lw = [1 for _ in range(len(tracks))], picker = True)
ax.add_collection(lc)
ax.autoscale()

fig.canvas.mpl_connect('pick_event', onpick_callback)
ax.set_xlabel('Longitude')
ax.set_ylabel("Latitude")

plt.show()

