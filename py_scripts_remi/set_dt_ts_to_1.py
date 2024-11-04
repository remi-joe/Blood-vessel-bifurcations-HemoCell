############### Created By: Remigius Joseph Selvaraj ####################
################### MSc. @ Cranfield University #########################
######################## DATE: 24/06/23 #################################
# This file changes the calues in the files 'dt.txt' and 'timestep.txt' to 1
# This cript is for testing on ARCHER2

import os

# Dictionary of files and their corresponding new content
file_contents = {
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_0/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_0/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_1/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_1/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_2/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_2/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_3/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_3/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_4/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_4/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3/timestep.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4/dt.txt': '1',
    '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4/timestep.txt': '1',
}

# Iterate over the dictionary of files and their new contents
for file_path, new_content in file_contents.items():
    # Check if the file exists
    if os.path.exists(file_path):
        # Update the file with the new content
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f'Updated file: {file_path}')
    else:
        print(f'File does not exist: {file_path}')

