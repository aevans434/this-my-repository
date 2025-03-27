#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:22:48 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 30.0  # initial velocity in m/s
theta_deg = 45.0  # launch angle in degrees
g = 9.81  # gravity in m/s^2

theta_rad = np.radians(theta_deg)

total_time = (2 * v0 * np.sin(theta_rad)) / g

time_intervals = np.linspace(0, total_time, num=100)

x_t = v0 * np.cos(theta_rad) * time_intervals
y_t = v0 * np.sin(theta_rad) * time_intervals - 0.5 * g * time_intervals**2

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].plot(time_intervals, x_t, 'b--')
axs[0].set_title('Horizontal Position vs Time')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Horizontal Position x(t) (m)')
# %%
axs[1].plot(time_intervals, y_t, 'g-.')

axs[1].set_title('Vertical Position vs Time')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Vertical Position y(t) (m)')

axs[2].plot(x_t, y_t, 'r-')
axs[2].set_title('Projectile Path (x vs y)')
axs[2].set_xlabel('Horizontal Position x(t) (m)')
axs[2].set_ylabel('Vertical Position y(t) (m)')

plt.tight_layout()
plt.show()





