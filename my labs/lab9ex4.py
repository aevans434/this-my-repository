#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:47:17 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 42)
num_steps = 500
x_step = rng.random(num_steps) > 0.5
y_step = rng.random(num_steps) > 0.5
x_step = 2*x_step - 1
y_step = 2*y_step - 1
x_position = np.cumsum(x_step)
y_position = np.cumsum(y_step)

plt.figure()
plt.plot(x_position, y_position)
plt.xlabel('x-position')
plt.ylabel( 'y-position')
plt.axis("equal")
plt.title('2D Random Walk')