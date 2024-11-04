#!/bin/bash
# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=remi_Hemo_2
#SBATCH --time=24:00:00
#SBATCH --nodes=11
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e745
#SBATCH --partition=standard
#SBATCH --qos=lowpriority

module load cmake
module load cray-hdf5
module load cray-mpich
module load cray-python

export CC=cc
export CXX=CC
export LDFLAGS="-L${CRAYLIBS_X86_64} $(CC --cray-print-opts=libs) -lmpi"

# Set the number of threads to 1
#   This prevents any threaded system libraries from automatically
#   using threading.
export OMP_NUM_THREADS=1

# Loop over 10 subjobs starting each of them on a separate node
first="/work/e745/e745/remi23/HemoCell/examples/"

name_generated=0
selected="0"
for j in $selected
    do
    for i in $(seq 0 4)
        do
        name[$name_generated]="D31.5_"$j"_"$i
        name_generated=$(($name_generated+1))
        done
    done
selected="0"
for j in $selected
    do
    for i in $(seq 0 4)
        do
        name[$name_generated]="D40.0_"$j"_"$i
        name_generated=$(($name_generated+1))
        done
    done

third="/work/e745/e745/remi23/job_submission1/log/"
fourth=".txt"

cpu_num_per_d=(106 106 106 106 106 113 113 113 113 113)
number_generated=0
for i in $(seq 0 9)
        do
        cpu_num_per_sim[$number_generated]=${cpu_num_per_d[i]}
        number_generated=$(($number_generated+1))
 done

for i in $(seq 0 9)
do
# Launch this subjob on 1 node, note nodes and ntasks options and & to place subjob in the background
cd $first${name[i]} && \
srun --nodes=1 --ntasks=128 --distribution=block:block --hint=nomultithread --mem=200000M \
-n ${cpu_num_per_sim[i]} ./${name[i]} checkpoint.xml > $third${name[i]}$fourth 2>&1 &
done
# Wait for all subjobs to finish
wait

cd /work/e745/e745/remi23/job_submission1/
python job_submission_temp_2.py
