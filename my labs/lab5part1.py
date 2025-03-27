#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 23:29:15 2025

@author: arielle
"""
import numpy as np
G = 6.674e-11
masses = np.array([
    (5.972e24, 7.348e22),   
    (1.989e30, 5.972e24)
    (6.417e23, 3.285e23)    
])
distances = np.array([
    3.844e8,
    1.496e11,
    9.2e10 
    ])
for i in range(len(masses)):
    m1, m2 = masses[i]
    d = distances[i]
    F = G * (m1 * m2) / d**2
    print(f"Gravitational Force between planet pair {i+1}: {F:.2e} N")
    