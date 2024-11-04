#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/csv/')

files = os.listdir()
list.sort(files)
cter = 0
for file in files:
    data = np.loadtxt(file, delimiter=',', skiprows=1)
    x = data[:,0]
    y = data[:,1]
    # plt.xticks(np.arange(0,800,50))
    plt.figure(figsize=(15, 5))
    plt.axis('off')
    plt.box(False)
    plt.plot(x*1e6,y*1e6, 'k.')
    plt.savefig('/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/csv/position_plot/' + 'figure'+'{:04d}'.format(cter)+'.png',dpi=300)
    plt.clf()
    cter = cter +1
    
