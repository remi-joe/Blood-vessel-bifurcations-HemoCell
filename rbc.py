#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import numpy as np
import matplotlib.pyplot as plt

case0 = "/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/csv/"
case1 = "/home/remi/irp/simulation_files/case_files/D31.5_0_1/output_0/csv/"
case2 = "/home/remi/irp/simulation_files/case_files/D31.5_0_2/output_0/csv/"
case3 = "/home/remi/irp/simulation_files/case_files/D31.5_0_3/output_0/csv/"
case4 = "/home/remi/irp/simulation_files/case_files/D31.5_0_4/output_0/csv/"
#
output_dir = "/home/remi/Desktop/post_processing_images/position_animations/"
#
files0 = os.listdir(case0)
files0.sort()
num_ts0 = len(files0)
#
files1 = os.listdir(case1)
files1.sort()
num_ts1 = len(files1)
#
files2 = os.listdir(case2)
files2.sort()
num_ts2 = len(files2)
#
files3 = os.listdir(case3)
files3.sort()
num_ts3 = len(files3)
#
files4 = os.listdir(case4)
files4.sort()
num_ts4 = len(files4)

# Single Timestep size
dt = 6.25e-8
# Increment in data
inc = 10000



# Volume of the larger child vessel
vlc = 7.73*(31.5*10**(-6))**(3)

# Volume of the smaller child vessel
vsc = 3.215*(31.5*10**(-6))**(3)

# The total volume will change for the different cases and the parent vessels
# The volumes were calculated from the FreeCAD geometries

##############################################################
################## TOTAL TUBE HEMATOCRIT #####################
##############################################################

################## Baseline ##################
os.chdir(case0)

# Timestep loop
value0 = []
for i in range(num_ts0):
    value = dt * i * inc
    value0.append(value)

# Total vessel volume 
tv_case0 = 19.86*(31.5*10**(-6))**(3)

# HCT_total
hct_total0 = []

for file in files0:
    data0 = np.loadtxt(file, delimiter=",", skiprows=1)
    hct_case0 = sum(data0[:,4])/tv_case0
    hct_total0.append(hct_case0*100)
label0 = "Baseline"     
################ End of Baseline #############
#
################# Case1 ##################
os.chdir(case1)
#
# Timestep loop
value1 = []
for i in range(num_ts1):
    value = dt * i * inc
    value1.append(value)
#
# Total vessel volume 
tv_case1 = 19.86*(31.5*10**(-6))**(3)
#
# HCT_total
hct_total1 = []
#
for file1 in files1:
    data1 = np.loadtxt(file1, delimiter=",", skiprows=1)
    hct_case1 = sum(data1[:,4])/tv_case1
    hct_total1.append(hct_case1*100)
label1 = "case1"    
################ End of case1 #############
#
################# Case2 ##################
os.chdir(case2)
#
# Timestep loop
value2 = []
for i in range(num_ts2):
    value = dt * i * inc
    value2.append(value)
#
# Total vessel volume 
tv_case2 = 19.86*(31.5*10**(-6))**(3)
#
# HCT_total
hct_total2 = []
#
for file2 in files2:
    data2 = np.loadtxt(file2, delimiter=",", skiprows=1)
    hct_case2 = sum(data2[:,4])/tv_case2
    hct_total2.append(hct_case2*100)
label2 = "case2"     
################ End of case2 #############
#
################# Case3 ##################
os.chdir(case3)
#
# Timestep loop
value3 = []
for i in range(num_ts3):
    value = dt * i * inc
    value3.append(value)
#
# Total vessel volume 
tv_case3 = 19.86*(31.5*10**(-6))**(3)
#
# HCT_total
hct_total3 = []
#
for file3 in files3:
    data3 = np.loadtxt(file3, delimiter=",", skiprows=1)
    hct_case3 = sum(data3[:,4])/tv_case2
    hct_total3.append(hct_case3*100)
label3 = "case3"    
################ End of case3 #############
#
################# Case4 ##################
os.chdir(case4)
#
# Timestep loop
value4 = []
for i in range(num_ts4):
    value = dt * i * inc
    value4.append(value)
#
# Total vessel volume 
tv_case4 = 19.86*(31.5*10**(-6))**(3)
#
# HCT_total
hct_total4 = []
#
for file4 in files4:
    data4 = np.loadtxt(file4, delimiter=",", skiprows=1)
    hct_case4 = sum(data4[:,4])/tv_case2
    hct_total4.append(hct_case4*100)
label4 = "case4"    
################ End of case4 #############

font = {'family': 'sans-serif', 'color': 'black', 'weight': 'normal', 'size': 18}        
plt.figure(figsize=(10,7))
plt.plot(value0, hct_total0,'k-', label=label0)
plt.plot(value1, hct_total1,'y-', label=label1)
plt.plot(value2, hct_total2,'g-', label=label2)
plt.plot(value3, hct_total3,'b.', label=label3)
plt.plot(value4, hct_total4,'r.', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Total Hct (%)', fontdict= font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
plt.show()
