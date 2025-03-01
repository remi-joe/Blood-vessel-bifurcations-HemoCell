**---------------- Written by ------------
**------------- Remigius J Selvaraj ----------
**--------- Computational Fluid Dynamics ----------
**------------- Cranfield University ---------

# This file contains the pointers to the different steps that were followed during the development of the project

## Building HEMOCELL
### Go into the building Hemocell folder to find the code needed to do it. There are three variations, one for building it on a personal system, one for the CRESCENT HPC system, and one for the ARCHER2 HPC system.
### Make sure you change the paths before you execute the program

## Install FREECAD
### [Freecad](https://www.freecad.org/) was used due to its open-source nature and its python integration. It was used to create the geometries and stl files needed for the cases. [Installation Wiki](https://wiki.freecad.org/Installing_on_Linux)

## Geometry_creation
### The geometry_plan folder has the 4 different cases that were created in Freecad and for which stl files were generated using the code in stl_code.
### The stl_code has two files which were used to scale and translate the stl file to the required dimensions. In Hemocell, the stl files required to satisfy certain conditions like 
- Shift the whole geometry to satisfy y<0, and 
- that the geometry is symmetric with the y-z plane
### this was how Hemocell was built 
### There are also two additional python code which was written by a PhD Scholar who has much more experience with HemoCell than I ever did. Please use them as you like, the code I've written is definitely inspired from his code. 
**Freecad files have an extension '.FCStd'(Freecad standard?)**

## Case Setup
### The folder job_submission1 has the necessary code and case setup to work on ARCHER2.
### The folder **D31.5_0_0** is an example folder of how a case is setp for a simulation. 
### To make use of the code, just make sure you have changed the file paths.
### The following order is how the code is executed,
1. Run the file **submit_all_cases.slurm** by using the command `sbatch submit_all_cases.slurm`
2. That runs the first iteration and then runs the py script **job_submission1.py**
3. This executes **Run_job_submission_temp_1.slurm** which then executes **job_submission_temp_1.py**
4. This revises checkpoints through the bash script **revise_all_checkpoint.sh** which goes through the files and executes the code **revise_checkpoint.py**, after which it runs **submit_all_cases_contd_temp_low_1.slurm**
5. This runs the py script **job_submission_temp_2.py** which runs the bash scripts **revise_all_timestep.sh** and **revise_all_checkpoint.sh** to revise all the checkpoints and timesteps after which it runs **submit_all_cases_contd_temp_low_2.slurm**
6. This, after its run executes **job_submission_temp_2.py** again and becomes iterative.
### The timesteps and checkpoints need to be revised because Hemocell is setup in a way where the simulation recognises and continues from the last checkpoint.
### This code was written with the help of the PhD Scholar - Wei who provided an outline and frankly I don't think i did justice to it. The code can be cleaned up to be more efficient which I would do given in time.

## Post Processing
### There are various python and matlab scripts that I've used to post process the data collected.

## The folder **py_scripts_remi** is just a folder with scripts that I made to aid in a lot of things during the project for which I will add descriptions here later since the code is fairly simple and self explanatory

## **logfile_merger.py** is a script to merge logfiles generated during different runs into one.

## Pointers
### This section is just to add things that aren;t documented well but I've figured while working with HemoCell
**I've opted not to write hdf5 data to reduce storage and Ill update that in time while I go through my work and figure out what lines need to modified in the source code**







