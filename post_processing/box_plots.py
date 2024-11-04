#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

work = "/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/"
case_name = "Baseline"
output_path = "/home/remi/Desktop/post_processing_images/box_plots/"

os.chdir(work+"csv")
files = os.listdir(os.getcwd())
files.sort()

dataset = []

for file in files:
    data = np.loadtxt(file, delimiter=",", skiprows=1)
    column_data = data[:,8]*1e3
    dataset.append(column_data)

# Calculate box positions
num_files = len(files)
box_positions = np.arange(1, num_files + 1)

figure, ax = plt.subplots(figsize=(30, 7))
bp = ax.boxplot(dataset, positions=box_positions, patch_artist=True)

# Customize plot appearance
font = {'family': 'sans-serif', 'color': 'black', 'weight': 'normal', 'size': 18}
ax.set_xticks([1, num_files])
ax.set_xticklabels([1, num_files], fontdict = font)
ax.set_xlabel("Timesteps", fontdict = font)
ax.set_ylabel("x-velocity in mm/s", fontdict = font)
ax.set_title("Red Blood Cells: "+case_name, fontdict = font)
ax.set_ylim(-0.2, 0.5)

for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontname('Arial')
    tick.label.set_fontsize(16)

plt.tight_layout()

# Saving 
plt.savefig(output_path + case_name + ".png", dpi=300)

plt.show()
