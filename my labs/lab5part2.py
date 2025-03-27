#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 23:41:43 2025

@author: arielle
"""
import numpy as np

v0 = 50
theta_deg = 45
g = 9.81

theta_rad = np.radians(theta_deg)
time_intervals = np.array ([0, 1, 2, 3, 4, 5])

for t in time_intervals: 
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    print (f" At t = {t}s: x = {x:.2f} m, y = {y:.2f} m")
           
