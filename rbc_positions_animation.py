
import os 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

case_name = "case0"
csvdir = "/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/csv/"
output_dir = "/home/remi/Desktop/post_processing_images/position_animations/"

# testdir = csvdir+"test/"
os.chdir(csvdir)

files = os.listdir(csvdir)
list.sort(files)
# cter = 0
# for file in files:
#     data = np.loadtxt(file, delimiter=',', skiprows=1)
#     x = data[:,0]
#     y = data[:,1]
#     plt.figure(figsize=(15, 5))
#     # plt.axis('off')
#     # plt.box(False)
#     plt.plot(x*1e6,y*1e6, "k.")
#     # plt.pause(0.01)
#     plt.savefig(testdir + 'figure'+'{:04d}'.format(cter)+'.png',dpi=300)
#     plt.clf()
#     cter = cter +1

font = {'family': 'sans-serif', 'color': 'black', 'weight': 'normal', 'size': 18}
fig, ax = plt.subplots(figsize=(15, 5))

def animate(i):
    file = files[i]
    data = np.loadtxt(file, delimiter=',', skiprows=1)
    x = data[:, 0]
    y = data[:, 1]
    
    ax.clear()
    ax.plot(x * 1e6, y * 1e6, "k.")
    # plt.rcParams["font.family"] = "Arial"
    
    plt.xlim([0,732])
    plt.ylim([0,130])
    plt.xlabel("x in " u"\u03bcm", fontdict=font)
    plt.ylabel("y in " u"\u03bcm", fontdict=font)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
   

ani = FuncAnimation(fig, animate, frames=len(files), interval=30)


# Save the animation as an MP4 file
ani.save(output_dir + case_name + ".mp4", dpi = 300)
