############### Created By: Remigius Joseph Selvaraj ####################
################### MSc. @ Cranfield University #########################
######################## DATE: 24/06/23 #################################
# This script is to change the values that impact the simulation time to its orignal values
# This is effectively a script that changes the same lines inside the same files located in different folders

import os
import fileinput

folders = ['/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4']

# Dictionary of line numbers and new content
lines_to_modify = {
    7: '<warmup>11000</warmup>',
    34: '<tmax>490000</tmax>',
    35: '<tmeas>10000</tmeas>',
    36: '<tcsv>10000</tcsv>',
    37: '<tcheckpoint>10000</tcheckpoint>'
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
