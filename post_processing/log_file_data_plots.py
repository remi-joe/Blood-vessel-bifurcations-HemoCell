#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the directory containing CSV files
csv_dir0 = "/home/remi/Desktop/post_processing_images/csv/D31.5_0_0.csv"
csv_dir1 = "/home/remi/Desktop/post_processing_images/csv/D31.5_0_1.csv"
csv_dir2 = "/home/remi/Desktop/post_processing_images/csv/D31.5_0_2.csv"
csv_dir3 = "/home/remi/Desktop/post_processing_images/csv/D31.5_0_3.csv"
csv_dir4 = "/home/remi/Desktop/post_processing_images/csv/D31.5_0_4.csv"
#
out_dir = "/home/remi/Desktop/post_processing_images/csv/"
#
################ LABELS ################
label0 = "Baseline" 
label1 = "Case-1" 
label2 = "Case-2" 
label3 = "Case-3" 
label4 = "Case-4" 
# 
# FONT
font = {'family': 'sans-serif', 'color': 'black', 'weight': 'normal', 'size': 28}  
#

### BASELINE
csv0 = pd.read_csv(csv_dir0)
time0 = np.array(csv0["Time (s)"])
mean_vel0 = np.array(csv0["Mean Velocity (m/s)"])
visc0 = np.array(csv0["Relative Viscosity"])

### Case1
csv1 = pd.read_csv(csv_dir1)
time1 = np.array(csv1["Time (s)"])
mean_vel1 = np.array(csv1["Mean Velocity (m/s)"])
visc1 = np.array(csv1["Relative Viscosity"])

### Case2
csv2 = pd.read_csv(csv_dir2)
time2 = np.array(csv2["Time (s)"])
mean_vel2 = np.array(csv2["Mean Velocity (m/s)"])
visc2 = np.array(csv2["Relative Viscosity"])

### Case3
csv3 = pd.read_csv(csv_dir3)
time3 = np.array(csv3["Time (s)"])
mean_vel3 = np.array(csv3["Mean Velocity (m/s)"])
visc3 = np.array(csv3["Relative Viscosity"])

### Case4
csv4 = pd.read_csv(csv_dir4)
time4 = np.array(csv4["Time (s)"])
mean_vel4 = np.array(csv4["Mean Velocity (m/s)"])
visc4 = np.array(csv4["Relative Viscosity"])

### MEAN VEL PLOT

#     
plt.figure(figsize=(14,7))
plt.plot(time0, mean_vel0*1000,'k.', label=label0)
plt.plot(time1, mean_vel1*1000,'.',color='#9467bd', label=label1)
plt.plot(time2, mean_vel2*1000,'g.', label=label2)
plt.plot(time3, mean_vel3*1000,'b.', label=label3)
plt.plot(time4, mean_vel4*1000,'r.', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Mean Velocity Magnitude (mm/s)', fontdict= font)
plt.title("Fluid (Plasma)", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4],fontsize = font['size'])
plt.tight_layout()
#
plt.savefig(out_dir + "mean_fluid_vel" + ".png", dpi = 300)
#


### VISCOSITY PLOT

#     
plt.figure(figsize=(14,7))
plt.plot(time0, visc0,'k.', label=label0)
plt.plot(time1, visc1,'.',color='#9467bd', label=label1)
plt.plot(time2, visc2,'g.', label=label2)
plt.plot(time3, visc3,'b.', label=label3)
plt.plot(time4, visc4,'r.', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Relative Apparent Viscosity', fontdict= font)
plt.title("Bifurcating Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4],fontsize = font['size'])
plt.tight_layout()
#
plt.savefig(out_dir + "rel_app_vis" + ".png", dpi = 300)
#


