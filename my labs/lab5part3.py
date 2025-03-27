#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 23:47:55 2025

@author: arielle
"""
import numpy as np

resistors_series = np.array ([10, 20, 30])
resistors_parallel = np.array ([5, 10, 15])

total_series = 0
for r in resistors_series: 
    total_series += r
inverse_total_parallel = 0
for r in resistors_parallel: 
    inverse_total_parallel += 1 / r
if inverse_total_parallel != 0: 
    total_parallel = 1 / inverse_total_parallel
else: 
    total_parallel = float('inf')
print(f"Total resistance in series: {total_series:.2f} ohms")
print(f"Total resistance in parallel: {total_parallel:.2f} ohms")
