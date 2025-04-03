#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:56:25 2025

@author: arielle
"""
import numpy as np

def rotate_vector(vector, theta_degrees):
    theta_radians = np.radians(theta_degrees)
    rotation_matrix = np.array ([
       [ np.cos(theta_radians), -np.sin(theta_radians)], 
        [np.sin(theta_radians), np.cos(theta_radians)]
        ])
    rotated_vector = np.dot(rotation_matrix, vector)
    return rotated_vector

v=(3,4)
theta = 90

rotated = rotate_vector(v,theta)

x_rotated, y_rotated = rotated
print (f"original vector: {v}")
print (f"Rotated vector by {theta}: {x_rotated:.2f}, {y_rotated: .2f})")