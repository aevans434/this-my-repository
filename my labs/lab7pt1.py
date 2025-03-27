#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:40:55 2025

@author: arielle
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2, 7, 100)
f_x = np.exp(x)          # e^x
g_x = x**3.6             # x^3.6

plt.figure(figsize=(8, 5))
plt.plot(x, f_x, label='e^x', color='blue')
plt.plot(x, g_x, label='x^3.6', color='green')
plt.title('Regular Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.semilogy(x, f_x, label='e^x', linestyle='--', color='blue')
plt.semilogy(x, g_x, label='x^3.6', linestyle='-.', color='green')
plt.title('Semilog Plot (log y-axis)')
plt.xlabel('x')
plt.ylabel('log(y)')
plt.legend()
plt.grid(True, which='both')
plt.show()

plt.figure(figsize=(8, 5))
plt.loglog(x, f_x, label='e^x', linestyle='--', color='blue')
plt.loglog(x, g_x, label='x^3.6', linestyle='-.', color='green')
plt.title('Log-Log Plot')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.legend()
plt.grid(True, which='both')
plt.show()

