#!/bin/bash
# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=remi_1
#SBATCH --time=0:5:0
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e745
#SBATCH --partition=serial
#SBATCH --qos=serial

module load cmake
module load cray-hdf5
module load cray-mpich
module load cray-python

export CC=cc
export CXX=CC
export LDFLAGS="-L${CRAYLIBS_X86_64} $(CC --cray-print-opts=libs) -lmpi"

cd /work/e745/e745/remi23/job_submission1/
python job_submission_temp_1.py
