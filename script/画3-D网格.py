# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations, permutations
import random

fig = plt.figure()


ax = fig.gca(projection='3d')
# ax.set_aspect("equal")


r = range(0, 4)

# line width
lw = 1

# line color
lc = '#919191'

# get all position in a 2d plane
coordinates = product(r, repeat=2)

# draw line parallel to x axis
x = (r[0], r[-1])
for y, z in coordinates:
    ax.plot3D(x, [y, y], [z, z], color=lc, lw=lw)
    ax.plot3D([y, y], x, [z, z], color=lc, lw=lw)
    ax.plot3D([y, y], [z, z], x, color=lc, lw=lw)
# get all points coordinates
coord_it = product(r, repeat=3)
# collect all points
coords = []
for c in coord_it:
    coords.append(c)
for c in random.sample(coords, 8):
    # if c[0] % 2 and c[1] % 2 and c[2] % 2:
    ax.scatter(*c, color='k', s=80, marker='o')
plt.axis('off')
plt.show()
