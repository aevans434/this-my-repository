#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:53:17 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt
temperatures = np.linspace(100, 1000, 50)  # temperatures from 100 K to 1000 K
k = 1.38e-23  # Boltzmann constant (J/K)
thermal_energy = k * temperatures + np.random.normal(scale=1e-21, size=temperatures.shape)
plt.figure(figsize=(8, 5))
plt.hist(thermal_energy, bins=10, color='orange', edgecolor='black')
plt.title("Histogram of Thermal Energy Distribution")
plt.xlabel("Thermal Energy (Joules)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
