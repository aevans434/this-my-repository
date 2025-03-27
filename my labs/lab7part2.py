#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:47:37 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt
masses = np.array([2, 5, 10, 15, 20])  # in kg
velocity = 4.0  # in m/s (same for all)
kinetic_energy = 0.5 * masses * velocity**2
plt.figure(figsize=(8, 5))
plt.bar(range(len(masses)), kinetic_energy, tick_label=[f"{m} kg" for m in masses], color='skyblue')
plt.title("Kinetic Energy of Objects with Varying Masses")
plt.xlabel("Object Mass")
plt.ylabel("Kinetic Energy (Joules)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

