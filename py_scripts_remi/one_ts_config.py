############### Created By: Remigius Joseph Selvaraj ####################
################### MSc. @ Cranfield University #########################
######################## DATE: 24/06/23 #################################
# This script is to change the values that impact the simulation time to 
# the least values ('1' here) to ensure the least simulation time for testing purposes
# For your own case modify the paths and simplify it for your own use-cases

import os
import fileinput

folders = ['/work/e745/e745/remi23/HemoCell/examples/D31.5_0_0', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_1', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_2', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_3', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_4', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4']

# Dictionary of line numbers and new content
lines_to_modify = {
    7: '<warmup>1</warmup>',   
    34: '<tmax>1</tmax>',
    35: '<tmeas>1</tmeas>',
    36: '<tcsv>1</tcsv>',
    37: '<tcheckpoint>1</tcheckpoint>'
}

for folder in folders:
    # Path to config.xml in each folder
    config_file = os.path.join(folder, 'config.xml')

    # Read the content of config.xml
    with fileinput.FileInput(config_file, inplace=True) as file:
        for line_number, line in enumerate(file, 1):
            # Modify the specific lines
            if line_number in lines_to_modify:
                line = lines_to_modify[line_number] + '\n'
            print(line, end='')
