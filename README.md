# Notes for Matplolib

# Intro

There are four privmative drawing objects in `matplotlib`:

- `Line2D`: this object is used to present a 2D line on the graph or any other curves that can be Bezier-approximated.
- `AxesImage`: this object takes a 2D data and interprete it as densities with a colormap. This is usually returned by the `imshow` method.
- `Patch`: It represent a 2D object that has a single colored "face". This object must have "path" which is much like a Line2D object enclosing a a face to filled with that color.
- `Text`: It represent the text in a graph such as legends, labels,...etc. It takes a string, coordinates and font parameters to instantiate this object.

Any sophisticated plots in matplotlib are build upon these four objects. In the following notes, I will mostly use these four objects to plot all the graph. See the python scripts in `challenges` directory for more advanced examples.

Switch to `interative` branch to see how to write interative matplotlib applications.

# Events and Callback

# Interative Applications

# References

- [Matplotlib Doc.](http://matplotlib.org/users/index.html)
- [Mapplotlib Gallery](http://matplotlib.org/gallery.html)
- [Challenges](http://www.labri.fr/perso/nrougier/teaching/matplotlib/#d-plots)
- [Colormaps](http://matplotlib.org/users/colormaps.html)
- [Transformation](http://matplotlib.org/users/transforms_tutorial.html)
- [Bezier Curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [Patch Collections](http://matplotlib.org/examples/api/patch_collection.html)
- [3D subplots](http://matplotlib.org/examples/mplot3d/mixed_subplots_demo.html)
- [GridSpec](http://matplotlib.org/users/gridspec.html)
