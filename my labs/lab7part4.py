#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:54:26 2025

@author: arielle
"""

import matplotlib.pyplot as plt
elements = ['Hydrogen', 'Helium', 'Oxygen', 'Carbon', 'Neon', 'Iron', 'Nitrogen', 'Silicon', 'Magnesium', 'Sulfur']
abundances = [75, 23, 1, 0.5, 0.13, 0.11, 0.1, 0.07, 0.06, 0.05]  # Approximate values
plt.figure(figsize=(10, 7))
plt.pie(abundances, labels=elements, autopct='%1.1f%%', startangle=140)
plt.title('Relative Abundances of Elements in the Universe')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(title="Elements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
plt.show()
