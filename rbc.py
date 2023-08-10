#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Remigius J Selvaraj, MSc CFD, Cranfield Univeristy
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
#
for file in files0:
    csv0 = pd.read_csv(file) # Reading csv file in the list files0
    x = np.array(csv0["X"]) # storing the values in the column "X"
    y = np.array(csv0["Y"]) # storing the values in the column "X"
    case0_v = np.array(csv0["volume"]) # storing the values in the column "volume"
    # the following are conditions set for locating the RBC's in the parent and child vessels
    condition_pv0_1 = (x < 160.65e-6)
    condition_pv0_2 = (x > 551.565e-6)
    condition_lv0 = (x > 160.65e-6) & (x < 551.565e-6) & (y > 64.18e-6)
    condition_sv0 = (x > 160.65e-6) & (x < 551.565e-6) & (y < 64.18e-6)
    #
    pv0_1 = case0_v[condition_pv0_1] # inlet section before the bifurcation
    pv0_2 = case0_v[condition_pv0_2] # outlet section after the bifurcation
    lv0 = case0_v[condition_lv0] # larger child vessel only
    sv0 = case0_v[condition_sv0] # smaller child vessel only
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
#
for file in files1:
    csv1 = pd.read_csv(file)
    x = np.array(csv1["X"])
    y = np.array(csv1["Y"])
    case1_v = np.array(csv1["volume"])
    #
    condition_pv1_1 = (x < 160.65e-6)
    condition_pv1_2 = (x > 551.565e-6)
    condition_lv1 = (x > 160.65e-6) & (x < 551.565e-6) & (y > 64.18e-6)
    condition_sv1 = (x > 160.65e-6) & (x < 551.565e-6) & (y < 64.18e-6)
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
#
for file in files2:
    csv2 = pd.read_csv(file)
    x = np.array(csv2["X"])
    y = np.array(csv2["Y"])
    case2_v = np.array(csv2["volume"])
    #
    condition_pv2_1 = (x < 160.65e-6)
    condition_pv2_2 = (x > 551.565e-6)
    condition_lv2 = (x > 160.65e-6) & (x < 551.565e-6) & (y > 64.18e-6)
    condition_sv2 = (x > 160.65e-6) & (x < 551.565e-6) & (y < 64.18e-6)
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
#
for file in files3:
    csv3 = pd.read_csv(file)
    x = np.array(csv3["X"])
    y = np.array(csv3["Y"])
    case3_v = np.array(csv3["volume"])
    #
    condition_pv3_1 = (x < 160.65e-6)
    condition_pv3_2 = (x > 551.565e-6)
    condition_lv3 = (x > 160.65e-6) & (x < 551.565e-6) & (y > 64.18e-6)
    condition_sv3 = (x > 160.65e-6) & (x < 551.565e-6) & (y < 64.18e-6)
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
#
for file in files4:
    csv4 = pd.read_csv(file)
    x = np.array(csv4["X"])
    y = np.array(csv4["Y"])
    case4_v = np.array(csv4["volume"])
    #
    condition_pv4_1 = (x < 160.65e-6)
    condition_pv4_2 = (x > 551.565e-6)
    condition_lv4 = (x > 160.65e-6) & (x < 551.565e-6) & (y > 64.18e-6)
    condition_sv4 = (x > 160.65e-6) & (x < 551.565e-6) & (y < 64.18e-6)
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
################ End of Case4 #############
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
#
############### PLOTS - TOTAL TUBE HCT ##################   
#   
plt.figure(figsize=(10,7))
plt.plot(value0, hct_total0,'k-', label=label0)
plt.plot(value1, hct_total1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_total2,'g-', label=label2)
plt.plot(value3, hct_total3,'b-', label=label3)
plt.plot(value4, hct_total4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Total Hct (%)', fontdict= font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "total_hct" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS PARENT VESSEL ################## 
#     
plt.figure(figsize=(10,7))
plt.plot(value0, hct_pv0,'k-', label=label0)
plt.plot(value1, hct_pv1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_pv2,'g-', label=label2)
plt.plot(value3, hct_pv3,'b-', label=label3)
plt.plot(value4, hct_pv4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct (%)', fontdict= font)
plt.title("Parent Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "parent_hct" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS LARGER VESSEL ##################      
plt.figure(figsize=(10,7))
plt.plot(value0, hct_lv0, "k-",label=label0)
plt.plot(value1, hct_lv1, "-",color='#9467bd',label=label1)
plt.plot(value2, hct_lv2, "g-",label=label2)
plt.plot(value3, hct_lv3, "b-",label=label3)
plt.plot(value4, hct_lv4, "r-",label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct (%)', fontdict= font)
plt.title("Larger Child Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "larger_vessel_hct" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS SMALLER VESSEL ################## 
#     
plt.figure(figsize=(10,7))
plt.plot(value0, hct_sv0,'k-', label=label0)
plt.plot(value1, hct_sv1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_sv2,'g-', label=label2)
plt.plot(value3, hct_sv3,'b-', label=label3)
plt.plot(value4, hct_sv4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct (%)', fontdict= font)
plt.title("Smaller Child Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "smaller_veesel_hct" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS Hct RATIO LARGER VESSEL ################## 
#     
plt.figure(figsize=(10,7))
plt.plot(value0, hct_rl0,'k-', label=label0)
plt.plot(value1, hct_rl1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_rl2,'g-', label=label2)
plt.plot(value3, hct_rl3,'b-', label=label3)
plt.plot(value4, hct_rl4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct Ratio', fontdict= font)
plt.title("Larger Child Vessel to Total Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "hct_ratio_larger_vessel" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS Hct RATIO SMALLER VESSEL ################## 
#     
plt.figure(figsize=(10,7))
plt.plot(value0, hct_rs0,'k-', label=label0)
plt.plot(value1, hct_rs1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_rs2,'g-', label=label2)
plt.plot(value3, hct_rs3,'b-', label=label3)
plt.plot(value4, hct_rs4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct Ratio', fontdict= font)
plt.title("Smaller Child Vessel to Total Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "hct_ratio_smaller_vessel" + ".png", dpi = 300)
#
plt.show()
#
############### PLOTS Hct RATIO LARGER v SMALLER VESSEL ################## 
#     
plt.figure(figsize=(10,7))
plt.plot(value0, hct_rls0,'k-', label=label0)
plt.plot(value1, hct_rls1,'-',color='#9467bd', label=label1)
plt.plot(value2, hct_rls2,'g-', label=label2)
plt.plot(value3, hct_rls3,'b-', label=label3)
plt.plot(value4, hct_rls4,'r-', label=label4)
plt.xticks(fontsize=font['size'])
plt.yticks(fontsize=font['size'])  
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Hct Ratio', fontdict= font)
plt.title("Larger to Smaller Child Vessel", fontdict=font)
plt.grid(True)
plt.legend([label0,label1, label2, label3, label4])
plt.tight_layout()
#
plt.savefig(output_dir + "hct_ratio_largerandsmaller_vessel" + ".png", dpi = 300)
#
plt.show()
