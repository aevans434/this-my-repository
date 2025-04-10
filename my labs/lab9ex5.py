#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:52:13 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 42)
num_steps = 500
x_step = rng.random(num_steps) > 0.5
y_step = rng.random(num_steps) > 0.5
z_step = rng.random(num_steps) > 0.5
x_step = 2*x_step -1
y_step = 2*y_step -1
z_step = 2*z_step -1
x_position = np.cumsum(x_step)
y_position = np.cumsum(y_step)
z_position = np.cumsum(z_step)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection ='3d')

ax1.plot(x_position, y_position, z_position)

ax1.set_xlabel('X position')
ax1.set_ylabel('Y position')
ax1.set_zlabel('Z posiiton')
ax1.set_title('3D Random Walk')

plt.show()
