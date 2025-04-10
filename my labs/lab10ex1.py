#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:48:15 2025

@author: arielle
"""

from scipy.integrate import quad 
import numpy as np
import matplotlib.pyplot as plt

f1 = lambda x: x**2
result_a, _ = quad(f1, 0, 2)
print("a. ∫₀² x² dx =", result_a)

f2 = lambda x: np.exp(-x**2/2)
x_vals = np.linspace(0, 5, 100)
integrals = [quad(f2, 0, x)[0] for x in x_vals]
plt.plot(x_vals, integrals)
plt.title("b. Integral of $e^{-x^2/2}$ from 0 to x")
plt.xlabel("x")
plt.ylabel("Integral value")
plt.grid(True)
plt.show()

result_c, _ = quad(f2, -np.inf, np.inf)
exact_value = np.sqrt(2* np.pi)
print ("c. ∫₋∞^∞ e^{-x²/2} dx =", result_c)
print("Exact value: sqrt(2pi) =", exact_value)
print("c. ∫_{-∞}^{∞} e^(-x^2/2) dx =", result_c)

