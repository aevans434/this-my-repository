#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:45:04 2025

@author: arielle
"""

import numpy as np

rng= np.random.default_rng()
samples = rng.random(100)
flips = samples < 0.5
num_heads = np.sum(flips)
print(f"Total number of heads: {num_heads}")
