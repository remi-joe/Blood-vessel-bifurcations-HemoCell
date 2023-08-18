#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Remigius J Selvaraj, MSc CFD, Cranfield Univeristy
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis
#
case0 = "/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/csv/"
case1 = "/home/remi/irp/simulation_files/case_files/D31.5_0_1/output_0/csv/"
case2 = "/home/remi/irp/simulation_files/case_files/D31.5_0_2/output_0/csv/"
case3 = "/home/remi/irp/simulation_files/case_files/D31.5_0_3/output_0/csv/"
case4 = "/home/remi/irp/simulation_files/case_files/D31.5_0_4/output_0/csv/"
#
output_dir = "/home/remi/Desktop/post_processing_images/hct/"
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
#
# Single Timestep size
dt = 6.25e-8
# Increment in data
inc = 10000
#
# Volume of the larger child vessel
vlc = 7.73*(31.5*10**(-6))**(3)

# Volume of the smaller child vessel
vsc = 3.215*(31.5*10**(-6))**(3)

# The total volume will change for the different cases and the parent vessels
# The volumes were calculated from the FreeCAD geometries

# #
##############################################################
################## INDIVIDUAL TUBE HEMATOCRIT #####################
##############################################################

################## Baseline ##################
os.chdir(case0)
#
# Timestep loop
#
value0 = []
for i in range(num_ts0):
    value = dt * i * inc
    value0.append(value)
#
# Total vessel volume 
tv_case0 = 19.635409190830046*(31.5*10**(-6))**(3)
#
# Parent Vessel Volume
pv_case0 = 8*(31.5*10**(-6))**(3)
#
hct_pv0 = [] # HCT of the parent vessel
hct_lv0 = [] # HCT of the larger vessel
hct_sv0 = [] # HCT of the smaller vessel
hct_rl0 = [] # HCT ratio of the larger and the parent vessels
hct_rs0 = [] # HCT ratio of the smaller and the parent vessels
hct_rls0 = [] # HCT ratio of the larger and the smaller vessels
hct_total0 = [] # Hct of the total domain
vel_mag_case0 = [] # RBC Velocity Magnitude total domain
vel_mag_pv_case0 = [] 
vel_mag_lv_case0 = []
vel_mag_sv_case0 = []
mean_vel_mag_ratio_lsv_case0 = []
mean_vel_mag_tot_case0 = []
mean_vel_mag_pv_case0 = []
mean_vel_mag_lv_case0 = []
mean_vel_mag_sv_case0 = []
rbc_num_tot_case0 = []
rbc_num_pv_case0 = []
rbc_num_lv_case0 = []
rbc_num_sv_case0 = []
y_dist_pv_case0 = []
y_dist_lv_case0 = []
y_dist_sv_case0 = []
#
for file in files0:
    csv0 = pd.read_csv(file) # Reading csv file in the list files0
    x0 = np.array(csv0["X"]) # storing the values in the column "X"
    y0 = np.array(csv0["Y"]) # storing the values in the column "X"
    case0_v = np.array(csv0["volume"]) # storing the values in the column "volume"
    vel_mag = np.sqrt( pow(np.array(csv0['velocity_x']),2) + pow(np.array(csv0['velocity_y']),2) + pow(np.array(csv0['velocity_z']),2) )
    # the following are conditions set for locating the RBC's in the parent and child vessels
    condition_pv0_1 = (x0 < 160.65e-6) # inlet section before the bifurcation
    condition_pv0_2 = (x0 > 551.565e-6) # outlet section after the bifurcation
    condition_lv0 = (x0 > 160.65e-6) & (x0 < 551.565e-6) & (y0 > 64.18e-6) # larger child vessel only
    condition_sv0 = (x0 > 160.65e-6) & (x0 < 551.565e-6) & (y0 < 64.18e-6) # smaller child vessel only
    #
    pv0_1 = case0_v[condition_pv0_1] 
    pv0_2 = case0_v[condition_pv0_2] 
    lv0 = case0_v[condition_lv0] 
    sv0 = case0_v[condition_sv0] 
    #
    hct_total0_single = sum(case0_v)/tv_case0 # Hct of the total tube
    hct_pv0_single = (sum(pv0_1) + sum(pv0_2))/pv_case0 # Hct of the inlet and outlet sections (parent)
    hct_lv0_single = sum(lv0)/vlc # Hct of the larger child vessel
    hct_sv0_single = sum(sv0)/vsc # Hct of the smaller child vessel
    hct_rl0_single = hct_lv0_single/hct_total0_single # Hct ratio of the Larger child vessel to total domain
    hct_rs0_single = hct_sv0_single/hct_total0_single # Hct ratio of the smaller child vessel to total domain
    hct_rls0_single = hct_rl0_single/hct_rs0_single # Hct ratio of the larger to smaller child vessels
    #
    hct_total0.append(hct_total0_single)
    hct_rl0.append(hct_rl0_single)
    hct_rs0.append(hct_rs0_single)
    hct_rls0.append(hct_rls0_single)
    hct_pv0.append(hct_pv0_single*100)
    hct_lv0.append(hct_lv0_single*100)
    hct_sv0.append(hct_sv0_single*100)
    #
    vel_mag_pv1_0 = vel_mag[condition_pv0_1]
    vel_mag_pv2_0 = vel_mag[condition_pv0_2]
    vel_mag_lv_0 = vel_mag[condition_lv0]
    vel_mag_sv_0 = vel_mag[condition_sv0]
    #
    vel_mag_case0.append(vel_mag)
    vel_mag_pv_case0.append(np.concatenate([vel_mag_pv1_0, vel_mag_pv2_0]))
    vel_mag_lv_case0.append(vel_mag_lv_0)
    vel_mag_sv_case0.append(vel_mag_sv_0)
    #
    mean_vel_mag_tot_single_case0 = sum(vel_mag)/len(vel_mag)
    mean_vel_mag_pv_single_case0 = (sum(vel_mag_pv1_0) + sum(vel_mag_pv2_0))/((len(vel_mag_pv1_0))+len(vel_mag_pv2_0))
    mean_vel_mag_lv_single_case0 = sum(vel_mag_lv_0)/len(vel_mag_lv_0)
    mean_vel_mag_sv_single_case0 = sum(vel_mag_sv_0)/len(vel_mag_sv_0)
    mean_vel_mag_ratio_lsv_single_case0 = mean_vel_mag_lv_single_case0/mean_vel_mag_sv_single_case0
    #
    mean_vel_mag_tot_case0.append(mean_vel_mag_tot_single_case0*1000)
    mean_vel_mag_pv_case0.append(mean_vel_mag_pv_single_case0*1000)
    mean_vel_mag_lv_case0.append(mean_vel_mag_lv_single_case0*1000)
    mean_vel_mag_sv_case0.append(mean_vel_mag_sv_single_case0*1000)
    mean_vel_mag_ratio_lsv_case0.append(mean_vel_mag_ratio_lsv_single_case0*1000)
    #
    rbc_num_tot_single_case0 = len(vel_mag)
    rbc_num_pv_single_case0 = len(vel_mag_pv1_0) + len(vel_mag_pv2_0)
    rbc_num_lv_single_case0 = len(vel_mag_lv_0)
    rbc_num_sv_single_case0 = len(vel_mag_sv_0)
    #
    rbc_num_tot_case0.append(rbc_num_tot_single_case0)
    rbc_num_pv_case0.append(rbc_num_pv_single_case0)
    rbc_num_lv_case0.append(rbc_num_lv_single_case0)
    rbc_num_sv_case0.append(rbc_num_sv_single_case0)
    #
    y_dist_pv_single_case0 = y0[condition_pv0_1]
    y_dist_lv_single_case0 = y0[condition_lv0]
    y_dist_sv_single_case0 = y0[condition_sv0]
    #
    y_dist_pv_case0.append(y_dist_pv_single_case0)
    y_dist_lv_case0.append(y_dist_lv_single_case0)
    y_dist_sv_case0.append(y_dist_sv_single_case0)
#
all_vel_mag_case0 = np.concatenate(vel_mag_case0)
all_vel_mag_pv_case0 = np.concatenate(vel_mag_pv_case0)
all_vel_mag_lv_case0 = np.concatenate(vel_mag_lv_case0)
all_vel_mag_sv_case0 = np.concatenate(vel_mag_sv_case0)
#
all_y_dist_pv_case0 = np.concatenate(y_dist_pv_case0)
all_y_dist_lv_case0 = np.concatenate(y_dist_lv_case0)
all_y_dist_sv_case0 = np.concatenate(y_dist_sv_case0)    
################ End of Baseline #############
#
################## Case1##################
os.chdir(case1)
#
# Timestep loop
value1 = []
for i in range(num_ts1):
    value = dt * i * inc
    value1.append(value)
#
# Total vessel volume 
tv_case1 = 19.53601425504993*(31.5*10**(-6))**(3)
#
# Parent Vessel Volume
pv_case1 = (8-(19.635409190830046-19.53601425504993))*(31.5*10**(-6))**(3)
#
hct_total1 = []# HCT_total
hct_pv1 = []
hct_lv1 = []
hct_sv1 = []
hct_rl1 = []
hct_rs1 = []
hct_rls1 = [] # HCT ratio of the larger and the smaller vessels
vel_mag_case1 = [] # RBC Velocity Magnitude total domain
vel_mag_pv_case1 = [] 
vel_mag_lv_case1 = []
vel_mag_sv_case1 = []
mean_vel_mag_ratio_lsv_case1 = []
mean_vel_mag_tot_case1 = []
mean_vel_mag_pv_case1 = []
mean_vel_mag_lv_case1 = []
mean_vel_mag_sv_case1 = []
rbc_num_tot_case1 = []
rbc_num_pv_case1 = []
rbc_num_lv_case1 = []
rbc_num_sv_case1 = []
y_dist_pv_case1 = []
y_dist_lv_case1 = []
y_dist_sv_case1 = []
#
for file in files1:
    csv1 = pd.read_csv(file)
    x1 = np.array(csv1["X"])
    y1 = np.array(csv1["Y"])
    case1_v = np.array(csv1["volume"])
    vel_mag = np.sqrt( pow(np.array(csv1['velocity_x']),2) + pow(np.array(csv1['velocity_y']),2) + pow(np.array(csv1['velocity_z']),2) )
    #
    condition_pv1_1 = (x1 < 160.65e-6)
    condition_pv1_2 = (x1 > 551.565e-6)
    condition_lv1 = (x1 > 160.65e-6) & (x1 < 551.565e-6) & (y1 > 64.18e-6)
    condition_sv1 = (x1 > 160.65e-6) & (x1 < 551.565e-6) & (y1 < 64.18e-6)
    #
    pv1_1 = case1_v[condition_pv1_1]
    pv1_2 = case1_v[condition_pv1_2]
    lv1 = case1_v[condition_lv1]
    sv1 = case1_v[condition_sv1]
    #
    hct_total1_single = sum(case1_v)/tv_case1
    hct_pv1_single = (sum(pv1_1) + sum(pv1_2))/pv_case1
    hct_lv1_single = sum(lv1)/vlc
    hct_sv1_single = sum(sv1)/vsc
    hct_rl1_single = hct_lv1_single/hct_total1_single
    hct_rs1_single = hct_sv1_single/hct_total1_single
    hct_rls1_single = hct_rl1_single/hct_rs1_single
    #
    hct_total1.append(hct_total1_single)
    hct_rl1.append(hct_rl1_single)
    hct_rs1.append(hct_rs1_single)
    hct_rls1.append(hct_rls1_single)
    hct_pv1.append(hct_pv1_single*100)
    hct_lv1.append(hct_lv1_single*100)
    hct_sv1.append(hct_sv1_single*100)
    #
    vel_mag_pv1_1 = vel_mag[condition_pv1_1]
    vel_mag_pv2_1 = vel_mag[condition_pv1_2]
    vel_mag_lv_1 = vel_mag[condition_lv1]
    vel_mag_sv_1 = vel_mag[condition_sv1]
    #
    vel_mag_case1.append(vel_mag)
    vel_mag_pv_case1.append(np.concatenate([vel_mag_pv1_1, vel_mag_pv2_1]))
    vel_mag_lv_case1.append(vel_mag_lv_1)
    vel_mag_sv_case1.append(vel_mag_sv_1)
    #
    mean_vel_mag_tot_single_case1 = sum(vel_mag)/len(vel_mag)
    mean_vel_mag_pv_single_case1 = (sum(vel_mag_pv1_1) + sum(vel_mag_pv2_1))/((len(vel_mag_pv1_1))+len(vel_mag_pv2_1))
    mean_vel_mag_lv_single_case1 = sum(vel_mag_lv_1)/len(vel_mag_lv_1)
    mean_vel_mag_sv_single_case1 = sum(vel_mag_sv_1)/len(vel_mag_sv_1)
    mean_vel_mag_ratio_lsv_single_case1 = mean_vel_mag_lv_single_case1/mean_vel_mag_sv_single_case1
    #
    mean_vel_mag_tot_case1.append(mean_vel_mag_tot_single_case1*1000)
    mean_vel_mag_pv_case1.append(mean_vel_mag_pv_single_case1*1000)
    mean_vel_mag_lv_case1.append(mean_vel_mag_lv_single_case1*1000)
    mean_vel_mag_sv_case1.append(mean_vel_mag_sv_single_case1*1000)
    mean_vel_mag_ratio_lsv_case1.append(mean_vel_mag_ratio_lsv_single_case1*1000)
    #
    rbc_num_tot_single_case1 = len(vel_mag)
    rbc_num_pv_single_case1 = len(vel_mag_pv1_1) + len(vel_mag_pv2_1)
    rbc_num_lv_single_case1 = len(vel_mag_lv_1)
    rbc_num_sv_single_case1 = len(vel_mag_sv_1)
    #
    rbc_num_tot_case1.append(rbc_num_tot_single_case1)
    rbc_num_pv_case1.append(rbc_num_pv_single_case1)
    rbc_num_lv_case1.append(rbc_num_lv_single_case1)
    rbc_num_sv_case1.append(rbc_num_sv_single_case1)
    #
    y_dist_pv_single_case1 = y1[condition_pv1_1]
    y_dist_lv_single_case1 = y1[condition_lv1]
    y_dist_sv_single_case1 = y1[condition_sv1]
    #
    y_dist_pv_case1.append(y_dist_pv_single_case1)
    y_dist_lv_case1.append(y_dist_lv_single_case1)
    y_dist_sv_case1.append(y_dist_sv_single_case1)
#
all_vel_mag_case1 = np.concatenate(vel_mag_case1)
all_vel_mag_pv_case1 = np.concatenate(vel_mag_pv_case1)
all_vel_mag_lv_case1 = np.concatenate(vel_mag_lv_case1)
all_vel_mag_sv_case1 = np.concatenate(vel_mag_sv_case1)
#
all_y_dist_pv_case1 = np.concatenate(y_dist_pv_case1)
all_y_dist_lv_case1 = np.concatenate(y_dist_lv_case1)
all_y_dist_sv_case1 = np.concatenate(y_dist_sv_case1)
#
################ End of Case1 #############
#
################## Case2 ##################
os.chdir(case2)
#
# Timestep loop
value2 = []
for i in range(num_ts2):
    value = dt * i * inc
    value2.append(value)
#
# Total vessel volume 
tv_case2 = 19.470052131408153*(31.5*10**(-6))**(3)
#
# Parent Vessel Volume
pv_case2 = (8-(19.635409190830046-19.470052131408153))*(31.5*10**(-6))**(3)
#
hct_total2 = [] # HCT_total
hct_pv2 = []
hct_lv2 = []
hct_sv2 = []
hct_rl2 = []
hct_rs2 = []
hct_rls2 = [] # HCT ratio of the larger and the smaller vessels
vel_mag_case2 = [] # RBC Velocity Magnitude total domain
vel_mag_pv_case2 = [] 
vel_mag_lv_case2 = []
vel_mag_sv_case2 = []
mean_vel_mag_ratio_lsv_case2 = []
mean_vel_mag_tot_case2 = []
mean_vel_mag_pv_case2 = []
mean_vel_mag_lv_case2 = []
mean_vel_mag_sv_case2 = []
rbc_num_tot_case2 = []
rbc_num_pv_case2 = []
rbc_num_lv_case2 = []
rbc_num_sv_case2 = []
y_dist_pv_case2 = []
y_dist_lv_case2 = []
y_dist_sv_case2 = []
#
for file in files2:
    csv2 = pd.read_csv(file)
    x2 = np.array(csv2["X"])
    y2 = np.array(csv2["Y"])
    case2_v = np.array(csv2["volume"])
    vel_mag = np.sqrt( pow(np.array(csv2['velocity_x']),2) + pow(np.array(csv2['velocity_y']),2) + pow(np.array(csv2['velocity_z']),2) )
    #
    condition_pv2_1 = (x2 < 160.65e-6)
    condition_pv2_2 = (x2 > 551.565e-6)
    condition_lv2 = (x2 > 160.65e-6) & (x2 < 551.565e-6) & (y2 > 64.18e-6)
    condition_sv2 = (x2 > 160.65e-6) & (x2 < 551.565e-6) & (y2 < 64.18e-6)
    #
    pv2_1 = case2_v[condition_pv2_1]
    pv2_2 = case2_v[condition_pv2_2]
    lv2 = case2_v[condition_lv2]
    sv2 = case2_v[condition_sv2]
    #
    hct_total2_single = sum(case2_v)/tv_case2
    hct_pv2_single = (sum(pv2_1) + sum(pv2_2))/pv_case2
    hct_lv2_single = sum(lv2)/vlc
    hct_sv2_single = sum(sv2)/vsc
    hct_rl2_single = hct_lv2_single/hct_total2_single
    hct_rs2_single = hct_sv2_single/hct_total2_single
    hct_rls2_single = hct_rl2_single/hct_rs2_single
    #
    hct_total2.append(hct_total2_single)
    hct_rl2.append(hct_rl2_single)
    hct_rs2.append(hct_rs2_single)
    hct_rls2.append(hct_rls2_single)
    hct_pv2.append(hct_pv2_single*100)
    hct_lv2.append(hct_lv2_single*100)
    hct_sv2.append(hct_sv2_single*100)
    #
    vel_mag_pv1_2 = vel_mag[condition_pv2_1]
    vel_mag_pv2_2 = vel_mag[condition_pv2_2]
    vel_mag_lv_2 = vel_mag[condition_lv2]
    vel_mag_sv_2 = vel_mag[condition_sv2]
    #
    vel_mag_case2.append(vel_mag)
    vel_mag_pv_case2.append(np.concatenate([vel_mag_pv1_2, vel_mag_pv2_2]))
    vel_mag_lv_case2.append(vel_mag_lv_2)
    vel_mag_sv_case2.append(vel_mag_sv_2)
    #
    mean_vel_mag_tot_single_case2 = sum(vel_mag)/len(vel_mag)
    mean_vel_mag_pv_single_case2 = (sum(vel_mag_pv1_2) + sum(vel_mag_pv2_2))/((len(vel_mag_pv1_2))+len(vel_mag_pv2_2))
    mean_vel_mag_lv_single_case2 = sum(vel_mag_lv_2)/len(vel_mag_lv_2)
    mean_vel_mag_sv_single_case2 = sum(vel_mag_sv_2)/len(vel_mag_sv_2)
    mean_vel_mag_ratio_lsv_single_case2 = mean_vel_mag_lv_single_case2/mean_vel_mag_sv_single_case2
    #
    mean_vel_mag_tot_case2.append(mean_vel_mag_tot_single_case2*1000)
    mean_vel_mag_pv_case2.append(mean_vel_mag_pv_single_case2*1000)
    mean_vel_mag_lv_case2.append(mean_vel_mag_lv_single_case2*1000)
    mean_vel_mag_sv_case2.append(mean_vel_mag_sv_single_case2*1000)
    mean_vel_mag_ratio_lsv_case2.append(mean_vel_mag_ratio_lsv_single_case2*1000)
    #
    rbc_num_tot_single_case2 = len(vel_mag)
    rbc_num_pv_single_case2 = len(vel_mag_pv1_2) + len(vel_mag_pv2_2)
    rbc_num_lv_single_case2 = len(vel_mag_lv_2)
    rbc_num_sv_single_case2 = len(vel_mag_sv_2)
    #
    rbc_num_tot_case2.append(rbc_num_tot_single_case2)
    rbc_num_pv_case2.append(rbc_num_pv_single_case2)
    rbc_num_lv_case2.append(rbc_num_lv_single_case2)
    rbc_num_sv_case2.append(rbc_num_sv_single_case2)
    #
    y_dist_pv_single_case2 = y2[condition_pv2_1]
    y_dist_lv_single_case2 = y2[condition_lv2]
    y_dist_sv_single_case2 = y2[condition_sv2]
    #
    y_dist_pv_case2.append(y_dist_pv_single_case2)
    y_dist_lv_case2.append(y_dist_lv_single_case2)
    y_dist_sv_case2.append(y_dist_sv_single_case2)
#
all_vel_mag_case2 = np.concatenate(vel_mag_case2)
all_vel_mag_pv_case2 = np.concatenate(vel_mag_pv_case2)
all_vel_mag_lv_case2 = np.concatenate(vel_mag_lv_case2)
all_vel_mag_sv_case2 = np.concatenate(vel_mag_sv_case2)
#
all_y_dist_pv_case2 = np.concatenate(y_dist_pv_case2)
all_y_dist_lv_case2 = np.concatenate(y_dist_lv_case2)
all_y_dist_sv_case2 = np.concatenate(y_dist_sv_case2)
#
################ End of Case2 #############
#
################## Case3 ##################
os.chdir(case3)
#
# Timestep loop
value3 = []
for i in range(num_ts3):
    value = dt * i * inc
    value3.append(value)
#
# Total vessel volume 
tv_case3 = 19.468457539339216*(31.5*10**(-6))**(3)
#
# Parent Vessel Volume
pv_case3 = (8-(19.635409190830046-19.468457539339216))*(31.5*10**(-6))**(3)
#
hct_total3 = [] # HCT_total
hct_pv3 = []
hct_lv3 = []
hct_sv3 = []
hct_rl3 = []
hct_rs3 = []
hct_rls3 = [] # HCT ratio of the larger and the smaller vessels
vel_mag_case3 = [] # RBC Velocity Magnitude total domain
vel_mag_pv_case3 = [] 
vel_mag_lv_case3 = []
vel_mag_sv_case3 = []
mean_vel_mag_ratio_lsv_case3 = []
mean_vel_mag_tot_case3 = []
mean_vel_mag_pv_case3 = []
mean_vel_mag_lv_case3 = []
mean_vel_mag_sv_case3 = []
rbc_num_tot_case3 = []
rbc_num_pv_case3 = []
rbc_num_lv_case3 = []
rbc_num_sv_case3 = []
y_dist_pv_case3 = []
y_dist_lv_case3 = []
y_dist_sv_case3 = []
#
for file in files3:
    csv3 = pd.read_csv(file)
    x3 = np.array(csv3["X"])
    y3 = np.array(csv3["Y"])
    case3_v = np.array(csv3["volume"])
    vel_mag = np.sqrt( pow(np.array(csv3['velocity_x']),2) + pow(np.array(csv3['velocity_y']),2) + pow(np.array(csv3['velocity_z']),2) )
    #
    condition_pv3_1 = (x3 < 160.65e-6)
    condition_pv3_2 = (x3 > 551.565e-6)
    condition_lv3 = (x3 > 160.65e-6) & (x3 < 551.565e-6) & (y3 > 64.18e-6)
    condition_sv3 = (x3 > 160.65e-6) & (x3 < 551.565e-6) & (y3 < 64.18e-6)
    #
    pv3_1 = case3_v[condition_pv3_1]
    pv3_2 = case3_v[condition_pv3_2]
    lv3 = case3_v[condition_lv3]
    sv3 = case3_v[condition_sv3]
    #
    hct_total3_single = sum(case3_v)/tv_case3
    hct_pv3_single = (sum(pv3_1) + sum(pv3_2))/pv_case3
    hct_lv3_single = sum(lv3)/vlc
    hct_sv3_single = sum(sv3)/vsc
    hct_rl3_single = hct_lv3_single/hct_total3_single
    hct_rs3_single = hct_sv3_single/hct_total3_single
    hct_rls3_single = hct_rl3_single/hct_rs3_single
    #
    hct_total3.append(hct_total3_single)
    hct_rl3.append(hct_rl3_single)
    hct_rs3.append(hct_rs3_single)
    hct_rls3.append(hct_rls3_single)
    hct_pv3.append(hct_pv3_single*100)
    hct_lv3.append(hct_lv3_single*100)
    hct_sv3.append(hct_sv3_single*100)
    #
    vel_mag_pv1_3 = vel_mag[condition_pv3_1]
    vel_mag_pv2_3 = vel_mag[condition_pv3_2]
    vel_mag_lv_3 = vel_mag[condition_lv3]
    vel_mag_sv_3 = vel_mag[condition_sv3]
    #
    vel_mag_case3.append(vel_mag)
    vel_mag_pv_case3.append(np.concatenate([vel_mag_pv1_3, vel_mag_pv2_3]))
    vel_mag_lv_case3.append(vel_mag_lv_3)
    vel_mag_sv_case3.append(vel_mag_sv_3)
    #
    mean_vel_mag_tot_single_case3 = sum(vel_mag)/len(vel_mag)
    mean_vel_mag_pv_single_case3 = (sum(vel_mag_pv1_3) + sum(vel_mag_pv2_3))/((len(vel_mag_pv1_3))+len(vel_mag_pv2_3))
    mean_vel_mag_lv_single_case3 = sum(vel_mag_lv_3)/len(vel_mag_lv_3)
    mean_vel_mag_sv_single_case3 = sum(vel_mag_sv_3)/len(vel_mag_sv_3)
    mean_vel_mag_ratio_lsv_single_case3 = mean_vel_mag_lv_single_case3/mean_vel_mag_sv_single_case3
    #
    mean_vel_mag_tot_case3.append(mean_vel_mag_tot_single_case3*1000)
    mean_vel_mag_pv_case3.append(mean_vel_mag_pv_single_case3*1000)
    mean_vel_mag_lv_case3.append(mean_vel_mag_lv_single_case3*1000)
    mean_vel_mag_sv_case3.append(mean_vel_mag_sv_single_case3*1000)
    mean_vel_mag_ratio_lsv_case3.append(mean_vel_mag_ratio_lsv_single_case3*1000)
    #
    rbc_num_tot_single_case3 = len(vel_mag)
    rbc_num_pv_single_case3 = len(vel_mag_pv1_3) + len(vel_mag_pv2_3)
    rbc_num_lv_single_case3 = len(vel_mag_lv_3)
    rbc_num_sv_single_case3 = len(vel_mag_sv_3)
    #
    rbc_num_tot_case3.append(rbc_num_tot_single_case3)
    rbc_num_pv_case3.append(rbc_num_pv_single_case3)
    rbc_num_lv_case3.append(rbc_num_lv_single_case3)
    rbc_num_sv_case3.append(rbc_num_sv_single_case3)
    #
    y_dist_pv_single_case3 = y3[condition_pv3_1]
    y_dist_lv_single_case3 = y3[condition_lv3]
    y_dist_sv_single_case3 = y3[condition_sv3]
    #
    y_dist_pv_case3.append(y_dist_pv_single_case3)
    y_dist_lv_case3.append(y_dist_lv_single_case3)
    y_dist_sv_case3.append(y_dist_sv_single_case3)
#
all_vel_mag_case3 = np.concatenate(vel_mag_case3)
all_vel_mag_pv_case3 = np.concatenate(vel_mag_pv_case3)
all_vel_mag_lv_case3 = np.concatenate(vel_mag_lv_case3)
all_vel_mag_sv_case3 = np.concatenate(vel_mag_sv_case3)
#
all_y_dist_pv_case3 = np.concatenate(y_dist_pv_case3)
all_y_dist_lv_case3 = np.concatenate(y_dist_lv_case3)
all_y_dist_sv_case3 = np.concatenate(y_dist_sv_case3)
#
################ End of Case3 #############
#
################## Case4 ##################
os.chdir(case4)
#
# Timestep loop
value4 = []
for i in range(num_ts4):
    value = dt * i * inc
    value4.append(value)
#
# Total vessel volume 
tv_case4 = 19.497669294100692*(31.5*10**(-6))**(3)
#
# Parent Vessel Volume
pv_case4 = (8-(19.635409190830046-19.497669294100692))*(31.5*10**(-6))**(3)
#
hct_total4 = [] # HCT_total
hct_pv4 = []
hct_lv4 = []
hct_sv4 = []
hct_rl4 = []
hct_rs4 = []
hct_rls4 = [] # HCT ratio of the larger and the smaller vessels
vel_mag_case4 = [] # RBC Velocity Magnitude total domain
vel_mag_pv_case4 = [] 
vel_mag_lv_case4 = []
vel_mag_sv_case4 = []
mean_vel_mag_ratio_lsv_case4 = []
mean_vel_mag_tot_case4 = []
mean_vel_mag_pv_case4 = []
mean_vel_mag_lv_case4 = []
mean_vel_mag_sv_case4 = []
rbc_num_tot_case4 = []
rbc_num_pv_case4 = []
rbc_num_lv_case4 = []
rbc_num_sv_case4 = []
y_dist_pv_case4 = []
y_dist_lv_case4 = []
y_dist_sv_case4 = []
#
for file in files4:
    csv4 = pd.read_csv(file)
    x4 = np.array(csv4["X"])
    y4 = np.array(csv4["Y"])
    case4_v = np.array(csv4["volume"])
    vel_mag = np.sqrt( pow(np.array(csv4['velocity_x']),2) + pow(np.array(csv4['velocity_y']),2) + pow(np.array(csv4['velocity_z']),2) )
    #
    condition_pv4_1 = (x4 < 160.65e-6)
    condition_pv4_2 = (x4 > 551.565e-6)
    condition_lv4 = (x4 > 160.65e-6) & (x4 < 551.565e-6) & (y4 > 64.18e-6)
    condition_sv4 = (x4 > 160.65e-6) & (x4 < 551.565e-6) & (y4 < 64.18e-6)
    #
    pv4_1 = case4_v[condition_pv4_1]
    pv4_2 = case4_v[condition_pv4_2]
    lv4 = case4_v[condition_lv4]
    sv4 = case4_v[condition_sv4]
    #
    hct_total4_single = sum(case4_v)/tv_case4
    hct_pv4_single = (sum(pv4_1) + sum(pv4_2))/pv_case4
    hct_lv4_single = sum(lv4)/vlc
    hct_sv4_single = sum(sv4)/vsc
    hct_rl4_single = hct_lv4_single/hct_total4_single
    hct_rs4_single = hct_sv4_single/hct_total4_single
    hct_rls4_single = hct_rl4_single/hct_rs4_single
    #
    hct_total4.append(hct_total4_single)
    hct_rls4.append(hct_rls4_single)
    hct_rl4.append(hct_rl4_single)
    hct_rs4.append(hct_rs4_single)
    hct_pv4.append(hct_pv4_single*100)
    hct_lv4.append(hct_lv4_single*100)
    hct_sv4.append(hct_sv4_single*100)
    #
    vel_mag_pv1_4 = vel_mag[condition_pv4_1]
    vel_mag_pv2_4 = vel_mag[condition_pv4_2]
    vel_mag_lv_4 = vel_mag[condition_lv4]
    vel_mag_sv_4 = vel_mag[condition_sv4]
    #
    vel_mag_case4.append(vel_mag)
    vel_mag_pv_case4.append(np.concatenate([vel_mag_pv1_4, vel_mag_pv2_4]))
    vel_mag_lv_case4.append(vel_mag_lv_4)
    vel_mag_sv_case4.append(vel_mag_sv_4)
    #
    mean_vel_mag_tot_single_case4 = sum(vel_mag)/len(vel_mag)
    mean_vel_mag_pv_single_case4 = (sum(vel_mag_pv1_4) + sum(vel_mag_pv2_4))/((len(vel_mag_pv1_4))+len(vel_mag_pv2_4))
    mean_vel_mag_lv_single_case4 = sum(vel_mag_lv_4)/len(vel_mag_lv_4)
    mean_vel_mag_sv_single_case4 = sum(vel_mag_sv_4)/len(vel_mag_sv_4)
    mean_vel_mag_ratio_lsv_single_case4 = mean_vel_mag_lv_single_case4/mean_vel_mag_sv_single_case4
    #
    mean_vel_mag_tot_case4.append(mean_vel_mag_tot_single_case4*1000)
    mean_vel_mag_pv_case4.append(mean_vel_mag_pv_single_case4*1000)
    mean_vel_mag_lv_case4.append(mean_vel_mag_lv_single_case4*1000)
    mean_vel_mag_sv_case4.append(mean_vel_mag_sv_single_case4*1000)
    mean_vel_mag_ratio_lsv_case4.append(mean_vel_mag_ratio_lsv_single_case4*1000)
    #
    rbc_num_tot_single_case4 = len(vel_mag)
    rbc_num_pv_single_case4 = len(vel_mag_pv1_4) + len(vel_mag_pv2_4)
    rbc_num_lv_single_case4 = len(vel_mag_lv_4)
    rbc_num_sv_single_case4 = len(vel_mag_sv_4)
    #
    rbc_num_tot_case4.append(rbc_num_tot_single_case4)
    rbc_num_pv_case4.append(rbc_num_pv_single_case4)
    rbc_num_lv_case4.append(rbc_num_lv_single_case4)
    rbc_num_sv_case4.append(rbc_num_sv_single_case4)
    #
    y_dist_pv_single_case4 = y4[condition_pv4_1]
    y_dist_lv_single_case4 = y4[condition_lv4]
    y_dist_sv_single_case4 = y4[condition_sv4]
    #
    y_dist_pv_case4.append(y_dist_pv_single_case4)
    y_dist_lv_case4.append(y_dist_lv_single_case4)
    y_dist_sv_case4.append(y_dist_sv_single_case4)
#
all_vel_mag_case4 = np.concatenate(vel_mag_case4)
all_vel_mag_pv_case4 = np.concatenate(vel_mag_pv_case4)
all_vel_mag_lv_case4 = np.concatenate(vel_mag_lv_case4)
all_vel_mag_sv_case4 = np.concatenate(vel_mag_sv_case4)
#
all_y_dist_pv_case4 = np.concatenate(y_dist_pv_case4)
all_y_dist_lv_case4 = np.concatenate(y_dist_lv_case4)
all_y_dist_sv_case4 = np.concatenate(y_dist_sv_case4)
#
################ End of Case4 #############
#
################ STATISTICAL MOMENTS FOR EACH CASE ##################
#
############### BASELINE ##############
### TOTAL DOMAIN
mean_value_vel_mag_case0 = np.mean(all_vel_mag_case0*1000)
std_dev_vel_mag_case0 = np.std(all_vel_mag_case0*1000)
data_skewness_vel_mag_case0 = skew(all_vel_mag_case0*1000)
data_kurtosis_vel_mag_case0 = kurtosis(all_vel_mag_case0*1000)
### PARENT VESSEL
mean_value_vel_mag_pv_case0 = np.mean(all_vel_mag_pv_case0*1000)
std_dev_vel_mag_pv_case0 = np.std(all_vel_mag_pv_case0*1000)
data_skewness_vel_mag_pv_case0 = skew(all_vel_mag_pv_case0*1000)
data_kurtosis_vel_mag_pv_case0 = kurtosis(all_vel_mag_pv_case0*1000)
### LARGER VESSEL
mean_value_vel_mag_lv_case0 = np.mean(all_vel_mag_lv_case0*1000)
std_dev_vel_mag_lv_case0 = np.std(all_vel_mag_lv_case0*1000)
data_skewness_vel_mag_lv_case0 = skew(all_vel_mag_lv_case0*1000)
data_kurtosis_vel_mag_lv_case0 = kurtosis(all_vel_mag_lv_case0*1000)
### SMALLER VESSEL
mean_value_vel_mag_sv_case0 = np.mean(all_vel_mag_sv_case0*1000)
std_dev_vel_mag_sv_case0 = np.std(all_vel_mag_sv_case0*1000)
data_skewness_vel_mag_sv_case0 = skew(all_vel_mag_sv_case0*1000)
data_kurtosis_vel_mag_sv_case0 = kurtosis(all_vel_mag_sv_case0*1000)
############ END OF BASELINE ############
#
############### CASE1 ##############
### TOTAL DOMAIN
mean_value_vel_mag_case1 = np.mean(all_vel_mag_case1*1000)
std_dev_vel_mag_case1 = np.std(all_vel_mag_case1*1000)
data_skewness_vel_mag_case1 = skew(all_vel_mag_case1*1000)
data_kurtosis_vel_mag_case1 = kurtosis(all_vel_mag_case1*1000)
### PARENT VESSEL
mean_value_vel_mag_pv_case1 = np.mean(all_vel_mag_pv_case1*1000)
std_dev_vel_mag_pv_case1 = np.std(all_vel_mag_pv_case1*1000)
data_skewness_vel_mag_pv_case1 = skew(all_vel_mag_pv_case1*1000)
data_kurtosis_vel_mag_pv_case1 = kurtosis(all_vel_mag_pv_case1*1000)
### LARGER VESSEL
mean_value_vel_mag_lv_case1 = np.mean(all_vel_mag_lv_case1*1000)
std_dev_vel_mag_lv_case1 = np.std(all_vel_mag_lv_case1*1000)
data_skewness_vel_mag_lv_case1 = skew(all_vel_mag_lv_case1*1000)
data_kurtosis_vel_mag_lv_case1 = kurtosis(all_vel_mag_lv_case1*1000)
### SMALLER VESSEL
mean_value_vel_mag_sv_case1 = np.mean(all_vel_mag_sv_case1*1000)
std_dev_vel_mag_sv_case1 = np.std(all_vel_mag_sv_case1*1000)
data_skewness_vel_mag_sv_case1 = skew(all_vel_mag_sv_case1*1000)
data_kurtosis_vel_mag_sv_case1 = kurtosis(all_vel_mag_sv_case1*1000)
############ END OF CASE1 ############
#
############### CASE2 ##############
### TOTAL DOMAIN
mean_value_vel_mag_case2 = np.mean(all_vel_mag_case2*1000)
std_dev_vel_mag_case2 = np.std(all_vel_mag_case2*1000)
data_skewness_vel_mag_case2 = skew(all_vel_mag_case2*1000)
data_kurtosis_vel_mag_case2 = kurtosis(all_vel_mag_case2*1000)
### PARENT VESSEL
mean_value_vel_mag_pv_case2 = np.mean(all_vel_mag_pv_case2*1000)
std_dev_vel_mag_pv_case2 = np.std(all_vel_mag_pv_case2*1000)
data_skewness_vel_mag_pv_case2 = skew(all_vel_mag_pv_case2*1000)
data_kurtosis_vel_mag_pv_case2 = kurtosis(all_vel_mag_pv_case2*1000)
### LARGER VESSEL
mean_value_vel_mag_lv_case2 = np.mean(all_vel_mag_lv_case2*1000)
std_dev_vel_mag_lv_case2 = np.std(all_vel_mag_lv_case2*1000)
data_skewness_vel_mag_lv_case2 = skew(all_vel_mag_lv_case2*1000)
data_kurtosis_vel_mag_lv_case2 = kurtosis(all_vel_mag_lv_case2*1000)
### SMALLER VESSEL
mean_value_vel_mag_sv_case2 = np.mean(all_vel_mag_sv_case2*1000)
std_dev_vel_mag_sv_case2 = np.std(all_vel_mag_sv_case2*1000)
data_skewness_vel_mag_sv_case2 = skew(all_vel_mag_sv_case2*1000)
data_kurtosis_vel_mag_sv_case2 = kurtosis(all_vel_mag_sv_case2*1000)
############ END OF CASE2 ############
#
############### CASE3 ##############
### TOTAL DOMAIN
mean_value_vel_mag_case3 = np.mean(all_vel_mag_case3*1000)
std_dev_vel_mag_case3 = np.std(all_vel_mag_case3*1000)
data_skewness_vel_mag_case3 = skew(all_vel_mag_case3*1000)
data_kurtosis_vel_mag_case3 = kurtosis(all_vel_mag_case3*1000)
### PARENT VESSEL
mean_value_vel_mag_pv_case3 = np.mean(all_vel_mag_pv_case3*1000)
std_dev_vel_mag_pv_case3 = np.std(all_vel_mag_pv_case3*1000)
data_skewness_vel_mag_pv_case3 = skew(all_vel_mag_pv_case3*1000)
data_kurtosis_vel_mag_pv_case3 = kurtosis(all_vel_mag_pv_case3*1000)
### LARGER VESSEL
mean_value_vel_mag_lv_case3 = np.mean(all_vel_mag_lv_case3*1000)
std_dev_vel_mag_lv_case3 = np.std(all_vel_mag_lv_case3*1000)
data_skewness_vel_mag_lv_case3 = skew(all_vel_mag_lv_case3*1000)
data_kurtosis_vel_mag_lv_case3 = kurtosis(all_vel_mag_lv_case3*1000)
### SMALLER VESSEL
mean_value_vel_mag_sv_case3 = np.mean(all_vel_mag_sv_case3*1000)
std_dev_vel_mag_sv_case3 = np.std(all_vel_mag_sv_case3*1000)
data_skewness_vel_mag_sv_case3 = skew(all_vel_mag_sv_case3*1000)
data_kurtosis_vel_mag_sv_case3 = kurtosis(all_vel_mag_sv_case3*1000)
############ END OF CASE3 ############
#
############### CASE4 ##############
### TOTAL DOMAIN
mean_value_vel_mag_case4 = np.mean(all_vel_mag_case4*1000)
std_dev_vel_mag_case4 = np.std(all_vel_mag_case4*1000)
data_skewness_vel_mag_case4 = skew(all_vel_mag_case4*1000)
data_kurtosis_vel_mag_case4 = kurtosis(all_vel_mag_case4*1000)
### PARENT VESSEL
mean_value_vel_mag_pv_case4 = np.mean(all_vel_mag_pv_case4*1000)
std_dev_vel_mag_pv_case4 = np.std(all_vel_mag_pv_case4*1000)
data_skewness_vel_mag_pv_case4 = skew(all_vel_mag_pv_case4*1000)
data_kurtosis_vel_mag_pv_case4 = kurtosis(all_vel_mag_pv_case4*1000)
### LARGER VESSEL
mean_value_vel_mag_lv_case4 = np.mean(all_vel_mag_lv_case4*1000)
std_dev_vel_mag_lv_case4 = np.std(all_vel_mag_lv_case4*1000)
data_skewness_vel_mag_lv_case4 = skew(all_vel_mag_lv_case4*1000)
data_kurtosis_vel_mag_lv_case4 = kurtosis(all_vel_mag_lv_case4*1000)
### SMALLER VESSEL
mean_value_vel_mag_sv_case4 = np.mean(all_vel_mag_sv_case4*1000)
std_dev_vel_mag_sv_case4 = np.std(all_vel_mag_sv_case4*1000)
data_skewness_vel_mag_sv_case4 = skew(all_vel_mag_sv_case4*1000)
data_kurtosis_vel_mag_sv_case4 = kurtosis(all_vel_mag_sv_case4*1000)
############ END OF CASE4 ############
#
################ END OF STATISTICS #########################
#
################ LABELS ################
label0 = "Baseline" 
label1 = "case1" 
label2 = "case2" 
label3 = "case3" 
label4 = "case4" 
# 
# FONT
font = {'family': 'sans-serif', 'color': 'black', 'weight': 'normal', 'size': 18}  
# #
# ############### PLOTS - TOTAL TUBE HCT ##################   
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_total0,'k-', label=label0)
# plt.plot(value1, hct_total1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_total2,'g--', label=label2)
# plt.plot(value3, hct_total3,'b:', label=label3)
# plt.plot(value4, hct_total4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Total Hct (%)', fontdict= font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "total_hct" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS PARENT VESSEL ################## 
# #     
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_pv0,'k-', label=label0)
# plt.plot(value1, hct_pv1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_pv2,'g--', label=label2)
# plt.plot(value3, hct_pv3,'b:', label=label3)
# plt.plot(value4, hct_pv4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct (%)', fontdict= font)
# plt.title("Parent Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "parent_hct" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS LARGER VESSEL ##################      
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_lv0, "k-",label=label0)
# plt.plot(value1, hct_lv1, ".-",color='#9467bd',label=label1)
# plt.plot(value2, hct_lv2, "g--",label=label2)
# plt.plot(value3, hct_lv3, "b:",label=label3)
# plt.plot(value4, hct_lv4, "r",label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct (%)', fontdict= font)
# plt.title("Larger Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "larger_vessel_hct" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS SMALLER VESSEL ################## 
# #     
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_sv0,'k-', label=label0)
# plt.plot(value1, hct_sv1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_sv2,'g--', label=label2)
# plt.plot(value3, hct_sv3,'b:', label=label3)
# plt.plot(value4, hct_sv4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct (%)', fontdict= font)
# plt.title("Smaller Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "smaller_veesel_hct" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS Hct RATIO LARGER VESSEL ################## 
# #     
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_rl0,'k-', label=label0)
# plt.plot(value1, hct_rl1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_rl2,'g--', label=label2)
# plt.plot(value3, hct_rl3,'b:', label=label3)
# plt.plot(value4, hct_rl4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct Ratio', fontdict= font)
# plt.title("Larger Child Vessel to Total Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "hct_ratio_larger_vessel" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS Hct RATIO SMALLER VESSEL ################## 
# #     
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_rs0,'k-', label=label0)
# plt.plot(value1, hct_rs1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_rs2,'g--', label=label2)
# plt.plot(value3, hct_rs3,'b:', label=label3)
# plt.plot(value4, hct_rs4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct Ratio', fontdict= font)
# plt.title("Smaller Child Vessel to Total Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "hct_ratio_smaller_vessel" + ".png", dpi = 300)
# #
# plt.show()
# #
# ############### PLOTS Hct RATIO LARGER v SMALLER VESSEL ################## 
# #     
# plt.figure(figsize=(10,7))
# plt.plot(value0, hct_rls0,'k-', label=label0)
# plt.plot(value1, hct_rls1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, hct_rls2,'g--', label=label2)
# plt.plot(value3, hct_rls3,'b:', label=label3)
# plt.plot(value4, hct_rls4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('Hct Ratio', fontdict= font)
# plt.title("Larger to Smaller Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "hct_ratio_largerandsmaller_vessel" + ".png", dpi = 300)
# #
# plt.show()

# ################################################################################
# ########################## HISTOGRAM AND DENSITY PLOTS #########################
# ################################################################################

# ########################### VELOCITY ###############################

# ############# BASELINE AND CASE 1 ################

# ###### Total domain
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_case1 * 1000, bins=25, alpha = 0.5, label=label1)
# plt.hist(all_vel_mag_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_case1 + std_dev_vel_mag_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_case1 - std_dev_vel_mag_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case1', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_total_bv1" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_case1 * 1000, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_case1 + std_dev_vel_mag_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_case1 - std_dev_vel_mag_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case1", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_total_bv1" + ".png", dpi = 300)
# #
# plt.show()

# ###### Parent Vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_pv_case1 * 1000, bins=25, alpha = 0.5, label=label1)
# plt.hist(all_vel_mag_pv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case1 - Parent Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend([label0, label1])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_pv_bv1" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_pv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_pv_case1 * 1000, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case1 - Parent vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_pv_bv1" + ".png", dpi = 300)
# #
# plt.show()

# ##### Larger vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_lv_case1 * 1000, bins=25, alpha = 0.5, label=label1)
# plt.hist(all_vel_mag_lv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_lv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_lv_case1 + std_dev_vel_mag_lv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_lv_case1 - std_dev_vel_mag_lv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case1 - Larger Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend([label0, label1])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_lv_bv1" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_lv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_lv_case1 * 1000, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_lv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_lv_case1 + std_dev_vel_mag_lv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_lv_case1 - std_dev_vel_mag_lv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case1 - Larger Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_lv_bv1" + ".png", dpi = 300)
# #
# plt.show()

# ##### Smaller vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_sv_case1 * 1000, bins=25, alpha = 0.5, label=label1)
# plt.hist(all_vel_mag_sv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_sv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_sv_case1 + std_dev_vel_mag_sv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_sv_case1 - std_dev_vel_mag_sv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case1 - Smaller Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend([label0, label1])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_sv_bv1" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_sv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_sv_case1 * 1000, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_sv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_sv_case1 + std_dev_vel_mag_sv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_sv_case1 - std_dev_vel_mag_sv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case1 - Smaller Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_sv_bv1" + ".png", dpi = 300)
# #
# plt.show()
# ######################## end of Baseline vs case1 ##############

# ############# BASELINE AND CASE 2 ################

# ###### Total domain
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_case2 * 1000, bins=25, alpha = 0.5, label=label2)
# plt.hist(all_vel_mag_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_case2 + std_dev_vel_mag_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_case2 - std_dev_vel_mag_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case2, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case2, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case2', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_total_bv2" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_case2 * 1000, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_case2 + std_dev_vel_mag_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_case2 - std_dev_vel_mag_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case2", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_total_bv2" + ".png", dpi = 300)
# #
# plt.show()

# ###### Parent Vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_pv_case2 * 1000, bins=25, alpha = 0.5, label=label2)
# plt.hist(all_vel_mag_pv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_pv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_pv_case2 + std_dev_vel_mag_pv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_pv_case2 - std_dev_vel_mag_pv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case2 - Parent Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_pv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_pv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_pv_case2 * 1000, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_pv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_pv_case2 + std_dev_vel_mag_pv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_pv_case2 - std_dev_vel_mag_pv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case2 - Parent vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_pv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# ##### Larger vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_lv_case2 * 1000, bins=25, alpha = 0.5, label=label2)
# plt.hist(all_vel_mag_lv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_lv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_lv_case2 + std_dev_vel_mag_lv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_lv_case2 - std_dev_vel_mag_lv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case2 - Larger Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_lv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_lv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_lv_case2 * 1000, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_lv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_lv_case2 + std_dev_vel_mag_lv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_lv_case2 - std_dev_vel_mag_lv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case2 - Larger Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_lv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# ##### Smaller vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_sv_case2 * 1000, bins=25, alpha = 0.5, label=label2)
# plt.hist(all_vel_mag_sv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_sv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_sv_case2 + std_dev_vel_mag_sv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_sv_case2 - std_dev_vel_mag_sv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case2 - Smaller Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_sv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_sv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_sv_case2 * 1000, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 2
# plt.axvline(mean_value_vel_mag_sv_case2, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case2')
# plt.axvline(mean_value_vel_mag_sv_case2 + std_dev_vel_mag_sv_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case2')
# plt.axvline(mean_value_vel_mag_sv_case2 - std_dev_vel_mag_sv_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case2')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case2 - Smaller Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_sv_bv2" + ".png", dpi = 300)
# #
# plt.show()

# ############### END OF BASELINE AND CASE 2 ###############################
# #
# ############# BASELINE AND CASE 3 ################

# ###### Total domain
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_case3 * 1000, bins=25, alpha = 0.5, label=label3)
# plt.hist(all_vel_mag_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_case3 + std_dev_vel_mag_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_case3 - std_dev_vel_mag_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case2, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case2, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case3', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_total_bv3" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_case3 * 1000, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_case3 + std_dev_vel_mag_case2, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_case3 - std_dev_vel_mag_case2, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case3", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_total_bv3" + ".png", dpi = 300)
# #
# plt.show()

# ###### Parent Vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_pv_case3 * 1000, bins=25, alpha = 0.5, label=label3)
# plt.hist(all_vel_mag_pv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_pv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_pv_case3 + std_dev_vel_mag_pv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_pv_case3 - std_dev_vel_mag_pv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case3 - Parent Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_pv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_pv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_pv_case2 * 1000, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_pv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_pv_case3 + std_dev_vel_mag_pv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_pv_case3 - std_dev_vel_mag_pv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case3 - Parent vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_pv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# ##### Larger vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_lv_case3 * 1000, bins=25, alpha = 0.5, label=label3)
# plt.hist(all_vel_mag_lv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_lv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_lv_case3 + std_dev_vel_mag_lv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_lv_case3 - std_dev_vel_mag_lv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case3 - Larger Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_lv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_lv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_lv_case2 * 1000, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_lv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_lv_case3 + std_dev_vel_mag_lv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_lv_case3 - std_dev_vel_mag_lv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case3 - Larger Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_lv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# ##### Smaller vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_sv_case3 * 1000, bins=25, alpha = 0.5, label=label3)
# plt.hist(all_vel_mag_sv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_sv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_sv_case3 + std_dev_vel_mag_sv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_sv_case3 - std_dev_vel_mag_sv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case3 - Smaller Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_sv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_sv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_sv_case3 * 1000, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_sv_case3, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case3')
# plt.axvline(mean_value_vel_mag_sv_case3 + std_dev_vel_mag_sv_case3, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case3')
# plt.axvline(mean_value_vel_mag_sv_case3 - std_dev_vel_mag_sv_case3, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case3')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case3 - Smaller Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_sv_bv3" + ".png", dpi = 300)
# #
# plt.show()

# ############### END OF BASELINE AND CASE 3 ###############################
# #
# ############# BASELINE AND CASE 4 ################

# ###### Total domain
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_case4 * 1000, bins=25, alpha = 0.5, label=label4)
# plt.hist(all_vel_mag_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 4
# plt.axvline(mean_value_vel_mag_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_case4 + std_dev_vel_mag_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_case4 - std_dev_vel_mag_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case2, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case2, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case4', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_total_bv4" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_case4 * 1000, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_case0 + std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_case0 - std_dev_vel_mag_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_case4 + std_dev_vel_mag_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_case4 - std_dev_vel_mag_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
# plt.title("Baseline vs Case4", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_total_bv4" + ".png", dpi = 300)
# #
# plt.show()

# ###### Parent Vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_pv_case4 * 1000, bins=25, alpha = 0.5, label=label4)
# plt.hist(all_vel_mag_pv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_pv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_pv_case4 + std_dev_vel_mag_pv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_pv_case4 - std_dev_vel_mag_pv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case4 - Parent Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_pv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_pv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_pv_case4 * 1000, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_pv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_pv_case4 + std_dev_vel_mag_pv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_pv_case4 - std_dev_vel_mag_pv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case3 - Parent vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_pv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# ##### Larger vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_lv_case4 * 1000, bins=25, alpha = 0.5, label=label4)
# plt.hist(all_vel_mag_lv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 4
# plt.axvline(mean_value_vel_mag_lv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_lv_case4 + std_dev_vel_mag_lv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_lv_case4 - std_dev_vel_mag_lv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case4 - Larger Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_lv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_lv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_lv_case4 * 1000, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_lv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_lv_case0 + std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_lv_case0 - std_dev_vel_mag_lv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 4
# plt.axvline(mean_value_vel_mag_lv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_lv_case4 + std_dev_vel_mag_lv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_lv_case4 - std_dev_vel_mag_lv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case4 - Larger Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_lv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# ##### Smaller vessel
# # Plot the histogram
# plt.figure(figsize=(10, 7))
# plt.hist(all_vel_mag_sv_case4 * 1000, bins=25, alpha = 0.5, label=label4)
# plt.hist(all_vel_mag_sv_case0 * 1000, bins=25, alpha = 0.5, label=label0)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 4
# plt.axvline(mean_value_vel_mag_sv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_sv_case4 + std_dev_vel_mag_sv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_sv_case4 - std_dev_vel_mag_sv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.xlabel('RBC Velocity Magnitude (mm/s)', fontdict=font)
# plt.ylabel('Frequency', fontdict=font)
# plt.title('Baseline vs Case4 - Smaller Child Vessel', fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/hist_sv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# # Plot the density plot
# plt.figure(figsize=(10, 7))
# sns.kdeplot(all_vel_mag_sv_case0 * 1000, alpha = 0.5, label=label0, color='blue', fill=True)
# sns.kdeplot(all_vel_mag_sv_case4 * 1000, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_sv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_sv_case0 + std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_sv_case0 - std_dev_vel_mag_sv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 3
# plt.axvline(mean_value_vel_mag_sv_case4, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case4')
# plt.axvline(mean_value_vel_mag_sv_case4 + std_dev_vel_mag_sv_case4, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case4')
# plt.axvline(mean_value_vel_mag_sv_case4 - std_dev_vel_mag_sv_case4, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case4')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case2')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case2')
# #
# plt.title("Baseline vs Case4 - Smaller Child vessel", fontdict=font)
# plt.xlabel("RBC Velocity Magnitude (mm/s)", fontdict=font)
# plt.ylabel("Density", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.legend()
# plt.tight_layout()
# #
# plt.savefig(output_dir + "histogram_density_plots/dens_sv_bv4" + ".png", dpi = 300)
# #
# plt.show()

# ############### END OF BASELINE AND CASE 4 ###############################
#


################# HISTOGRAM AND DENSITY PLOTS OF THE Y-DISTRIBUTION OF THE RBC's #################
#
############## BASELINE AND CASE 1 #############################
###### Parent Vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_pv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_pv_case1 * 1e6, bins=25, alpha = 0.5, label=label1)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case1 - Parent Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label1])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_pv_bv1" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_pv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_pv_case1 * 1e6, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case1 - Parent vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_pv_bv1" + ".png", dpi = 300)
#
plt.show()

##### Larger vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_lv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_lv_case1 * 1e6, bins=25, alpha = 0.5, label=label1)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case1 - Larger Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label1])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_lv_bv1" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_lv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_lv_case1 * 1e6, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case1 - Larger Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_lv_bv1" + ".png", dpi = 300)
#
plt.show()

##### Smaller vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_sv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_sv_case1 * 1e6, bins=25, alpha = 0.5, label=label1)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case1 - Smaller Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label1])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_sv_bv1" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_sv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_sv_case1 * 1e6, alpha = 0.5, label=label1, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case1 - Smaller Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_sv_bv1" + ".png", dpi = 300)
#
plt.show()
######################## end of Baseline vs case1 ##############
#
############## BASELINE AND CASE 2 #############################
###### Parent Vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_pv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_pv_case2 * 1e6, bins=25, alpha = 0.5, label=label2)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case1 - Parent Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label2])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_pv_bv2" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_pv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_pv_case2 * 1e6, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case2 - Parent vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_pv_bv2" + ".png", dpi = 300)
#
plt.show()

##### Larger vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_lv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_lv_case2 * 1e6, bins=25, alpha = 0.5, label=label2)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case2 - Larger Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label2])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_lv_bv2" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_lv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_lv_case2 * 1e6, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case2 - Larger Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_lv_bv2" + ".png", dpi = 300)
#
plt.show()

##### Smaller vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_sv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_sv_case2 * 1e6, bins=25, alpha = 0.5, label=label2)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case2 - Smaller Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend([label0, label2])
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_sv_bv2" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_sv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_sv_case2 * 1e6, alpha = 0.5, label=label2, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case2 - Smaller Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_sv_bv2" + ".png", dpi = 300)
#
plt.show()
######################## end of Baseline vs case2 ##############
#
############## BASELINE AND CASE 3 #############################
###### Parent Vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_pv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_pv_case3 * 1e6, bins=25, alpha = 0.5, label=label3)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case3 - Parent Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_pv_bv3" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_pv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_pv_case3 * 1e6, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case3 - Parent vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_pv_bv3" + ".png", dpi = 300)
#
plt.show()

##### Larger vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_lv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_lv_case3 * 1e6, bins=25, alpha = 0.5, label=label3)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case3 - Larger Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_lv_bv3" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_lv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_lv_case3 * 1e6, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case3 - Larger Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_lv_bv3" + ".png", dpi = 300)
#
plt.show()

##### Smaller vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_sv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_sv_case3 * 1e6, bins=25, alpha = 0.5, label=label3)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case3 - Smaller Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_sv_bv3" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_sv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_sv_case3 * 1e6, alpha = 0.5, label=label3, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case3 - Smaller Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_sv_bv3" + ".png", dpi = 300)
#
plt.show()
######################## end of Baseline vs case3 ##############
#
############## BASELINE AND CASE 4 #############################
###### Parent Vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_pv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_pv_case4 * 1e6, bins=25, alpha = 0.5, label=label4)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case4 - Parent Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_pv_bv4" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_pv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_pv_case4 * 1e6, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case4 - Parent vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_pv_bv4" + ".png", dpi = 300)
#
plt.show()

##### Larger vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_lv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_lv_case4 * 1e6, bins=25, alpha = 0.5, label=label4)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case4 - Larger Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_lv_bv4" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_lv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_lv_case4 * 1e6, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case4 - Larger Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_lv_bv4" + ".png", dpi = 300)
#
plt.show()

##### Smaller vessel
# Plot the histogram
plt.figure(figsize=(10, 7))
plt.hist(all_y_dist_sv_case0 * 1e6, bins=25, alpha = 0.5, label=label0)
plt.hist(all_y_dist_sv_case4 * 1e6, bins=25, alpha = 0.5, label=label4)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.xlabel('RBC y Distribution (μm)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.title('Baseline vs Case4 - Smaller Child Vessel', fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/hist_y_sv_bv4" + ".png", dpi = 300)
#
plt.show()

# Plot the density plot
plt.figure(figsize=(10, 7))
sns.kdeplot(all_y_dist_sv_case0 * 1e6, alpha = 0.5, label=label0, color='blue', fill=True)
sns.kdeplot(all_y_dist_sv_case4 * 1e6, alpha = 0.5, label=label4, color='green', fill=True)
# # STAT MOMENTS FOR BASELINE
# plt.axvline(mean_value_vel_mag_pv_case0, color='red', linestyle='dashed', linewidth=1, label='Mean - Baseline')
# plt.axvline(mean_value_vel_mag_pv_case0 + std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean + Std Dev - Basline')
# plt.axvline(mean_value_vel_mag_pv_case0 - std_dev_vel_mag_pv_case0, color='green', linestyle='dashed', linewidth=1, label='Mean - Std Dev - Baseline')
# # plt.axvline(data_skewness_vel_mag_case0, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Baseline')
# # plt.axvline(data_kurtosis_vel_mag_case0, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Baseline')
# #
# # STAT MOMENTS FOR CASE 1
# plt.axvline(mean_value_vel_mag_pv_case1, color='yellow', linestyle='dotted', linewidth=1, label='Mean - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 + std_dev_vel_mag_pv_case1, color='purple', linestyle='dotted', linewidth=1, label='Mean + Std Dev - Case1')
# plt.axvline(mean_value_vel_mag_pv_case1 - std_dev_vel_mag_pv_case1, color='blue', linestyle='dotted', linewidth=1, label='Mean - Std Dev - Case1')
# # plt.axvline(data_skewness_vel_mag_case1, color='purple', linestyle='dashed', linewidth=2, label='Skewness - Case1')
# # plt.axvline(data_kurtosis_vel_mag_case1, color='orange', linestyle='dashed', linewidth=2, label='Kurtosis - Case1')
# #
plt.title("Baseline vs Case4 - Smaller Child vessel", fontdict=font)
plt.xlabel("RBC y Distribution (μm)", fontdict=font)
plt.ylabel("Density", fontdict=font)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size']) 
plt.legend()
plt.tight_layout()
#
plt.savefig(output_dir + "y_distribution/dens_y_sv_bv4" + ".png", dpi = 300)
#
plt.show()
######################## end of Baseline vs case4 ##############





# ################################################################################
# ################################ RBC VELOCITY PLOTS ############################
# ################################################################################
# #
# ########## BOX PLOTS ##############
# #
# all_vel_data = [all_vel_mag_case0*1000,all_vel_mag_case1*1000,all_vel_mag_case2*1000,all_vel_mag_case3*1000,all_vel_mag_case4*1000]
# #
# figure, ax = plt.subplots(figsize=(10, 7))
# labels = ['Baseline', 'Case 1', 'Case 2', 'Case 3', 'Case 4']
# bp = ax.boxplot(all_vel_data, patch_artist=True, labels = labels)
# # plt.xlabel("Cases", fontdict=font)
# plt.ylabel("RBC Velocity Magnitude (mm/s) ", fontdict=font)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size']) 
# plt.title('Box Plot of Velocity Magnitude for Different Cases', fontdict=font)
# plt.tight_layout()
# #
# plt.savefig(output_dir + "box_plots/vel_box_plot" + ".png", dpi = 300)
# #
# plt.show()
# #
# ########## END OF BOX PLOTS #########
# #
# ########### LINE PLOTS ##############
# #
# ### PLOTS - TOTAL TUBE 
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, mean_vel_mag_tot_case0,'k-', label=label0)
# plt.plot(value1, mean_vel_mag_tot_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, mean_vel_mag_tot_case2,'g--', label=label2)
# plt.plot(value3, mean_vel_mag_tot_case3,'b:', label=label3)
# plt.plot(value4, mean_vel_mag_tot_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('RBC Mean Velocity Magnitude (mm/s)', fontdict= font)
# plt.title("Total Domain", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "velocity_plots/total_vel_mag" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - PARENT VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, mean_vel_mag_pv_case0,'k-', label=label0)
# plt.plot(value1, mean_vel_mag_pv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, mean_vel_mag_pv_case2,'g--', label=label2)
# plt.plot(value3, mean_vel_mag_pv_case3,'b:', label=label3)
# plt.plot(value4, mean_vel_mag_pv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('RBC Mean Velocity Magnitude (mm/s)', fontdict= font)
# plt.title("Parent Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "velocity_plots/pv_vel_mag" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - LARGE CHILD VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, mean_vel_mag_lv_case0,'k-', label=label0)
# plt.plot(value1, mean_vel_mag_lv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, mean_vel_mag_lv_case2,'g--', label=label2)
# plt.plot(value3, mean_vel_mag_lv_case3,'b:', label=label3)
# plt.plot(value4, mean_vel_mag_lv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('RBC Mean Velocity Magnitude (mm/s)', fontdict= font)
# plt.title("Larger Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "velocity_plots/lv_vel_mag" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - SMALLER CHILD VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, mean_vel_mag_sv_case0,'k-', label=label0)
# plt.plot(value1, mean_vel_mag_sv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, mean_vel_mag_sv_case2,'g--', label=label2)
# plt.plot(value3, mean_vel_mag_sv_case3,'b:', label=label3)
# plt.plot(value4, mean_vel_mag_sv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel('RBC Mean Velocity Magnitude (mm/s)', fontdict= font)
# plt.title("Smaller Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "velocity_plots/sv_vel_mag" + ".png", dpi = 300)
# #
# plt.show()
# #
# ######################## END OF VELOCITY LINE PLOTS ##################
# #
# ######################################################################
# ###################### RBC NUMBER PLOTS ##############################
# ######################################################################
# #
# ### PLOTS - TOTAL TUBE 
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, rbc_num_tot_case0,'k-', label=label0)
# plt.plot(value1, rbc_num_tot_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, rbc_num_tot_case2,'g--', label=label2)
# plt.plot(value3, rbc_num_tot_case3,'b:', label=label3)
# plt.plot(value4, rbc_num_tot_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel("Number of RBC's", fontdict= font)
# plt.title("Total Domain", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "rbc_number/total_domain" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - PARENT VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, rbc_num_pv_case0,'k-', label=label0)
# plt.plot(value1, rbc_num_pv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, rbc_num_pv_case2,'g--', label=label2)
# plt.plot(value3, rbc_num_pv_case3,'b:', label=label3)
# plt.plot(value4, rbc_num_pv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel("Number of RBC's", fontdict= font)
# plt.title("Parent Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "rbc_number/pv_rbc_num" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - LARGE CHILD VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, rbc_num_lv_case0,'k-', label=label0)
# plt.plot(value1, rbc_num_lv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, rbc_num_lv_case2,'g--', label=label2)
# plt.plot(value3, rbc_num_lv_case3,'b:', label=label3)
# plt.plot(value4, rbc_num_lv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel("Number of RBC's", fontdict= font)
# plt.title("Larger Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "rbc_number/lv_rbc_num" + ".png", dpi = 300)
# #
# plt.show()
# #
# ### PLOTS - SMALLER CHILD VESSEL
# #   
# plt.figure(figsize=(10,7))
# plt.plot(value0, rbc_num_sv_case0,'k-', label=label0)
# plt.plot(value1, rbc_num_sv_case1,'.-',color='#9467bd', label=label1)
# plt.plot(value2, rbc_num_sv_case2,'g--', label=label2)
# plt.plot(value3, rbc_num_sv_case3,'b:', label=label3)
# plt.plot(value4, rbc_num_sv_case4,'r', label=label4)
# plt.xticks(fontsize=font['size'])
# plt.yticks(fontsize=font['size'])  
# plt.xlabel('Time (s)', fontdict=font)
# plt.ylabel("Number of RBC's", fontdict= font)
# plt.title("Smaller Child Vessel", fontdict=font)
# plt.grid(True)
# plt.legend([label0,label1, label2, label3, label4])
# plt.tight_layout()
# #
# plt.savefig(output_dir + "rbc_number/sv_rbc_num" + ".png", dpi = 300)
# #
# plt.show()
# #
