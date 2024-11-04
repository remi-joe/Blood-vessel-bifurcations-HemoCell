#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 09:35:07 2023

@author: remi
"""

import numpy as np
import matplotlib.pyplot as plt

def read_csv_mod(max_iter, step_size, Diameter, Geometry, case_number):
    np.seterr(all='raise')
    
    # Child vessel diameters
    if Geometry == 0:
        DC1 = Diameter * 0.93
    DC2 = (Diameter**3 - DC1**3)**(1/3)
    
    dt = 6.25e-8  # s
    total_record = int(max_iter / step_size) + 1
    RBC_number = np.zeros(total_record)
    
    # Get stats from the logfile
    logfile_data = np.zeros((7, total_record - 1))  # excluding t=0
    number = 0
    line_number = 0
    first_line = 55
    path = f"/home/remi/irp/simulation_files/case_files/D{Diameter:.1f}_{Geometry}_{case_number}/output_0/log_test/logfile"
    
    with open(path, 'r') as fid:
        for current_line in fid:
            line_number += 1
            if line_number >= first_line and current_line[2] == "#":
                number += 1
                logfile_data[0, number - 1] = float(current_line[(current_line.find('s:') + 3):(current_line.find('|') - 2)])
                logfile_data[1, number - 1] = float(current_line[(current_line.find('.:') + 3):(current_line.find(', m') - 5)])
                logfile_data[2, number - 1] = float(current_line[(current_line.find('n:') + 3):(current_line.find(', r') - 5)])
                logfile_data[3, number - 1] = float(current_line[(current_line.find('y:') + 3):])
            if line_number >= first_line and current_line[2] == "F":
                logfile_data[4, number - 1] = float(current_line[(current_line.find('n.') + 4):(current_line.find('N,') - 3)])
                logfile_data[5, number - 1] = float(current_line[(current_line.find('x.') + 4):(current_line.find('N ') - 3)])
                logfile_data[6, number - 1] = float(current_line[(current_line.find('n:') + 3):(len(current_line) - 3)])
    
    RBC_number[1:] = logfile_data[0, :]
    
    # Get the number of RBCs at t=0
    file_name = f"/home/remi/irp/simulation_files/case_files/D{Diameter:.1f}_{Geometry}_{case_number}/output_0/csv/RBC.{0:012d}.csv"
    temp = np.loadtxt(file_name, delimiter=',', skiprows=1)
    RBC_number[0] = temp.shape[0]
    
    # Get stats from csv files
    dx = 0.5  # um
    csv_data = np.zeros((int(RBC_number[0]), 7, total_record))
    
    # t=0
    csv_data[:, 0:3, 0] = temp[:, 0:3] * 1e6  # um
    csv_data[:, 3, 0] = temp[:, 4] * (1e6)**3  # um3
    csv_data[:, 4:7, 0] = temp[:, 8:11] * 1e3  # mm/s
    
    for i in range(1, total_record):
        file_name = f"/home/remi/irp/simulation_files/case_files/D{Diameter:.1f}_{Geometry}_{case_number}/output_0/csv/RBC.{(i - 1) * step_size:012d}.csv"
        temp = np.loadtxt(file_name, delimiter=',', skiprows=1)
        csv_data[0:int(RBC_number[i]), 0:3, i] = temp[:, 0:3] * 1e6  # um
        csv_data[0:int(RBC_number[i]), 3, i] = temp[:, 4] * (1e6)**3  # um3
        csv_data[0:int(RBC_number[i]), 4:7, i] = temp[:, 8:11] * 1e3  # mm/s
    
    # # Calculate the magnitude of velocity of each RBC
    # velocity = np.zeros((int(RBC_number[0]), total_record))
    
    # for i in range(1, total_record):
    #     velocity[0:int(RBC_number[i]), i] = np.sqrt(csv_data[0:int(RBC_number[i]), 4, i]**2 +
    #                                                csv_data[0:int(RBC_number[i]), 5, i]**2 +
    #                                                csv_data[0:int(RBC_number[i]), 6, i]**2)
    
    # # Calculate the Ht, average velocity, line density, and flux of RBCs in each vessel
    # # Vessel 5 is the combination of 1 and 4
    # RBC_number_vessel = np.zeros((5, total_record))
    # V_total = np.zeros((5, total_record))
    # u_total = np.zeros((5, total_record))
    
    # for i in range(total_record):
    #     for j in range(int(RBC_number[i])):
    #         if csv_data[j, 0, i] <= 5 * Diameter:
    #             # Parent vessel
    #             RBC_number_vessel[0, i] += 1
    #             u_total[0, i] += velocity[j, i]
    #             V_total[0, i] += csv_data[j, 3, i]
    #         elif csv_data[j, 0, i] >= (1395.5 - 5 * 63.5) / 63.5 * Diameter:
    #             # 4th vessel
    #             RBC_number_vessel[3, i] += 1
    #             u_total[3, i] += velocity[j, i]
    #             V_total[3, i] += csv_data[j, 3, i]
    #         elif csv_data[j, 1, i] >= 121.34 / 63.5 * Diameter:
    #             # Upper child vessel
    #             RBC_number_vessel[1, i] += 1
    #             u_total[1, i] += velocity[j, i]
    #             V_total[1, i] += csv_data[j, 3, i]
    #         else:
    #             # Lower child vessel
    #             RBC_number_vessel[2, i] += 1
    #             u_total[2, i] += velocity[j, i]
    #             V_total[2, i] += csv_data[j, 3, i]
    
    # RBC_number_vessel[4, :] = RBC_number_vessel[0, :] + RBC_number_vessel[3, :]
    # V_total[4, :] = V_total[0, :] + V_total[3, :]
    # u_total[4, :] = u_total[0, :] + u_total[3, :]
    
    # # Ht
    # V_vessel = np
