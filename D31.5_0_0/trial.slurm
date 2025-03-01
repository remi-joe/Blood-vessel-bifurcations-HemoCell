#!/bin/bash

# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=HemoCell_test
#SBATCH --time=1:00:0
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e745             
#SBATCH --partition=standard
#SBATCH --qos=lowpriority

# Set the number of threads to 1
#   This prevents any threaded system libraries from automatically 
#   using threading.
export OMP_NUM_THREADS=1

# Propagate the cpus-per-task setting from script to srun commands
#    By default, Slurm does not propagate this setting from the sbatch
#    options to srun commands in the job script. If this is not done,
#    process/thread pinning may be incorrect leading to poor performance
export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK

# Launch the parallel job
#   Using 32 MPI processes and 32 MPI processes per node
#   srun picks up the distribution from the sbatch options

srun --distribution=block:block --hint=nomultithread ./D31.5_0_0 config.xml
