#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

f = lambda x, y: (1 - x/2 + x**5 + y**3)*np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)


