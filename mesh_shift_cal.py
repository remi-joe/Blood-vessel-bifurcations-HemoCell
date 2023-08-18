#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:15:29 2023

@author: remi
"""

from numpy import sin,cos,tan,pi

D1 = 0.93
D2 = 0.58
D_max = max(D1, D2)

S23_z = 0.5 / tan(pi / 12)
S45_x = (0.5 / sin(pi / 12) + 5 * D_max * cos(pi / 12)) * sin(pi / 12)
S45_z = (0.5 / sin(pi / 12) + 5 * D_max * cos(pi / 12)) * cos(pi / 12)
S6_z = 2 * S45_z
S78_z = S6_z - S23_z

mov_x =  - 5 - S45_z 
mov_y = - D1 / 2 - S45_x

print(mov_x)
print(mov_y)
