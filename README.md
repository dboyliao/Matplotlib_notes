# Notes for Matplolib

# Intro

There are four privmative drawing objects in `matplotlib`:

- `Line2D`: this object is used to present a 2D line on the graph or any other curves that can be Bezier-approximated.
- `AxesImage`: this object takes a 2D data and interprete it as densities with a colormap. This is usually returned by the `imshow` method.
- `Patch`: It represent a 2D object that has a single colored "face". This object must have "path" which is much like a Line2D object enclosing a a face to filled with that color.
- `Text`: It represent the text in a graph such as legends, labels,...etc. It takes a string, coordinates and font parameters to instantiate this object.

Any sophisticated plots in matplotlib are build upon these four objects. In the following notes, I will mostly use these four objects to plot all the graph. See the python scripts in `pracs` directory for more advanced examples.

Switch to `interative` branch to see how to write interative matplotlib applications.

# Events and Callback

## Line Picking

```{python}
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pickle

with open("../data/tracks.pickle") as pf:
    tracks = pickle.load(pf)
    tracks = dict((tid, t) for tid, t in tracks.items() if tid != -9)

fig, ax = plt.subplots(1, 1)

# Define th callback function.
# `event` obj has some useful attributes such as `x`, `y` (the `position`), `xdata` and `ydata` (the `value`).
def onpick_callback(event):
    if not isinstance(event.artist, LineCollection):
        return
    lws = event.artist.get_linewidths()
    print event.ind
    for i in event.ind:
        lws[i] = 4 if lws[i] != 4 else 1
    event.artist.set_linewidths(lws)
    fig.canvas.draw_idle()
    # `fig.canvas.draw_idle` is equivalent as `fig.canvas.draw` except the 
    # time when the drawing actually happen. `draw_idle` will wait in a queue
    # to be queued.

lc = LineCollection(tracks.values(), color = 'b', lw = [1 for _ in range(len(tracks))], picker = True)
ax.add_collection(lc)
ax.autoscale()

fig.canvas.mpl_connect('pick_event', onpick_callback)
ax.set_xlabel('Longitude')
ax.set_ylabel("Latitude")

plt.show()
```

## Drawing Span

# Interative Applications

# References

- [Matplotlib Collections](http://matplotlib.org/api/collections_api.html)
