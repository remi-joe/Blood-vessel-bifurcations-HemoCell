import os

# Update time_step.txt and checkpoint.xml
os.system("bash revise_all_timestep.sh")
os.system("bash revise_all_checkpoint.sh")
#Go to next step
os.system("sbatch submit_all_cases_contd_temp_low_2.slurm")
os._exit(0)
